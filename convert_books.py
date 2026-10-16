import os
import subprocess

def convert_docx_to_md():
    book_dir = "book"
    
    if not os.path.exists(book_dir):
        print(f"Error: Directory '{book_dir}' not found.")
        return

    converted_count = 0

    # Iterate through files in the book folder
    for filename in os.listdir(book_dir):
        # Process only .docx files and ignore Microsoft Word temporary lock files (starting with ~$)
        if filename.lower().endswith(".docx") and not filename.startswith("~$"):
            docx_path = os.path.join(book_dir, filename)
            base_name = os.path.splitext(filename)[0]
            md_path = os.path.join(book_dir, f"{base_name}.md")
            
            # Create a dedicated isolated media directory for this specific book: book/images/<book_name>
            book_images_dir = os.path.join(book_dir, "images", base_name)
            os.makedirs(book_images_dir, exist_ok=True)
            
            # Check if .md already exists and is newer than the .docx file
            if os.path.exists(md_path):
                docx_mtime = os.path.getmtime(docx_path)
                md_mtime = os.path.getmtime(md_path)
                
                # If the docx hasn't changed since the last conversion, skip it
                if md_mtime > docx_mtime:
                    print(f"Skipping {filename} (No changes detected)")
                    continue

            # Pandoc command to convert docx -> markdown and extract media to its own folder
            cmd = [
                "pandoc",
                docx_path,
                "-f", "docx",
                "-t", "markdown",
                "-o", md_path,
                f"--extract-media={book_images_dir}"
            ]
            
            print(f"Converting: {filename} -> {base_name}.md ...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                # Post-processing: Prepend YAML frontmatter if it doesn't already exist
                with open(md_path, "r+", encoding="utf-8") as f:
                    content = f.read()
                    if not content.startswith("---"):
                        frontmatter = f"---\ntitle: \"{base_name}\"\ntype: book\n---\n\n"
                        f.seek(0, 0)
                        f.write(frontmatter + content)
                
                print(f"Successfully converted and updated metadata for {filename}")
                converted_count += 1
            else:
                print(f"Failed to convert {filename}:\n{result.stderr}")

    if converted_count == 0:
        print("All Markdown files are up to date!")

if __name__ == "__main__":
    convert_docx_to_md()
