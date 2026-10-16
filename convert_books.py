import os
import subprocess

def convert_docx_to_md():
    book_dir = "book"
    images_dir = os.path.join(book_dir, "images")
    
    # Ensure images directory exists
    os.makedirs(images_dir, exist_ok=True)
    
    if not os.path.exists(book_dir):
        print(f"Error: Directory '{book_dir}' not found.")
        return

    # Iterate through files in the book folder
    for filename in os.listdir(book_dir):
        if filename.lower().endswith(".docx"):
            docx_path = os.path.join(book_dir, filename)
            base_name = os.path.splitext(filename)[0]
            md_path = os.path.join(book_dir, f"{base_name}.md")
            
            # Pandoc command to convert docx -> markdown and extract media
            cmd = [
                "pandoc",
                docx_path,
                "-f", "docx",
                "-t", "markdown",
                "-o", md_path,
                f"--extract-media={images_dir}"
            ]
            
            print(f"Converting: {filename} -> {base_name}.md ...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"Successfully converted {filename}")
            else:
                print(f"Failed to convert {filename}:\n{result.stderr}")

if __name__ == "__main__":
    convert_docx_to_md()
