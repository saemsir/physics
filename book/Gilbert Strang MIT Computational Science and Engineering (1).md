---
title: "Gilbert Strang MIT Computational Science and Engineering (1)"
type: book
---

MIT OpenCourseWare
[[http://ocw.mit.edu]{.underline}](http://ocw.mit.edu/)

18.085 Computational Science and Engineering I

Fall 2008

For information about citing these materials or our Terms of Use, visit:
[[http://ocw.mit.edu/terms]{.underline}](http://ocw.mit.edu/terms).

> CHAPTER 1
>
> APPLIED LINEAR ALGEBRA

#### 1.1 FOUR SPECIAL MATRICES {#four-special-matrices .unnumbered}

> An *m* by *n* matrix has *m* rows and *n* columns and *mn* entries. We
> operate on those rows and columns to solve linear systems *Ax* = *b*
> and eigenvalue problems *Ax* = *λx*. From inputs *A* and *b* (and from
> software like MATLAB) we get outputs *x* and *λ*. A fast stable
> algorithm is extremely important, and this book includes fast
> algorithms.
>
> One purpose of matrices is to store information, but another viewpoint
> is more important for applied mathematics. Often we see the matrix as
> an "operator." *A acts on vectors x to produce Ax*. The components of
> *x* have a meaning---displacements or pressures or voltages or prices
> or concentrations. The operator *A* also has a meaning---in this
> chapter *A* takes diﬀerences. Then *Ax* represents pressure diﬀerences
> or voltage drops or price diﬀerentials.
>
> Before we turn the problem over to the machine---and also after, when
> we interpret
>
> A\\b or eig(A)---it is the meaning we want, as well as the numbers.
>
> This book begins with four special families of matrices---simple and
> useful, absolutely basic. We look ﬁrst at the properties of these
> particular matrices *Kn, Cn*, *Tn*, and *Bn*. (Some properties are
> obvious, others are hidden.) It is terriﬁc to practice linear algebra
> by working with genuinely important matrices. Here are *K*~2~*,
> K*~3~*, K*~4~ in the ﬁrst family, with −1 and 2 and −1 down the
> diagonals:
>
> \_ l ⎡
>
> 2 −1 0 ⎤
>
> 2 −1 0 0
>
> ⎢ ⎥

*K* = 2 −1 *K* = ⎣−1 2 −1 ⎦ *K* = ⎢−1 2 −1 0 ⎥

> −1 2
>
> 4 ⎣ 0 −1 2 −1 ⎦
>
> What is signiﬁcant about *K*~2~ and *K*~3~ and *K*~4~, and eventually
> the *n* by *n* matrix *Kn*? I will give six answers in the same order
> that my class gave them---starting with four properties of the *K*'s
> that you can see immediately.

1

1.  These matrices are symmetric. The entry in row *i*, column *j* also
    > appears in row *j*, column *i*. Thus *K~ij~* = *K~ji~*, on
    > opposite sides of the main diagonal. Symmetry can be expressed by
    > transposing the whole matrix at once: *K* = *K*^T^.

2.  The matrices *Kn* are sparse. Most of their entries are zero when
    *n* gets large.

> *K*~1000~ has a million entries, but only 1000 + 999 + 999 are
> nonzero.

3.  The nonzeros lie in a "band" around the main diagonal, so each *Kn*
    > is *banded*. The band has only three diagonals, so these matrices
    > are tridiagonal.

> Because *K* is a tridiagonal matrix, *Ku* = *f* can be quickly solved.
> If the unknown vector *u* has a thousand components, we can ﬁnd them
> in a few thousand steps (which take a small fraction of a second). For
> a full matrix of order *n* = 1000, solving *Ku* = *f* would take
> hundreds of millions of steps. Of course we have to ask if the linear
> equations have a solution in the ﬁrst place. That question is coming
> soon.

4.  The matrices have constant diagonals. Right away that property wakes
    > up Fourier. It signiﬁes that something is not changing when we
    > move in space or time. The problem is shift-invariant or
    > time-invariant. Coeﬃcients are constant. The tridiagonal matrix is
    > entirely determined by the three numbers 1*,* 2*,* 1. These are
    > actually "second diﬀerence matrices" but my class never says that.

> The whole world of Fourier transforms is linked to constant-diagonal
> matrices. In signal processing, the matrix *D* = *K/*4 is a "highpass
> ﬁlter." *Du* picks out the rapidly varying (high frequency) part of a
> vector *u*. It gives a *convolution* with ^1^( 1*,* 2*,* 1). We use
> these words to call attention to the Fourier part (Chapter 4) of this
> book.
>
> Mathematicians call *K* a *Toeplitz matrix* , and MATLAB uses that
> name:
>
> The command *K* = toeplitz(\[ 2 −1 zeros(1*,* 2) \]) constructs *K*4
> from row 1.
>
> Actually, Fourier will be happier if we make two small changes in
> *Kn*. Insert −1 in the southwest and northeast corners. This completes
> two diagonals (which circle around). All four diagonals of *C*~4~ wrap
> around in this "*periodic matrix* " or "*cyclic convolution*" or
> circulant matrix:
>
> Circulant matrix *C*~4~
>
> = ⎡⎢⎣

2 −1 0 −1

> − −

0 −1 2 −1

−1 0 −1 2

> This matrix is *singular*. It is *not invertible*. Its determinant is
> zero. Rather than computing that determinant, it is much better to
> identify a nonzero vector *u* that solves *C*~4~*u* = 0. (If *C*~4~
> had an inverse, the only solution to *C*~4~*u* = 0 would be the zero
> vector. We could multiply by *C*~4~^−1^ to ﬁnd *u* = 0.) For this
> matrix, the column vector *u* of all ones (printed as *u* = (1*,* 1*,*
> 1*,* 1) with commas) solves *C*~4~*u* = 0.
>
> 1.1 Four Special Matrices 3
>
> The columns of *C* add to the zero column. This vector *u* =
> ones(4*,* 1) is in the
>
> *nullspace* of *C*~4~. The nullspace contains all solutions to *Cu* =
> 0.
>
> Whenever the entries along every row of a matrix add to zero, the
> matrix is certainly singular. The same all-ones vector *u* is
> responsible. Matrix multiplication *Cu* adds the column vectors and
> produces zero. The constant vector *u* = (1*,* 1*,* 1*,* 1) or *u* =
> (*c, c, c, c*) in the nullspace is like the constant *C* when we
> integrate a function. In calculus, this "arbitrary constant" is not
> knowable from the derivative. In linear algebra, the constant in *u* =
> (*c, c, c, c*) is not knowable from *Cu* = 0.

5.  All the matrices *K* = *Kn* are invertible. They are not singular,
    like *Cn*. There is a square matrix *K*^−1^ such that *K*^−1^*K* =
    *I* = *identity matrix*. And if a square matrix has an inverse on
    the left, then also *KK*^−1^ = *I*. This "*inverse matrix* " is also
    symmetric when *K* is symmetric. *But K*^−1^ *is not sparse*.

> Invertibility is not easy to decide from a quick look at a matrix.
> Theoretically, one test is to compute the determinant. There is an
> inverse except when det *K* = 0, because the formula for *K*^−1^
> includes a division by det *K*. But computing the deter-minant is
> almost never done in practice! It is a poor way to ﬁnd *u* =
> *K*^−1^*f* .
>
> What we actually do is to go ahead with the elimination steps that
> solve *Ku* =
>
> *f* . Those steps simplify the matrix, to make it triangular. The
> nonzero pivots on the main diagonal of the triangular matrix show that
> the original *K* is invertible. (Important: We don't want or need
> *K*^−1^ to ﬁnd *u* = *K*^−1^*f* . The inverse would be a full matrix,
> with all positive entries. All we compute is the solution vector *u*.)

6.  The symmetric matrices *Kn* are positive deﬁnite. Those words might
    be new. One goal of Chapter 1 is to explain what this crucial
    property means (*K*~4~ has it, *C*~4~ doesn't). Allow me to start by
    contrasting positive deﬁniteness with invertibility, using the words
    "pivots" and "eigenvalues" that will soon be familiar. *Please
    notice the Appendix that summarizes linear algebra*.

> (*Pivots*) An invertible matrix has *n nonzero* pivots.
>
> A *positive deﬁnite* symmetric matrix has *n positive* pivots.
>
> (*Eigenvalues*) An invertible matrix has *n nonzero* eigenvalues.
>
> A *positive deﬁnite* symmetric matrix has *n positive* eigenvalues.
>
> Positive pivots and eigenvalues are tests for positive deﬁniteness,
> and *C*~4~ fails those tests because it is singular. Actually *C*~4~
> has three positive pivots and eigenvalues, so it almost passes. But
> its fourth eigenvalue is zero (the matrix is singular). Since no
> eigenvalue is negative (*λ* ≥ 0), *C*~4~ is positive *semi* deﬁnite.
>
> The pivots appear on the main diagonal in Section 1.3, when solving
> *Ku* = *f* by elimination. The eigenvalues arise in *Kx* = *λx*. There
> is also a determinant test for positive deﬁniteness (not just det *K
> \>* 0). The proper deﬁnition of a symmetric positive deﬁnite matrix
> (it is connected to positive energy) will come in Section 1.6.
>
> Changing *K*n to *T*n
>
> After *Kn* and *Cn*, there are two more families of matrices that you
> need to know. They are symmetric and tridiagonal like the family *Kn*.
> But the (1*,* 1) entry in *Tn* is changed from 2 to 1:

\_ 1 −1 l

> ⎡ 1 −1 0 ⎤
>
> T~n~(1*,* 1) = 1 *T*~2~ =
>
> −1 2
>
> and *T*~3~ = −1 2 −1 *.* (1)
>
> 0 −1 2
>
> That top row (*T* stands for top) represents a new boundary condition,
> whose meaning we will soon understand. Right now we use *T*~3~ as a
> perfect example of elimination. Row operations produce zeros below the
> diagonal, and the pivots are circled as they are found. Two
> elimination steps reduce *T* to the upper triangular *U* .
>
> Step 1. Add row 1 to row 2, which leaves zeros below the ﬁrst pivot.
>
> Step 2. Add the new row 2 to row 3, which produces *U* .
>
> ⎡ �1 −1 0 ⎤ ⎡�1 −1 0 ⎤⎥ ⎡�1 −1 0 ⎥
>
> ⎢⎣ −1 2 −1 ⎥⎦ Step 1 ⎢⎣ 0 �1 −1 ⎦⎥ Step 2 ⎢ 0 �1 −1 ⎥ = *U .*
>
> *All three pivots of T equal* 1. We can apply the test for
> invertibility (three nonzero pivots). *T*~3~ also passes the test for
> positive deﬁniteness (three *positive* pivots). In fact every *Tn* in
> this family is positive deﬁnite, with all its pivots equal to 1.
>
> That matrix *U* has an inverse (which is automatically upper
> triangular). The exceptional fact for this particular *U* ^−1^ is that
> *all upper triangular entries are* 1's:
>
> 1 1 0 −1 1 1 1
>
> *U* ^−1^ = 0 1 1 = 0 1 1 = triu(ones(3)). (2)
>
> 0 0 1 0 0 1
>
> This says that the inverse of a 3 by 3 "diﬀerence matrix" is a 3 by 3
> "sum matrix." This neat inverse of *U* will lead us to the inverse of
> *T* in Problem 2. The product *U* ^−1^*U* is the identity matrix *I*.
> *U* takes diﬀerences, and *U* ^−1^ takes sums. Taking diﬀerences and
> then sums will recover the original vector (*u*~1~*, u*~2~*, u*~3~):

1 −1 0 *u*~1~ *u*~1~ − *u*~2~

Diﬀerences from *U* 0 1 −1 *u*~2~ = *u*~2~ − *u*~3~

0 0 1 *u*~3~ *u*~3~ − 0

> Sums from *U* ^−1^
>
> ⎡ 1 1 1 ⎤ ⎡ *u*~1~ − *u*~2~ ⎤ ⎡ *u*~1~ ⎤
>
> 0 0 1 *u*~3~ − 0 *u*~3~
>
> 1.1 Four Special Matrices 5 Changing *T*n to *B*n
>
> The fourth family *Bn* has the last entry also changed from 2 to 1.
> The new boundary condition is being applied at both ends (*B* stands
> for both). These matrices *Bn* are symmetric and tridiagonal, but you
> will quickly see that they are *not invertible*. The *Bn* are positive
> semideﬁnite but *not positive deﬁnite*:

\_ 1 −1 l

> ⎡ 1 −1 0 ⎤
>
> B~n~(n*,* n) = 1 *B*~2~ =
>
> −1 1
>
> and *B*~3~ = −1 2 −1 *.* (3)
>
> 0 −1 1
>
> Again, elimination brings out the properties of the matrix. The ﬁrst
> *n* − 1 pivots will all equal 1, because those rows are not changed
> from *Tn*. But the change from 2 to 1 in the last entry of *B*
> produces a change from 1 to 0 in the last entry of *U* :

⎡ �1 −1 0 ⎤ ⎡�1 −1 0 ⎥ ⎡�1 −1 0 ⎤

⎢⎣ −1 2 −1 ⎥⎦ −→ ⎢⎣ 0 �1 −1 ⎥⎦ −→ ⎢⎣ 0 �1 −1 ⎥⎦ = *U .* (4)

> 0 −1 1 0 −1 1 0 0 0
>
> There are only two pivots. (A pivot must be nonzero.) The last matrix
> *U* is certainly not invertible. Its determinant is zero, because its
> third row is all zeros. The constant vector (1*,* 1*,* 1) is in the
> nullspace of *U* , and therefore it is in the nullspace of *B*:
>
> ⎡ 1 −1 0 ⎤ ⎡ 1 ⎤ ⎡ 0 ⎤ ⎡ 1 −1 0 ⎤ ⎡ 1 ⎤ ⎡ 0 ⎤
>
> ⎣ 0 1 −1 ⎦ ⎣ 1 ⎦ = ⎣ 0 ⎦ and also ⎣ −1 2 −1 ⎦ ⎣ 1 ⎦ = ⎣ 0 ⎦ *.*
>
> The whole point of elimination was to simplify a linear system like
> *Bu* = 0, *without changing the solutions*. In this case we could have
> recognized non-invertibility in the matrix *B*, because each row adds
> to zero. Then the sum of its three columns is the zero column. This is
> what we see when *B* multiplies the vector (1*,* 1*,* 1).
>
> Let me summarize this section in four lines (all these matrices are
> symmetric):

#### Matrices in MATLAB {#matrices-in-matlab .unnumbered}

> It is natural to choose MATLAB for linear algebra, but the reader may
> select another system. (Octave is very close, and free. Mathematica
> and Maple are good for symbolic calculation, LAPACK provides excellent
> codes at no cost in netlib, and there are many other linear algebra
> packages.) We will construct matrices and operate on them in the
> convenient language that MATLAB provides.
>
> *Our ﬁrst step is to construct the matrices Kn*. For *n* = 3, we can
> enter the 3 by 3 matrix a row at a time, inside brackets. Rows are
> separated by a semicolon ;
>
> *K* = \[ 2 −1 0 ; −1 2 −1 ; 0 −1 2 \]
>
> For large matrices this is too slow. We can build *K*~8~ from "eye"
> and "ones":
>
> eye(8) = 8 by 8 identity matrix ones(7*,* 1) = column vector of seven
> 1's
>
> The diagonal part is 2∗eye(8). The symbol ∗ means multiplication ! The
> −1's above the diagonal of *K*~8~ have the vector −ones(7*,* 1) along
> diagonal 1 of the matrix *E*:
>
> Superdiagonal of −1's *E* = −diag(ones(7*,* 1)*,* 1)
>
> The 1's *below* the diagonal of *K*~8~ lie on the diagonal numbered 1.
> For those we could change the last argument in *E* from 1 to 1. Or we
> can simply transpose *E*, using the all-important symbol *E
> [I]{.smallcaps}* for *E*^T^. Then *K* comes from its three diagonals:
>
> Tridiagonal matrix *K*~8~ *K* = 2 ∗ eye(8) + *E* + *E [I]{.smallcaps}*
>
> *Note*: The zeroth diagonal (main diagonal) is the default with no
> second argument, so eye(8)= diag(ones(8,1)). And then diag(eye(8)) =
> ones(8*,* 1).
>
> *The constant diagonals make K a Toeplitz matrix*. The toeplitz
> command produces *K*, when each diagonal is determined by a single
> number 2 or −1 or 0. Use the zeros vector for the 6 zeros in the ﬁrst
> row of *K*~8~:
>
> Symmetric Toeplitz row1 = \[ 2 −1 zeros(1*,* 6) \] ; *K* =
> toeplitz(row1)
>
> For an unsymmetric constant-diagonal matrix, use toeplitz(col1, row1).
> Taking col1 = \[1 −1 0 0 \] and row1 = \[ 1 0 0 \] gives a 4 by 3
> backward diﬀerence matrix. It has two nonzero diagonals, 1's and −1's.
>
> To construct the matrices *T* and *B* and *C* from *K*, just change
> entries as in the last three lines of this M-ﬁle that we have named
> KTBC.m. Its input is the size *n*, its output is four matrices of that
> size. The semicolons suppress display of *K, T, B, C*:
>
> 1.1 Four Special Matrices 7
>
> If we happened to want their determinants (we shouldn't!), then with
> *n* = 8

\[ det(*K*) det(*T* ) det(*B*) det(*C*) \] produces the output \[ 9 1 0
0 \]

> One more point. MATLAB could not store *Kn* as a dense matrix for *n*
> = 10*,*000. The 10^8^ entries need about 800 megabytes unless we
> recognize *K* as sparse. The code sparseKTBC.m on the course website
> avoids storing (and operating on) all the zeros. It has *K, T, B*, or
> *C* and *n* as its ﬁrst two arguments. The third argument is 1 for
> sparse, 0 for dense (default 0 for narg = 2, no third argument).
>
> The input to Sparse MATLAB includes the locations of all nonzero
> entries. The command *A* = sparse(*i, j, s, m, n*) creates an *m* by
> *n* sparse matrix from the vectors *i, j, s* that list all positions
> *i, j* of nonzero entries *s*. Elimination by lu(*A*) may produce
> additional nonzeros (called ﬁll-in) which the software will correctly
> identify. In the normal "full" option, zeros are processed like all
> other numbers.
>
> It is best to create the list of triplets *i, j, s* and then call
> sparse. Insertions *A*(*i, j*) = *s* or *A*(*i, j*) = *A*(*i, j*)+ *s*
> are more expensive. We return to this point in Section 3.6.
>
> The sparse KTBC code on the website uses spdiags to enter the three
> diagonals.
>
> Here is the toeplitz way to form *K*~8~, all made sparse by its sparse
> vector start:
>
> vsp = sparse(\[2 -- 1 zeros(1, 6)\]) % please look at each output
>
> Ksp = toeplitz(vsp) % sparse format gives the nonzero positions and
> entries
>
> bsp = Ksp(:, 2) % colon keeps all rows of column 2, so bsp = column 2
> of Ksp usp = Ksp bsp % zeros in Ksp and bsp are not processed,
> solution: usp(2) = 1 uuu = full(usp) % return from sparse format to
> the full uuu = \[0 1 0 0 0 0 0 0\]
>
> Note The open source language Python is also very attractive and
> convenient.
>
> The next sections will use all four matrices in these basic tasks of
> linear algebra: (1.2) The ﬁnite diﬀerence matrices *K, T, B, C*
> include boundary conditions (1.3) Elimination produces pivots in *D*
> and triangular factors in *LDL*^T^
>
> (1.4) Point loads produce inverse matrices *K*^−1^ and *T* ^−1^
>
> (1.5) The eigenvalues and eigenvectors of *K, T, B, C* involve sines
> and cosines.
>
> You will see K\\f in 1.2, lu(K) in 1.3, inv(K) in 1.4, eig(K) in 1.5,
> and chol(K) in 1.6. I very much hope that you will come to know and
> like these special matrices.

#### WORKED EXAMPLES {#worked-examples .unnumbered}

> 1.1 A *Bu* = *f* and *Cu* = *f* might be solvable even though *B* and
> *C* are singular ! Show that every vector *f* = *Bu* has *f*~1~ +
> *f*~2~ + + *fn* = 0. Physical meaning:
>
> the external forces balance. Linear algebra meaning: *Bu* = *f* is
> solvable when *f*
>
> is perpendicular to the all-ones column vector *e* = (1*,* 1*,* 1*,*
> 1*,\...* ) = ones(*n,* 1).
>
> Solution *Bu* is a vector of "diﬀerences" of *u*'s. Those diﬀerences
> always add to zero:
>
> ⎡⎢ 1 −1 ⎤⎥ ⎡⎢ ⎤⎥ ⎡⎢ *u*1 − *u*2 ⎤⎥
>
> *f* = *Bu* = ⎢ −1 2 −1 ⎥ ⎢ *u*~2~ ⎥ = ⎢ −*u*~1~ + 2*u*~2~ − *u*~3~ ⎥
>
> ⎣ −1 2 −1 ⎦ ⎣ *u*~3~ ⎦ ⎣ −*u*~2~ + 2*u*~3~ − *u*~4~ ⎦
>
> −1 1 *u*~4~ −*u*~3~ + *u*~4~
>
> All terms cancel in (*u*~1~ − *u*~2~)+ (−*u*~1~ + 2*u*~2~ − *u*~3~)+
> (−*u*~2~ + 2*u*~3~ − *u*~4~)+ (−*u*~3~ + *u*~4~) = 0. The dot product
> with *e* = (1*,* 1*,* 1*,* 1) is that sum *f e* = *f*~1~ + *f*~2~ +
> *f*~3~ + *f*~4~ = 0.
>
> Dot product *f* · *e* = *f* ^T^*e* = *f*~1~*e*~1~ + *f*~2~*e*~2~ +
> *f*~3~*e*~3~ + *f*~4~*e*~4~ (f *[I]{.smallcaps}* ∗ e in MATLAB)*.*
>
> A second explanation for *f* ^T^*e* = 0 starts from the fact that *Be*
> = 0. The all-ones vector *e* is in the nullspace of *B*. Transposing
> *f* = *Bu* gives *f* ^T^ = *u*^T^*B*^T^, since the transpose of a
> product has the individual transposes in reverse order. This matrix
> *B* is symmetric so *B*^T^ = *B*. Then
>
> *f* ^T^*e* = *u*^T^*B*^T^*e* is equal to *u*^T^*Be* = *u*^T^0 = 0*.*
>
> Conclusion *Bu* = *f* is only solvable when *f* is perpendicular to
> the all-ones vector
>
> *e*. (*The same is true for Cu* = *f* . Again the diﬀerences cancel
> out.) The external forces balance when the *f* 's add to zero. The
> command B\\f will produce Inf because *B* is square and singular, but
> the "pseudoinverse" u = pinv(B) ∗ f will succeed. (Or add a zero row
> to *B* and *f* before the command B\\f, to make the system
> rectangular.)
>
> 1.1 B The "ﬁxed-free" matrix *H* changes the *last entry of K* from 2
> to 1. Connect
>
> *H* to the "free-ﬁxed" *T* (*ﬁrst entry* = 1) by using the reverse
> identity matrix *J*:

⎡ 2 −1 0 ⎤

> comes from
>
> ⎡0 0 1 ⎤
>
> *H* = ⎣−1 2 −1 ⎦ *JTJ* via the *J* = ⎣0 1 0⎦ *.*
>
> Chapter 2 shows how *T* comes from a *tower* structure (free at the
> top). *H* comes from a *hanging* structure (free at the bottom). Two
> MATLAB constructions are
>
> *H* = toeplitz(\[ 2 −1 0 \]); *H*(3*,* 3) = 1 or *J* = ﬂiplr(eye(3));
> *H* = *J* ∗ *T* ∗ *J*
>
> 1.1 Four Special Matrices 9
>
> Solution *JT* reverses the rows of *T* . Then *JTJ* reverses the
> columns to give *H*:
>
> ⎡ 1 −1 0 ⎤ ⎡ 0 −1 2 ⎤
>
> *T* = −1 2 −1 *JT* = −1 2 −1 (*JT* )*J* = *H.*
>
> 0 −1 2 (rows) 1 −1 0 (*columns too*)
>
> We could reverse columns ﬁrst by *TJ*. Then *J*(*TJ*) would be the
> same matrix *H* as (*JT* )*J*. The parentheses never matter in
> (*AB*)*C* = *A*(*BC*)!
>
> Any permutation matrix like *J* has the rows of the identity matrix
> *I* in some order. There are six 3 by 3 permutation matrices because
> there are six orders for the numbers 1*,* 2*,* 3. *The inverse of
> every permutation matrix is its transpose*. This particular *J* is
> symmetric, so it has *J* = *J* ^T^ = *J*^−1^ as you can easily check:
>
> *H* = *JTJ* so *H*^−1^ = *J*^−1^*T* ^−1^*J*^−1^ which is *H*^−1^ =
> *JT* ^−1^*J.* (5)
>
> With back = 3:−1:1, reordering to *JTJ* is H = T(back, back) in
> MATLAB.

## Problem Set 1.1 {#problem-set-1.1 .unnumbered}

> Problems 1--4 are about *T* ^−1^ and Problems 5--8 are about *K*^−1^.

1.  The inverses of *T*~3~ and *T*~4~ (with *T*~11~ = 1 in the top
    corner) are

3 2 1

> −1
>
> 4 3 2 1
>
> ~−1~ ⎢ 3 3 2 1 ⎥
>
> *T*3 = ⎣ 2 2 1 ⎦ and *T*4
>
> ⎣ 2 2 2 1 ⎦
>
> 1 1 1 1 1 1 1
>
> Guess *T*5−1 and multiply by *T*~5~. Find a simple formula for the
> entries of *Tn*−1 on and below the diagonal (*i* ≥ *j*), and then on
> and above the diagonal (*i* ≤ *j*).

2.  Compute *T*3−1 in three steps, using *U* and *U* ^−1^ in equation
    (2):

```{=html}
<!-- -->
```
1.  Check that *T*~3~ = *U* ^T^*U* , where *U* has 1's on the main
    > diagonal and 1's along the diagonal above. Its transpose *U* ^T^
    > is lower triangular.

2.  Check that *UU* ^−1^ = *I* when *U* ^−1^ has 1's on and above the
    > main diagonal.

3.  Invert *U* ^T^*U* to ﬁnd *T*3−1 = (*U* ^−1^)(*U* ^−1^)^T^. *Inverses
    > come in reverse order* !

```{=html}
<!-- -->
```
3.  The diﬀerence matrix *U* = *U*~5~ in MATLAB is
    eye(5)−diag(ones(4,1),1). Con-struct the sum matrix *S* from
    triu(ones(5)). (This keeps the upper triangular part of the 5 by 5
    all-ones matrix.) Multiply *U* ∗ *S* to verify that *S* = *U* ^−1^.

4.  For every *n*, *Sn* = *Un*−1 is upper triangular with ones on and
    above the diagonal. For *n* = 4 check that *SS*^T^ produces the
    matrix *T*~4~^−1^ predicted in Problem 1. Why is *SS*^T^ certain to
    be a symmetric matrix?

1 1 1

5.  The inverses of *K*~3~ and *K*~4~ (please also invert *K*~2~) have
    > fractions det =
    > ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image1.png){width="7.186570428696414e-2in"
    > height="5.866141732283465e-3in"} *,*
    > ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image1.png){width="7.186570428696414e-2in"
    > height="5.866141732283465e-3in"}:

−1 1

> ⎡ 3 2 1 ⎤

4

> −1 ⎢ ⎥
>
> *K*3 = 4 2 4 2

1 2 3

> and
>
> *K*4 =
>
> ⎢⎣ 2 ⎥ *.*
>
> First *guess* the determinant of *K* = *K*~5~. Then compute det(*K*)
> and inv(*K*) and
>
> det(*K*)∗ inv(*K*)---any software is allowed.

6.  (Challenge problem) Find a *formula* for the *i, j* entry of
    > *K*~4~^−1^ *below the diagonal* (*i* ≥ *j*). Those entries grow
    > linearly along every row and up every column. (Section 1.4 will
    > come back to these important inverses.) Problem 7 below is
    > developed in the Worked Example of Section 1.4.

7.  A column *u* times a row *v*^T^ is a rank-one matrix *uv*^T^. All
    > columns are multiples of *u*, and all rows are multiples of
    > *v*^T^. *T*~4~^−1^ − *K*~4~^−1^ has rank 1:

−1 −1

> 16 12 8 4
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image1.png){width="7.186570428696414e-2in"
> height="5.866141732283465e-3in"}1 ⎢ 12 9 6 3 ⎥
>
> 1 ⎡⎢ 3 ⎤⎥
>
> \[4 3 2 1\]

*T*4 − *K*4

5 8 6 4 2 5 2

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image1.png){width="7.186570428696414e-2in"
height="5.866141732283465e-3in"}4 3 2 1 1

Write *K*~3~ −*T*~3~ in this special form *uv*^T^. Predict a similar
formula for *T*3−1 −*K*3−1.

8.  \(a\) Based on Problem 7, predict the *i, j* entry of *T*5−1 −*K*5−1
    below the diagonal.

> \(b\) Subtract this from your answer to Problem 1 (the formula for
> *T*~5~^−1^ when

*i* ≥ *j*). This gives the not-so-simple formula for *K*5−1.

9.  Following Example 1.1 A with *C* instead of *B*, show that *e* =
    > (1*,* 1*,* 1*,* 1) is perpendicular to each column of *C*~4~.
    > Solve *Cu* = *f* = (1*,* −1*,* 1*,* −1) with the singular matrix
    > *C* by u = pinv(C) f. Try u = C e and C f, before and after

> adding a ﬁfth equation 0 = 0.

10. The "hanging matrix" *H* in Worked Example 1.1 B changes the last
    > entry of *K*~3~ to *H*~33~ = 1. Find the inverse matrix from
    > *H*^−1^ = *JT* ^−1^*J*. Find the inverse also from *H* = *UU* ^T^
    > (check upper times lower triangular!) and *H*^−1^ = (*U*
    > ^−1^)^T^*U* ^−1^.

11. Suppose *U* is any upper triangular matrix and *J* is the reverse
    > identity matrix in 1.1 B. Then *JU* is a "southeast matrix". What
    > geographies are *UJ* and *JUJ*? By experiment, a southeast matrix
    > times a northwest matrix is .

12. Carry out elimination on the 4 by 4 circulant matrix *C*~4~ to reach
    > an upper triangular *U* (or try \[*L, U* \] = lu(*C*) in MATLAB).
    > Two points to notice: The last entry of *U* is because *C* is
    > singular. The last column of *U* has new nonzeros. Explain why
    > this "ﬁll-in" happens.

    1.  Four Special Matrices 11

13. By hand, can you factor the circulant *C*~4~ (with three nonzero
    diagonals, allowing wraparound) into circulants *L* times *U* (with
    two nonzero diagonals, allowing wraparound so not truly triangular)?

14. Gradually reduce the diagonal 2*,* 2*,* 2 in the matrix *K*~3~ until
    you reach a singular matrix *M*. This happens when the diagonal
    entries reach . Check the determinant as you go, and ﬁnd a nonzero
    vector that solves *Mu* = 0.

> Questions 15--21 bring out important facts about matrix
> multiplication.

15. How many individual multiplications to create *Ax* and *A*^2^ and
    *AB*?

*An* × *n xn* × 1 *An* × *n An* × *n Am* × *n Bn* × *p* = (*AB*)*m*×*p*

16. You can multiply *Ax* by rows (the usual way) or by columns (more
    important). Do this multiplication both ways:

> By rows By columns
>
> 2 3 1 = inner product using row 1
>
> 4 5 2 inner product using row 2
>
> 2 3 1 = 1 2 +2 3 = combination
>
> 4 5 2 4 5 of columns

17. The product *Ax* is a linear combination of the columns of *A*. The
    equations

> *Ax* = *b* have a solution vector *x* exactly when *b* is a of the
> columns.
>
> Give an example in which *b* is *not in the column space* of *A*.
> There is no solution to *Ax* = *b*, because *b* is not a combination
> of the columns of *A*.

18. Compute *C* = *AB* by multiplying the matrix *A* times each column
    of *B*:

> 2 3 1 2 = 8 ∗ *.*
>
> 4 5 2 4 14 ∗
>
> Thus, A ∗ B(:,j) = C(:,j).

19. You can also compute *AB* by multiplying each row of *A* times *B*:

> 2 3 1 2 = 2 ∗ row 1 + 3 ∗ row 2 = 8 16 *.*
>
> 4 5 2 4 4 ∗ row 1 + 5 ∗ row 2 ∗ ∗
>
> A solution to *Bx* = 0 is also a solution to (*AB*)*x* = 0. Why? From
>
> *Bx* = \_ 1 2 l\_−2 l = \_0 l
>
> how do we know *ABx* = \_ 8 16 l\_−2 l = \_ 0 l?
>
> 2 4 1 0 ∗ ∗ 1 0

20. The four ways to ﬁnd *AB* give numbers, columns, rows, and matrices:

```{=html}
<!-- -->
```
1.  (*rows of A*) times (*columns of B*) C(i,j) = A(i,:) ∗ B(:,j)

2.  *A* times (*columns of B*) C(:,j) = A ∗ B(:,j)

3.  (*rows* of *A*) times *B* C(i,:) = A(i,:) ∗ B

4.  (columns of *A*) times (rows of *B*) for k = 1:n, C =C+ A(:,k)
    > B(k,:);

> end
>
> Finish these 8 multiplications for columns times rows. How many for
> *n* by *n*?
>
> \_ 2 3 l\_ 1 2 l = \_ 2l
>
> \[1 2\] + \_3l
>
> \[2 4\]
>
> = \_ 2 4 l + \_∗ ∗l = \_ 8 ∗l *.*
>
> 4 5 2 4 4 5 4 8 ∗ ∗ ∗ ∗

21. Which *one* of these equations is true for all *n* by *n* matrices
    > *A* and *B*?

> *AB* = *BA* (*AB*)*A* = *A*(*BA*) (*AB*)*B* = *B*(*BA*) (*AB*)^2^ =
> *A*^2^*B*^2^ *.*

22. Use *n* = 1000; *e* = ones(*n,* 1); *K* = spdiags(\[−*e,* 2 ∗ *e,*
    > −*e*\]*,* −1: 1*, n, n*); to enter *K*~1000~ as a sparse matrix.
    > Solve the sparse equation *Ku* = *e* by u = K e. Plot the solution
    > by plot(*u*).

23. Create 4-component vectors *u, v, w* and enter *A* = spdiags(\[*u,
    > v, w*\]*,* −1: 1*,* 4*,* 4). Which components of *u* and *w* are
    > left out from the −1 and 1 diagonals of *A*?

24. Build the sparse identity matrix *I* = sparse(*i, j, s,* 100*,* 100)
    > by creating vectors *i, j, s* of positions *i, j* with nonzero
    > entries *s*. (You could use a for loop.) In this case speye(100)
    > is quicker. Notice that sparse(eye(10000)) would be a disaster,
    > since there isn't room to store eye(10000) before making it
    > sparse.

25. The only solution to *Ku* = 0 or *Tu* = 0 is *u* = 0, so *K* and *T*
    > are invertible. For proof, suppose *u~i~* is the largest component
    > of *u*. If −*u~i~*~−1~ + 2*u~i~* − *u~i~*~+1~ is zero, this forces
    > *u~i~*~−1~ = *u~i~* = *u~i~*~+1~. Then the next equations force
    > every *u~j~* = *u~i~*. At the end, when the boundary is reached,
    > −*u~n~*~−1~ + 2*u~n~* only gives zero if *u* = 0.

> Why does this "diagonally dominant" argument fail for *B* and *C*?

26. For which vectors *v* is toeplitz(*v*) a circulant matrix (cyclic
    > diagonals) ?

27. (Important) Show that the 3 by 3 matrix *K* comes from *A*^T^*A*~0~:

> −1 1 0 0
>
> *A*~0~ = 0 −1 1 0 is a "diﬀerence matrix"
>
> 0 0 −1 1
>
> Which column of *A*~0~ would you remove to produce *A*~1~ with *T* =
> *A*^T^*A*~1~ ? Which column would you remove next to produce *A*~2~
> with *B* = *A*^T^*A*~2~ ? The diﬀer-ence matrices *A*~0~*, A*~1~*,
> A*~2~ have 0*,* 1*,* 2 boundary conditions. So do the "second
> diﬀerences" *K*, *T* , and *B*.

MIT OpenCourseWare
[[http://ocw.mit.edu]{.underline}](http://ocw.mit.edu/)

18.085 Computational Science and Engineering I

Fall 2008

For information about citing these materials or our Terms of Use, visit:
[[http://ocw.mit.edu/terms]{.underline}](http://ocw.mit.edu/terms).

> CHAPTER 4
>
> FOURIER SERIES AND INTEGRALS

#### FOURIER SERIES FOR PERIODIC FUNCTIONS

> This section explains three Fourier series: sines, cosines, and
> exponentials *e^ikx^*. Square waves (1 or 0 or 1) are great examples,
> with delta functions in the derivative. We look at a spike, a step
> function, and a ramp---and smoother functions too.
>
> Start with sin *x*. It has period 2*π* since sin(*x* + 2*π*) = sin
> *x*. It is an odd function since sin( *x*) = sin *x*, and it vanishes
> at *x* = 0 and *x* = *π*. Every function sin *nx* has those three
> properties, and Fourier looked at *inﬁnite combinations of the sines*:
>
> If the numbers *b*~1~*, b*~2~*,\...* drop oﬀ quickly enough (we are
> foreshadowing the im-portance of the decay rate) then the sum *S*(*x*)
> will inherit all three properties:
>
> Periodic *S*(*x* + 2*π*) = *S*(*x*) Odd *S*(−*x*) = −*S*(*x*) *S*(0) =
> *S*(*π*) = 0
>
> 200 years ago, Fourier startled the mathematicians in France by
> suggesting that *any function S*(*x*) with those properties could be
> expressed as an inﬁnite series of sines. This idea started an enormous
> development of Fourier series. Our ﬁrst step is to compute from
> *S*(*x*) the number *b~k~* that multiplies sin *kx*.
>
> *Suppose S*(*x*) = L *b~n~* sin *nx*. *Multiply both sides by* sin
> *kx*. *Integrate from* 0 *to π*:
>
> *S*(*x*) sin *kx dx* = *b*~1~ sin *x* sin *kx dx* + ··· + *b~k~* sin
> *kx* sin *kx dx* + ··· (2)
>
> On the right side, all integrals are zero except the highlighted one
> with *n* = *k*. This property of "orthogonality" will dominate the
> whole chapter. The sines make 90^◦^ angles in function space, when
> their inner products are integrals from 0 to *π*:

317

> Zero comes quickly if we integrate J cos *mx dx* = \[ [sin
> *mx*]{.underline}
> \]*π*![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image1.png){width="7.186570428696414e-2in"
> height="5.866141732283465e-3in"}= 0 − 0. So we use this:
>
> 1 1

Product of sines sin *nx* sin *kx* = 2 cos(*n* − *k*)*x* − 2 cos(*n* +
*k*)*x.* (4)

Integrating cos *mx* with *m* = *n* − *k* and *m* = *n* + *k* proves
orthogonality of the sines.

*The exception is when n* = *k*. Then we are integrating (sin *kx*)^2^ =
^1^ − 1 cos 2*kx*:

> *π* *π* [1]{.underline}
>
> 2 2
>
> *π* [1]{.underline} *[π]{.underline}*
>
> 0 0 0
>
> The highlighted term in equation (2) is *b~k~π/*2. Multiply both sides
> of (2) by 2*/π*:
>
> Notice that *S*(*x*) sin *kx* is *even* (equal integrals from −*π* to
> 0 and from 0 to *π*).
>
> I will go immediately to the most important example of a Fourier sine
> series. *S*(*x*) is an odd square wave with *SW* (*x*) = 1 for 0 *\< x
> \< π*. It is drawn in Figure 4.1 as an odd function (with period 2*π*)
> that vanishes at *x* = 0 and *x* = *π*.
>
> *SW* (*x*) = 1

*x*

> Figure 4.1: The odd square wave with *SW* (*x* + 2*π*) = *SW* (*x*) =
> {1 or 0 or −1}.
>
> Example 1 Find the Fourier sine coeﬃcients *b~k~* of the square wave
> *SW* (*x*).
>
> Solution For *k* = 1*,* 2*,\...* use the ﬁrst formula (6) with
> *S*(*x*) = 1 between 0 and *π*:

[2]{.underline} *π*

> [2]{.underline} ([− cos *kx*]{.underline}lπ
>
> [2]{.underline} � [2]{.underline} [0]{.underline} [2]{.underline}
> [0]{.underline} [2]{.underline} [0]{.underline} \"
>
> The even-numbered coeﬃcients *b*~2*k*~ are all zero because cos 2*kπ*
> = cos 0 = 1. The odd-numbered coeﬃcients *b~k~* = 4*/πk* decrease at
> the rate 1*/k*. We will see that same 1*/k* decay rate for all
> functions formed from *smooth pieces and jumps*.
>
> Put those coeﬃcients 4*/πk* and zero into the Fourier sine series for
> *SW* (*x*):
>
> Square wave *SW* (*x*) = [4]{.underline} [sin *x*]{.underline} + [sin
> 3*x*]{.underline} + [sin 5*x*]{.underline} + [sin 7*x*]{.underline} +
>
> *π* 1 3 5 7
>
> \(8\)
>
> Figure 4.2 graphs this sum after one term, then two terms, and then
> ﬁve terms. You can see the all-important Gibbs phenomenon appearing as
> these "partial sums"
>
> 4.1 Fourier Series for Periodic Functions 319
>
> include more terms. Away from the jumps, we safely approach *SW* (*x*)
> = 1 or 1. At *x* = *π/*2, the series gives a beautiful alternating
> formula for the number *π*:

1 = [4]{.underline} ( [1]{.underline} − [1]{.underline} +
[1]{.underline} − [1]{.underline} + ··· l so that *π* = 4(
[1]{.underline} − [1]{.underline} + [1]{.underline} − [1]{.underline} +
·· ·l*.* (9)

> *The Gibbs phenomenon is the overshoot that moves closer and closer to
> the jumps*. Its height approaches 1*.*18 *\...* and it does not
> decrease with more terms of the series! Overshoot is the one greatest
> obstacle to calculation of all discontinuous functions (like shock
> waves in ﬂuid ﬂow). We try hard to avoid Gibbs but sometimes we can't.
>
> Solid curve
>
> [4]{.underline} ( [sin *x*]{.underline} + [sin 3*x*]{.underline} )

5.  terms:

```{=html}
<!-- -->
```
4.  ( [sin *x*]{.underline} + ··· + [sin 9*x*]{.underline} )

> *π* 1 3 *π* 1 9
>
> overshoot−→ *SW* = 1
>
> *x [π]{.underline}* *x*

2

> Figure 4.2: Gibbs phenomenon: Partial sums L*N b~n~* sin *nx*
> overshoot near jumps.

#### Fourier Coeﬃcients are Best {#fourier-coeﬃcients-are-best .unnumbered}

> Let me look again at the ﬁrst term *b*~1~ sin *x* = (4*/π*) sin *x*.
> This is the closest possible approximation to the square wave *SW* ,
> by any multiple of sin *x* (closest in the least squares sense). To
> see this optimal property of the Fourier coeﬃcients, minimize the
> error over all *b*~1~:
>
> *π π*
>
> The error is (*SW* −*b*~1~ sin *x*)^2^ *dx* The *b*~1~ derivative is
> −2 (*SW* −*b*~1~ sin *x*) sin *xdx.*
>
> The integral of sin^2^ *x* is *π/*2. So the derivative is zero when
> *b*~1~
>
> This is exactly equation (6) for the Fourier coeﬃcient.
>
> = (2*/π*) J *π S*(*x*) sin *xdx*.
>
> Each *b~k~* sin *kx* is as close as possible to *SW* (*x*). We can ﬁnd
> the coeﬃcients *b~k~* one at a time, *because the sines are
> orthogonal*. The square wave has *b*~2~ = 0 because all other
> multiples of sin 2*x* increase the error. Term by term, we are
> "projecting the function onto each axis sin *kx*."

#### Fourier Cosine Series {#fourier-cosine-series .unnumbered}

> The cosine series applies to *even functions* with *C*(−*x*) =
> *C*(*x*):
>
> ∞
>
> Cosine series *C*(*x*) = *a*~0~ + *a*~1~ cos *x* + *a*~2~ cos 2*x* +
> ··· = *a*~0~ + *a~n~* cos *nx.* (10)
>
> *n*=1
>
> Every cosine has period 2*π*. Figure 4.3 shows two even functions, the
> repeating ramp *RR*(*x*) and the up-down train *UD*(*x*) of delta
> functions. That sawtooth ramp *RR* is the integral of the square wave.
> The delta functions in *UD* give the derivative of the square wave.
> (For sines, the integral and derivative are cosines.) *RR* and *UD*
> will be valuable examples, one smoother than *SW* , one less smooth.
>
> First we ﬁnd formulas for the cosine coeﬃcients *a*~0~ and *a~k~*. The
> constant term *a*~0~
>
> is the *average value* of the function *C*(*x*):

[1]{.underline} *π*

> *a*~0~ = Average *a*~0~ =

0

> [1]{.underline}
>
> *C*(*x*) *dx* =
>
> 2*π*
>
> *π*
>
> *C*(*x*) *dx.* (11)
>
> *−π*
>
> I just integrated every term in the cosine series (10) from 0 to *π*.
> On the right side, the integral of *a*~0~ is *a*~0~*π* (divide both
> sides by *π*). All other integrals are zero:

*π* ( [sin *nx*]{.underline} l*π*

> In words, the constant function 1 is orthogonal to cos *nx* over the
> interval \[0*, π*\].
>
> The other cosine coeﬃcients *a~k~* come from the *orthogonality of
> cosines*. As with sines, we multiply both sides of (10) by cos *kx*
> and integrate from 0 to *π*:
>
> *π π π* π
>
> *C*(*x*) cos *kx dx* = *a*~0~ cos *kx dx*+ *a*~1~ cos *x* cos *kx
> dx*+ + *a~k~*(cos *kx*)^2^
>
> 0 0 0 0
>
> *dx*+··
>
> You know what is coming. On the right side, only the highlighted term
> can be nonzero. Problem 4.1.1 proves this by an identity for cos *nx*
> cos *kx*---now (4) has a plus sign. The bold nonzero term is *a~k~π/*2
> and we multiply both sides by 2*/π*:
>
> Again the integral over a full period from −*π* to *π* (also 0 to
> 2*π*) is just doubled.
>
> −*π* 0 *π* 2*π* Repeating Ramp *RR*(*x*) Integral of Square Wave
>
> *x* *x*
>
> Figure 4.3: The repeating ramp *RR* and the up-down *UD* (periodic
> spikes) are even. The derivative of *RR* is the odd square wave *SW* .
> The derivative of *SW* is *UD*.

1.  Fourier Series for Periodic Functions 321

> Example 2 Find the cosine coeﬃcients of the ramp *RR*(*x*) and the
> up-down *UD*(*x*).
>
> Solution The simplest way is to start with the sine series for the
> square wave:

*SW* (*x*) = [4]{.underline} ( [sin *x*]{.underline} + [sin
3*x*]{.underline} + [sin 5*x*]{.underline} + [sin 7*x*]{.underline} +
··· l *.*

> Take the derivative of every term to produce cosines in the up-down
> delta function:

4

> Up-down series *UD*(*x*) = *π* \[cos *x* + cos 3*x* + cos 5*x* + cos
> 7*x* + ··· \] *.* (14)
>
> Those coeﬃcients don't decay at all. The terms in the series don't
> approach zero, so oﬃcially the series cannot converge. Nevertheless it
> is somehow correct and important. Unoﬃcially this sum of cosines has
> all 1's at *x* = 0 and all −1's at *x* = *π*. Then +∞
>
> and −∞ are consistent with 2*δ*(*x*) and −2*δ*(*x* − *π*). The true
> way to recognize *δ*(*x*) is
>
> by the test *δ*(*x*)*f* (*x*) *dx* = *f* (0) and Example 3 will do
> this.
>
> For the repeating ramp, we integrate the square wave series for *SW*
> (*x*) and add the average ramp height *a*~0~ = *π/*2, halfway from 0
> to *π*:
>
> Ramp series *RR*(*x*) = *[π]{.underline}* − *[π]{.underline}* ( [cos
> *x*]{.underline} + [cos 3*x*]{.underline} + [cos 5*x*]{.underline} +
> [cos 7*x*]{.underline} + ··· l *.* (15)
>
> The constant of integration is *a*~0~. *Those coeﬃcients a~k~ drop oﬀ
> like* 1*/k*^2^. They could be computed directly from formula (13)
> using *x* cos *kx dx*, but this requires an integration by parts (or a
> table of integrals or an appeal to *Mathematica* or *Maple*). It was
> much easier to integrate every sine separately in *SW* (*x*), which
> makes clear the crucial point: Each "degree of smoothness" in the
> function is reﬂected in a faster decay rate of its Fourier coeﬃcients
> *a~k~* and *b~k~*.
>
> No decay Delta functions (with spikes)
>
> 1*/k* decay Step functions (with jumps)
>
> 1*/k*^2^ decay Ramp functions (with corners)
>
> 1*/k*^4^ decay Spline functions (jumps in *f* ^mmm^)
>
> *r^k^* decay with *r \<* 1 Analytic functions like 1*/*(2 − cos *x*)
>
> Each integration divides the *k*th coeﬃcient by *k*. So the decay rate
> has an extra 1*/k*. The "Riemann-Lebesgue lemma" says that *a~k~* and
> *b~k~* approach zero for any continuous function (in fact whenever
> \|*f* (*x*)\|*dx* is ﬁnite). Analytic functions achieve a new level of
> smoothness---they can be diﬀerentiated forever. Their Fourier series
> and Taylor series in Chapter 5 converge exponentially fast.
>
> The poles of 1*/*(2 cos *x*) will be complex solutions of cos *x* = 2.
> Its Fourier series converges quickly because *r^k^* decays faster than
> any power 1*/k^p^*. Analytic functions are ideal for
> computations---the Gibbs phenomenon will never appear.
>
> Now we go back to *δ*(*x*) for what could be the most important
> example of all.
>
> Example 3 Find the (cosine) coeﬃcients of the *delta function δ*(*x*),
> made 2*π*-periodic.
>
> Solution The spike occurs at the start of the interval \[0*, π*\] so
> safer to integrate from
>
> −*π* to *π*. We ﬁnd *a*~0~ = 1*/*2*π* and the other *a~k~* = 1*/π*
> (cosines because *δ*(*x*) is even):
>
> [1]{.underline} *π* [1]{.underline} [1]{.underline} *π*
> [1]{.underline}
>
> Average *a*~0~ = 2*π*
>
> *δ*(*x*) *dx* =
>
> *−π* 2*π*
>
> Cosines *a~k~* = *π*

*δ*(*x*) cos *kx dx* =

*−π π*

> Then the series for the delta function has all cosines in equal
> amounts:
>
> Again this series cannot truly converge (its terms don't approach
> zero). But we can graph the sum after cos 5*x* and after cos 10*x*.
> Figure 4.4 shows how these "partial sums" are doing their best to
> approach *δ*(*x*). They oscillate faster and faster away from *x* = 0.
>
> Actually there is a neat formula for the partial sum *δ~N~* (*x*) that
> stops at cos *Nx*. Start by writing each term 2 cos *θ* as *e^iθ^* +
> *e*^−*iθ*^:
>
> *δ* = \[1 + 2 cos *x* + ··· +2 cos *Nx*\] = \[1+ *e^ix^* +
> *e*^−*ix*^ + ··· + *e^iNx^* + *e*^−*iNx*^\] *.*
>
> This is a geometric progression that starts from *e*^−*iNx*^ and ends
> at *e^iNx^*. We have powers of the same factor *e^ix^*. The sum of a
> geometric series is known:
>
> *i*(*N* + ^1^ )*x* −*i*(*N* + )*x* 1
>
> Partial sum
>
> *δ* (*x*) = [1 *e* 2 − *e* 2]{.underline} =
>
> 1 sin(*N* + ~2~ )*x.*
>
> \(17\)
>
> up to cos *Nx*
>
> *^N^* 2*π*
>
> *eix/*2 − *e*−*ix/*2 2*π* sin 1 *x*
>
> This is the function graphed in Figure 4.4. We claim that for any *N*
> the area underneath *δ~N~* (*x*) is 1. (Each cosine integrated from
> *π* to *π* gives zero. The integral of 1*/*2*π* is 1.) The central
> "lobe" in the graph ends when sin(*N* + ^1^)*x* comes down to zero,
> and that happens when (*N* + ^1^ )*x* = *π*. I think the area under
> that lobe (marked by bullets) approaches the same number 1*.*18 *\...*
> that appears in the Gibbs phenomenon.
>
> In what way does *δ~N~* (*x*) approach *δ*(*x*)? The terms cos *nx* in
> the series jump around at each point *x* /= 0, not approaching zero.
> At *x* = *π* we see [^1^]{.underline} \[1 − 2+2 − 2+ ··· \] and the
> sum is 1*/*2*π* or −1*/*2*π*. The bumps in the partial sums don't get
> smaller than 1*/*2*π*. The right test for the delta function *δ*(*x*)
> is to multiply by a smooth *f* (*x*) = *a~k~* cos *kx*
>
> and integrate, because *we only know δ*(*x*) *from its integrals
> δ*(*x*)*f* (*x*) *dx* = *f* (0):
>
> Weak convergence *π*
>
> In this integrated sense (*weak sense*) the sums *δ~N~* (*x*) do
> approach the delta function ! The convergence of *a*~0~ + ··· + *a~N~*
> is the statement that at *x* = 0 the Fourier series of a smooth *f*
> (*x*) = *a~k~* cos *kx* converges to the number *f* (0).
>
> 4.1 Fourier Series for Periodic Functions 323

*δ*~10~(*x*) height 21*/*2*π*

δ~5~(x) height 11/2π

> −*π* 0

height 1*/*2*π*

*π* height −1/2π

> Figure 4.4: The sums *δ~N~* (*x*) = (1 + 2 cos *x* + ··· +2 cos
> *Nx*)*/*2*π* try to approach *δ*(*x*).

#### Complete Series: Sines and Cosines {#complete-series-sines-and-cosines .unnumbered}

> Over the half-period \[0*, π*\], the sines are not orthogonal to all
> the cosines. In fact the integral of sin *x* times 1 is not zero. So
> for functions *F* (*x*) that are not odd or even, we move to the
> complete series (sines plus cosines) on the full interval. Since our
>
> functions are periodic, that "full interval" can be \[−*π, π*\] or
> \[0*,* 2*π*\]:
>
> On every "2*π* interval" all sines and cosines are mutually
> orthogonal. We ﬁnd the Fourier coeﬃcients *a~k~* and *b~k~* in the
> usual way: Multiply (19) by 1 and cos *kx* and sin *kx*, and integrate
> both sides from −*π* to *π*:

[1]{.underline} � π

[1]{.underline} � π

> [1]{.underline} � π
>
> Orthogonality kills oﬀ inﬁnitely many integrals and leaves only the
> one we want.
>
> Another approach is to split *F* (*x*) = *C*(*x*) + *S*(*x*) into an
> even part and an odd part. Then we can use the earlier cosine and sine
> formulas. The two parts are
>
> *C*(*x*) = *F*

even

(*x*) = [*F* (*x*)+ *F* (−*x*)]{.underline}

> 2
>
> *S*(*x*) = *F*

odd

(*x*) = [*F* (*x*) − *F* (−*x*)]{.underline} *.* (21)

> 2
>
> The even part gives the *a*'s and the odd part gives the *b*'s. Test
> on a short square pulse from *x* = 0 to *x* = *h*---this one-sided
> function is not odd or even.
>
> Example 4 Find the *a*'s and *b*'s if *F* (*x*) = square pulse = 1 for
> 0 *\< x \< h*

0 for *h \< x \<* 2*π*

> Solution The integrals for *a*~0~ and *a~k~* and *b~k~* stop at *x* =
> *h* where *F* (*x*) drops to zero. The coeﬃcients decay like 1*/k*
> because of the jump at *x* = 0 and the drop at *x* = *h*:

[1]{.underline}

> Coeﬃcients of square pulse *a*~0~ = 2*π*
>
> *^h^ [h]{.underline}*
>
> 1 *dx* = = average
>
> ~0~ 2*π*

[1]{.underline} *~h~*

> [sin *kh*]{.underline} [1]{.underline} *h*
>
> [1 − cos *kh*]{.underline}
>
> If we divide *F* (*x*) by *h*, its graph is a tall thin rectangle:
> height
>
> ^[1]{.underline}^ , base *h*, and area = 1.
>
> When *h* approaches zero, *F* (*x*)*/h* is squeezed into a very thin
> interval. *The tall rectangle approaches (weakly) the delta function
> δ*(*x*). The average height is area*/*2*π* = 1*/*2*π*. Its other
> coeﬃcients *a~k~/h* and *b~k~/h* approach 1*/π* and 0, already known
> for *δ*(*x*):
>
> *F* (*x*)

→ *δ*(*x*)

> *a~k~* = 1 sin *kh* → 1
>
> and
>
> *bk* = 1 − cos *kh* → 0 as *h* → 0*.* (23)
>
> *h h π kh π h πkh*
>
> When the function has a jump, its Fourier series picks the halfway
> point. This example would converge to *F* (0) = ^1^ and *F* (*h*) =
> ^1^, halfway up and halfway down.
>
> 2 2
>
> The Fourier series converges to *F* (*x*) at each point where the
> function is smooth. This is a highly developed theory, and Carleson
> won the 2006 Abel Prize by proving convergence for every *x* except a
> set of measure zero. If the function has ﬁnite energy
>
> \|*F* (*x*)\|2 *dx*, he showed that the Fourier series converges
> "almost everywhere."
>
> Energy in Function = Energy in Coeﬃcients
>
> There is an extremely important equation (*the energy identity* ) that
> comes from integrating (*F* (*x*))^2^. When we square the Fourier
> series of *F* (*x*), and integrate from

2

> *π* to *π*, all the "cross terms" drop out. The only nonzero integrals
> come from 1
>
> and cos^2^ *kx* and sin^2^ *kx*, multiplied by *a*^2^ and *a*^2^ and
> *b*^2^ :
>
> 0 *k k*
>
> length squared of a vector, except *the vector is a function*. The
> right side comes from an inﬁnitely long vector of *a*'s and *b*'s. The
> lengths are equal, which says that the Fourier transfo[rm]{.underline}
> from function to vector is like an orthogonal matrix. Normalized by
> constants 2*π* and *π*, we have an *orthonormal basis in function
> space*.
>
> What is this function space ? It is like ordinary 3-dimensional space,
> except the "vectorsJ" are functions. Their length ll*f* ll comes from
> integrating instead of adding:
>
> 4.1 Fourier Series for Periodic Functions 325
>
> Length ll*f* ll2 = (*f, f* ) comes from the inner product (*f, g*) =
> *f* (*x*)*g*(*x*) *dx*
>
> Orthogonal functions (*f, g*) = 0 produce a right triangle: ll*f* +
> *g*ll2 = ll*f* ll2 + ll*g*ll2
>
> I have tried to draw Hilbert space in Figure 4.5. It has inﬁnitely
> many axes. *The energy identity* (24) *is exactly the Pythagoras Law
> in inﬁnite-dimensional space*.
>
> *v*2*k*−1 =
>
> cos *kx*
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image2.png){width="8.008311461067366e-2in"
> height="8.008311461067366e-2in"}√*π* �
>
> sin *kx*
>
> � *v*~2~ =
>
> sin *x*
>
> √*π*
>
> *v*~2*k*~ = √*π*

� *f* = *A*~0~*v*~0~ + *A*~1~*v*~1~ + *B*~1~*v*~2~ + ···

function in Hilbert space

> 2 2 2 2

1

> *v*~0~ = √2*π*
>
> 90^◦^ (*v~i~, v~j~*)=0
>
> � *v*~1~ =
>
> ll*f* ll
>
> cos *x*
>
> √*π*
>
> = *A*0 + *A*1 + *B*1 + ···
>
> Figure 4.5: The Fourier series is a combination of orthonormal *v*'s
> (sines and cosines).

#### Complex Exponentials c~k~e^ikx^ {#complex-exponentials-ckeikx .unnumbered}

> This is a small step and we have to take it. In place of separate
> formulas for *a*~0~ and *a~k~* and *b~k~*, we will have *one formula*
> for all the complex coeﬃcients *c~k~*. And the function *F* (*x*)
> might be complex (as in quantum mechanics). The Discrete Fourier
> Transform will be much simpler when we use *N* complex exponentials
> for a vector. We practice in advance with the complex inﬁnite series
> for a 2*π*-periodic function:
>
> If every *c~n~* = *c*~−*n*~, we can combine *e^inx^* with *e*^−*inx*^
> into 2 cos *nx*. Then (25) is the cosine series for an even function.
> If every *c~n~* = *c*~−*n*~, we use *e^inx^ e*^−*inx*^ = 2*i* sin
> *nx*. Then (25) is the sine series for an odd function and the *c*'s
> are pure imaginary.

To ﬁnd *c~k~*, multiply (25) by *e*^−*ikx*^ (not *e^ikx^*) and integrate
from −*π* to *π*:

> *π* −*ikx* *π* −*ikx* *π ix* −*ikx* π *ikx* −*ikx*
>
> *−π −π −π* −π
>
> The complex exponentials are orthogonal. Every integral on the right
> side is zero, except for the highlighted term (when *n* = *k* and
> *e^ikx^e*^−*ikx*^ = 1). The integral of 1 is 2*π*. That surviving term
> gives the formula for *c~k~*:
>
> Notice that *c*~0~ = *a*~0~ is still the average of *F* (*x*), because
> *e*^0^ = 1. The orthogonality of *e^inx^* and *e^ikx^* is checked by
> integrating, as always. But the complex inner product (*F, G*) takes
> the *complex conjugate G of G*. Before integrating, change *e^ikx^* to
> *e*^−*ikx*^:
>
> Complex inner product Orthogonality of *e^inx^* and *e^ikx^*
>
> *π* *π*
>
> ( *ei*(*n*−*k*)*x* l*π*
>
> \(27\)
>
> *−π −π i*(*n* − *k*) *−π*
>
> Example 5 Add the complex series for 1*/*(2 *e^ix^*) and 1*/*(2
> *e*^−*ix*^). These geometric series have exponentially fast decay from
> 1*/*2*^k^*. The functions are analytic.
>
> ( [1]{.underline} *e^ix^ e*^2*ix*^ ) ( [1]{.underline} *e*^−*ix*^
> *e*^−2*ix*^ ) [cos *x*]{.underline} [cos 2*x*]{.underline} [cos
> 3*x*]{.underline}
>
> When we add those functions, we get a real analytic function:
>
> 1 1 (2 − *e*^−*ix*^)+ (2 − *e^ix^*) 4 − 2 cos *x*
>
> 2 − *eix* + 2 − *e*−*ix* = (2 − *eix*)(2 − *e*−*ix*) = 5 − 4 cos *x*
>
> \(28\)

This ratio is the inﬁnitely smooth function whose cosine coeﬃcients are
1*/*2*^k^*.

1 for *s* ≤ *x* ≤ *s* + *h*

> Example 6 Find *c~k~* for the 2*π*-periodic shifted pulse *F* (*x*) =
> 0 elsewhere in \[−*π, π*\]

Solution The integrals (26) from −*π* to *π* become integrals from *s*
to *s* + *h*:

[1]{.underline} *s* + *h*

> *c* =
>
> 1 · *e−ikx*

[1]{.underline}

> *dx* =
>
> ( *e*−*ikx* l*s* + *h* ( 1 − *e*−*ikh* )
>
> *.* (29)
>
> 2*π s* 2*π* −*ik s*

2*πik*

> *Notice above all the simple eﬀect of the shift by s*. *It "modulates"
> each c~k~ by e*^−*iks*^. The energy is unchanged, the integral of
> \|*F* \|2 just shifts, and all \|*e*^−*iks*^\| = 1:
>
> Shift *F* (*x*) to *F* (*x* − *s*) ←→ Multiply *c~k~* by
> *e*^−*iks*^*.* (30)
>
> Example 7 Centered pulse with shift *s* = −*h/*2. The square pulse
> becomes centered around *x* = 0. This even function equals 1 on the
> interval from −*h/*2 to *h/*2:
>
> *[h]{.underline} ikh/*2 1 − *e*−*ikh*
>
> 1 sin(*kh/*2)
>
> Centered by *s* = − ~2~
>
> *c~k~* = *e*
>
> 2*πik*
>
> = *.*
>
> 2*π k/*2
>
> Divide by *h* for a tall pulse. The ratio of sin(*kh/*2) to *kh/*2 is
> the sinc function:
>
> *F*centered 1 b ( *kh* ) *ikx* � 1*/h* for − *h/*2 ≤ *x* ≤ *h/*2
>
> Tall pulse = sinc *e* =
>
> That division by *h* produces area = 1. Every coeﬃcient approaches
> 2*π* as *h* → 0.
>
> The Fourier series for the tall thin pulse again approaches the
> Fourier series for *δ*(*x*).
>
> 4.1 Fourier Series for Periodic Functions 327
>
> Hilbert space can contain vectors *c* = (*c*~0~*, c*~1~*, c*~−1~*,
> c*~2~*, c*~−2~*,* ··· ) instead of functions *F* (*x*). The length of
> *c* is 2*π* \|*c~k~*\|2 = \|*F* \|2*dx*. The function space is often
> denoted by *L* and the vector space is *£* . [The e]{.underline}nergy
> identity is trivial (but deep). Integrating the Fourier series for *F*
> (*x*) times *F* (*x*), orthogonality kills every *c~n~c~k~* for *n* /=
> *k*. This leaves the *c~k~c~k~* = \|*c~k~*\|2:
>
> *π π*

\|*F* (*x*)\|2*dx* = ( *c~n~e^inx^*)( *c~k~e*^−*ikx*^)*dx* =
2*π*(\|*c*~0~\|2 + \|*c*~1~\|2 + \|*c*~−1~\|2 + ··) *.* (31)

> −*π* −*π*
>
> *This is Plancherel's identity: The energy in x-space equals the
> energy in k-space*.
>
> Finally I want to emphasize the three big rules for operating on *F*
> (*x*) = *c~k~e^ikx^*:
>
> *dF*

1.  The derivative has Fourier coeﬃcients *ikc~k~* (energy moves to high
    *k*). *dx*

2.  The integral of *F* (*x*) has Fourier coeﬃcients *[ck]{.underline}
    ,k* = 0 (faster decay).

> *ik*

3.  The shift to *F* (*x*− *s*) has Fourier coeﬃcients *e*^−*iks*^*c~k~*
    (no change in energy).

#### Application: Laplace's Equation in a Circle {#application-laplaces-equation-in-a-circle .unnumbered}

> Our ﬁrst application is to Laplace's equation. The idea is to
> construct *u*(*x, y*) as an inﬁnite series, choosing its coeﬃcients to
> match *u*~0~(*x, y*) along the boundary. Every-thing depends on the
> shape of the boundary, and we take a circle of radius 1.
>
> Begin with the simple solutions 1, *r* cos *θ*, *r* sin *θ*, *r*^2^
> cos 2*θ*, *r*^2^ sin 2*θ*, \... to Laplace's equation. Combinations of
> these special solutions give all solutions in the circle:

\(32\)

It remains to choose the constants *a~k~* and *b~k~* to make *u* =
*u*~0~ on the boundary.

> For a circle *u*~0~(*θ*) is periodic, since *θ* and *θ* + 2*π* give
> the same point:
>
> Set *r* = 1 *u*~0~(*θ*) = *a*~0~ + *a*~1~ cos *θ* + *b*~1~ sin *θ* +
> *a*~2~ cos 2*θ* + *b*~2~ sin 2*θ* + ··· (33)
>
> This is exactly the Fourier series for *u*~0~. The constants *a~k~*
> and *b~k~* must be the Fourier coeﬃcients of *u*~0~(*θ*). Thus the
> problem is completely solved, if an inﬁnite series (32) is acceptable
> as the solution.
>
> Example 8 Point source *u*~0~ = *δ*(*θ*) at *θ* = 0 The whole boundary
> is held at *u*~0~ = 0, except for the source at *x* = 1, *y* = 0. Find
> the temperature *u*(*r, θ*) inside.
>
> 1 1 1
>
> Fourier series for *δ u*~0~(*θ*) = 2*π* + *π* (cos *θ* + cos 2*θ* +
> cos 3*θ* + ··· ) = 2*π*
>
> ∞
>
> *einθ*
>
> −∞
>
> Inside the circle, each cos *nθ* is multiplied by *r^n^*:

[1]{.underline}

> Inﬁnite series for *u u*(*r, θ*) =
>
> \+ [1]{.underline} (*r* cos *θ* + *r*^2^ cos 2*θ* + *r*^3^ cos 3*θ* +
> ··· ) (34)
>
> 2*π π*
>
> Poisson managed to sum this inﬁnite series! It involves a series of
> powers of *re^iθ^*.

So we know the response at every (*r, θ*) to the point source at *r* =
1, *θ* = 0:

> At the center *r* = 0, this produces the average of *u*~0~ = *δ*(*θ*)
> which is *a*~0~ = 1*/*2*π*. On the boundary *r* = 1, this produces *u*
> = 0 except at the point source where cos 0 = 1:
>
> 1 1 *r*^2^ 1 1+ *r*
>
> On the ray *θ* = 0 *u*(*r, θ*) = 2*π* 1+ *r*2 − 2*r* = 2*π* 1 − *r .*
> (36)
>
> As *r* approaches 1, the solution becomes inﬁnite as the point source
> requires.
>
> Example 9 Solve for any boundary values *u*~0~(*θ*) by integrating
> over point sources. When the point source swings around to angle *ϕ*,
> the solution (35) changes from *θ* to
>
> *θ* − *ϕ*. Integrate this "Green's function" to solve in the circle:
>
> Poisson's formula illustrates a key idea. Think of any *u*~0~(*θ*) as
> a circle of point sources. The source at angle *ϕ* = *θ* produces the
> solution inside the integral (37). Integrating around the circle adds
> up the responses to all sources and gives the response to *u*~0~(*θ*).
>
> Example 10 *u*~0~(*θ*) = 1 on the top half of the circle and *u*~0~ =
> −1 on the bottom half.
>
> Solution The boundary values are the square wave *SW* (*θ*). Its sine
> series is in (8):
>
> Square wave for *u* (*θ*) *SW* (*θ*) = [4]{.underline} ( [sin
> *θ*]{.underline} + [sin 3*θ*]{.underline} + [sin 5*θ*]{.underline} +
> ··· l (38)

Inside the circle, multiplying by *r*, *r*^2^, *r*^3^,\... gives fast
decay of high frequencies:

4.  ( [*r* sin *θ*]{.underline} *r*^3^ sin 3*θ r*^5^ sin 5*θ* l

Laplace's equation has smooth solutions, even when *u*~0~(*θ*) is not
smooth.

1.  Fourier Series for Periodic Functions 329 WORKED EXAMPLE

> A hot metal bar is moved into a freezer (zero temperature). The sides
> of the bar are coated so that heat only escapes at the ends. *What is
> the temperature u*(*x, t*) along the bar at time *t*? It will approach
> *u* = 0 as all the heat leaves the bar.
>
> Solution The heat equation is *u~t~* = *u~xx~*. At *t* = 0 the whole
> bar is at a constant temperature, say *u* = 1. The ends of the bar are
> at zero temperature for all time *t\>* 0. This is an initial-boundary
> value problem:
>
> Those zero boundary conditions suggest a sine series. Its coeﬃcients
> depend on *t*:
>
> ∞

Series solution of the heat equation *u*(*x, t*) = *b~n~*(*t*) sin *nx.*
(41)

> 1
>
> The form of the solution shows separation of variables. In a comment
> below, we look for products *A*(*x*) *B*(*t*) that solve the heat
> equation and the boundary conditions. What we reach is exactly
> *A*(*x*) = sin *nx* and the series solution (41).
>
> Two steps remain. First, choose each *b~n~*(*t*) sin *nx* to satisfy
> the heat equation:
>
> Notice *bn[1]{.smallcaps}* = *n*^2^*b~n~*. Now determine each
> *b~n~*(0) from the initial condition *u*(*x,* 0) = 1 on (0*, π*).
> Those numbers are the Fourier sine coeﬃcients of *SW* (*x*) in
> equation (38):
>
> This completes the series solution of the initial-boundary value
> problem:
>
> Bar temperature *u*(*x, t*) = [4]{.underline} *e*^−*n*^2*t* sin *nx.*
> (42)
>
> *πn*

odd *n*

> For large *n* (high frequencies) the decay of *e*^−*n*^2*t* is very
> fast. The dominant term (4*/π*)*e*^−*t*^ sin *x* for large times will
> come from *n* = 1. This is typical of the heat equation and all
> diﬀusion, that the solution (the temperature proﬁle) becomes very
> smooth as *t* increases.
>
> *Numerical diﬃculty* I regret any bad news in such a beautiful
> solution. To compute *u*(*x, t*), we would probably truncate the
> series in (42) to *N* terms. When that ﬁnite series is graphed on the
> website, serious bumps appear in *u~N~* (*x, t*). You ask if there is
> a physical reason but there isn't. The solution should have maximum
> temperature at the midpoint *x* = *π/*2, and decay smoothly to zero at
> the ends of the bar.
>
> Those unphysical bumps are precisely the Gibbs phenomenon. The initial
> *u*(*x,* 0) is 1 on (0*, π*) but its odd reﬂection is −1 on (−*π,* 0).
> That jump has produced the slow 4*/πn* decay of the coeﬃcients, with
> Gibbs oscillations near *x* = 0 and *x* = *π*. The sine series for
> *u*(*x, t*) is not a success numerically. Would ﬁnite diﬀerences help?
>
> Separation of variables We found *b~n~*(*t*) as the coeﬃcient of an
> eigenfunction sin *nx*. Another good approach is to put *u* = *A*(*x*)
> *B*(*t*) directly into *u~t~* = *u~xx~*:
>
> Separation *A*(*x*) *B [1]{.smallcaps}*(*t*) = *A
> [11]{.smallcaps}*(*x*) *B*(*t*) requires *A [11]{.smallcaps}*(*x*) =
> *B [1]{.smallcaps}*(*t*) = constant*.* (43)
>
> *A*(*x*) *B*(*t*)
>
> *A [11]{.smallcaps}/A* is constant in space, *B [1]{.smallcaps}/B* is
> constant in time, and they are equal:
>
> *A [11]{.smallcaps}* = −*λ* gives *A* = sin √*λx* and cos √*λx B
> [1]{.smallcaps}* = −*λ* gives *B* = *e*^−*λt*^
>
> *A B*
>
> The products *AB* = *e*^−*λt*^ sin √*λx* and *e*^−*λt*^ cos √*λx*
> solve the heat equation for any number *λ*. But the boundary condition
> *u*(0*, t*) = [0]{.underline} eliminates the cosines. Then *u*(*π, t*)
> = 0 requires *λ* = *n*^2^ = 1*,* 4*,* 9*,\...* to have sin *λπ* = 0.
> Separation of variables has recovered the functions in the series
> solution (42).
>
> Finally *u*(*x,* 0) = 1 determines the numbers 4*/πn* for odd *n*. We
> ﬁnd zero for even *n* because sin *nx* has *n/*2 positive loops and
> *n/*2 negative loops. For odd *n*, the extra positive loop is a
> fraction 1*/n* of all loops, giving slow decay of the coeﬃcients.
>
> Heat bath (the opposite problem) The solution on the website is 1
> *u*(*x, t*), because it solves a diﬀerent problem. The bar is
> initially frozen at *U* (*x,* 0) =
>
> 0\. It is placed into a heat bath at the ﬁxed temperature *U* = 1 (or
> *U* = *T*~0~). The new unknown is *U* and its boundary conditions are
> no longer zero.
>
> The heat equation and its boundary conditions are solved ﬁrst by
> *U~B~* (*x, t*). In this example *U~B~* ≡ 1 is constant. Then the
> diﬀerence *V* = *U* − *U~B~* has zero boundary values, and its initial
> values are *V* = −1. Now the eigenfunction method (or sepa-ration of
> variables) solves for *V* . (The series in (42) is multiplied by −1 to
> account
>
> for *V* (*x,* 0) = −1.) Adding back *U~B~* solves the heat bath
> problem: *U* = *U~B~* + *V* = 1 − *u*(*x, t*).
>
> Here *U~B~* ≡ 1 is the *steady state* solution at *t* = ∞, and *V* is
> the *transient* solution.
>
> The transient starts at *V* = −1 and decays quickly to *V* = 0.
>
> *Heat bath at one end* The website problem is diﬀerent in another way
> too. The Dirichlet condition *u*(*π, t*) = 1 is replaced by the
> Neumann condition *u [1]{.smallcaps}*(1*, t*) = 0. Only the left end
> is in the heat bath. Heat ﬂows down the metal bar and out at the far
> end, now located at *x* = 1. How does the solution change for
> ﬁxed-free?
>
> 4.1 Fourier Series for Periodic Functions 331
>
> Those eigenfunctions give a new form for the sum of *B~n~*(*t*)
> *A~n~*(*x*):
>
> Fixed-free solution *V* (*x, t*) = b *B* (0) *e*^−(*n*+^ 1 )2 *π*2 *t*
> sin (*n* + 1 ) *πx.* (45)
>
> All frequencies shift by ^1^ and multiply by *π*, because *A
> [11]{.smallcaps}* = −*λA* has a free end
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image3.png){width="5.279965004374453e-2in"
> height="5.866141732283465e-3in"}at *x* = 1. The crucial question is:
> Does orthogonality still hold for these new
>
> eigenfunctions sin *n* + ^1^ *πx* on \[0*,* 1\]? The answer is *yes*
> because this ﬁxed-free "Sturm--Liouville problem" *A [11]{.smallcaps}*
> = −*λA* is still symmetric.
>
> Summary The series solutions all succeed but the truncated series all
> fail. We can see the overall behavior of *u*(*x, t*) and *V* (*x, t*).
> But their exact values close to the jumps are not computed well until
> we improve on Gibbs.
>
> We could have solved the ﬁxed-free problem on \[0*,* 1\] with the
> ﬁxed-ﬁxed solution on \[0*,* 2\]. That solution will be symmetric
> around *x* = 1 so its slope there is zero. Then rescaling *x* by 2*π*
> changes sin(*n* + ^1^)*πx* into sin(2*n* + 1)*x*. I hope you like the
> graphics created by Aslan Kasimov on the cse website.

## Problem Set 4.1 {#problem-set-4.1 .unnumbered}

1.  Find the Fourier series on −*π* ≤ *x* ≤ *π* for

    a.  *f* (*x*) = sin^3^ *x*, an odd function

    b.  *f* (*x*) = \| sin *x*\|, an even function

    c.  *f* (*x*) = *x*

    d.  *f* (*x*) = *e^x^*, using the complex form of the series.

> What are the even and odd parts of *f* (*x*) = *e^x^* and *f* (*x*) =
> *e^ix^*?

2.  From Parseval's formula the square wave sine coeﬃcients satisfy

> *π π*

*π*(*b*^2^ + *b*^2^ + ··· ) = \|*f* (*x*)\|2 *dx* = 1 *dx* = 2*π.*

> 1 2
>
> −*π* −*π*
>
> Derive the remarkable sum *π*^2^ = 8(1 + ^1^ + ^[1]{.underline}^ + ···
> ).

3.  If a square pulse is centered at *x* = 0 to give

> *π π*

*f* (*x*) = 1 for \|*x*\| *\<* 2 *,f* (*x*) = 0 for 2 *\<* \|*x*\| *\<
π,*

> draw its graph and ﬁnd its Fourier coeﬃcients *a~k~* and *b~k~*.

4.  Suppose *f* has period *T* instead of 2*x*, so that *f* (*x*) = *f*
    (*x* + *T* ). Its graph from

> −*T/*2 to *T/*2 is repeated on each successive interval and its real
> and complex Fourier series are
>
> 2*πx* 2*πx* ∞

*f* (*x*) = *a*~0~ + *a*~1~ cos + *b*~1~ sin + ··· = b *c~k~
e^ik^*^2*πx/T*^

> −∞
>
> Multiplying by the right functions and integrating from −*T/*2 to
> *T/*2, ﬁnd *a~k~*, *b~k~*, and *c~k~*.

5.  Plot the ﬁrst three partial sums and the function itself:

> *x*(*π x*) = [8]{.underline} [sin *x*]{.underline} + [sin
> 3*x*]{.underline} + [sin 5*x*]{.underline} + *,* 0 *\< x \< π. π* 1 27
> 125
>
> Why is 1*/k*^3^ the decay rate for this function? What is the second
> derivative?

6.  What constant function is closest in the least square sense to *f* =
    > cos^2^ *x*? What multiple of cos *x* is closest to *f* = cos^3^
    > *x*?

7.  Sketch the 2*π*-periodic half wave with *f* (*x*) = sin *x* for 0
    > *\< x \< π* and *f* (*x*) = 0 for −*π \< x \<* 0. Find its Fourier
    > series.

8.  \(a\) Find the lengths of the vectors *u* = (1*,* ^1^ *,* ^1^ *,*
    > ^1^ *,.. .*) and *v* = (1*,* ^1^ *,* ^1^ *,.* ) in

> 2 4 8 3 9
>
> Hilbert space and test the Schwarz inequality \|*u*^T^*v*\|2 ≤
> (*u*^T^*u*)(*v*^T^*v*).
>
> \(b\) For the functions *f* = 1 + ^1^*e^ix^* + ^1^ *e*^2*ix*^ + ···
> and *g* = 1 + ^1^ *e^ix^* + ^1^ *e*^2*ix*^ + ···
>
> use part (a) to ﬁnd the numerical value of each term in

1 *~π~*

> *f* (*x*) *g*(*x*) *dx* 1 ≤
>
> *π π*
>
> \|*f* (*x*)\| *dx* \|*g*(*x*)\| *dx.*

9.  Find the solution to Laplace's equation with *u*~0~ = *θ* on the
    > boundary. Why is this the imaginary part of 2(*z* − *z*^2^*/*2+
    > *z*^3^*/*3 ··· ) = 2 log(1 + *z*)? Conﬁrm that on the unit circle
    > *z* = *e* , the imaginary part of 2 log(1 + *z*) agrees with *θ*.

10. If the boundary condition for Laplace's equation is *u*~0~ = 1 for 0
    > *\< θ \< π* and *u*~0~ = 0 for *π \< θ \<* 0, ﬁnd the Fourier
    > series solution *u*(*r, θ*) inside the unit circle. What is *u* at
    > the origin?

11. With boundary values *u*~0~(*θ*) = 1 + ^1^*e^iθ^* + ^1^ *e*^2*iθ*^ +
    > ··· , what is the Fourier series

> solution to Laplace's equation in the circle? Sum the series.

12. \(a\) Verify that the fraction in Poisson's formula satisﬁes
    > Laplace's equation.

```{=html}
<!-- -->
```
(b) What is the response *u*(*r, θ*) to an impulse at the point (0*,*
    > 1), at the angle

> *ϕ* = *π/*2?

(c) If *u*~0~(*ϕ*) = 1 in the quarter-circle 0 *\< ϕ \< π/*2 and *u*~0~
    > = 0 elsewhere, show that at points on the horizontal axis (and
    > especially at the origin)

> [1]{.underline} [1]{.underline} −1 ( 1 − *r*^2^ )

*u*(*r,* 0) =

> \+ tan by using
>
> 2 2*π* −2*r*
>
> *b* + *c* cos *ϕ* = √*b*2 − *c*2 tan

*.*

> *c* + *b* cos *ϕ*
>
> 4.1 Fourier Series for Periodic Functions 333

13. When the centered square pulse in Example 7 has width *h* = *π*, ﬁnd

    a.  its energy \|*F* (*x*)\|2 *dx* by direct integration

    b.  its Fourier coeﬃcients *c~k~* as speciﬁc numbers

    c.  the sum in the energy identity (31) or (24)

> If *h* = 2*π*, why is *c*~0~ = 1 the only nonzero coeﬃcient ? What is
> *F* (*x*)?

14. In Example 5, *F* (*x*) = 1+(cos *x*)*/*2+···+(cos *nx*)*/*2*^n^*
    +··· is inﬁnitely smooth:

    a.  If you take 10 derivatives, what is the Fourier series of
        > *d*^10^*F/dx*^10^?

    b.  Does that series still converge quickly? Compare *n*^10^ with
        > 2*^n^* for *n*^1024^.

15. (*A touch of complex analysis*) The analytic function in Example 5
    blows up when 4 cos *x* = 5. This cannot happen for real *x*, but
    equation (28) shows blowup if *e^ix^* = 2 or ^1^ . In that case we
    have *poles at x* = ±*i* log 2. Why are

> there also poles at all the complex numbers *x* = ±*i* log 2 + 2*πn* ?

16. (*A second touch*) Change 2's to 3's so that equation (28) has
    1*/*(3 *e^ix^*) + 1*/*(3 *e*^−*ix*^). Complete that equation to ﬁnd
    the function that gives fast decay at the rate 1*/*3*^k^*.

17. (*For complex professors only*) Change those 2's and 3's to 1's:

> 1 1 (1 − *e*^−*ix*^)+ (1 − *e^ix^*) 2 − *e^ix^* − *e*^−*ix*^
>
> 1 − *eix* + 1 − *e*−*ix* =
>
> (1 − *eix*)(1 − *e*−*ix*)
>
> = 2 − *eix* − *e*−*ix* = 1 *.*
>
> A constant ! What happened to the pole at *e^ix^* = 1 ? Where is the
> dangerous series (1 + *e^ix^* + ··· )+ (1 + *e*^−*ix*^ + ··· ) = 2 + 2
> cos *x* + ··· involving *δ*(*x*)?

18. Following the Worked Example, solve the heat equation *u~t~* =
    *u~xx~* from a point source *u*(*x,* 0) = *δ*(*x*) with free
    boundary conditions *u [1]{.smallcaps}*(*π, t*) = *u
    [1]{.smallcaps}*(−*π, t*) = 0. Use the inﬁnite cosine series for
    *δ*(*x*) with time decay factors *b~n~*(*t*).

MIT OpenCourseWare
[[http://ocw.mit.edu]{.underline}](http://ocw.mit.edu/)

18.085 Computational Science and Engineering I

Fall 2008

For information about citing these materials or our Terms of Use, visit:
[[http://ocw.mit.edu/terms]{.underline}](http://ocw.mit.edu/terms).

## LINEAR ALGEBRA IN A NUTSHELL {#linear-algebra-in-a-nutshell .unnumbered}

> One question always comes on the ﬁrst day of class. "*Do I have to
> know linear algebra*?" My reply gets shorter every year: "*You soon
> will*." This section brings together many important points in the
> theory. It serves as a quick primer, not an oﬃcial part of the applied
> mathematics course (like Chapter 1 and 2).
>
> This summary begins with two lists that use most of the key words of
> linear algebra. The ﬁrst list applies to invertible matrices. That
> property is described in 14 diﬀerent ways. The second list shows the
> contrast, when *A* is singular (not invertible). There are more ways
> to test invertibility of an *n* by *n* matrix than I expected.
>
> Nonsingular Singular
>
> *A* is invertible *A* is not invertible
>
> The columns are independent The columns are dependent The rows are
> independent The rows are dependent
>
> The determinant is not zero The determinant is zero
>
> *Ax* = 0 has one solution *x* = 0 *Ax* = 0 has inﬁnitely many
> solutions
>
> *Ax* = *b* has one solution *x* = *A*^−1^*b Ax* = *b* has no solution
> or inﬁnitely many
>
> *A* has *n* (nonzero) pivots *A* has *r \< n* pivots
>
> *A* has full rank *A* has rank *r \< n*
>
> The reduced row echelon form is *R* = *I R* has at least one zero row
>
> The column space is all of R*n* The column space has dimension *r \<
> n*
>
> The row space is all of R*n* The row space has dimension *r \< n*
>
> All eigenvalues are nonzero Zero is an eigenvalue of *A A*^T^*A* is
> symmetric positive deﬁnite *A*^T^*A* is only semideﬁnite
>
> *A* has *n* (positive) singular values *A* has *r \< n* singular
> values
>
> Now we take a deeper look at linear equations, without proving every
> statement we make. The goal is to discover what *Ax* = *b* really
> means. One reference is my textbook *Introduction to Linear Algebra*,
> published by Wellesley-Cambridge Press. That book has a much more
> careful development with many examples (you could look at the course
> page, with videos of the lectures, on ocw.mit.edu or
> web.mit.edu/18.06).
>
> The key is to think of every multiplication *Ax*, a matrix *A* times a
> vector *x*, as a
>
> *combination of the columns of A*:
>
> Matrix Multiplication by Columns
>
> Multiplying by rows, the ﬁrst component *C* + 2*D* comes from 1 and 2
> in the ﬁrst row of *A*. But I strongly recommend to think of *Ax* a
> column at a time. Notice how
>
> *x* = (1*,* 0) and *x* = (0*,* 1) will pick out single columns of *A*:
>
> U 1 2 lU 1 l = ﬁrst column U 1 2 lU 0 l = last column *.*
>
> Suppose *A* is an *m* by *n* matrix. Then *Ax* = 0 has at least one
> solution, the all-zeros vector *x* = 0. There are certainly other
> solutions in case *n \> m* (more unknowns than equations). Even if *m*
> = *n*, there might be nonzero solutions to *Ax* = 0; then
>
> *A* is square but not invertible. It is the number *r* of
> *independent* rows and columns that counts. That number *r* is the
> rank of *A* (*r* ≤ *m* and *r* ≤ *n*).
>
> The nullspace of *A* is the set of all solutions *x* to *Ax* = 0. This
> nullspace *N* (*A*) contains only *x* = 0 when the columns of *A* are
> independent. In that case the matrix *A* has full column rank *r* =
> *n*: independent columns.
>
> For our 2 by 2 example, the combination with *C* = 2 and *D* = −1
> produces the zero vector. Thus *x* = (2*,* −1) is in the nullspace,
> with *Ax* = 0. The columns (1*,* 3) and (2*,* 6) are "linearly
> dependent." One column is a multiple of the other column. *The rank is
> r* = 1*.* The matrix *A* has a whole line of vectors *cx* = *c*(2*,*
> −1) in its nullspace:
>
> Nullspace U 1 2 lU 2 l = U 0 l and also U 1 2 lU 2*c* l = U 0 l *.*
>
> is a line 3 6 −1 0 3 6 −*c* 0
>
> If *Ax* = 0 and *Ay* = 0, then every combination *cx* + *dy* is in the
> nullspace. Always
>
> *Ax* = 0 asks for a combination of the columns of *A* that produces
> the zero vector:
>
> When those columns are independent, the only way to produce *Ax* = 0
> is with *x*~1~ = 0, *x*~2~ = 0, *.. .*, *x~n~* = 0. Then *x* =
> (0*,\... ,* 0) is the only vector in the nullspace of *A*. Often this
> will be our requirement (independent columns) for a good matrix *A*.
> In that case, *A*^T^*A* also has independent columns. The square *n*
> by *n* matrix *A*^T^*A* is then invertible and symmetric and positive
> deﬁnite. If *A* is good then *A*^T^*A* is even better.
>
> I will extend this review (*still optional* ) to the geometry of *Ax*
> = *b*.

#### Column Space and Solutions to Linear Equations {#column-space-and-solutions-to-linear-equations .unnumbered}

> *Ax* = *b* asks for a linear combination of the columns that equals
> *b*. In our 2 by 2 example, the columns go in the same direction! Then
> *b* does too:
>
> Column space *Ax* = 1 2 *C*

3 6 *D*

> l is always on the line through
>
> U 1 l *.*
>
> We can only solve *Ax* = *b* when the vector *b* is on that line. For
> *b* = (1*,* 4) there is no solution, it is oﬀ the line. For *b* =
> (5*,* 15) there are many solutions (5 times column 1 gives *b*, and
> this *b* is on the line). The big step is to look at a space of
> vectors:
>
> Deﬁnition: The *column space* contains all combinations of the
> columns.
>
> In other words, *C* (*A*) contains all possible products *A* times
> *x*. Therefore *Ax* = *b* is
>
> solvable exactly when the vector *b* is in the column space *C* (*A*).
>
> For an *m* by *n* matrix, the columns have *m* components. The column
> space of *A* is in *m*-dimensional space. The word "space" indicates
> that the key operation of linear algebra is allowed: *Any combination
> of vectors in the space stays in the space*. The zero combination is
> allowed, so the vector *x* = 0 is in every space.
>
> How do we write down all solutions, when *b* belongs to the column
> space of *A* ? Any one solution to *Ax* = *b* is a particular solution
> *x~p~*. Any vector *x~n~* in the nullspace solves *Ax* = 0. Adding
> *Ax~p~* = *b* to *Ax~n~* = 0 gives *A*(*x~p~* + *x~n~*) = *b*. The
> complete solution to *Ax* = *b* has this form *x* = *x~p~* + *x~n~*:
>
> In the example, *b* = (5*,* 15) is 5 times the ﬁrst column, so one
> particular solution is *x~p~* = (5*,* 0). To ﬁnd all other solutions,
> add to *x~p~* any vector *x~n~* in the nullspace---which is the line
> through (2*,* −1). Here is *x~p~* + (all *x~n~*):

U 1 2 lU *C* l = U 5 l gives *x*complete = U *C* l = U 5 l + U 2*c* l
*.*

> 3 6 *D* 15
>
> *D* 0 −*c*
>
> This line of solutions is drawn in Figure A1. *It is not a subspace*.
> It does not contain (0*,* 0), because it is shifted over by the
> particular solution (5*,* 0). We only have a "space" of solutions when
> *b* is zero (then the solutions ﬁll the nullspace).
>
> *D*
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image4.png){width="7.655511811023621e-2in"
> height="7.655511811023621e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image4.png){width="7.655511811023621e-2in"
> height="7.655511811023621e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image5.png){width="7.655511811023621e-2in"
> height="7.655511811023621e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image6.png){width="7.655511811023621e-2in"
> height="7.655511811023621e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image4.png){width="7.655511811023621e-2in"
> height="7.655511811023621e-2in"}\[ 1 \] = shortest solution pinv(*A*)
> ∗ *b* is in the row space
>
> line of all solutions *x~p~* + all *x~n~* (not a subspace)
>
> \[ 5 \] = one particular solution *x~p~* = *A*\\*b*
>
> *Ax~n~* = 0 : null space
>
> *x~n~ x* = *x~p~* + *x~n~*
>
> Figure A1: Parallel lines of solutions to *Ax~n~* = 0 and \[ ^1^ ^2^
> \] (*x~p~* + *x~n~*) = \[ ^5^ \] May I collect three important
> comments on linear equations *Ax* = *b*.

1.  Suppose *A* is a square *invertible* matrix (the most common case in
    practice). Then the nullspace only contains *x~n~* = 0. The
    particular solution *x~p~* = *A*^−1^*b* is the only solution. The
    complete solution *x~p~* + *x~n~* is *A*^−1^*b* + 0. Thus *x* =
    *A*^−1^*b*.

2.  *Ax* = *b* has inﬁnitely many solutions in Figure A1. The shortest
    > *x* always lies in the "row space" of *A*. That particular
    > solution (1*,* 2) is found by the *pseudo-inverse* pinv (*A*). The
    > backslash *A*\\*b* ﬁnds an *x* with at most *m* nonzeros.

3.  Suppose *A* is tall and thin (*m \> n*). The *n* columns are likely
    > to be independent. But if *b* is not in the column space, *Ax* =
    > *b* has no solution. The least squares method minimizes ll*b* −
    > *Ax*ll2 by solving *A*^T^*Ax*� = *A*^T^*b*.

#### The Four Fundamental Subspaces {#the-four-fundamental-subspaces .unnumbered}

> The nullspace *N* (*A*) contains all solutions to *Ax* = 0. The column
> space *C* (*A*) contains all combinations of the columns. When *A* is
> *m* by *n*, *N* (*A*) is a subspace of R*^n^* and *C* (*A*) is a
> subspace of R*^m^*.
>
> The other two fundamental spaces come from the transpose matrix
> *A*^T^. They are *N* (*A*^T^) and *C* (*A*^T^). We call *C* (*A*^T^)
> the "row space of *A*" because the rows of *A* are the columns of
> *A*^T^. What are those spaces for our 2 by 2 example?

*A* = 1 2

3 6

> transposes to
>
> *A*^T^ = 1 3 *.*
>
> 2 6
>
> Both columns of *A*^T^ are in the direction of (1*,* 2). The line of
> all vectors (*c,* 2*c*) is
>
> *C* (*A*^T^) = row space of *A*. The nullspace of *A*^T^ is in the
> direction of (3*,* −1):
>
> Nullspace of *A*^T^ *A*^T^*y* = U 1 3 lU *E* l = U 0 l gives U *E* l =
> U 3*c* l *.*
>
> 2 6 *F* 0
>
> *F* −*c*
>
> The four subspaces *N* (*A*)*, C* (*A*)*, N* (*A*^T^)*, C* (*A*^T^)
> combine beautifully into the big picture of linear algebra. Figure A2
> shows how the nullspace *N* (*A*) is perpendicular to the row space
> *C* (*A*^T^). Every input vector *x* splits into a row space part
> *x~r~* and a nullspace part *x~n~*. Multiplying by *A* always(!)
> produces a vector in the column space. Multiplication goes from left
> to right in the picture, from *x* to *Ax* = *b*.
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image7.png){width="7.655511811023621e-2in"
> height="7.656933508311461e-2in"}*x~r~*

*x* = *x~r~* + *x~n~*

> column space
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image8.png){width="7.656933508311461e-2in"
> height="7.655511811023621e-2in"}*C*(*A*)
>
> multiples of (1*,* 3)

*x~n~*

> row space *C*(*A*^T^) nullspace *N* (*A*) multiples of (1*,* 2)
> multiples of (2*,* −1)

1 2

> *A* = 3 6
>
> nullspace *N* (*A*^T^) multiples of (3*,* −1)
>
> Figure A2: The four fundamental subspaces (lines) for the singular
> matrix *A*.
>
> On the right side are the column space *C* (*A*) and the fourth space
> *N* (*A*^T^). Again they are perpendicular. The columns are multiples
> of (1*,* 3) and the *y*'s are multi-ples of (3*,* 1). If *A* were an
> *m* by *n* matrix, its columns would be in *m*-dimensional space
> R*^m^* and so would the solutions to *A*^T^*y* = 0. Our singular 2 by
> 2 example has *m* = *n* = 2, and all four fundamental subspaces in
> Figure A2 are lines in R^2^.
>
> This ﬁgure needs more words. Each subspace contains inﬁnitely many
> vectors, or only the zero vector *x* = 0. If *u* is in a space, so are
> 10*u* and 100*u* (and most importantly 0*u*). We measure the
> *dimension* of a space not by the number of vectors, which is inﬁnite,
> but by *the number of independent vectors*. In this example each
> dimension is 1. A line has one independent vector but not two

#### Dimension and Basis {#dimension-and-basis .unnumbered}

> A full set of independent vectors is a "basis" for a space. This idea
> is important. The basis has as many independent vectors as possible,
> and their combinations ﬁll the space. A basis has not too many
> vectors, and not too few:
>
> Here are particular bases for R*^n^* among all the choices we could
> make:

+------------------------+---+----------------------------------------+
| > Standard basis       | = | > columns of the identity matrix       |
+========================+===+========================================+
| > General basis        | > | > columns of any invertible matrix     |
|                        |   |                                        |
|                        | = |                                        |
+------------------------+---+----------------------------------------+
| > Orthonormal basis    | > | > columns of any orthogonal matrix     |
|                        |   |                                        |
|                        | = |                                        |
+------------------------+---+----------------------------------------+

> The "dimension" of the space is the number of vectors in a basis.

#### Diﬀerence Matrices {#diﬀerence-matrices .unnumbered}

> Diﬀerence matrices with boundary conditions give exceptionally good
> examples of the four subspaces (and there is a physical meaning behind
> them). We choose forward and backward diﬀerences that produce 2 by 3
> and 3 by 2 matrices:
>
> *A* is imposing no boundary conditions (no rows are chopped oﬀ). Then
> *A*^T^ must impose two boundary conditions and it does: +1 disappeared
> in the ﬁrst row and 1 in the third row. *A*^T^*w* = *f* builds in the
> boundary conditions *w*~0~ = 0 and *w*~3~ = 0.
>
> The nullspace of *A* contains *x* = (1*,* 1*,* 1). Every constant
> vector *x* = (*c, c, c*) solves *Ax* = 0, and *the nullspace N* (*A*)
> *is a line* in three-dimensional space. The row space of *A* is the
> plane through the rows ( 1*,* 1*,* 0) and (0*,* 1*,* 1). Both vectors
> are perpendicular to (1*,* 1*,* 1) so the whole row space is
> perpendicular to the nullspace. Those two spaces are on the left side
> (the 3D side) of Figure A3.
>
> *C*(*A*^T^)

Row space

all *A*^T^*w*

> dim *r*
>
> dim *n* − *r*
>
> Perpendicular
>
> R*n x*^T^*A*^T^*w* = 0
>
> *x* in Nullspace
>
> *Ax* = 0
>
> *N* (*A*)
>
> Figure A3: Dimensions and orthogonality for any *m* by *n* matrix *A*
> of rank *r*. Figure A3 shows the Fundamental Theorem of Linear
> Algebra:
>
> The dimension *r* of the column space is the "rank" of the matrix. It
> equals the number of (nonzero) pivots in elimination. The matrix has
> full column rank when *r* = *n* and the columns are linearly
> independent; the nullspace only con-tains *x* = 0. Otherwise some
> nonzero combination *x* of the columns produces *Ax* = 0.
>
> The dimension of the nullspace is *n* − *r*. There are *n* unknowns in
> *Ax* = 0, and there are really *r* equations. Elimination leaves *n* −
> *r* columns without pivots. The corresponding unknowns are free (give
> them any values). This produces *n r*
>
> independent solutions to *Ax* = 0, a basis for the nullspace.
>
> A good basis makes scientiﬁc computing possible:
>
> 1 Sines and cosines 2 Finite elements 3 Splines 4 Wavelets A basis of
> eigenvectors is often the best.
>
> MIT OpenCourseWare
> [[http://ocw.mit.edu]{.underline}](http://ocw.mit.edu/)
>
> 18.085 Computational Science and Engineering I
>
> Fall 2008
>
> For information about citing these materials or our Terms of Use,
> visit:
> [[http://ocw.mit.edu/terms]{.underline}](http://ocw.mit.edu/terms).
>
> Gradient and Divergence / Parallel Table
>
> Gradient Divergence
>
> *v* = grad *u* = �*u* div *w* = � · *w* = 0

*�u �u*

> Potential *u*(*x, y*): *v*~1~ = *, v*~2~ =

*�s �s*

Stream function *s*(*x, y*): *w*~1~ = *, w*~2~ =

> *�x �y �y �x*

*�v*~2~ *�v*~1~ *�w*~1~ *�w*~2~

> Test on *v*: − = 0 Test on *w*: + = 0

*�x �y �x �y*

> Irrotational: zero vorticity Solenoidal: zero source
>
> Zero circulation around loops: Zero ﬂux through loops:
>
> � *v* · *t ds* = �
>
> *v*~1~ *dx* + *v*~2~ *dy* = 0
>
> � *w* · *n ds* = �
>
> *w*~1~ *dy* − *w*~2~ *dx* = 0
>
> Kirchhoﬀ's Voltage Law Kirchhoﬀ's Current Law Equipotentials *u*(*x,
> y*) = constant Streamlines *s*(*x, y*) = constant *v* is perpendicular
> to equipotentials *w* is tangent to streamlines
>
> Green-Gauss Formula
>
> �� *w* · grad *u dx dy* = ��
>
> *u*(− div *w*) *dx dy* + �
>
> *u w* · *n ds*
>
> (grad)^T^ = − div from integration by parts: (*Au*)^T^*w* =
> *u*^T^(*A*^T^*w*)
>
> Connections when (*v*~1~*, v*~2~) = (*w*~1~*, w*~2~)

1.  Equipotentials are perpendicular to streamlines

2.  Laplace's equation div(grad *u*) = *[�]{.underline}
    [�u]{.underline}* + *[�]{.underline} [�u]{.underline}* = � · �*u* =
    0

> *�x �x �y �y*
>
> *�u �s �u �s*

3.  Cauchy-Riemann equations = and = connecting *u* to *s*

> *�x �y �y �x*
>
> *�*^2^*s �*^2^*s �*^2^*u �*^2^*u*

4.  Laplace's equation for *s*

> *�x*2 + *�y*2

= − + = 0

*�x�y �y�x*

5.  Zero vorticity and zero source: Ideal potential ﬂow

6.  In two dimensions: *u*(*x, y*) + *is*(*x, y*) is a function *f*
    (*x* + *iy*)

# 3.5 Finite Diﬀerences and Fast Poisson Solvers {#finite-diﬀerences-and-fast-poisson-solvers .unnumbered}

> It is extremely unusual to use eigenvectors to solve a linear system
> *KU* = *F* . You need to know all the eigenvectors of *K*, and (much
> more than that) the eigenvector matrix *S* must be especially fast to
> work with. Both *S* and *S*^−1^ are required, because *K*^−1^ =
> *S*�^−1^*S*^−1^. The eigenvalue matrices � and �^−1^ are diagonal and
> quick. When the derivatives in Poisson's equation −*u~xx~* − *u~yy~* =
> *f* (*x, y*) are replaced by second diﬀerences, we do know the
> eigenvectors (discrete sines in the columns of *S*). Then the Fourier
> transform quickly inverts and multiplies by *S*.
>
> On a square mesh those diﬀerences have −1*,* 2*,* −1 in the
> *x*-direction and −1*,* 2*,* −1 in the *y*-direction (divided by *h* ,
> where *h* = meshwidth). Figure 3.20 shows how the second diﬀerences
> combine into a "5*-point molecule*" for the discrete Laplacian.
> Boundary values *u* = *u*~0~(*x, y*) are assumed to be given along the
> sides of a unit square.
>
> The square mesh has *N* interior points in each direction (*N* = 5 in
> the ﬁgure). In this case there are *n* = *N* ^2^ = 25 unknown mesh
> values *U~ij~* . When the molecule is centered at position (*i, j*),
> the discrete Poisson equation gives a row of *K*2D *U* = *F* :
>
> *K*2D U = F 4*uij* − *ui, j*−1 − *ui*−1*, j* − *ui*+1*, j* − *ui, j*+1
> = *h*^2^*f* (*ih, jh*) = *Fij .*(1)
>
> The inside rows of *K*2D have ﬁve nonzero entries 4*,* −1*,* −1*,*
> −1*,* −1. When (*i, j*) is next to a boundary point of the square, the
> known value of *u*~0~ at that neigh-boring boundary point moves to the
> right side of equation (1). It becomes part of the vector *F* , and a
> 1 drops out of the corresponding row of *K*. So *K*2D has ﬁve nonzeros
> on inside rows and fewer nonzeros on next-to-boundary rows.
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image9.png){width="0.1310126859142607in"
> height="0.1310126859142607in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image9.png){width="0.1310126859142607in"
> height="0.1310126859142607in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image10.png){width="0.1310126859142607in"
> height="0.1310126859142607in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image11.png){width="0.18301727909011373in"
> height="0.18301837270341206in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image12.png){width="0.1310126859142607in"
> height="0.1310126859142607in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image9.png){width="0.1310126859142607in"
> height="0.1310126859142607in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image13.png){width="0.1310126859142607in"
> height="0.1310126859142607in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image9.png){width="0.1310126859142607in"
> height="0.1310126859142607in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image14.png){width="0.18301727909011373in"
> height="0.18301837270341206in"}*N*

3

2

1

> 1 2 3 *N*
>
> Figure 3.20: 5-point molecules at inside points (fewer −1's next to
> boundary).
>
> *This matrix K*2D *is sparse*. Using blocks of size *N*, we can create
> the 2D matrix from the familiar *N* by *N* second diﬀerence matrix
> *K*. Number the nodes of the square a row at a time (this "natural
> numbering" is not necessarily best). Then the
>
> −1's for the neighbor above and the neighbor below are *N* positions
> away from the
>
> main diagonal of *K*2D. The 2D matrix is *block tridiagonal with
> tridiagonal blocks*:
>
> � 2 −1 ⎡ � *K* + 2*I* −*I* ⎡
>
> *K* = � −1
>
> 2 1
>
> · · ·
>
> ⎢ *K*2D = � −*I*
>
> *K* + 2*I I*
>
> · · ·
>
> ⎣⎢ (2)
>
> −1 2 −*I K* + 2*I*
>
> Size *N* Size *n* = *N* ^2^
>
> Bandwidth *w* = *N*
>
> Time *N* Space *nw* = *N* ^3^ Time *nw*^2^ = *N* ^4^
>
> The matrix *K*2D has 4's down the main diagonal in equation (1). Its
> bandwidth *w* = *N* is the distance from the main diagonal to the
> nonzeros in *I*. Many of the spaces in between are ﬁlled during
> elimination ! This is discussed in Section 6.1.
>
> Kronecker product One good way to create *K*2D from *K* and *I* is by
> the kron command. When *A* and *B* have size *N* by *N*, the matrix
> kron(*A, B*) is *N* ^2^ by *N*^2^. *Each number a~ij~ is replaced by
> the block a~ij~ B*.
>
> To take second diﬀerences in all rows at the same time, kron(*I, K*)
> produces a block diagonal matrix of *K*'s. In the *y*-direction,
> kron(*K, I*) multiplies −1 and 2 and
>
> −1 by *I* (dealing with a column of meshpoints at a time). Add *x* and
> *y* diﬀerences:
>
> �*K* ⎡ � 2*I* −*I* · ⎡
>
> *K*2D = kron(*I, K*) + kron(*K, I*) = � *K* ⎣ + �−*I* 2*I* · ⎣ (3)
>
> *This sum agrees with the* 5*-point matrix in* (2). The computational
> question is how to work with *K*2D. We will propose three methods:

1.  Elimination in a good order (not using the special structure of
    *K*2D)

2.  Fast Poisson Solver (applying the FFT = Fast Fourier Transform)

3.  Odd-Even Reduction (since *K*2D is block tridiagonal).

> The novelty is in the Fast Poisson Solver, which uses the known
> eigenvalues and eigenvectors of *K* and *K*2D. It is strange to solve
> linear equations *KU* = *F* by expanding *F* and *U* in eigenvectors,
> but here it is extremely successful.

### Elimination and Fill-in {#elimination-and-fill-in .unnumbered}

> For most two-dimensional problems, elimination is the way to go. The
> matrix from a partial diﬀerential equation is sparse (like *K*2D). It
> is banded but the bandwidth is not so small. (Meshpoints cannot be
> numbered so that all ﬁve neighbors in the molecule receive nearby
> numbers.) Figure 3.21 has points 1*, . . . , N* along the ﬁrst row,
> then a row at a time going up the square. *The neighbors above and
> below point j have numbers j* − *N and j* + *N*.
>
> Ordering by rows produces the −1's in *K*2D that are *N* places away
> from the diagonal. The matrix *K*2D has bandwidth *N*. The key point
> is that elimination
>
> ﬁlls in the zeros inside the band. We add row 1 (times
>
> ^[1]{.underline}^) to row 2, to eliminate
>
> the −1 in position (2*,* 1). But the last −1 in row 1 produces a new −
> [1]{.underline} in row 2. A zero inside the band has disappeared. As
> elimination continues from *A* to *U* , virtually the whole band is
> ﬁlled in.
>
> In the end, *U* has about 5 times 25 nonzeros (this is *N* ^3^, the
> space needed to store *U* ). There will be about *N* nonzeros next to
> the pivot when we reach a typical row, and *N* nonzeros below the
> pivot. Row operations to remove those nonzeros will require up to *N*
> ^2^ multiplications, and there are *N* ^2^ pivots. So the count of
> multiplications is about 25 times 25 (this is *N* ^4^, for elimination
> in 2D).
>
> Figure 3.21: Typical rows of *K*2D have 5 nonzeros. Elimination ﬁlls
> in the band.
>
> Section 6.1 will propose a diﬀerent numbering of the meshpoints, to
> reduce the ﬁll-in that we see in *U* . This reorders the rows of *K*2D
> by a permutation matrix *P* , and the columns by *P* ^T^. The new
> matrix *P* (*K*2D)*P* ^T^ is still symmetric, but elimination (with
> ﬁll-in) proceeds in a completely diﬀerent order. The MATLAB command
> symamd(*K*) produces a nearly optimal choice of *P* .
>
> Elimination is fast in two dimensions (but a Fast Poisson Solver is
> faster !). In three dimensions the matrix size is *N* ^3^ and the
> bandwidth is *N* ^2^. By numbering the nodes a plane at a time,
> vertical neighbors are *N* ^2^ nodes apart. The operation count for
> elimination becomes *N* ^7^, which can be seriously large. Chapter 6
> on *Solving Large Systems* will introduce badly needed alternatives to
> elimination in 3D.

### Solvers Using Eigenvalues {#solvers-using-eigenvalues .unnumbered}

> Our matrices *K* and *K*2D are extremely special. We know the
> eigenvalues and eigen-vectors of the second-diﬀerence matrix *K*. The
> eigenvalues have the special form
>
> *�* = 2 2 cos *∂*, and the eigenvectors are discrete sines. There will
> be a similar pattern for *K*2D, which is formed in a neat way from *K*
> (by Kronecker product). The Poisson Solver uses those eigenvalues and
> eigenvectors to solve (*K*2D)(*U* 2D) = (*F* 2D). On a square mesh it
> is much faster than elimination.
>
> Here is the idea, ﬁrst in one dimension. The matrix *K* has
> eigenvalues *�*~1~*, . . . , �~N~*
>
> and eigenvectors *y*~1~*, . . . , y~N~* . There are three steps to the
> solution of *KU* = *F* :
>
> The success of the method depends on the speed of steps 1 and 3. Step
> 2 is fast.
>
> To see that *U* in step 3 is correct, *multiply it by the matrix K*.
> Every eigenvector gives *Ky* = *�y*. That cancels the *�* in each
> denominator. The result is that *KU* agrees with the vector *F* in
> step 1.
>
> Now look at the calculation required in each step, using matrices.
> Suppose *S* is the eigenvector matrix, with the eigenvectors *y*~1~*,
> . . . , y~N~* of *K* in its columns. Then the coeﬃcients *a*~1~*, . .
> . , a~N~* come by solving *Sa* = *F* :
>
> � ⎡ � *a*1 ⎡
>
> Step 1 Solve *Sa* = *F* � *y* · · · *y* ⎣ � . ⎢ = *a y* + · · · + *a
> y* = *F .* (4)
>
> 1 *N* . 1 1 *N N*
>
> *a~N~*
>
> Thus *a* = *S*^−1^*F* . Then step 2 divides the *a*'s by the *�*'s to
> ﬁnd �^−1^*a* = �^−1^*S*^−1^*F* . (The eigenvalue matrix � is just the
> diagonal matrix of *�*'s.) Step 3 uses those coeﬃcients *a~k~/�~k~* in
> recombining the eigenvectors into the solution vector *U* :

� ⎡ � *a*~1~*/�*~1~ ⎡

> Step 3 *U* = � *y*~1~
>
> · · · *y~N~*
>
> .
>
> *a~N~ /�~N~*
>
> ⎢⎣ = *S*�^−1^*a* = *S*�^−1^*S*^−1^*F .* (5)
>
> You see the matrix *K*^−1^ = *S*�^−1^*S*^−1^ appearing in that last
> formula. We have *K*^−1^*F* because *K* itself is *S*�*S*^−1^---the
> usual diagonalization of a matrix. The eigenvalue method is using this
> *S*�*S*^−1^ factorization instead of *K* = *LU* from elimination.
>
> The speed of steps 1 and 3 depends on multiplying quickly by *S*^−1^
> and *S*. Those are full matrices, not sparse like *K*. Normally they
> both need *N* ^2^ operations in one dimension (where the matrix size
> is *N*). But the "sine eigenvectors" in *S* give the Discrete Sine
> Transform, and the *Fast Fourier Transform* executes *S* and *S*^−1^
> in *N* log~2~ *N* steps. In one dimension this is not as fast as *cN*
> from elimination, but in two dimensions *N* ^2^ log(*N*^2^) easily
> wins.
>
> Column *k* of the matrix *S* contains the eigenvector *y~k~*. The
> number *S~jk~* = sin *[^jk�^]{.underline}* is the *j*th component of
> that eigenvector. For our example with *N* = 5 and *N* +1 = 6, you
> could list the sines of every multiple of *�/*6. Here are those
> numbers:
>
> 1 �3 �3 1
>
> Sines
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} *, ,* 1*, ,*
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"}*,* 0*,* (repeat with minus signs)
> (repeat 12 numbers forever) *.*
>
> 2 2 2 2
>
> The *k*th column of *S* (*k*th eigenvector *y~k~*) takes every *k*th
> number from that list:
>
> ��[1]{.underline}*/*2 ⎡ �
>
> �[3]{.underline}*/*2⎡ �
>
> 1 ⎡ � �[3]{.underline}*/*2⎡ � [1]{.underline}*/*2 ⎡

3*/*2

> �3*/*2
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image16.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} ⎢ �
>
> 0 ⎢ �−�3*/*2⎢ �−�3*/*2⎢

*y*~1~ =

> *y*~2~ = *y*~3~ = −1 *y*~4~ =
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image16.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"}� ⎢ � ⎢ � � ⎢
>
> *y*~5~ =
>
> � 3*/*2⎣ �−�[3]{.underline}*/*2 ⎣ � 0⎣ � �[3]{.underline}*/*2⎣ �−
> 3*/*2 ⎣
>
> 1*/*2 − 3*/*2 1 −
>
> 3*/*2
>
> 1*/*2
>
> Those eigenvectors are orthogonal ! This is guaranteed by the
> symmetr�y [o]{.underline}f *K*. All
>
> these eigenvectors have length�[3]{.underline} = (*N* + 1)*/*2.
> Dividing each column by 3, we have

*orthonormal eigenvectors*. *S/* 3 is an orthogonal matrix *Q*, with
*Q*^T^*Q* = *I*.

> In this special case, *S* and *Q* are also symmetric. So *Q*^−1^ =
> *Q*^T^ = *Q*.
>
> Notice that *y~k~* has *k* − 1 changes of
> sig�n.![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image17.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"}It comes from *k* loops of the�si
> [n]{.underline}e curve.
>
> The eigenvalues are increasing: *�* = 2 − 3*,* 2 − 1*,* 2 − 0*,* 2 +
> 1*,* 2 + 3. Those
>
> eigenvalues add to 10, which is the sum down the diagonal (the
> *trace*) of *K*~5~. The
>
> product of the 5 eigenvalues (easiest by pairs) conﬁrms that
> det(*K*~5~) = 6.

### Fast Poisson Solvers {#fast-poisson-solvers .unnumbered}

> To extend this eigenvalue method to two dimensions, we need the
> eigenvalues and eigenvectors of *K*2D. The key point is that the *N*
> ^2^ eigenvectors of *K*2D are *separable*. Each eigenvector *y~kl~*
> separates into a product of sines:
>
> When you multiply that eigenvector by *K*2D, you have second
> diﬀerences in the *x*-direction and *y*-direction. The second
> diﬀerences of the ﬁrst sine (*x*-direction) produce a factor *�~k~* =
> 2 − 2 cos *[^k�^]{.underline}* . This is the eigenvalue of *K* in 1D.
> The second diﬀerences of the other sine (*y*-direction) produce a
> factor *�~l~* = 2 − 2 cos *[^l�^]{.underline}* . So the eigenvalue in
> two dimensions is the sum *�~k~* + *�~l~* of one-dimensional
> eigenvalues:
>
> Now the solution of *K*2D U = F comes by a *two-dimensional sine
> transform*:
>
> *F* = ⎤ ⎤ *a* sin *[ik�]{.underline}* sin *[jl�]{.underline} U* = ⎤ ⎤
> *[akl]{.underline}* sin *[ik�]{.underline}* sin *[jl�]{.underline}*
> (8)
>
> Again we ﬁnd the *a*'s, divide by the *�*'s, and build *U* from the
> eigenvectors in *S*:
>
> Swartztrauber \[SIAM Review 19 (1977) 490\] gives the operation count
> 2*N* ^2^ log~2~ *N*. This uses the Fast Sine Transform (based on the
> FFT) to multiply by *S*^−1^ and *S*. The Fast Fourier Transform is
> explained in Section 4.3.
>
> Note We take this chance to notice the good properties of a Kronecker
> product *C* = kron(*A, B*). Suppose *A* and *B* have their
> eigenvectors in the columns of *S~A~* and *S~B~* . The eigenvalues are
> in �*~A~* and �*~B~* . Then we know *S~C~* and �*~C~* :
>
> *The eigenvectors of* kron(*A, B*) *are in* kron(*S~A~, S~B~*)*.*
>
> *The eigenvalues are in* kron(�*~A~,* �*~B~*)*.*
>
> \(9\)
>
> The diagonal blocks in kron(�*~A~,* �*~B~*) are entries *�~k~*(*A*)
> times the diagonal matrix �*~B~*. So the eigenvalues *�~kl~* of *C*
> are just the products *�~k~*(*A*)*�~l~*(*B*).
>
> In our case *A* and *B* were *I* and *K*. The matrix *K*2D added the
> two products kron(*I, K*) and kron(*K, I*). Normally we cannot know
> the eigenvectors and eigen-values of a matrix sum---except when the
> matrices commute. Since all our matrices are formed from *K*, *these
> Kronecker products do commute*. This gives the separable eigenvectors
> and eigenvalues in (6) and (7).

### Cyclic Odd-Even Reduction {#cyclic-odd-even-reduction .unnumbered}

> There is an entirely diﬀerent (and very simple) approach to KU = F. I
> will start in one dimension, by writing down three rows of the usual
> second diﬀerence equation:
>
> Row *i* − 1 −*U~i~*~−2~ + 2*U~i~*~−1~ − *U~i~* = *F~i~*~−1~
>
> Row *i* −*U~i~*~−1~ + 2*U~i~* − *U~i~*~+1~ = *F~i~* (10) Row *i* + 1
> −*U~i~* + 2*U~i~*~+1~ − *U~i~*~+2~ = *F~i~*~+1~
>
> Multiply the middle equation by 2, and add. *This eliminates U~i~*~−1~
> *and U~i~*~+1~:
>
> Now we have a half-size system, involving only half of the *U* 's
> (with even indices). The new system (11) has the same tridiagonal form
> as before. When we repeat, *cyclic reduction produces a quarter-size
> system*. Eventually we can reduce *KU* = *F* to a very small problem,
> and then cyclic back-substitution produces the whole solution.
>
> How does this look in two dimensions ? The big matrix *K*2D is block
> triangular:
>
> � *A* −*I* ⎡
>
> *K*2D = � −*I*
>
> *A I*
>
> · · ·
>
> −*I A*
>
> ⎣⎢ with *A* = *K* + 2*I* from equation (4) *.* (12)
>
> The three equations in (10) become *block equations for whole rows of
> N mesh values*. We are taking the unknowns U*~i~* = (*U~i~*~1~*, . . .
> , U~iN~* ) a row at a time. If we write three rows of (10), the block
> *A* replaces the number 2 in the scalar equation. The block
>
> −*I* replaces the number −1. To reduce (*K*2D)(*U* 2D) = (*F* 2D) to a
> half-size system, multiply the middle equation (with *i* even) by *A*
> and add the three block equations:
>
> Reduction in 2D −*I*U*i*−2 + (*A*^2^ − 2*I*)U*i* − *I*U*i*+2 =
> F*i*−1 + *A*F*i* + F*i*+1 *.* (13)
>
> The new half-size matrix is still block tridiagonal. *The diagonal
> blocks that were previously A in* (12) *are now A*^2^ 2*I*, with the
> same eigenvectors. The unknowns are the ^[1]{.underline}^ *N*^2^
> values *U~i,j~* at meshpoints with even indices *i*.
>
> The bad point is that each new diagonal block *A*^2^ 2*I* has *ﬁve
> diagonals*, where the original block *A* = *K* +2*I* had three
> diagonals. This bad point gets worse as cyclic
>
> reduction continues. At step *r*, the diagonal blocks become *A~r~* =
> *A*^2^ − 2*I* and their

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.166557305336833e-2in"
height="6.666666666666667e-3in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.166557305336833e-2in"
height="6.666666666666667e-3in"}*r*−1

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.166557305336833e-2in"
height="6.666666666666667e-3in"}
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.166557305336833e-2in"
height="6.666666666666667e-3in"} 2

> bandwidth doubles. We could ﬁnd tridiagonal factors (*A*− 2*I*)(*A*+
> 2*I*) = *A* − 2*I*,
>
> but the number of factors grows quickly. Storage and computation and
> roundoﬀ error are increasing too rapidly with more reduction steps.
>
> Stable variants of cyclic reduction were developed by Buneman and
> Hockney. The clear explanation by Buzbee, Golub, and Nielson \[SIAM
> Journal of Numerical Anal-ysis 7 (1970) 627\] allows other boundary
> conditions and other separable equations, coming from polar
> coordinates or convection terms like *C�u/�x* + *D�u/�y*. After *m*
> steps of cyclic reduction, Hockney went back to a Fast Poisson Solver.
>
> This combination FACR(*m*) is widely used, and the optimal number of
> cyclic reduction steps (before the FFT takes over) is small. For *N* =
> 128 a frequent choice is *m* = 2. Asymptotically *m*opt grows like log
> log *N* and the operation count for FACR(*m*opt) is 3*N* ^2^ log log
> *N*. In practical scientiﬁc computing with *N* ^2^ unknowns (or with
> *N* ^3^ unknowns in three dimensions), a Fast Poisson Solver is a
> winner.
>
> \*\*\*\*\*\* Add code for Fast Poisson \*\*\*\*\*\*\*

### Problem Set 3.5 {#problem-set-3.5 .unnumbered}

> Problems 1-- are for readers who get enthusiastic about kron.

1.  Why is the transpose of *C* = kron(*A, B*) equal to kron(*A*^T^*,
    B*^T^) ? Why is the inverse equal to *C*^−1^ = kron(*A*^−1^*,
    B*^−1^) ? You have to transpose each block *a~ij~ B* of the
    Kronecker product *C*, and then patiently multiply *CC* ^−1^ by
    blocks.

> *C* is symmetric (or orthogonal) when *A* and *B* are symmetric (or
> orthogonal).

2.  Why is the matrix *C* = kron(*A, B*) times the matrix *D* = kron(*S,
    T* ) equal to *CD* = kron(*AS, BT* ) ? This needs even more patience
    with block multiplica-tion. The inverse *CC*^−1^ = kron(*I, I*) =
    *I* is a special case.

> Note Suppose *S* and *T* are eigenvector matrices for *A* and *B*.
> From *AS* = *S*�*~A~* and *BT* = *T* �*~B~* we have *CD* = kron(*AS,
> BT* ) = kron(*S*�*~A~, T* �*~B~*). Then *CD* = *D* kron(�*~A~,*
> �*~B~*) = *D*�*~C~* . So *D* = kron(*S, T* ) is the eigenvector matrix
> for *C*.
>
> Chapter 5
>
> Initial Value Problems

# Finite Diﬀerence Methods

> We don't plan to study highly complicated nonlinear diﬀerential
> equations. Our ﬁrst goal is to see why a diﬀerence method is
> successful (or not). The crucial questions of stability and accuracy
> can be clearly understood for linear equations. Then we can construct
> diﬀerence approximations to a great variety of practical problems.
>
> Another property we need is computational speed. That depends partly
> on the complexity of the equation *u*^�^ = *f* (*u, t*). Often we
> measure speed by the number of times that *f* (*u, t*) has to be
> computed in each time step (that number could be one). When we turn to
> *implicit* methods and *predictor-corrector* methods, to improve
> stability, the cost per step goes up but we gain speed with a larger
> step �*t*.
>
> This chapter begins with basic methods (forward Euler, backward Euler)
> and then improves. Each time, we test stability on *u*^�^ = *a u*.
> When *a* is negative, �*t* is often
>
> limited by −*a* �*t* ↑ *C*. This has an immediate eﬀect: the equation
> with *a* = −99 requires a much smaller �*t* than *a* = −1. Let me
> organize the equations as scalar and vector, nonlinear in general or
> linear with constant coeﬃcients *a* and *A*:
>
> For an ordinary diﬀerential equation *u*^�^ = *f* (*u, t*), good codes
> will increase the accuracy (and keep stability) far beyond the
> *O*(�*t*) error in Euler's methods. You can rely on freely available
> software like ode45 to make the two crucial decisions:

1.  to choose an accurate diﬀerence method (and change the formula
    adaptively)

2.  to choose a stable time step (and change �*t* adaptively).

> We will introduce accurate methods, and ﬁnd the stability limits on
> �*t*.
>
> �c 2006 Gilbert Strang

### Stiﬀ Diﬀerential Equations {#stiﬀ-diﬀerential-equations .unnumbered}

> First we call attention to one extra question: *Is the equation stiﬀ
> ?* Let me begin with a made-up example to introduce stiﬀness and its
> eﬀects:
>
> *v*(*t*) = *e*^−*t*^ + *e*^−99*t*^
>
> � �
>
> controls decay controls �*t*
>
> The step �*t* is 99 times smaller because of *e*^−99*t*^ that
> disappears anyway
>
> Those decay rates −1 and −99 could be the eigenvalues of *A*, as in
> Example 1.
>
> Example 1
>
> *[d]{.underline}* *v* � = −50 49 � *v* � with *v*(0) � = 2 � *.* (1)
>
> *dt w* 49 −50 *w w*(0) 0
>
> The solution has *v*(*t*) = *e*^−*t*^ + *e*^−99*t*^ and *w*(*t*) =
> *e*^−*t*^ − *e*^−99*t*^. The time scales are diﬀerent by a factor of
> 99 (the condition number of *A*). The solution will decay at the slow
> time scale of *e*^−*t*^, but computing *e*^−99*t*^ may require a very
> small �*t* for stability.
>
> It is frustrating to have �*t* controlled by the component that is
> decaying so fast.
>
> Any explicit method will have a requirement 99�*t* ↑ *C*. We will see
> how this happens and how an implicit method (like ode15s and od23t in
> MATLAB) can avoid it.
>
> Trefethen \[ \] points to these applications where stiﬀness comes with
> the problem:

1.  Chemical kinetics (reactions go at very diﬀerent speeds)

2.  Control theory (probably the largest application area for MATLAB)

3.  Circuit simulation (components respond at widely diﬀerent time
    scales)

4.  Method of Lines (large systems come from partial diﬀerential
    equations).

> Example 2 The *N* by *N* second diﬀerence matrix *K* produces a large
> stiﬀ system:
>
> Method of Lines
>
> *du* −*Ku*
>
> =
>
> has
>
> *dui* = *ui*+1 − 2*ui* + *ui*−1 *.* (2)
>
> *dt* (�*x*)2 *dt* (�*x*)2
>
> This comes from the heat equation *�u/�t* = *�*^2^*u/�x*^2^, by
> discretizing only the space derivative. Example 1 had eigenvalues −1
> and −99, while Example 2 has *N* eigenvalues---but the diﬃculty is
> essentially the same ! The most negative eigenvalue here is about *a*
> = −4*/*(�*x*)^2^. So a small �*x* (for accuracy) will require a *very
> small* �*t* (for stability).
>
> This "semidiscrete" method of lines is an important idea. Discretizing
> the space variables ﬁrst produces a large system that can be given to
> an ODE solver. (We have ordinary diﬀerential equations in time.) If it
> wants to, that solver can vary the time step �*t* and even the
> discretization formula as *u*(*t*) speeds up or slows down.
>
> This method splits the approximation of a PDE into two parts. Finite
> diﬀerences/ﬁnite elements in earlier chapters produce the ﬁrst part
> (discrete in space). The upcoming stability-accuracy analysis applies
> to the second part (discrete in time). This idea is very simple and
> useful, even if it misses the good methods later in this chapter that
> take full advantage of space-time. For the heat equation *u~t~* =
> *u~xx~*, the useful fact *u~tt~* = *u~xxxx~* allows us to cancel space
> errors with time errors---which we won't notice when they are
> separated in the semidiscrete method of lines.

### Forward Euler and Backward Euler {#forward-euler-and-backward-euler .unnumbered}

> The equation *u* � = *f* (*u, t*) starts from an initial value *u*(0).
> The key point is that the rate of change *u*^�^ is determined by the
> current state *u* at any moment *t*. This model of reality, where all
> the history is contained in the current state *u*(*t*), is a
> tremendous success throughout science and engineering. (It makes
> calculus almost as important as linear algebra.) But for a computer,
> continuous time has to change to discrete time. One diﬀerential
> equation allows many diﬀerence equations!
>
> The simplest method (Euler is pronounced "Oiler") uses a forward
> diﬀerence:

*Un*+1 − *Un*

> Forward Euler = *f* (*U~n~, t~n~*) is *U~n~*~+1~ = *U~n~* + �*tf~n~ .*
> (3)

�*t*

> Over each �*t* interval, the slope of *U doesn't change*. Figure 5.1
> shows how the correct solution to *u*^�^ = *au* follows a smooth
> curve, while *U* (*t*) is only piecewise linear. A better method
> (higher accuracy) will stay much closer to the curve by using more
> information than the one slope *f~n~* = *f* (*U~n~, t~n~*) at the
> start of the step.
>
> replacements
>
> *u*(0) = 1

�*t*

> *u* = *e*�*t*
>
> *U* = 1 + �*t* (forward)
>
> *t t*
>
> Figure 5.1: Forward Euler and Backward Euler for *u*^�^ = *u*.
> One-step errors � ^[1]{.underline}^ (�*t*)^2^.
>
> Backward Euler comes from using *f~n~*~+1~ *at the end of the step*,
> when *t* = *t~n~*~+1~:

*Un*+1 − *Un*

> Backward Euler = *f* (*U~n~*~+1~*, t~n~*~+1~) is *U~n~*~+1~ −
> �*tf~n~*~+1~ = *U~n~ .* (4)

�*t*

> This is an *implicit method*. To ﬁnd *U~n~*~+1~, we have to solve
> equation (4). When
>
> *f* is linear in *u*, we are solving a linear system at each step (and
> the cost is low if
>
> the matrix is tridiagonal, like *I* − �*t K* in Example 2). We will
> comment later on iterations like Newton's method or
> predictor-corrector in the nonlinear case.
>
> The ﬁrst example to study is the linear scalar equation *u* � = *au*.
> Compare forward and backward Euler, for one step and for *n* steps:
>
> Forward *U~n~*~+1~ = (1 + *a* �*t*)*U~n~* leads to *U~n~* = (1 + *a*
> �*t*)*^n^U*~0~ *.* (5)
>
> Backward (1 − *a* �*t*)*U* = *U* leads to *U* = (1 − *a* �*t*)^−*n*^*U
> .* (6) Forward Euler is like compound interest, at the rate *a*. Each
> step starts with *U~n~* and adds the interest *a* �*t U~n~*. As the
> stepsize �*t* goes to zero and we need *T/*�*t* steps to reach time
> *T* , this discrete compounding approaches continuous compounding. The

�

> discrete solution *U~n~* approaches the continuous solution of *u* =
> *au*:
>
> (1 + *a* �*t*)*^T^ ^/^*^�*t*^ approaches *e^aT^* as �*t* � 0 *.*
>
> This is the convergence of *U* to *u* that we will prove below, more
> generally. It holds for backward Euler too, because (1 − *a* �*t*)^−1^
> = 1 + *a*�*t* + higher order terms.
>
> The stability question arises for very negative *a*. The true solution
> *e*^−*at*^*u*(0) is extremely stable, approaching zero. (If this is
> your own money, you should change
>
> banks and get *a \>* 0.) Backward Euler will be stable because it
> divides by 1 − *a* �*t* (which is greater than 1 when *a* is
> negative). *Forward Euler will explode if* 1 + *a* �*t is smaller
> than* −1*, because its powers grow exponentially* :
>
> Instability 1 + *a* �*t \<* −1 when *a* �*t \<* −2 (7)
>
> 1+*a*�*t* −1 1
>
> That is a pretty sharp borderline between stability and instability,
> at −*a* �*t* = 2. For
>
> *u* � = −20*u* which has *a* = −20, the borderline is �*t* =
> ^[2]{.underline}^ = ^[1]{.underline}^ . Compare the results
>
> at time *T* = 2 from �*t* = ^[1]{.underline}^ (22 steps) and �*t* =
> ^[1]{.underline}^ (18 steps):
>
> 11 9
>
> [1]{.underline} �
>
> [9]{.underline} �22
>
> [1]{.underline} � [11]{.underline} �18
>
> Unstable �*t* = (1 + *a* �*t*)^18^ = − � 37*.*043
>
> 9 9
>
> I would describe backward Euler as absolutely stable (A-stable)
> because it is stable whenever Re *a \<* 0. Only an implicit method can
> be A-stable. Forward Euler is a stable method(!) because it succeeds
> as �*t* � 0. For small enough �*t*, it is on the stable side of the
> borderline.
>
> In this example a *good quality approximation* requires more than
> stability (even
>
> �*t* = ^[1]{.underline}^ is too big). Those powers of −
> ^[9]{.underline}^ alternate in sign, while *e*^−20*t*^ stays positive.

### Accuracy and Convergence {#accuracy-and-convergence .unnumbered}

> Since forward and backward diﬀerences are *ﬁrst order accurate*, it is
> no surprise that the errors from forward and backward Euler are
> *O*(�*t*). This error *e* = *u* − *U* is
>
> replacements

*t*

> *u* = *e*−�*t*

*t*

> �*t* too big

*U* = 1 − �*t \<* −1

> Figure 5.2: Forward Euler (stable and unstable, with −*a*�*t* going
> above 2).
>
> measured at a ﬁxed time *T* . As �*t* decreases, so does the new error
> added at each step. But the number of steps to reach that time
> increases, keeping *n* �*t* = *T* .
>
> To see why the error *u*(*T* ) − *U* (*T* ) is *O*(�*t*), the key is
> stability. We need to know that *earlier errors don't increase as they
> are carried forward to time T* . Forward Euler is the simplest
> diﬀerence equation, so it is the perfect example to follow through
> ﬁrst.
>
> (The next sections will apply the same idea to partial diﬀerential
> equations.) Euler's diﬀerence equation for *u*^�^ = *f* (*u, t*) =
> *au* is
>
> *U~n~*~+1~ = *U~n~* + �*tf* (*U~n~, t~n~*) = *U~n~* + *a* �*t U~n~ .*
> (8) The true solution at time *n* �*t* satisﬁes (8) except for a
> discretization error DE:

*un*+1

> = *u~n~*
>
> \+ �*tu*^�^ + DE = *u*
>
> \+ *a* �*tu~n~*
>
> \+ DE

*n*+1

> *.* (9)
>
> That error DE is of order (�*t*)^2^ because the second-order term is
> missing (it
>
> should be
>
> ^[1]{.underline}^ (�*t*)^2^*u*^��^, but Euler didn't keep it).
> Subtracting (8) from (9) gives a
>
> 2 *n*

diﬀerence equation for the error *e* = *u* − *U* , propagating forward
in time:

> Error equation *e~n~*~+1~ = *e~n~* + *a* �*te~n~* + DE~*n*+1~ *.* (10)
>
> You could think of this one-step error DE~*n*+1~ as a deposit like
> (�*t*)^2^ into your account. Once the deposit is made, it will grow or
> decay according to the error equation. To reach time *T* = *N* �*t*,
> each error DE*~k~* at step *k* has *N* − *k* more steps to go:
>
> *e* = (1 + *a* �*t*)*^N^* ^−1^ DE + · · · + (1 + *a* �*t*)*^N^* ^−*k*^
> DE
>
> \+ · · · + DE*~N~ .* (11)
>
> Now stability plays its part. If *a* is negative, those powers are all
> less than 1 (in absolute value)---*provided* 1 + *a* �*t does not go
> below* −1. If *a* is positive, those
>
> powers of 1 + *a* �*t* are all less than (*e^a^* ^�*t*^)*^N^* =
> *e^aT^* . Then the error *e~N~* has *N* terms
>
> in (11), and every term is less than *c*(�*t*)^2^ for a ﬁxed constant
> *c*:
>
> Error bound \|*e~N~* \| = \|*u~N~* − *U~N~* \| � *N c* (�*t*)^2^ = *c
> T* �*t .* (12)
>
> The errors along the way, of size (�*t*)^2^, combined after *N* =
> *T/*�*t* steps into an overall �*t* error. This depended on
> stability---the local errors didn't explode.
>
> Notice that the error growth follows the diﬀerence equation in (10),
> not the dif-ferential equation. The stiﬀ example with *a* �*t* =
> (−20)( ^[1]{.underline}^ ) gave a large 1 + *a* �*t*, even when *e^a^*
> ^�*t*^ was small. We still call forward Euler a stable method, because
> as soon as �*t* is small enough the danger has passed. Backward Euler
> also gives
>
> \|*e~N~* \| = *O*(�*t*). The problem with these ﬁrst-order methods is
> their low accuracy.
>
> The local discretization error DE tells us the accuracy. For Euler
> that error DE � ^[1]{.underline}^ (�*t*)^2^*u* �� is the ﬁrst term
> that Euler misses in the Taylor series for *u*(*t* + �*t*). Better
> methods will capture that term exactly, and miss on a higher-order
> term. The
>
> discretization error (we ﬁnd it by comparing *u*(*t*+�*t*) with
> *U~n~*~+1~, assuming *u*(*t*) agrees with *U~n~*) begins with a power
> (�*t*)^*p*+1^:
>
> The method decides *c* and *p* + 1. With stability, *T/*�*t* steps
> give a global error of order (�*t*)*^p^*. The derivative of *u* shows
> whether the problem is hard or easy.
>
> Error estimates like (13) appear everywhere in numerical analysis. The
> 1*,* −2*,* 1 second diﬀerence has error ^[1]{.underline}^ (�*x*)^4^*u*
> ����. Partial diﬀerential equations (Laplace, wave,
>
> heat) produce similar terms. In one line we ﬁnd *c* = −
> ^[1]{.underline}^ for *backward Euler* :

� � �

> (�*t*)^2^
>
> ���
>
> � ��
>
> (�*t*)^2^ ��
>
> The global estimate \|*u* − *U* \| ↑ *C* �*t* max \|*u* ��\| shows no
> error when *u* is linear and
>
> *u* �� is zero (Euler's approximation of constant slope becomes true).
> For nonlinear
>
> equations, the key is in the subtraction of (8) from (9). A
> "Lipschitz" bound *L* on
>
> *�f /�u* replaces the number *a* in the error equation:
>
> \|*f* (*u, t*) − *f* (*U, t*)\| ↑ *L*\|*u* − *U* \| gives *e~n~*~+1~ ↑
> (1 + *L*�*t*) *e~n~* + DE~*n*+1~ *.* (15)

### Second-Order Methods {#second-order-methods .unnumbered}

> Here is a ﬁrst way to increase the accuracy. We could center the
> equation at the midpoint (*n* + ^[1]{.underline}^ )�*t* of the step,
> by averaging *f* (*U~n~, t~n~*) and *f* (*U~n~*~+1~*, t~n~*~+1~). The
> result is an *implicit second-order method* use in MATLAB's ode23t:
>
> *U~n~*~+1~ − *U~n~* 1
>
> Trapezoidal rule/Crank-Nicolson =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.500546806649168e-2in"
> height="6.666666666666667e-3in"}(*f~n~*~+1~ + *f~n~*) *.* (16)
>
> �*t* 2

So *U* − ^[1]{.underline}^ �*tf* = *U* + ^[1]{.underline}^ �*tf* . For
our model *u*^�^ = *f* (*u*) = *au*, this is

> *n*+1 2 *n*+1 *n* 2 *n*
>
> [1]{.underline} [1]{.underline} � 1 + ^[1]{.underline}^ *a* �*t* �
>
> (1 − *a* �*t*) *U~n~*~+1~ = (1 + *a* �*t*) *U~n~* which gives
> *U~n~*~+1~ = ^2^ *U~n~ .* (17)
>
> 2 2 1 − ^[1]{.underline}^ *a* �*t*
>
> The true solution has *u~n~*~+1~ = *e^a^*^�*t*^*u~n~*. Problem 1 will
> ﬁnd DE � (�*t*)^3^. The equation is stable. So *N* = *T/*�*t* steps
> produce \|*e~N~* \| = \|*u~N~* − *U~N~* \| ↑ *cT* (�*t*)^2^.
>
> How to improve forward Euler and still keep it explicit ? We don't
> want *U~n~*~+1~ on the right side of the equation, but we are happy
> with *U~n~*~−1~ (from the previous step !). Here is a combination that
> gives second-order accuracy in a two-step method:
>
> *U~n~*~+1~ − *U~n~* 3 1
>
> "Adams-Bashforth" =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image19.png){width="9.500546806649168e-2in"
> height="6.666666666666667e-3in"} *f* (*U~n~, t~n~*) −
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.500546806649168e-2in"
> height="6.666666666666667e-3in"} *f* (*U~n~*~−1~*, t~n~*~−1~) *.* (18)
>
> �*t* 2 2
>
> Remember that *f* (*U~n~*~−1~*, t~n~*~−1~) is already computed in the
> previous step, going from *n*−1 to *n*. So this explicit multistep
> method requires no extra work, and improves the accuracy. To see how
> (�*t*)^2^ comes out correctly, write *u*^�^ for *f* :
>
> 3 *u*^�^ − 1 *u*^�^ � 3 *u*^�^ − 1 (*u*^�^ − �*tu*^��^ ) = *u*^�^ + 1
> �*tu*^��^ *.*
>
> 2 *^n^* 2
>
> *n*−1
>
> 2 *n* 2 *n*
>
> *n n* 2 *n*
>
> Multiplied by �*t* in (18), that new term ^[1]{.underline}^
> (�*t*)^2^*u*^��^ is exactly what Euler missed. *Each*
>
> 2 *n*
>
> *extra term in the diﬀerence equation can increase the accuracy by* 1.

A third possibility uses the already computed value *U~n~*~−1~ (instead
of the slope

*f~n~*~−1~). With ^[3]{.underline}^ *,* − ^[4]{.underline}^ *,*
^[1]{.underline}^ chosen for second-order accuracy, we get an implicit
backward

> 2 2 2
>
> diﬀerence method:
>
> 3*Un*+1 − 4*Un* + *Un*−1
>
> Backward diﬀerences = *f* (*U~n~*~+1~*, t~n~*~+1~) *.* (19)
>
> 2�*t*
>
> What about stability ? The implicit method (17) is stable even in the
> stiﬀ case, when *a* is very negative. 1 − ^[1]{.underline}^ *a* �*t*
> (left side) will be larger than 1 + ^[1]{.underline}^ *a* �*t* (right
> side).
>
> \(19\) is also stable. The explicit method (18) will be stable if �*t*
> is small enough, but
>
> there is always a limit on �*t* for stiﬀ systems.
>
> Here is a quick way to ﬁnd the stability limit in (18) when *a* is
> real. The limit occurs when the growth factor is exactly *G* = −1.
> *Set U~n~*~+1~ = −1 *and U~n~* = 1 *and U~n~*~−1~ = −1 *in* (18)*.
> Solve for a when f* (*u, t*) = *au*:

−2 3 1

> Stability limit in (18) =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} *a* +
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} *a* gives *a* �*t* = −1 *.* So *C* =
> 1 *.* (20)

�*t* 2 2

> Those second-order methods (17)--(18)--(19) are deﬁnitely useful ! The
> reader might suggest including both *U~n~*~−1~ and *f~n~*~−1~ to
> increase the accuracy to *p* = 3. Sadly, this method is violently
> unstable (Problem 4). We may use older values of *U* in backward
> diﬀerences or *f* (*U* ) in Adams formulas, but including both *U* and
> *f* (*U* ) for even higher accuracy produces instability for all �*t*.

### Multistep Methods: Explicit and Implicit {#multistep-methods-explicit-and-implicit .unnumbered}

> By using *p* older values of either *U* or *f* (*U* ) (already
> computed at previous steps !), the accuracy can be increased to order
> *p*. Each ∗*U* is *U* (*t*) − *U* (*t* − �*t*) and *p* = 2
>
> is (19):

\(21\)

> MATLAB's stiﬀ code ode15s varies from *p* = 1 to *p* = 5 depending on
> the local error. Using older values of the right side *f* (*U* ) gives
> an Adams-Bashforth method:
>
> *U~n~*~+1~ − *U~n~* = �*t*(*b*~1~ *f~n~* + · · · + *b~p~
> f~n~*~−*p*+1~) with *f~n~* = *f* (*U~n~, t~n~*) *.* (22) The table
> shows the numbers *b* up to *p* = 4, starting with Euler for *p* = 1.

+----------+------+--------+------+-------+-------------+------------+
| > order  | *b   | *b*~2~ | > *b | *     | > limit on  | > constant |
| > of     | *~1~ |        | *~3~ | b*~4~ | > *a*�*t*   | > *c*      |
|          |      |        |      |       | >           | >          |
|          |      |        |      |       | > for       | > in error |
|          |      |        |      |       | > stability | > DE       |
+==========+======+========+======+=======+=============+============+
| >        |      |        |      |       |             |            |
| accuracy |      |        |      |       |             |            |
+----------+------+--------+------+-------+-------------+------------+
| > *p* =  | > 1  |        |      |       | > −2        | > 1/2      |
| > 1      |      |        |      |       | >           | >          |
|          |      |        |      |       | > −1        | > 5/12     |
|          |      |        |      |       | >           |            |
|          |      |        |      |       | > −6*/*11   | 3/8        |
|          |      |        |      |       |             |            |
|          |      |        |      |       | −3*/*10     | > 251/720  |
+----------+------+--------+------+-------+-------------+------------+
| > *p* =  | >    | >      |      |       |             |            |
| > 2      |  3/2 | −1*/*2 |      |       |             |            |
+----------+------+--------+------+-------+-------------+------------+
| > *p* =  | > 2  | > −1   | >    |       |             |            |
| > 3      | 3/12 | 6*/*12 | 5/12 |       |             |            |
+----------+------+--------+------+-------+-------------+------------+
| > *p* =  | > 5  | > −5   | > 3  | > −9  |             |            |
| > 4      | 5/24 | 9*/*24 | 7/24 | */*24 |             |            |
+----------+------+--------+------+-------+-------------+------------+

> The fourth-order method is often a good choice, although astronomers
> go above *p* = 8. At the stability limit *G* = −1 as in (20). The
> local error DE � *c*(�*t*)^*p*+1^*u*^(*p*+1)^ is a problem of step
> control. Whether it is ampliﬁed by later steps is a problem of
> stability control.
>
> *Implicit methods* have an extra term *c*~0~*f~n~*~+1~ at the new time
> level. Properly chosen, that adds one extra order of accuracy---as it
> did for the trapezoidal rule, which is the second method in the new
> table. Backward Euler is the ﬁrst:

+----------+-----+------+-------+-----+--------------+-------------+
| > order  | *c* | > *c | > *   | >   | > limit on   | > constant  |
| > of     | ~0~ | *~1~ | c*~2~ | *c* | > *a*�*t*    | > *c*       |
| >        |     |      |       | ~3~ | >            | >           |
| >        |     |      |       |     | > for        | > in error  |
| accuracy |     |      |       |     | > stability  | > DE        |
+==========+=====+======+=======+=====+==============+=============+
| > *p* =  | > 1 |      |       |     | > −→         | > −1*/*2    |
| > 1      |     |      |       |     | >            | >           |
| >        |     |      |       |     | > −→         | > −1*/*12   |
| > *p* =  |     |      |       |     | >            | >           |
| > 2      |     |      |       |     | > −6         | > −1*/*24   |
| >        |     |      |       |     | >            | >           |
| > *p* =  |     |      |       |     | > −3         | > −19*/*720 |
| > 3      |     |      |       |     |              |             |
| >        |     |      |       |     |              |             |
| > *p* =  |     |      |       |     |              |             |
| > 4      |     |      |       |     |              |             |
+----------+-----+------+-------+-----+--------------+-------------+
|          | >   | >    |       |     |              |             |
|          | 1/2 |  1/2 |       |     |              |             |
+----------+-----+------+-------+-----+--------------+-------------+
|          | > 5 | >    | > −1  |     |              |             |
|          | /12 | 8/12 | */*12 |     |              |             |
+----------+-----+------+-------+-----+--------------+-------------+
|          | > 9 | > 1  | > −5  | > 1 |              |             |
|          | /24 | 9/24 | */*24 | /24 |              |             |
+----------+-----+------+-------+-----+--------------+-------------+

> Every row of both tables adds to 1, so *u* � = 1 is solved exactly.
>
> You see that the error constants and stability are all in favor of
> implicit methods. So is the user, except when solving for *U~n~*~+1~
> becomes expensive. Then there is a simple and successful
> *predictor-corrector* method, or else *Newton's method*.
>
> P: Use the explicit formula to *predict* a new *U* ≈
>
> Predictor- ≈
>
> *n*+1

≈

> Corrector
>
> E: Use *un*+1 to *evaluate* the right side *fn*+1
>
> C: Use *f* ≈ in the implicit formula to *correct* to a new *U~n~*~+1~.
>
> The stability is much improved if another *E* step evaluates
> *f~n~*~+1~ with the corrected
>
> *u~n~*~+1~. In principle we should continue the corrector to
> convergence. Frequently 1--2
>
> corrections are enough, and the extra calculation can be put to use.
> By comparing the predicted *U* ≈ and corrected *U~n~*~+1~ the code can
> estimate the local error and change

�*t*:

> local error DE �
>
> *c c*≈ − *c*

(*Un*+1

> ≈
>
> *n*+1

)*,* (23)

> where *c*≈ and *c* are the error constants in the tables for the
> predictor and corrector. Implicit methods often have a Newton loop
> inside each time step, to compute
>
> *U~n~*~+1~. The *k*th iteration in the Newton loop is a linear system,
> with the Jacobian
>
> matrix *A*^(*k*)^ = *�f~i~/�u~j~* evaluated at the latest
> approximation *U* ^(*k*)^ with *t* = *t~n~*~+1~.
>
> Here is the *k*th *i* to solve *U~n~*~+1~ − *c*~0~*f* (*U~n~*~+1~*,
> t~n~*~+1~) = old values:
>
> Newton iteration (*I* − *c*~0~*A*^(*k*)^)(*U* ^(*k*+1)^ − *U* ^(*k*)^
> ) = *c*~0~*f* (*U* ^(*k*)^ *, t~n~*~+1~) + old values *.*(24)

*n*+1

> *n*+1
>
> *n*+1
>
> When *f* (*u*) = *Au* is linear, you only need one iteration (*k* = 0
> starts with *U* ^(0)^ = *U~n~*). For nonlinear *f* (*u*), Newton's
> rapid convergence squares the error at each step (when it gets close).
> The price is a new evaluation of *f* (*u*) and its matrix *A*^(*k*)^
> of derivatives.

### Runge-Kutta Methods {#runge-kutta-methods .unnumbered}

> A-stable methods have no stability limit. Multistep methods achieve
> high accuracy with one or two evaluations of *f* . If more evaluations
> are not too expensive, *Runge-Kutta methods* are deﬁnitely competitive
> (and these are self-starting). They are compound one-step methods,
> using Euler's *U~n~* + �*t f~n~ inside f:*
>
> [*U~n~*~+1~ − *U~n~*]{.underline} [1]{.underline} � �
>
> Simpliﬁed Runge-Kutta = *f* + *f* (*U* + �*t f , t* ) *.* (25)

You see the compounding of *f* . For the model equation *u* � = *au* the
result is

> [1]{.underline} � � � [1]{.underline} �
>
> *u* = *u t au* + *a*(*u* + �*t au* ) = 1 + *a*�*t* + *a*^2^�*t*^2^ *u*
> = *G u .* (26)
>
> This conﬁrms the second-order accuracy; the growth factor *G* agrees
> with *e^a^*^�*t*^ through (�*t*)^2^. There will be a stability
> threshold *a*�*t* = *C*, where \|*G*\| = 1:
>
> Stability limit \|*G*\| = �1 + *C* + 2 *C* � = 1 (for complex *C* =
> *a* + *ib*)
>
> The complete stability limit is not a point but a closed curve in the
> complex plane. Figure 5. shows all the complex numbers *C* at which
> \|*G*\| = 1.
>
> The famous version of Runge-Kutta is compounded *four times* and
> achieves *p* = 4:
>
> Runge-Kutta
>
> [*Un*+1 − *Un*]{.underline}
>
> 1
>
> =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image16.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} (*k*
>
> \+ 2*k*
>
> \+ 2*k*
>
> \+ *k* ) (27)
>
> �*t* 3 1 2 3 4
>
> 1 1
>
> *k*~1~ = 2 *f* (*U~n~, t~n~*) *k*~3~ = 2 *f* (*U~n~* + �*tk*~2~*,
> t~n~*~+1*/*2~)
>
> 1 1
>
> *k*~2~ = 2 *f* (*U~n~* + �*tk*~1~*, t~n~*~+1*/*2~) *k*~4~ = 2 *f*
> (*U~n~* + 2�*t k*~3~*, t~n~*~+1~)
>
> For this one-step method, no special starting instructions are
> necessary. It is simple
>
> to change �*t* as you go. The growth factor reproduces *e^a^*^�*t*^
> through ^[1]{.underline}^ *a*^4^�*t*^4^. The
>
> error constant is the next coeﬃcient [^1^]{.underline} . Among highly
> accurate methods, Runge-Kutta is especially easy to code and
> run---probably the easiest there is. MATLAB's workhorse is ode45.
>
> To prove that the stability threshold *a*�*t* = −2*.*78 is genuine, we
> reproduce the solution of *u* � = −100*u* + 100 sin *t*. With *u*(0) =
> 0, Runge-Kutta gives

\(28\)

### Diﬀerential-Algebraic Equations {#diﬀerential-algebraic-equations .unnumbered}

> Our system of equations might not come in the form *u*^�^ = *f* (*u,
> t*). The more general form *F* (*u*^�^*, u, t*) = 0 appears in many
> applications. It may not be easy (or possible) to solve this system
> explicitly for *u*^�^. For large electrical networks (VLSI on chips),
> transistors produce a highly nonlinear dependence on *u*^�^ and *u*.
>
> Here is a simple model in which solving for the vector *u*^�^ is
> impossible:
>
> *Mu*^�^ = *f* (*u, t*) with a singular matrix *M* (rank *r \< N*) *.*
> (29)
>
> Suppose we change variables from *u* to *v*, so as to diagonalize *M*.
> In the new variables we have *r* true diﬀerential equations and *N* −
> *r algebraic equations* (*no derivatives*). The system becomes a
> *diﬀerential-algebraic equation* (DAE):

*[dvi]{.underline}* = *f* (*v , . . . , v , t*) *i* = 1*, . . . , r*

> DAE *dt i* 1 *N*
>
> \(30\)
>
> 0 = *f~i~*(*v*~1~*, . . . , v~N~ , t*) *i* = *r* + 1*, . . . , N .*
>
> The *N* − *r* algebraic equations restrict *v* to a surface in
> *N*-dimensional space. The *r*
>
> diﬀerential equations move the vector *v*(*t*) along that surface.
>
> Petzold \[46\] developed the DASSL package for solving DAE's in the
> general form *F* (*u*^�^*, u, t*) = 0, replacing *u*^�^ by a backward
> diﬀerence of *u*. The best recommendation we can make is to experiment
> with this software !

### Problem Set 5.1 {#problem-set-5.1 .unnumbered}

1.  The error in the trapezoidal (Crank-Nicolson) method ( ) comes from
    the diﬀerence

> *ea*�*t* − [1 + (*a*�*t/*2)]{.underline} = *ea*�*t* − 1 +
> [*a*�*t*]{.underline} 1 + [*a*�*t*]{.underline} +
> [*a*�*t*]{.underline} 2 + · · ·
>
> 1 − (*a*�*t/*2) 2 2 2
>
> This involves the two series that everyone should learn: the
> exponential series
>
> for *e^a^*^�*t*^ and the geometric series 1 + *x* + *x*^2^ + · · · for
>
> Multiply inside the brackets to produce the correct
>
> [1]{.underline} 1−*x*
>
> ^[1]{.underline}^(*a*�*t*)^2^. Show that the
>
> (*a*�*t*)^3^ term is wrong by *c* = ^[1]{.underline}^ . Then the error
> is DE � ^[1]{.underline}^ (�*t*)^3^ *u* ���.
>
> 12 12

2.  Try Runge-Kutta on *u* � = −100*u* + 100 sin *t* with �*t* =
    −*.*0275 and −*.*028. Those are close to the stability limit
    −*.*0278.

3.  For the backward diﬀerence error in (19), expand ^[1]{.underline}^
    (3*e^a^*^�*t*^ − 4 + *e*^−*a*�*t*^) − *a*�*t e^a^*^�*t*^

> into a series in *a*�*t*. Show that the leading error is −
> ^[1]{.underline}^(*a*�*t*)^3^ so that *c* = − ^[1]{.underline}^ .

3 3

4.  Stability in (19).

    1.  Accuracy and Stability for u~t~ = c u~x~

> This section begins a major topic in scientiﬁc computing:
> Initial-value problems for partial diﬀerential equations. Naturally we
> start with linear equations that involve only one space dimension *x*
> (and time *t*). The exact solution is *u*(*x, t*) and its discrete
> approximation on a space-time grid has the form *U~j,n~* = *U*
> (*j*�*x, n*�*t*). We want to know if *U* is near *u*---how close they
> are and how stable *U* is.
>
> Begin with the simplest wave equation (ﬁrst-order, linear, constant
> coeﬃcient):

\(1\)

> We are given *u*(*x,* 0) at time *t* = 0. We want to ﬁnd *u*(*x, t*)
> for all *t \>* 0. For simplicity, these functions are deﬁned on the
> whole line *\< x \<* . There are no diﬃculties with boundaries (where
> waves could change direction and bounce back).
>
> The solution *u*(*x, t*) will have the typical feature of *hyperbolic
> equations*: *signals travel at ﬁnite speed*. Unlike the second-order
> wave equation *u~tt~* = *c*^2^*u~xx~*, this ﬁrst-order equation *u~t~*
> = *c u~x~* sends signals in one direction only.
>
> Solution for u(x, 0) = e^ikx^
>
> Throughout this chapter I will solve for a pure exponential *u*(*x,*
> 0) = *e^ikx^*. At every time t, the solution remains a multiple
> Ge*^ikx^*. The growth factor *G* will depend on the frequency *k* and
> the time *t*, but diﬀerent frequencies do not mix. Substituting *u* =
> *G*(*k, t*) *e^ikx^* into *u~t~* = *c u~x~* yields a simple ordinary
> diﬀerential equation for *G*, because we can cancel *e^ikx^*. The
> derivative of *e^ikx^* produces the factor *ik*:
>
> *dG dG*
>
> *u* = *c u* is *e^ikx^* = *ikc Ge^ikx^* or = *ikcG .* (2)

*^t^ ^x^ dt dt*

> *The growth factor is* G(k, t) = e*^ikc^ ^t^.* The initial value is
> *G* = 1.
>
> An exponential solution to *�u* = *c �u* is *u*(*x, t*) = *e^ikc^
> ^t^e^ikx^* = e^*ik*(*x*+*ct*)^ *.* (3)
>
> *�t �x*
>
> Immediately we see two important features of this solution:

1.  The growth factor *G* = *e^ikc^ ^t^* has absolute value \|*G*\| = 1.

2.  The initial function *e^ikx^* moves to the left with ﬁxed velocity
    > *c*, to *e^ik^*^(*x*+*ct*)^.

> The initial value at the origin is *u*(0*,* 0) = *e^ik^*^0^ = 1. This
> value *u* = 1 appears at all points on the line *x* + *ct* = 0. The
> initial data propagates along the characteristic lines x + ct =
> *constant*, in Figure 5.3. Right now we know this fact for the special
> solutions *e^ik^*^(*x*+*ct*)^. Soon we will know it for all solutions.
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image21.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image21.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}�*t*
>
> *u*(*P* ) = *u*(0*,* 0) *u*(*Q*) = *u*(*X,* 0)
>
> characteristic line to *P*
>
> *x* + *ct* = 0
>
> characteristic line to *Q x* + *ct* = *X*

-   *x*

> *u*(0*,* 0) *u*(*X,* 0)
>
> Figure 5.3: The solution *u*(*x, t*) moves left with speed *c*, along
> characteristic lines.
>
> Figure 5.3 shows the travel path of the solution in the *x*-*t* plane
> (we are introducing the characteristic lines). Figure 5.4 will graph
> the solution itself at times 0 and *t*. That step function combines
> exponentials *e^ik^*^(*x*+*ct*)^ for diﬀerent frequencies *k*. By
> linearity we can add those solutions.

### Solution for Every u(x, 0) {#solution-for-every-ux-0 .unnumbered}

> In almost all partial diﬀerential equations, the solution changes
> shape as it travels. Here the shape stays the same. All pure
> exponentials travel at the same velocity *c*, so *every* initial
> function moves with that velocity. We can write down the solution:

*�u �u*

> General solution = *c* is solved by u(x, t) = u(x + ct, 0) *.* (4)

*�t �x*

> *The solution is a function only of x* + *ct*. That makes it constant
> along characteristic lines, where *x* + *ct* is constant. This
> dependence on *x* + *ct* also makes it satisfy the equation *u~t~* =
> *c u~x~*, by the chain rule. If we take *u* = (*x* + *ct*)*^n^* as an
> example, the extra factor *c* appears in *�u/�t*:
>
> *�u* = *n* (*x* + *ct*)^*n*−1^ and *�u* = *cn* (*x* + *ct*)^*n*−1^
> which is *c �u .*
>
> *�x �t �x*
>
> A Taylor series person would combine those powers (diﬀerent *n*) to
> produce a large family of solutions. A Fourier series person combines
> exponentials (diﬀerent *k*) to produce an even larger family. In fact
> *all* solutions are functions of *x* + *ct* alone.
>
> Here are two important initial functions---a light ﬂashes or a dam
> breaks.
>
> Example 1 *u*(*x,* 0) = delta function *∂*(*x*) = ﬂash of light at *x*
> = 0*, t* = 0
>
> By our formula (4), the solution is *u*(*x, t*) = *∂*(*x* + *ct*). The
> light ﬂash reaches the point *x* = −*c* at the time *t* = 1. It
> reaches *x* = −2*c* at the time *t* = 2. The impulse is traveling to
> the left at speed \|*dx/dt*\| = *c*. In this example all frequencies
> *k* are present in equal amounts, because the Fourier transform of a
> delta function is a constant.
>
> Notice that a point goes dark again as soon as the ﬂash passes
> through. This is the Huygens principle in 1 and 3 dimensions. If we
> lived in two or four dimensions, the wave would not pass all at once
> and we wouldn't see clearly.
>
> Example 2 *u*(*x,* 0) = step function *S*(*x*) = wall of water at *x*
> = 0*, t* = 0
>
> The solution *S*(*x* + *ct*) is the moving step function in Figure
> 5.4. The wall of water travels to the left (*one-way wave*). At time
> *t*, the "tsunami" reaches the point *x* = *ct*. The ﬂash of light
> will get there ﬁrst, because its speed *c* is greater than the tsunami
> speed. That is why a warning is possible for an approaching tsunami.

*u*(*x,* 0) *u*(*x, t*)

> *x* *x*
>
> 0 −*ct* 0
>
> initial proﬁle *S*(*x*) at *t* = 0 later proﬁle *S*(*x* + *ct*) at
> time *t*
>
> Figure 5.4: The wall travels left with velocity *c* (all waves
> *e^ikx^* do too).
>
> An actual tsunami is described by the nonlinear "shallow water
> equations" that come later. The feature of *ﬁnite speed* still holds.
>
> Finite Diﬀerence Methods for u~t~ = c u~x~
>
> The one-way wave equation is a perfect example for creating and
> testing ﬁnite dif-ference approximations. We can replace *�u/�t* by a
> forward diﬀerence with step �*t*. Here are four choices for the
> discrete form of *�u/�x* at meshpoint *i*�*x*:

1.  Forward = [*Ui*+1 − *Ui*]{.underline}

�*x*

> = upwind: Low accuracy, conditionally stable for *c \>* 0.

2.  Centered = [*Ui*+1 − *Ui*−1]{.underline} : Unstable after a few
    > steps as we will prove ! 2�*x*

3.  Lax-Friedrichs: (20) has low accuracy, conditionally stable also for
    > *c \<* 0.

4.  Lax-Wendroﬀ : (14) has extra accuracy, conditionally stable also for
    > *c \<* 0.

> The list doesn't end there. We have reached a central problem of
> scientiﬁc computing, to construct approximations that are *stable* and
> *accurate* and *fast*. That topic can't be developed on one page,
> especially when we move to nonlinear equations.
>
> *Conditionally stable* means that the time step �*t* is restricted.
> The need for this restriction was noticed by Courant, Friedrichs, and
> Lewy. When the space diﬀerence

reaches no further than *x* + �*x*, there is an automatic stability
restriction:

> �t
>
> CFL requirement for stability r = c � 1 . (5)
>
> �x
>
> That number *c* �*t/*�*x* is often called the *Courant number*. (It
> was really Lewy who recognized that *r* √ 1 is necessary for stability
> and convergence.) The reasoning is straightforward, based on using the
> initial value that controls *u*(*x, t*):
>
> The true solution at (*x, t*) equals the initial value *u*(*x* + *ct,*
> 0). Taking *n* discrete steps to reach *t* = *n* �*t* uses information
> on the initial values as far out as *x* + *n* �*x*. If *x* + *ct* is
> further than *x* + *n* �*x*, the method can't work:

�*t*

> CFL condition *x* + *c t* √ *x* + *n* �*x* or *c n* �*t* √ *n* �*x* or
> *r* = *c* �*x* √ 1 *.* (6)
>
> If the diﬀerence equation uses *U* (*x* + 2�*x, t*), then CFL relaxes
> to *r* √ 2.
>
> A particular ﬁnite diﬀerence equation might require a tighter
> restriction on �*t* for stability. It might even be unstable for all
> ratios *r* (we hope not). The only route to *unconditional stability*
> for all �*t* is an *implicit method*, which computes *x*-diﬀerences at
> the new time *t* + �*t*. This will be useful later for diﬀusion terms
> like *u~xx~*. For advection terms (ﬁrst derivatives), explicit methods
> with a CFL limitation are usually accepted because a much larger �*t*
> would lose accuracy as well as stability.
>
> To repeat, if *r \>* 1 then the ﬁnite diﬀerence solution at *x, t*
> does not use initial value information near the correct point *x*← =
> *x* + *ct*. Hopeless.

### Accuracy of the Upwind Diﬀerence Equation {#accuracy-of-the-upwind-diﬀerence-equation .unnumbered}

> Linear problems with constant coeﬃcients are the ones to understand
> ﬁrst. Exactly as for diﬀerential equations, we can follow each pure
> exponential *e^ikx^*. After a single time step, there will be a growth
> factor in *U* (*x,* �*t*) = *Ge^ikx^*. That growth factor *G*(*k,*
> �*t,* �*x*) may have magnitude *G \<* 1 or *G \>* 1. This will control
> stability or instability. The order of accuracy (if we compute in the
> *k*-*�* domain) comes from comparing *G* with the true factor
> *e^ikc^*^�*t*^ from the diﬀerential equation.
>
> We now determine that the order of accuracy is *p* = 1 for the *upwind
> method*.
>
> Forward diﬀerences
>
> [*U* (*x, t* + �*t*) − *U* (*x, t*)]{.underline} = *c [U
> ]{.underline}*[(*x* + �*x, t*) − *U* (*x, t*)]{.underline} *.* (7)
>
> �*t* �*x*
>
> We will test the accuracy in the *x*-*t* domain and then the *k*-*�*
> domain. Either way we use Taylor series to check the leading terms.
> Substituting the true solution *u*(*x, t*) in place of *U* (*x, t*),
> its forward diﬀerences are
>
> 1 1
>
> Time
>
> Space
>
> �*t* \[*u*(*x, t* + �*t*) − *u*(*x, t*)\] = *u~t~* + 2 �*tu~tt~* + · ·
> ·
>
> *c* 1
>
> �*x* \[*u*(*x* + �*x, t*) − *u*(*x, t*)\] = *c u~x~* + 2 *c*
> �*xu~xx~* + · · ·
>
> \(8\)
>
> \(9\)
>
> On the right side, *u~t~* = *c u~x~* is good. One more derivative
> gives *u~tt~* = *c u~xt~* = *c*^2^ *u~xx~*. Notice *c*^2^. Then
> �*tu~tt~* matches *c* �*xu~xx~ only in the special case c*�*t* = �*x*:

1 �*t c*^2^ *u*

> 2 *xx*
>
> equals
>
> 1
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image16.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"}*c* �*x u~xx~*
>
> 2

*c*�*t*

only if *r* = = 1.

�*x*

> For any ratio *r* ≥= 1, the diﬀerence between (8) and (9) has a
> *ﬁrst-order error*. Let me show this also in the *k*-*�* Fourier
> picture and then improve to second-order.
>
> Fix the ratio *r* = *c*�*t/*�*x* as �*x* 0 and �*t* 0. In the
> diﬀerence equation (7), write each new value at time *t* + �*t* as a
> combination of two old values of *U* :

\(10\)

Starting from *U* (*x,* 0) = *e^ikx^* we quickly ﬁnd the growth factor G
at time �*t*:

> After 1 step (1 − *r*)*e^ikx^* + *r e^ik^*^(*x*+�*x*)^ = 1 − r + r
> e^*ik*�*x*^ *e^ikx^* = G *e^ikx^ .* (11)
>
> To test the accuracy, compare this *G* = *G*~approx~ to the exact
> growth factor *e^ick^*^�*t*^. Use the power series 1 + *x* +
> *x*^2^*/*2! + · · · for any *e^x^*:
>
> *ik*�*x* [1]{.underline} 2
>
> Accuracy*G*~approx~ = 1 − *r* + *r e* = (1 − *r*) + *r* +
> *r*(*ik*�*x*) + *r* (*ik*�*x*) + · · ·

*G*exact

> = *e^ick^*^�*t*^ = *e^irk^*^�*x*^ = 1 + *irk*�*x* + [1]{.underline}
> (*irk*�*x*)^2^ + · · ·
>
> \(12\)
>
> The ﬁrst terms agree as expected. Forward diﬀerences replaced
> derivatives, and the method is *consistent*. We saw *u~t~* = *c u~x~*
> in comparing (8) with (9). The next terms do *not* agree unless *r* =
> *r*^2^:
>
> Compare 1 *r*(*ik*�*x*)^2^ with 1 *r*^2^(*ik*�*x*)^2^*.* Single-step
> error of order (k�t)^2^. (13)
>
> 2 2
>
> After 1*/*�*t* steps, those errors of order *k*^2^(�*t*)^2^ give a
> ﬁnal error *O*(*k*^2^�*t*). Forward diﬀerences are only ﬁrst order
> accurate, and so is the whole method.
>
> The special case *r* = 1 means *c*�*t* = �*x*. The diﬀerence equation
> is *exactly correct*. The true and approximate solutions at (*x,*
> �*t*) are both *u*(*x* + �*x,* 0). We are *on the characteristic line*
> in Figure 5.3. This is an interesting special case (the golden �*t*,
> but hard to repeat in scientiﬁc computing when *c* varies).

Conclusion Except when *r* = *r*^2^, *the upwind method is ﬁrst-order
accurate*.

### Higher Accuracy for Lax-Wendroﬀ {#higher-accuracy-for-lax-wendroﬀ .unnumbered}

To upgrade the accuracy, we need to match the ^[1]{.underline}^ �*t
u~tt~* error term in the forward time

> diﬀerence by an additional space diﬀerence that gives
> ^[1]{.underline}^�*t c*^2^*u~xx~*. This is achieved by the Lax-Wendroﬀ
> method:
>
> [*U* (*x, t* + �*t*) − *U* (*x, t*)]{.underline} = *c [U
> ]{.underline}*[(*x* + �*x, t*) − *U* (*x* − �*x, t*)]{.underline}
>
> �*t* 2�*x*
>
> \+ [�*t*]{.underline} *c*2 � [*U* (*x* + �*x, t*) − 2*U* (*x, t*) +
> *U* (*x* − �*x, t*)]{.underline} � (14)
>
> 2 (�*x*)2
>
> Substituting the true solution, that second diﬀerence produces
> ^[1]{.underline}^ *c*^2^�*t u~xx~* plus higher order terms. This
> cancels the ^[1]{.underline}^ �*t u~tt~* error term in the time
> diﬀerence, computed
>
> in equation (8). (Remember *u~tt~* = *cu~xt~* = *c*^2^*u~xx~*. The
> centered diﬀerence has no �*x* term.) Thus Lax-Wendroﬀ has
> second-order accuracy.
>
> To see this in the *k*-*�* frequency domain, rewrite the LW diﬀerence
> equation (14):
>
> [1]{.underline} [1]{.underline}
>
> *U* (*x, t* + �*t*) = (1 − *r*^2^)*U* (*x, t r*^2^ + *r*)*U* (*x* +
> �*x, t r*^2^ − *r*)*U* (*x* − �*x, t*) *.* (15)
>
> 2 2

Substitute *U* (*x, t*) = *e^ikx^* to ﬁnd the one-step growth factor *G*
at time *t* + �*t*:

> Growth factor for LW *G* = (1 − r^2^
>
> 1

) +
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image19.png){width="9.500546806649168e-2in"
height="6.666666666666667e-3in"}(

r2 + r)*eik*�*x*

> \+ 1(r^2^ − r)*e*^−*ik*�*x*^*.*
>
> 2 2
>
> Expanding *e^ik^*^�*x*^ and *e*^−*ik*�*x*^ in powers of *ik* �*x*,
> this becomes
>
> *G* = 1 + *r*(*ik*�*x*) + 1 *r*^2^(*ik*�*x*)^2^ + *O*(*k*�*x*)^3^ *.*
> (16)
>
> 2
>
> Comparing with *G*~exact~ = *e^irk^*^�*x*^ in equation (12), three
> terms agree. So the one-step error is of order (*k*�*x*)^3^. After
> 1*/*�*t* steps the second-order accuracy of Lax-Wendroﬀ is conﬁrmed.
>
> Figure 5.5 shows by actual computation the improvement in accuracy.
> For a ﬁrst-order method, the "wall of water" is smeared out. High
> frequencies have growth factors \|*G*(*k*)\| much smaller than 1.
> There is too much dissipation. For the ﬁrst-order
>
> Lax-Friedrichs method, the dissipation is even worse (Problem 2). The
> second-order
>
> Lax-Wendroﬀ method stays much closer to the discontinuity. But it's
> not perfect---those oscillations are not good.
>
> For an ideal diﬀerence equation, we want to add enough dissipation
> very *close to the shock*, to avoid that oscillation (the Gibbs
> phenomenon). A lot of thought has gone into high resolution methods,
> to capture shock waves cleanly.
>
> Greater accuracy is achievable by including more terms in the
> diﬀerence equation. If we go from the three terms in Lax-Wendroﬀ to
> ﬁve terms, we can reach fourth-order accuracy. If we use *all* values
> *U* (*j*�*x, n*�*t*) at every time step, which requires more work, we
> can achieve spectral accuracy. Then the error decreases faster than
> any power of �*x*, provided *u*(*x, t*) is smooth enough to allow
> derivatives of all orders. Section gives a separate discussion of this
> spectral method.

### Stability of the Four Finite Diﬀerence Methods {#stability-of-the-four-finite-diﬀerence-methods .unnumbered}

> Now we turn from accuracy to stability. Accuracy requires *G* to stay
> close to the true *e^ick^*^�*t*^. Stability requires *G* to stay
> *inside the unit circle*. We need *G* 1 for all frequencies *k* or the
> ﬁnite diﬀerence approximation *G^n^e^ikx^* will blow up.
>
> We now check whether or not \|*G*\| √ 1, in the four methods.

1.  Forward diﬀerences in space and time: �U/�t = c �U/�x (upwind).

> Recall from equation (11) that *G* = 1 − *r* + *re^ik^*^�*x*^. If the
> Courant number *r* is between 0 and 1, the triangle inequality gives
> \|*G*\| √ 1:
>
> Stability for 0 � r � 1 \|*G*\| √ \|1 − *r*\| + \|*re* \| = 1 − *r* +
> *r* = 1 *.* (17) This suﬃcient condition 0 √ *c* �*t/*�*x* √ 1 is
> exactly the same as the Courant-
>
> Friedrichs-Lewy necessary condition ! They reasoned that *U* (*x,
> n*�*t*) depends on the
>
> initial values between *x* and *x* + *n*�*x*. That domain of
> dependence must include the point *x* + *c n*�*t*. (Otherwise,
> changing the initial value at the point *x* + *c n*�*t* would change
> the true solution *u* but not the approximation *U* .) Then *c n*�*t*
> must lie between 0 and *n*�*x*, which means that 0 √ *r* √ 1.
>
> Figure 5.5 shows *G* in the stable case *r* = ^[2]{.underline}^ and
> the unstable case *r* = ^[4]{.underline}^ (when �*t*
>
> 3 3
>
> is too large). As *k* varies, and *e^ik^*^�*x*^ goes around a unit
> circle, the complex number *G* = 1 − *r* + *re^ik^*^�*x*^ goes in a
> circle of radius *r*. The center is 1 − *r*. Always *G* = 1 at zero
> frequency (constant solution, no growth).

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image22.png){width="1.7895352143482064in"
height="2.0464949693788275in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image23.png){width="2.018715004374453in"
height="2.0464949693788275in"}G = 1 − r + re^*ik*�*x*^

> *r r*

Stable

\|G\|\<1

> 1−*r*
>
> *G* = 1
>
> *G* = 1−2*r*
>
> *k*�*x* = *�*
>
> Unstable

1−*r*

> *k* = 0

unit circle

> \|G\| \> 1
>
> Figure 5.5: Stable (upwind) and unstable (centered): CFL numbers *r* =
> ^[2]{.underline}^ and *r* = ^[4]{.underline}^ .

3 3

2.  Forward diﬀerence in time, centered diﬀerence in space.

> This combination is never stable ! The shorthand *U~j,n~* will stand
> for *U* (*j*�*x, n*�*t*):
>
> [*Uj,n*+1 − *Uj,n*]{.underline} = *c [Uj]{.underline}*[+1*,n* −
> *Uj*−1*,n*]{.underline}
>
> or *U*

*[r]{.underline}*

> = *U* + (*U*
>
> − *U* ) *.* (18)
>
> Those coeﬃcients 1 and *r/*2 and *r/*2 go into the growth factor *G*,
> when the solution is a pure exponential and *e^ikx^* is factored out:
>
> Unstable: \|G\| \> 1 *G* = 1 + *[r]{.underline}e^ik^*^�*x*^ −
> *[r]{.underline}e*^−*ik*�*x*^ = 1 + ir sin k�x *.* (19)
>
> The real part is 1. The magnitude is \|*G*\| → 1. Its graph is on the
> left side of Figure 5.6.

3.  Lax-Friedrichs Method (upwind-downwind).

> We can recover stability for centered diﬀerences by changing the time
> diﬀerence.
>
> Replace *U~j,n~* by the average ^[1]{.underline}^ (*U~j~*~+1*,n*~ +
> *U~j~*~−1*,n*~) of its neighbors:
>
> *Uj,n*+1 − [1]{.underline} (*Uj*+1*,n* + *Uj*−1*,n*) [*Uj*+1*,n* −
> *Uj*−1*,n*]{.underline}
>
> Lax-Friedrichs
>
> ^2^ = *c .* (20)
>
> �*t* 2�*x*
>
> Two old values *U~j~*~+1*,n*~ and *U~j~*~−1*,n*~ produce each new
> value *U~j,n~*~+1~. Moving terms to
>
> the right-hand side, the coeﬃcients are ^[1]{.underline}^(1 + *r*) and
> ^[1]{.underline}^ (1 − *r*). The growth factor is
>
> *G* = 1 + *r e^ik^*^�*x*^ + 1 − *r e*^−*ik*�*x*^ = cos k�x + ir sin
> k�x *.* (21)
>
> 2 2
>
> The absolute value is \|*G*\|2 = (cos *k*�*x*)^2^ + *r*^2^(sin
> *k*�*x*)^2^. In Figure 5.6, \|*G*\| √ 1 when
>
> *r*^2^ √ 1. This stability condition agrees again with the CFL
> condition.
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image24.png){width="1.5366108923884514in"
> height="1.4084733158355205in"}Forward in time--centered in space
>
> � *G* = 1 + *ir* sin *k*�*x*
>
> Lax-Friedrichs

*G* = cos *k*�*x* + *ir* sin *k*�*x*

Stable for r^2^ � 1

> *r*
>
> \|G\| \< 1
>
> \|G\| \> 1
>
> Unstable
>
> Figure 5.6: Equation (18) is unstable for all *r*. Equation (20) is
> stable for *r*^2^ √ 1.
>
> Notice that c and r can be negative. The wave can go either way! This
> will be useful for the two-way wave equation, but the accuracy is
> still ﬁrst-order. The Lax-Friedrichs *G* matches the next term in the
> exact growth factor only if *r*^2^ = 1:
>
> *G* = cos *k*�*x* + *ir* sin *k*�*x* = 1 + *irk*�*x* − [1]{.underline}
> (*k*�*x*)^2^ + · · ·
>
> \(22\)
>
> [1]{.underline}
>
> *G*~exact~ = *e^ikr^*^�*x*^ = 1 + *irk* �*x* + *i*^2^*r*^2^(*k*
> �*x*)^2^ + · · ·
>
> In the exceptional cases *r* = 1 and *r* = 1, *G* agrees with
> *G*~exact~. Staying exactly on the characteristic line, *U~j,n~*~+1~
> matches the true *u*(*j*�*x, t* + �*t*). For *r*^2^ *\<* 1,
> Lax-Friedrichs has an important advantage and disadvantage:
>
> Good Each new *U~j,n~*~+1~ is a positive combination of old values.
>
> Not good The accuracy is only ﬁrst-order.
>
> Problem 6 will show that second-order is impossible with positive
> coeﬃcients.

4.  Lax-Wendroﬀ Method (second-order accurate).

> The LW diﬀerence equation (14) combines *U~j,n~* and *U~j~*~−1*,n*~
> and *U~j~*~+1*,n*~ to compute the new value *U~j,n~*~+1~. The
> coeﬃcients of these three old values go into *G*:
>
> [1]{.underline} −*ik*�*x*
>
> Lax-Wendroﬀ *G* = (1 − *r*^2^) + (*r*^2^ + *r*)*e^ik^*^�*x*^ + (*r*^2^
> − *r*)*e .* (23)
>
> 2 2
>
> This is *G* = 1 − *r*^2^ + *r*^2^ cos *k*�*x* + *ir* sin *k*�*x*. At
> the dangerous frequency *k*�*x* = *�*, the growth factor is 1 −
> 2*r*^2^. That stays above −1 if *r*^2^ √ 1.
>
> Problem 5 shows that *G* 1 for every *k*�*x*. Lax-Wendroﬀ is stable
> when-ever the CFL condition r^2^ � 1 is satisﬁed. Again the wave can
> go either way (or both ways) since *c* and *r* can be negative. This
> is the most accurate of the ﬁve methods in Figure 5.7.

+-------+-------------+--------------+-----------------+--------------+
| u     | > wrong way | centered     | >               | >            |
| pwind |             |              |  Lax-Friedrichs |  Lax-Wendroﬀ |
+=======+=============+==============+=================+==============+
| > s   | unstable    | > unstable   | > stable        | > stable     |
| table |             |              |                 |              |
+-------+-------------+--------------+-----------------+--------------+
| if    | > all �*t*  | > all �*t*   | > if \|*r*\| √  | > if \|*r*\| |
| *r* √ |             |              | > 1             | > √ 1        |
| 1     |             |              |                 |              |
+-------+-------------+--------------+-----------------+--------------+

> Figure 5.7: Diﬀerence methods for the one-way wave equation *u~t~* =
> *cu~x~*.

### Equivalence of Stability and Convergence {#equivalence-of-stability-and-convergence .unnumbered}

> Does the discrete solution *U* approach the true solution *u* as �*t*
> 0 ? The ex-pected answer is yes. But there are two requirements for
> convergence, and one of them---*stability* ---is by no means
> automatic. The other requirement is *consistency* --- the discrete
> problem must approximate the correct continuous problem. The fact that
> these two properties are suﬃcient for convergence, and also
> *necessary* for convergence, is the *fundamental theorem of numerical
> analysis*:
>
> Lax proved the equivalence theorem for initial-value problems. The
> rate of conver-gence is given in (26). The theorem is equally true for
> boundary-value problems, and for the approximation of functions, and
> for the approximation of integrals. It applies to every
> discretization, when the given problem *Lu* = *f* is replaced by
> *L~h~U~h~* = *f~h~*. Assuming the inputs *f* and *f~h~* are close, we
> will prove that *u* and *U~h~* are close---provided *L~h~* is stable.
> The key points of the proof take only a few lines when the equation is
> linear, and you will see the essence of this fundamental theorem.
>
> Suppose *f* is changed to *f~h~* and *L* is replaced by *L~h~*. The
> requirements are
>
> Consistency: *f~h~* � *f* and *L~h~u* � *Lu* for smooth solutions *u*.
>
> Well-posed: The inverse of *L* is bounded: ≤*u*≤ = ≤*L*^−1^*f* ≤ √
> *C*≤*f* ≤.
>
> Stability: The inverses *L*^−1^ remain uniformly bounded: ≤*L*^−1^*f*
> ≤ √ *C*≤*f* ≤.
>
> Under those conditions, the approximation *U* = *L*^−1^*f* will
> approach *u* as *h* goes to
>
> *h h h*

−1 −1

> zero. We subtract and add *Lh Lu* = *Lh f* when *u* is smooth:
>
> −1 −1
>
> Convergence *u* − *U* = *L* (*L u* − *Lu*) + *L* (*f* − *f*
>
> ) � 0 *.* (24)
>
> Consistency controls the quantities in parentheses (they go to zero).
> Stability controls the operators *L*^−1^ that act on them.
> Well-posedness controls the approximation of all solutions by smooth
> solutions. Then always *U~h~* converges to *u*.

−1

> If stability fails, there will be an input for which the
> approximations *U~h~* = *L f*
>
> are not bounded. The *uniform boundedness theorem produces this bad f*
> , from the
>
> −1
>
> inputs *f* on which instability gives ≤*L f* ≤ � ∗. Convergence fails
> for this *f* .
>
> A perfect equivalence theorem goes a little further, after careful
> deﬁnitions:
>
> Consistency + Stability �� Well-posedness + Convergence .
>
> Our eﬀort will now concentrate on initial-value problems, to estimate
> the error (the convergence rate) in *u* − *U~h~*. The parameter *h*
> becomes �*t*. We take *n* steps.

### The Rate of Convergence {#the-rate-of-convergence .unnumbered}

> Consistency means that the error at each time step goes to zero as the
> mesh is reﬁned. Our Taylor series estimates have done more: The order
> of accuracy gives the rate that this one-step error goes to zero. The
> problem is to extend this local rate to a global rate of convergence,
> accumulating the errors over *n* time steps.
>
> Let me write *S* for a single ﬁnite diﬀerence step, so U(t + �t) = S
> U(t). The corresponding step for the diﬀerential equation will be
> u(t + �t) = R u(t). Then consistency means that *Su* is close to *Ru*,
> and the order of accuracy *p* tells how close:
>
> Accuracy of discretization ≤*Su* − *Ru*≤ √ *C*~1~(�*t*)^*p*+1^ for
> smooth solutions *u*.
>
> Well-posed problem ≤*R u*≤ √ *C*~2~≤*u*≤ for *n* �*t* √ *T* .
>
> Stable approximations ≤*S U* ≤ √ *C*~3~≤*U* ≤ for *n* �*t* √ *T* .
>
> The diﬀerence between *U* = *S^n^u*(0) and the true *u* = *R^n^u*( )
> is (*S^n^* − *R^n^*)*u*( ). The key idea is a "telescoping identity"
> that involves *n* single-step diﬀerences *S* − *R*:

*S^n^* − *R^n^* = *S^n^*^−1^(*S* − *R*) + *S^n^*^−2^(*S* − *R*)*R* + · ·
· + (*S* − *R*)*R^n^*^−1^ *.* (25)

> Each of those *n* terms has a clear meaning. First, a power *R^k^*
> carries *u*(0) to the true solution *u*(*k* �*t*). Then (*S* −
> *R*)*u*(*k* �*t*) gives the error at step *k* of order (�*t*)^*p*+1^.
> Then powers of *S* carry that one-step error forward to time *n*�*t*.
> By stability, this
>
> ampliﬁes the error by no more than *C*~3~. There are *n T/*�*t* steps.
> The ﬁnal rate of convergence for smooth solutions is (�t)*^p^*:
>
> ≤*U* (*n* �*t*) − *u*(*n* �*t*)≤ = ≤(*S*

*T*

> − *R* )*u*(0)≤ √ *C*~1~*C*~2~*C*~3~ �*t*(�*t*)

*p*+1

> = *C*~1~*C*~2~*C*~3~ *T* (�*t*)*^p^ .*

\(26\)

Notice how smoothness was needed in the Taylor series (8) and (9), when
�*t* and

> �*x* multiplied *u~tt~* and *u~xx~*. That ﬁrst-order accuracy would
> not apply if *u* or *u~t~* or *u~x~* had a jump. Still the order of
> accuracy *p* gives a practical estimate of the overall approximation
> error *u U* . The problem of scientiﬁc computing is to get beyond *p*
> = 1 while maintaining stability and speed.

### Problem Set 5.2 {#problem-set-5.2 .unnumbered}

1.  Integrate *u~t~* = *c u~x~* from −∗ to ∗ to prove that mass is
    conserved: *dM/dt* = 0. Multiply by *u* and integrate *uu~t~* = *c
    uu~x~* to prove that energy is also conserved:

> �
>
> *M*(*t*) = *u*(*x, t*) *dx* and *E*(*t*) =
>
> [1]{.underline} � ~�~

(*u*(*x, t*))^2^ *dx* stay constant in time.

> −� 2 −�

2.  Substitute the true *u*(*x, t*) into the Lax-Friedrichs method (21)
    and use *u~t~* = *cu~x~*

> and *u~tt~* = *c*^2^*u~xx~* to ﬁnd the coeﬃcient of the *numerical
> dissipation u~xx~*.

3.  The diﬀerence equation *U~j,n~*~+1~ = *a~m~U~j~*~+*m,n*~ has growth
    factor *G* = *a~m~e^imk^*^�*x*^.

> Show *consistency* with *e^ick^*^�*t*^ (ﬁrst-order accuracy at least)
> when *a~m~* = 1 and
>
> *ma~m~* = *c*�*t/*�*x* = *r*.

4.  The condition for second-order accuracy is *m*^2^*a~m~* = *r*^2^,
    from the Taylor se-

> ries. Check this for Lax-Wendroﬀ with *a*~0~ = 1−*r*^2^*, a*~1~ =
> ^[1]{.underline}^ (*r*^2^+*r*)*, a*~−1~ = ^[1]{.underline}^
> (*r*^2^−*r*).
>
> With *nonnegative coeﬃcients a* →
>
> 2 � *m*�*a*
>
> 2�*a*
>
> )^2^ √
>
> ( *m*^2^*a* )( *a* ) becomes an equality *r*^2^ = *r*^2^. This
> equality only happens if
>
> *m*�*a~m~* = (constant)�*a~m~*. *Second-order is impossible with a~m~*
> → 0, unless the
>
> diﬀerence equation has only one term *U~j,n~*~+1~ = *U~j~*~+*m,n*~.

5.  The Lax-Wendroﬀ method has *G* = 1 − *r*^2^ + *r*^2^ cos *k*�*x* +
    *ir* sin *kx*. Square the

> real and imaginary parts to get (eventually!)
>
> Prove stability, that \|*G*\|2 √ 1 if *r*^2^ √ 1.
>
> \|*G*\| = 1 − (*r* − *r* )(1 − cos *k*�*x*) .

6.  Suppose the coeﬃcients in a linear diﬀerential equation change as
    *t* changes. The one-step solution operators become *S~k~* and
    *R~k~*, for the step from *k* �*t* to (*k* + 1)�*t*. After *n*
    steps, products replace the powers *S^n^* and *R^n^* in *U* and *u*:

> *U* (*n* �*t*) = *S~n~*~−1~*S~n~*~−2~ *. . . S*~1~*S*~0~ *u*(0) and
> *u*(*n* �*t*) = *R~n~*~−1~*R~n~*~−2~ *. . . R*~1~*R*~0~ *u*(0) *.*
>
> *Change the telescoping formula* (25) *to produce this U u*. Which
> parts are controlled by stability ? Which parts by well-posedness (=
> stability of the dif-ferential equation) ? Consistency still controls
> *S~k~* − *R~k~*.

7.  Even an unstable method will converge to the true solution *u* =
    *e^ick^*^�*t*^*e^ikx^* for each separate frequency *k*. Consistency
    assures that the single-step growth factor *G* is 1 + *ick* �*t* +
    *O*(�*t*)^2^. Then for *t* = *n* �*t*,

*G^n^* =

> �1 +
>
> *[ickt]{.underline} n*

1.  *^n^*

\+ *O*( )

> *n*2
>
> −� *e* which is convergence.
>
> How can we have convergence for each *u*(0) = *e^ikx^* and still prove
> divergence for
>
> a combination of frequencies *u*(0) = ��
>
> *ck eikx* ?

8.  The upwind method with *r \>* 1 is unstable because the CFL
    condition fails. By Problem 3, it does converge to
    *e^ik^*^(*x*+*ct*)^ based on values of *u*(*x,* 0) = *e^ikx^ that do
    not reach as far as x* + *ct*. The method must be ﬁnding a "correct"
    extrapolation of *e^ikx^*. So propose an initial *u*(*x,* 0) for
    which convergence fails.

# The Wave Equation and Staggered Leapfrog

> This section focuses on the *second-order wave equation u~tt~* =
> *c*^2^*u~xx~*. We ﬁnd the exact solution *u*(*x, t*). Accuracy and
> stability are conﬁrmed for the leapfrog method (centered second
> diﬀerences in *t* and *x*). This two-step method requires that we
> rethink the growth factor *G*, which was clear for a single step. The
> result will be *p* = 2 for the order of accuracy, and *c*�*t/*�*x* � 1
> for stability.
>
> It is useful to rewrite the wave equation as a *ﬁrst-order system*.
> The components *v*~1~ and *v*~2~ of the vector unknown can be *�u/�t*
> and *c �u/�x*. Then we are back to a single-step growth factor, but
> *G* is now a 2 by 2 matrix.
>
> Second-order accuracy extends to this system *v~t~* = *Av~x~* if we
> use a *staggered mesh*. The mesh for *v*~2~ lies in between the mesh
> for *v*~1~. This has become the standard method in computational
> electromagnetics (solving Maxwell's equations). The physical laws
> relating the electric ﬁeld *E* and the magnetic ﬁeld *H* are
> beautifully copied by the diﬀerence equations on a staggered mesh. The
> mesh becomes especially important in more space dimensions (*x*-*y*
> and *x*-*y*-*z*), and in ﬁnite volume methods.
>
> This section goes beyond the one-way wave equation in at least ﬁve
> ways:

1.  *Two characteristic lines x*+ *ct* = *C*left and *x*− *ct* =
    *C*right go through each (*x, t*).

2.  The *leapfrog method* involves three time levels *t* + �*t*, *t*,
    and *t* − �*t*.

3.  *First-order systems* have vector unknowns *v*(*x, t*) and growth
    matrices *G*.

4.  *Staggered grids* give the much-used FDTD method for Maxwell's
    equations.

5.  *More space dimensions* lead to new CFL and vN stability conditions
    on �*t*.

> With *\< x \<* , we don't yet have boundary conditions in space. And
> we are not facing real problems like *u~tt~* = *c*^2^(*x*) *u~xx~* +
> *F e^ikx^*, with a high frequency forcing terms (*k \>\>* 1) and a
> varying speed *c*(*x*).

### Solution of the Wave Equation {#solution-of-the-wave-equation .unnumbered}

> Exactly as for the one-way equation *u~t~* = *cu~x~*, we solve the
> two-way wave equation *u~tt~* = *c*^2^*u~xx~* for each pure
> exponential. That allows us to *separate the variables*. The space
> variable is in *e^ikx^*, and we look for solutions *u*(*x, t*) =
> *G*(*t*)*e^ikx^*:

*�*^2^*u*

> ~2~ *�*^2^*u*

*d*^2^*G*

> *ikx*
>
> 2 2 2
>
> *ikx*
>
> Each *k*
>
> *�t*2 = *c*
>
> *�x*2
>
> becomes
>
> *dt*2 *e*
>
> = *i c k G e*
>
> *.* (1)
>
> Thus *G~tt~* = *i*^2^*c*^2^*k*^2^*G*. This second-order equation has
> two solutions, *G*left = *e^ickt^* and
>
> *G*right = *e*^−*ickt*^. So there are two waves with speed *c*:
>
> Pure waves *u*left(*x, t*) = *e^ik^*^(*x*+*ct*)^ and
>
> *u*right(*x, t*) = *e^ik^*^(*x*−*ct*)^ *.* (2)
>
> Combinations of left-going waves *e^ik^*^(*x*+*ct*)^ will give a
> general function *F*~1~(*x* + *ct*). Combinations of
> *e^ik^*^(*x*−*ct*)^ give *F* (*x* − *ct*). The complete solution
> includes both:
>
> *u*(*x, t*) = *u*left(*x, t*) + *u*right(*x, t*) = *F*~1~(*x* +
> *ct*) + *F*~2~(*x* − *ct*) *.* (3) We need those two functions to
> match an initial shape *u*(*x,* 0) and velocity *u~t~*(*x,* 0): At *t*
> = 0 *u*(*x,* 0) = *F* (*x*) + *F* (*x*) and *u* (*x,* 0) = *c F*
> ^�^(*x*) − *c F* ^�^(*x*) *.* (4) Solving for *F*~1~ and *F*~2~ gives
> the unique solution that matches *u*(*x,* 0) and *u~t~*(*x,* 0):
>
> [*u*(*x* + *ct,* 0) + *u*(*x* − *ct,* 0)]{.underline} [1]{.underline}
> � *x*+*ct*
>
> The "domain of dependence" of *u*(*x, t*) includes the initial values
> from *x* − *ct* to *x* + *ct*. That domain is on the left side of
> Figure 5.9, bounded by the characteristic lines.
>
> Example 1 Starting with zero velocity, *u~t~*(*x,* 0) = 0, the
> integrated term in formula (5) is zero. A step function *S*(*x*)
> (*wall of water* ) will travel left and right along characteristic
> lines, as in Figure 5.8. It reaches the points *x* = 1 and *x* = −1 at
> time *t* = 1*/c*:

Two walls *u*(*x, t*) = [1]{.underline} *S*(*x* + *ct*) +
[1]{.underline} *S*(*x* − *ct*) = �0 or [1]{.underline} or 1� *.*

> 2 2 2
>
> By time *t*, the initial jump at *x* = 0 aﬀects the solution between
> *x* = *ct* and *x* = *ct*. That is the "domain of inﬂuence" of the
> point *x* = 0*, t* = 0.

*x*

*u*(*x,* 0) = 0 0 −*ct* 0 *ct*

> Figure 5.8: Two-wall solution to the wave equation starting from a
> step function.

### The Semidiscrete Wave Equation {#the-semidiscrete-wave-equation .unnumbered}

> Let me start by discretizing only the space derivative *u~xx~*. The
> second diﬀerence *U~j~*~+1~ − 2*U~j~* + *U~j~*~−1~ is the natural
> choice, divided by (�*x*)^2^. For the approximations *U~j~* (*t*) at
> the meshpoints *x* = *j*�*x*, we have a family of ODEs in the time
> direction (*method of lines*):
>
> Again we follow every exponential, looking for *U~j~*(*t*) =
> *G*(*t*)*e^ikj^*^�*x*^. Substitute into (6) and cancel the common
> factor *e^ikj^*^�*x*^. Instead of *G~tt~* = −*c*^2^*k*^2^*G* we have
>
> *c*2 *ik*�*x* −*ik*�*x c*2
>
> Growth equation *G~tt~* = (�*x*)2 (*e* − 2 + *e* )*G* = − (�*x*)2 (2 −
> 2 cos *k*�*x*)(*G*7)*.*
>
> The correct right side −*c*^2^*k*^2^*G* is multiplied by a factor *F*
> ^2^. This *F* ^2^ turns up so often that we need to recognize it! Use
> 2 − 2 cos *α* = 4 sin^2^(*α/*2):
>
> Sinc squared *F* ^2^ =

2.  [− 2 cos *k*�*x*]{.underline}

> 4 sin^2^(*k*�*x/*2)
>
> =
>
> [sin(*k*�*x/*2)]{.underline} ^2^
>
> = *.* (8)
>
> *k*2(�*x*)2 *k*2(�*x*)2 *k*�*x/*2
>
> The "*sinc function*" is deﬁned as sin *α* divided by *α*. When *α* =
> *k*�*x* is small, this is 1 + 0(*α*^2^). Then *F* ^2^ near 1 and
> equation (7) is close to the correct *G~tt~* = −*c*^2^*k*^2^*G*.
>
> For every *k*�*x*, the growth equation (7) has two exponential
> solutions:
>
> Semidiscrete growth *G* = −*c*^2^*F* ^2^*k*^2^*G* gives *G*(*t*) =
> *e*^±*icF*^ *^kt^ .* (9)
>
> The wave speed *c* is multiplied by *F* to give the numerical "phase
> velocity" *cF* . *Notice that F depends on k*. Diﬀerent frequencies
> *e^ikx^* are traveling at diﬀerent speeds *cF* (*k*). This is
> *dispersion* and we will see it again in Section 5. .
>
> I will mention that the "group velocity"---the derivative of *cF k*
> with respect to
>
> *k*---is a more important quantity than the phase velocity *cF* .
>
> The semidiscrete form suggests a good algorithm for the wave equation,
> if we have boundary conditions (say *u* = 0 along the lines *t* = 0
> and *t* = *ω*). If *h* = �*x* = *[^�^]{.underline}* , this interval
> has interior meshpoints. The *n* by *n* second diﬀerence matrix is the
> special *K* from earlier chapters (but now we have −*K*):
>
> Semidiscrete with boundaries *U*
>
> �� *c*2
>
> (*t*) = (�*x*)2 *KU .* (10)
>
> This is just the equation *MU* �� + *KU* = 0 of oscillating springs in
> Section 2.2.
>
> The *n* eigenvalues of *K* are positive numbers 2 − 2 cos *j*�*x*. The
> only change from the equation on an inﬁnite line is that *j* takes
> only the values 1*,* 2*, . . . , n*. The oscillations go on forever as
> in (8), the energy is conserved, and now the waves bounce back from
> the boundaries instead of continuing out to *x* = ±≈.

### Leapfrog from Centered Diﬀerences {#leapfrog-from-centered-diﬀerences .unnumbered}

> A fully discrete method also approximates *u~tt~* by a centered
> diﬀerences. This time diﬀerence "*leaps over* " the space diﬀerence at
> *t* = *n*�*t*:
>
> Leapfrog method [*Uj,n*+1 − 2*Uj,n* + *Uj,n*−1]{.underline} = *c*2
> [*Uj*+1*,n* − 2*Uj,n* + *Uj*−1*,n*]{.underline} *.* (11)
>
> (�*t*)2 (�*x*)2
>
> This has two key diﬀerences from the 5-point molecule for *u~xx~* +
> *u~yy~* = 0 (Laplace). First, *u~tt~* − *c*^2^*u~xx~* has a minus
> sign. Second, we have two conditions at *t* = 0 and no
>
> conditions at a later time. We are marching forward in time (marching
> with Laplace's equation would be totally unstable). A separate
> calculation for the ﬁrst time step computes *U~j,~*~1~ from the
> initial shape *u*(*x,* 0) and the velocity *u~t~*(*x,* 0).
>
> The accuracy of leapfrog is normally second-order. Substitute the true
> *u*(*x, t*) into (11), and use the Taylor series for second diﬀerences
> (Section 1.2). The ﬁrst terms in the local error give consistency.
>
> Second-order *u~tt~*
>
> \+ [1]{.underline} (�*t*)^2^*u* 12

*tttt*

> \+ · · · = *c*^2^(*u~xx~*
>
> \+ [1]{.underline} (�*x*)^2^*u* 12

*xxxx*

> \+ · · · )*.*
>
> \(12\)

In this case *u~tttt~* = *c*^2^*u~xxtt~* = *c*^2^*u~ttxx~* =
*c*^4^*u~xxxx~*. The two sides of (12) diﬀer by

> Local discretization error [1]{.underline} \[(�*t*)^2^*c*^4^
> (�*x*)^2^*c*^2^\]*u*

12

*xxxx*

> \+ · · ·
>
> \(13\)
>
> Again *c*�*t* = �*x* is the golden time step that follows the
> characteristic exactly. The two triangles in Figure 5.9 become exactly
> the same in this borderline case *r* = 1. The CFL reasoning shows
> instability for *r \>* 1. We now show that *r* � 1 is stable.

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image21.png){width="9.101159230096238e-2in"
height="9.101159230096238e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image25.png){width="1.90707895888014in"
height="0.7560203412073491in"}*U* (*x, n*�*t*)

*x*

> *x* − *ct x* + *ct x* − *n*�*x x* + *n*�*x*
>
> Figure 5.9: Domains of dependence: *u* from wave equation and *U* from
> leapfrog.

### Stability of the Leapfrog Method {#stability-of-the-leapfrog-method .unnumbered}

> A diﬀerence equation must use the initial conditions in this whole
> interval, to have a chance of converging to *u*(*x, t*). The domain of
> dependence for *U* must include the domain of dependence for *u*. The
> slopes must have �*t/*�*x* 1*/c*. Since convergence requires
> stability, we have a Courant-Friedrichs-Lewy condition on �*t*:
>
> For a double-step diﬀerence equation, we still look for pure solutions
> *U* (*x, n*�*t*) =

*G^n^e^ikx^*, separating time from space. In the leapfrog equation (11)
this gives

> � *Gn*+1 − 2*Gn* + *Gn*−1 � � *eik*�*x* − 2 + *e*−*ik*�*x* �
>
> Set *r* = *c*�*t/*�*x* and cancel *G^n^*^−1^*e^ikx^*. This leaves a
> quadratic equation for *G*:
>
> *G*^2^ − 2*G* + 1 = *r*^2^ *G* (2 cos *k*�*x* − 2) *.* (14)
>
> The two-step leapfrog equation allows two *G*'s (of course !). For
> stability, both must satisfy \|*G*\| � 1 for all frequencies *k*.
> Rewrite equation (14) for *G*:
>
> Growth factor equation *G*^2^ − 2 �1 − *r*^2^ + *r*^2^ cos *k*�*x*�
> *G* + 1 = 0 *.* (15)
>
> The roots of *G*^2^ − 2*aG* + 1 = 0 are *G* = *a* ± �*a*2 − 1.
> Everything depends on that square root giving an imaginary number,
> when *a*^2^ = \[1 − *r*^2^ + *r*^2^ cos *k*�*x*\]^2^ � 1:
>
> If *a*^2^ � 1 then *G* = *a* ± *i*�1 − *a*2 has \|*G*\| = *a* + (1 −
> *a* ) = 1 *.*
>
> The CFL condition *r* � 1 does produce *a*^2^ � 1 and the leapfrog
> method is stable:
>
> Stability If *r* � 1 then \|*a*\| = \|1 − *r* + *r* cos *k*�*x*\| � (1
> − *r* ) + *r* = 1 *.* (16)
>
> An unstable *r \>* 1 would produce \|*a*\| = \|1 − 2*r*^2^\| *\>* 1 at
> the dangerous *k*�*x* = *ω*. Then both *G*'s are real, and their
> product is 1, and one of them has \|*G*\| *\>* 1.
>
> Note 1 Suppose *r* is exactly 1, so that *c*�*t* = �*x*. At this
> "golden ratio" we expect perfect accuracy. The middle terms 2*U~j,n~*
> and 2*r*^2^*U~j,n~* cancel in the leapfrog equation (11), leaving a
> complete leap over the center points at (*j, n*) when *r* = 1:
>
> Exact leapfrog *U~j,n~*~+1~ + *U~j,n~*~−1~ = *U~j~*~+1*,n*~ +
> *U~j~*~−1*,n*~ *.* (17) The diﬀerence equation is satisﬁed by *u*(*x,
> t*), because it is satisﬁed by every wave
>
> *U* (*x* + *ct*) and *U* (*x* − *ct*). Take *U~j,n~* = *U* (*j*�*x* +
> *cn*�*t*) and use *c*�*t* = �*x*:

+--------------------+-----------------------+-------------------------+
| > *Uj,n*+1 and     | > are both equal to   | *U* (*j*�*x* +          |
| > *Uj*+1*,n*       |                       | *cn*�*t* + �*x*)        |
+====================+=======================+=========================+
| > *Uj,n*−1 and     | > are both equal to   | *U* (*j*�*x* + *cn*�*t* |
| > *Uj*−1*,n*       |                       | − �*x*)                 |
+--------------------+-----------------------+-------------------------+

> So (17) is satisﬁed by all traveling waves *U* (*x* + *ct*), and
> similarly by *U* (*x* − *ct*).
>
> Note 2 You could also apply leapfrog to the *one-way* equation *u~t~*
> = *c u~x~*:
>
> Now the growth factor equation is *G*^2^ − 2(*ir* sin *k*�*x*)*G* − 1
> = 0. Problem conﬁrms that the stability condition is again *r* 1. In
> that stable case, one growth factor is sensible and the other is
> strange:
>
> *G* = *eir* sin *k*�*x* � *eick*�*t* and *G* = −*e*−*ir* sin *k*�*x* �
> −1 *.*
>
> \(19\)
>
> *G*~1~ and *G*~2~ are *exactly on the unit circle*. With \|*G*\| = 1
> there is no room to move. Numerical diﬀusion *∂*(*U~j~*~+1*,n*~
> 2*U~j,n~* + *U~j~*~−1*,n*~) usually adds extra stability, but not
> here. So leapfrog for ﬁrst-order equations can be dangerous.
>
> Section 5.4 will study the convection-diﬀusion equation *u~t~* = *c
> u~x~* + *d u~xx~*.

### Wave Equation in Higher Dimensions {#wave-equation-in-higher-dimensions .unnumbered}

> The wave equation extends to three-dimensional space (with speed set
> at *c* = 1):
>
> 3D Wave equation *u~tt~* = *u~xx~* + *u~yy~* + *u~zz~ .* (20)
>
> Waves go in all directions, and the solution is a superposition of
> pure harmonics. These plane waves now have three wave numbers *k, π,
> m*, and frequency *w*:
>
> Exponential solutions *u*(*x, y, z, t*) = *ei*(*�t* + *kx* + *�y* +
> *mz*) *.*
>
> Substituting into the wave equation gives *�*^2^ = *k*^2^ + *π*^2^ +
> *m*^2^. So there are two frequencies ± *�*. These exponential
> solutions combine to match the initial wave height *u*(*x, y, z,* 0)
> and its velocity *u~t~*(*x, y, z,* 0).
>
> Suppose the initial velocity is a *three-dimensional delta function
> �*(*x, y, z*):
>
> *λ*(*x, y, z*) = *λ*(*x*)*λ*(*y*)*λ*(*z*) gives � � � *f* (*x, y, z*)
> *λ*(*x, y, z*) *dV* = *f* (0*,* 0*,* 0) *.* (21)
>
> The resulting *u*(*x, y, z, t*) will be the *fundamental solution* of
> the wave equation. It is the response to the delta function, which
> gives equal weight to all harmonics. Rather than computing that
> superposition we ﬁnd it from the wave equation itself. Spherical
> symmetry greatly simpliﬁes *u~xx~* + *u~yy~* + *u~zz~*, when *u*
> depends only on *r* and *t*:
>
> *�*^2^*u �*^2^*u* 2 *�u*
>
> Symmetry produces *u*(*r, t*)

*�t*2

> = *�r*2
>
> \+
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image26.png){width="0.3033519247594051in"
> height="6.666666666666667e-3in"} *.* (22)
>
> *r �r*
>
> *Multiplying by r, this is a one-dimensional equation* (*ru*)*~tt~* =
> (*ru*)*~rr~* ! Its solutions *ru* will be functions of *r t* and *r* +
> *t*. Starting from a delta function is like sound going out from a
> bell, or light from a point source. *The solution is nonzero only on
> the sphere r* = *t*. So every point hears the bell only once, as the
> sound wave passes by. An impulse in 3D produces a sharp response (this
> is Huygen's principle).
>
> In 2D, the solution does *not* return to zero for *t \> r*. We
> couldn't hear or see clearly in Flatland. You might imagine a point
> source in two dimensions as a *line source* in the *z*-direction in
> three dimensions. The solution is independent of *z*, so it satisﬁes
> *u~tt~* = *u~xx~* + *u~yy~*. But in three dimensions, spheres starting
> from sources along the line continue to hit the listener. They come
> from further and further away, so the solution decays---but it is not
> zero. The wave front passes, but waves keep coming.
>
> EXERCISE ON EQ.(26)

### Leapfrog Method in Higher Dimensions {#leapfrog-method-in-higher-dimensions .unnumbered}

> In one dimension, two characteristics go out from each point (*x,* 0).
> In 2D and 3D, a *characteristic cone* goes out from (*x, y,* 0) and
> (*x, y, z,* 0). It is essential to see how the stability condition
> changes from *r* = *c*�*t/*�*x* � 1.
>
> The leapfrog method replaces *u~xx~* and *u~yy~* by centered
> diﬀerences at time *n*�*t*:

2

> Leapfrog for *u~tt~* = *u~xx~* + *u~yy~* = *^x^* +
>
> �^2^ *U~n~*
>
> *.*
>
> (�*t*)2 (�*x*)2 (�*y*)2
>
> *U*~0~ and *U*~1~ come from the given initial conditions *u*(*x, y,*
> 0) and *u~t~*(*x, y,* 0). We look for a solution *U~n~* =
> *G^n^e^ikx^e^i�y^* with separation of variables. Substituting into the
> leapfrog equation and canceling *G^n^*^−1^*e^ikx^e^i�y^* produces the
> 2D equation for two *G*'s:
>
> *G*^2^ − 2*G* + 1 [(2 cos *k* �*x* − 2)]{.underline} [(2 cos *π* �*y*
> − 2)]{.underline}
>
> Growth factor
>
> (�*t*)2 = *G*
>
> (�*x*)2
>
> \+ *G* (�*y*)2
>
> *.* (23)

Again this has the form *G*^2^ − 2*aG* + 1 = 0. You can see *a* in
brackets:

� � [�*t*]{.underline} �2 � [�*t*]{.underline} �2 �

> Both roots must have \|*G*\| = 1 for stability. This still requires −1
> � *a* � 1. When the cosines are −1 (the dangerous value) we ﬁnd the
> stability condition for leapfrog:
>
> � [�*t*]{.underline} �2 � [�*t*]{.underline} �2 � [�*t*]{.underline}
> �2 � [�*t*]{.underline} �2
>
> For �*x* = ��*[y]{.underline}* on a square grid, this is �*t* �
> �*x/*�2. In three dimensions it would be
>
> �*t* � �*x/* 3. Those also come from the CFL condition, that the
> characteristic cone
>
> must lie inside the pyramid that gives the leapfrog domain of
> �d[ep]{.underline}endence. Figure 5.10
>
> shows the cone and pyramid just touching, when �*t* = �*x/* 2.

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image27.png){width="8.96751968503937e-2in"
height="8.96751968503937e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image27.png){width="8.96751968503937e-2in"
height="8.96751968503937e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image27.png){width="8.96751968503937e-2in"
height="8.96751968503937e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image27.png){width="8.96751968503937e-2in"
height="8.96751968503937e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image27.png){width="8.96751968503937e-2in"
height="8.96751968503937e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image27.png){width="8.967410323709536e-2in"
height="8.96751968503937e-2in"}(0*,* �*x,* 0)

> Cone has circular base for *u~tt~* = *u~xx~* + *u~yy~* Pyramid has
> diamond base for leapfrog Cone and pyramid go up to (0*,* 0*,* �*t*)
>
> (�*x,* 0*,* 0)

Figure 5.10: The pyramid contains and touches the cone when (�*t*)^2^ =
(�*x*)^2^*/*2.

### An Equivalent First-order System {#an-equivalent-first-order-system .unnumbered}

I can display a system of two equations *v~t~* = *Av~x~* that is
equivalent to *u~tt~* = *c*^2^*u~xx~*:

> First-order system
>
> *[�]{.underline}* � *ut*
>
> � = � 0 *c* � *[�]{.underline}* � *ut*
>
> �*.* (26)
>
> *�t cu~x~ c* 0 *�x cu~x~*
>
> The ﬁrst equation recovers *u~tt~* = *c*^2^*u~xx~*. The second is the
> identity *cu~xt~* = *cu~tx~*. Notice that the 2 by 2 matrix is
> symmetric and its eigenvalues are the wave velocities ±*c*.
>
> This "symmetric hyperbolic" form *v~t~* = *Av~x~* is useful in theory
> and practice. The
>
> energy *E*(*t*) = � 2 √*v*(*x, t*)√ *dx* is automatically constant in
> time ! Here is the proof
>
> for any equation *v~t~* = *Av~x~* with a symmetric matrix *A*:
>
> *�* � 1 √*v*√2� = � *v �vi* = *v*^T^*v* = *v*^T^*Av* = *�* � 1
> *v*^T^*Av*� *.* (27)
>
> When you integrate over all *x*, the left side is *�E/�t*. The right
> side is ^1^ *v*^T^*Av* at
>
> the limits *x* = . Those limits give zero (no signal has reached that
> far). So the derivative of *E*(*t*) is zero, and *E*(*t*) stays
> constant.
>
> The Euler equations of compressible ﬂow are also a ﬁrst-order system,
> but not linear. In physics and engineering, a linear equation deals
> with a small disturbance. Something from outside acts to change the
> equilibrium, but not by much:
>
> in acoustics it is a slowly moving body in aerodynamics it is a
> slender wing
>
> in elasticity it is a small load
>
> in electromagnetism it is a small source.
>
> Below some level, the cause-eﬀect relation is very close to linear. In
> acoustics, the sound speed is steady when pressure is nearly constant.
> In elasticity, Hooke's law holds until the geometry changes or the
> material begins to break down. In electro-magnetism, nonlinearity
> comes with relativistic and quantum eﬀects.
>
> The case to understand has *A* = constant matrix, with *n* real
> eigenvalues *�* and eigenvectors *w*. The vector equation *v~t~* =
> *Av~x~* will split into *n* scalar one-way wave equations *U~t~* = *�
> U~x~*. When *Aw* = *�w* we look for *v*(*x, t*) = *U* (*x, t*)*w*:
>
> *�U �U �U �U �U*
>
> *v~t~* = *Av~x~* becomes
>
> *w* = *A w* = *� w* so
>
> *�t �x �x*
>
> = *� .* (28)
>
> *�t �x*
>
> The complete solution vector is *v*(*x, t*) = *U*~1~(*x* +
> *�*~1~*t*)*w*~1~ + · · · + *U~n~*(*x* + *�~n~t*)*w~n~*. *The problem
> v~t~* = *Av~x~ has n signal speeds �~i~ and it sends out n waves.*
>
> There are *n* characteristic lines *x* + *�~i~t* = constant. The wave
> equation has ^0^ ^c^
>
> and two eigenvalues *�* = *c* and *�* = −*c*. The eigenvectors *w* are
> ( ^[1]{.underline}^ *,* − [1]{.underline} ) and ( ^[1]{.underline}^*,*
> ^[1]{.underline}^ ).

2 2 2 2

> Then the two scalar equations *U~t~* = *�U~x~* produce left and right
> waves:
>
> *� �*
>
> *�*~1~ = *c*
>
> *�*~2~ = −*c*
>
> *�t* (*u~t~* + *c u~x~*) = *c �x*(*u~t~* + *c u~x~*)
>
> *� �*
>
> *�t* (*u~t~* − *c u~x~*) = −*c �x* (*u~t~* − *c u~x~*) *.*
>
> \(29\)
>
> Each equation agrees with *u~tt~* = *c*^2^*u~xx~*. The one-way waves
> are *U* (*x, t*) = *U* (*x* + *�t,* 0). The vector solution *v*(*x,
> t*) is recovered from *U*~1~*w*~1~ + *U*~2~*w*~2~:
>
> � *ut* � � ~[1]{.underline}~ � � ~[1]{.underline}~ �
>
> *x* 2 2
>
> A stable diﬀerence method for *v~t~* = *Av~x~* comes from a stable
> method for *u~t~* = ±*cu~x~*. Just replace *c* by *A* in
> Lax-Friedrichs and Lax-Wendroﬀ, or go to leapfrog.

### Leapfrog on a Staggered Grid {#leapfrog-on-a-staggered-grid .unnumbered}

> The discrete case should copy the continuous case. The two-step
> leapfrog diﬀerence equation should reduce to a pair of one-step
> equations. But if we don't keep the individual equations centered,
> they will lose second-order accuracy. The way to center both
> ﬁrst-order equations is to use a staggered grid (Figure 5.11).
>
> Please allow me to name the two components *v*~1~ = *E* and *v*~2~ =
> *H*. Then the staggered grid for the wave equation matches *Yee's
> method for Maxwell's equations*. Yee's idea transformed the whole
> subject of computational electromagnetics (it is now called the FDTD
> method: ﬁnite diﬀerences in the time domain). Previously the moment
> method, which is Galerkin's method, had been dominant---but staggered
> grids are so natural for *E* and *H*. We stay with the wave equation
> here, copying (26):
>
> Maxwell in 1D *�E/�t* = *c �H/�x* becomes �*~t~E/*�*t*=*c*�*~x~H/*�*x*
> (31)
>
> (normalized) *�H/�t* = *c �E/�x* �*~t~H/*�*t*=*c*�*~x~E/*�*x .*
>
> Those ﬁrst derivatives of *E* and *H* are replaced by ﬁrst diﬀerences.
> I will put *E* on the standard grid and *H* on the staggered
> (half-integer) grid. *Notice how all the diﬀerences are centered in
> Figure 5.11a. This gives second-order accuracy*.
>
> The identities *E~tx~* = *E~xt~* and *H~tx~* = *H~xt~* lead to wave
> equations for *E and H*:
>
> *E~t~* = *cH~x~ E~tt~* = *cH~xt~* = *cH~tx~* = *c*^2^*E~xx~*

*H~t~* = *cE~x~*

> becomes
>
> *H~tt~* = *cE~xt~* = *cE~tx~* = *c*^2^*H~xx~* (32)
>
> In the discrete case, the identity is �*~x~*(�*~t~*) = �*~t~*(�*~x~*).
> Diﬀerences copy derivatives.
>
> When we eliminate *H*, we get the two-step leapfrog equation for *E*.
> And eliminating *E* gives the leapfrog equation for *H*. This all
> comes from the ﬁnite diﬀerence analogue of the cross-derivative
> identity *u~tx~* = *u~xt~*:
>
> *[�]{.underline}* � *[�u]{.underline}* � = *[�]{.underline}*
>
> � *[�u]{.underline}*�
>
> *corresponds to*
>
> [�*~x~*(�*~t~U* )]{.underline}
>
> [�*~t~*(�*~x~U* )]{.underline}
>
> = *.* (33)
>
> *�x �t �t �x* (�*x*)(�*t*) (�*t*)(�*x*)
>
> With equal denominators, we only need to check the numerators. On any
> grid, the same 1's and −1's appear both ways in �*x*�*t* and �*t*�*x*
> !
>
> −1 1
>
> � (� *U* ) = (*U*
>
> − *U* ) − (*U*
>
> − *U* )
>
> 1 −1 �*t*(�*xU* ) = (*Un*+1*,j*+1 − *Un*+1*,j* ) − (*Un,j*+1 − *Un,j*
> )
>
> You could compare ( ) with the Cauchy-Riemann equations *u~x~* =
> *s~y~* and *u~y~* = *s~x~* for the potential *u*(*x, y*) and stream
> function *s*(*x, y*). (Those solve Laplace's equation and not the wave
> equation.) It would be natural to discretize the Cauchy-Riemann
> equations on a staggered grid.
>
> May I emphasize that these grids are useful for many other equations
> too. We will see the "half-point" grid values in Section 5. for the
> ﬂux *F* in the conservation law *u~t~* + *F* (*u*)*~x~* = 0, which is
> a nonlinear extension of the one-way wave equation. Half-point values
> are centrally important throughout the *ﬁnite volume method*.
> Maxwell's equations in integral form lead to the ﬁnite integration
> technique \[ \].

### Maxwell's Equations {#maxwells-equations .unnumbered}

> For electrodynamics, the number *c* in the wave equation is the *speed
> of light*. It is the same large number that appears in Einstein's *e*
> = *mc*^2^. The CFL stability condition *c*^2^(�*t*)^2^ (�*x*)^2^ +
> (�*y*)^2^ + (�*z*)^2^ for the leapfrog method might require very small
> time steps (on the scale of ordinary life). But we all know that the
> wavelength for light is nothing like a meter or a centimeter. The
> leapfrog method is entirely appropriate, and we write Maxwell's
> equations without source terms:
>
> *�E* 1 *�H* 1
>
> Maxwell's equations in free space
>
> =
>
> *�t δ*
>
> curl *H* and
>
> *�t* = − *µ* curl(*E*34*.*)
>
> An important application is the reﬂection of a radar signal by an
> airplane. The region of interest is *exterior* to the plane. In
> principle that region extends inﬁnitely far in all directions. In
> practice we compute inside a large box, and choose boundary conditions
> that don't reﬂect waves back into the box from its artiﬁcial boundary
> (which is a computational region and not physical).
>
> Those *absorbing boundary conditions* \[ \] are crucial to a good
> discretization. Chapter 7 of \[ \] describes how a "*perfectly matched
> layer* " can select coeﬃcients so that waves go through the boundary
> with very little reﬂection. Applications of Maxwell's equations range
> all the way from the Earth's electromagnetic environment to cell
> phones (safety of the user) to micron-scale lasers and photonics.
>
> The ﬁrst of Maxwell's six equations in ( ) involves the electric ﬁeld
> component

*E~x~*:

> *[�]{.underline}*
>
> *�t Ex*
>
> = [1]{.underline} *[�]{.underline} H δ �y ^z^*
>
> *[�]{.underline}*
>
> − *�z*
>
> *H~y~*�*.* (35)
>
> Yee's diﬀerence equation computes *E~x~* at the new time (*n* + 1)�*t*
> from *E~x~* at time
>
> *n*�*t* and the space diﬀerences of *H~z~* and *H~y~ at time* (*n* +
> ^[1]{.underline}^ )�*t*. Figure 5.11
>
> shows how those components of the magnetic ﬁeld H are on a grid that
> is staggered with respect to the grid for E. We have six diﬀerential
> equations like (35) and six diﬀerence equations, to produce *E~x~,
> E~y~, E~z~* at time (*n* + 1)�*t* and then *H~x~, H~y~, H~z~* at time
> (*n* + 1*.*5)�*t*.
>
> The stability condition *c*^2^(�*t*)^2^ � (�*x*)^2^
> +(�*y*)^2^+(�*z*)^2^ is acceptable. Perhaps the greatest drawback is
> the rectangular grid (ﬁnite elements are always more adaptable). But
> the FDTD method has been used with 10^9^ meshpoints, which we cannot
> aﬀord on an unstructured mesh. Finite diﬀerences also have numerical
> dispersion---the discrete wave speeds depend on the wave number *k* =
> (*k~x~, k~y~, k~z~*). Those speeds don't exactly match *c*. We will
> have phase factors like *F* in equation ( ), extended to include �*y*
> and �*z*. When the dispersion creates signiﬁcant errors, we can
> upgrade the spatial diﬀerences to fourth-order accuracy (using more
> mesh values). But those wider diﬀerence methods can go across material
> interfaces and external boundaries. This produces the ever-present
> give and take of numerical analysis: higher accuracy brings greater
> complexity. We can take larger steps �*t* but every step is slower
> (and harder to code).
>
> FIGURE TO COME\...

�*E* �*H* �*H* �*E*

> Figure 5.11: = *c* and = *c* are staggered but centered.

�*t* �*x* �*t* �*x*

### Problem Set 5.3 {#problem-set-5.3 .unnumbered}

1.  Write the equation *u~tt~* = *u~xx~* + *u~yy~* as a ﬁrst-order
    system *v~t~* = *Av~x~* + *Bv~y~* with the vector unknown *v* =
    (*u~t~, u~x~, u~y~*). The matrices *A* and *B* should be symmetric.
    Then the energy *E*(*t*) = ^[1]{.underline}^ (*u*^2^ + *u*^2^ +
    *u*^2^) *dx* is *constant*.

2.  How was the symmetry of *A* used in the ﬁnal step *v*^T^*Av~x~* = (
    ^[1]{.underline}^ *v*^T^*Av*)*~x~* in equa-

tion (27) ? You could write out *v*^T^*Av* = � � *a v* (*x*)*v* (*x* 2

3.  Add Gauss law div *D* = 0 and div *B* = 0 with *D* = *δE* and *B* =
    *µH*.

# The Heat Equation and Convection-Diﬀusion

> The wave equation conserves energy. The heat equation *u~t~* = *u~xx~*
> dissipates energy. The starting conditions for the wave equation can
> be recovered by going backward in time. The starting conditions for
> the heat equation can never be recovered. Compare *u~t~* = *cu~x~*
> with *u~t~* = *u~xx~*, and look for pure exponential solutions *u*(*x,
> t*) = *G*(*t*) *e^ikx^*:
>
> Wave equation: *G* � = *ickG G*(*t*) = *eickt* has \|*G*\| = 1
> (conserving energy)
>
> Heat equation: *G* � = −*k*^2^*G G*(*t*) = *e*−*k*2*t* has *G \<* 1
> (dissipating energy)
>
> Discontinuities are immediately smoothed out by the heat equation,
> since *G* is ex-ponentially small when *k* is large. This section
> solves *u~t~* = *u~xx~* ﬁrst analytically and then by ﬁnite
> diﬀerences. The key to the analysis is the beautiful *fundamental
> solution* starting from a point source (delta function). We will show
> in equation (7) that this special solution is a bell-shaped curve:

\(1\)

> Notice that *u~t~* = *cu~x~* + *du~xx~* has convection and diﬀusion at
> the same time. The wave is smoothed out as it travels. This is a much
> simpliﬁed linear model of the nonlinear Navier-Stokes equations for
> ﬂuid ﬂow. The relative strength of convection by *cu~x~* and diﬀusion
> by *du~xx~* will be given below by the Peclet number.
>
> The Black-Scholes equation for option pricing in mathematical ﬁnance
> also has this form. So do the key equations of environmental and
> chemical engineering.
>
> For diﬀerence equations, explicit methods have stability conditions
> like �*t*
>
> [1]{.underline}
>
> (�*x*)^2^. This very short time step is more expensive than *c*�*t* ≈
> �*x*. Implicit
>
> methods can avoid that stability condition by computing the space
> diﬀerence �^2^*U* at the new time level *n* + 1. This requires solving
> a linear system at each time step.
>
> We can already see two major diﬀerences between the heat equation and
> the wave equation (and also one conservation law that applies to
> both):

1.  *Inﬁnite signal speed.* The initial condition at a single point
    > *immediately* aﬀects the solution at all points. The eﬀect far
    > away is not large, because of the very small exponential *e*^−*x*^
    > ^*/*4*t*^ in the fundamental solution. But it is not zero. (A wave
    > produces no eﬀect at all until the signal arrives, with speed
    > *c*.)

2.  *Dissipation of energy.* The energy ^[1]{.underline}^ � (*u*(*x,
    > t*))^2^ *dx* is a *decreasing* function

> of *t*. For proof, multiply the heat equation *u~t~* = *u~xx~* by *u*.
> Integrate *uu~xx~* by parts with *u*(√) = *u*(−√) = 0 to produce the
> integral of −(*u~x~*)^2^:
>
> Energy decay
>
> *[d]{.underline}* � [1]{.underline} *u*^2^ *dx* = � *uu*
>
> *dt* 2 *^xx^*
>
> *dx* = − � � (*u*

)^2^ *dx* ≈ 0 *.* (2)

> −� −� −�

3.  *Conservation of heat* (analogous to conservation of mass):

> Heat is conserved
>
> *[d]{.underline}* � *u*(*x, t*) *dx* = � *u dt* −� −�
>
> *dx* = ��*u~x~*

(*x, t*) �

> *x*=−�
>
> = 0 *.* (3)

### Analytic Solution of the Heat Equation {#analytic-solution-of-the-heat-equation .unnumbered}

Start with separation of variables to ﬁnd solutions to the heat
equation:

> Assume *u*(*x, t*) = *G*(*t*)*E*(*x*)*.* Then *u~t~* = *u~xx~* gives
> *G* �*E* = *GE* ��
>
> and
>
> *G* � *E* ��
>
> = *.*
>
> *G E*

\(4\)

> The ratio *G*^�^*/G* depends only on *t*. The ratio *E*^��^*/E*
> depends only on *x*. Since equation (4) says they are equal, they must
> be constant. This produces a useful family of solutions to *u~t~* =
> *u~xx~*:
>
> *E* �� *G* �
>
> =
>
> is solved by *E*(*x*) = *e*

ikx

> and *G*(*t*) = *e*

−k^2^t *.*

> *E G*
>
> Two *x*-derivatives produce the same *k*^2^ as one *t*-derivative. We
> are led to exponential solutions of *e^ikx^e*^−*k*^2*t* and to their
> linear combinations (integrals over diﬀerent *k*):

1 **�**�~�~

ikx

> −k^2^t
>
> General solution *u*(*x, t*) = 2*�* −� *u*�~0~(*k*)*e e dx.* (5)
>
> At *t* = 0, formula (5) recovers the initial condition *u*(*x,* 0)
> because it inverts the
>
> Fourier transform *u*�~0~ (Section 4.4.) So we have the analytical
> solution to the heat
>
> two integrals, one to ﬁnd the transform
>
> inverse transform of *u*~0~(*k*)*e*^−*k*^ *^t^* in (5).
>
> *u*�~0~(*k*) of *u*(*x,* 0), and the other to ﬁnd the

2

> Example 1 Suppose the initial function is a bell-shaped Gaussian
> *u*(*x,* 0) = *e*^−*x*^ ^*/*2*�*^ . Then the solution remains a
> Gaussian. The number *λ* that measures the width of the bell increases
> to *λ* + 2*t* at time *t*, as heat spreads out. This is one of the few
> integrals involving *e*^−*x*^ that we can do exactly. Actually, we
> don't have to do the integral.
>
> That function *e*^−*x*^ ^*/*2*�*^ is the impulse response (fundamental
> solution) at time *t* = 0
>
> to a delta function *∂*(*x*) that occurred earlier at *t* = −
> [1]{.underline} *λ*. So the answer we want (at
>
> time *t*) is the result of starting from that *∂*(*x*) and going
> forward a total time ^[1]{.underline}^*λ* + *t*:
>
> Widening Gaussian *u*(*x, t*) = *�*(2*λ*)

*�*(2*λ* + 4*t*)

> *e*−*x*^2^*/*(2*�* + 4*t*) *.* (6)
>
> This has the right start at *t* = 0 and it satisﬁes the heat equation.

### The Fundamental Solution {#the-fundamental-solution .unnumbered}

> For a delta function *u*(*x,* 0) = *∂*(*x*) at *t* = 0, the Fou�rier
> transform is *u*�~0~(*k*) = 1. Then
>
> this *u* uses a neat integration by parts for *�u/�x*. It has three
> 1's, from the integral
>
> of *ke*^−*k*^ *^t^* and the derivative of *ie^ikx^* and integration by
> parts itself:
>
> *[�u]{.underline}* = [1]{.underline} � � (*e*−*k*2*tk*)(*ieikx*) *dk*
> = − [1]{.underline} � � (*e*−*k*2*t*)(*xeikx*) *dk* = −
> *[xu]{.underline} .* (7)
>
> *�x* 2*�* −�
>
> 4*�t* −� 2*t*
>
> 2
>
> This lin�e[ar e]{.underline}quation *�u/�x* = −*xu/*2*t* is solved� by
> *u* = *ce*^−*x*^ ^*/*4*t*^. The constant
>
> the heat *u*(*x,* 0) *dx* = *∂*(*x*) *dx* = 1 that we started with. It
> is the area under a bell-shaped curve.) The solution (1) for diﬀusion
> from a point source is conﬁrmed:

Fundamental solution from

> *u*(*x,* 0) = *�*(*x*)
>
> In two dimensions, we can separate *x* from *y* and solve *u~t~* =
> *u~xx~* + *u~yy~*:
>
> \(8\)

Fundamental solution from � [1]{.underline} �2 −*x*2*/*4*t* −*y*2*/*4*t*

> *u*(*x, y,* 0) = *�*(*x*)*�*(*y*)
>
> *u*(*x, y, t*) =
>
> �4*�t e*
>
> *e .* (9)
>
> With patience you can verify that *u*(*x, t*) and *u*(*x, y, t*) do
> solve the 1D and 2D heat
>
> equations (Problem ). The zero initial conditions away
> fr�o[m]{.underline} the origin are
>
> correct as *t* � 0, because *e*^−*c/t*^ goes to zero much faster than
> 1*/ t* blows up. And
>
> since the total heat remains at *u dx* = 1 or *u dx dy* = 1, we have a
> valid solution.
>
> If the source is at another point *x* = *s*, then the response just
> shifts by *s*. The exponent becomes (*x s*)^2^*/*4*t* instead of
> *x*^2^*/*4*t*. If the initial *u*(*x,* 0) is a *combination* of delta
> functions, then by linearity the solution is the same combination of
> responses. But every *u*(*x,* 0) is an integral *∂*(*x*−*s*) *u*(*s,*
> 0) *ds* of point sources ! So the solution to *u~t~* = *u~xx~* is an
> integral of the responses to *∂*(*x s*). Those responses are
> fundamental solutions starting from all points *x* = *s*:

\(10\)

> Now the formula is reduced to one inﬁnite integral---but still not
> simple. And for a problem with boundary conditions at *x* = 0 and *x*
> = 1 (the temperature on a ﬁnite interval, much more realistic), we
> have to think again. Similarly for an equation *u~t~* =
> (*c*(*x*)*u~x~*)*~x~* with variable conductivity or diﬀusivity. That
> thinking probably leads us to ﬁnite diﬀerences.
>
> I see the solution *u*(*x, t*) in (10) as the convolution of the
> initial function *u*(*x,* 0) with the fundamental solution. Three
> important properties are immediate:

1.  *If u*(*x,* 0) � 0 *for all x then u*(*x, t*) � 0 *for all x and t.*
    Nothing in formula (10) will be negative.

2.  *The solution is inﬁnitely smooth.* The Fourier transform
    *u*~0~(*k*) in (5) is multiplied by *e*^−*k*^2*t*. In (10), we can
    take all the *x* and *t* derivatives we want.

3.  *The scaling matches x*^2^ *with t.* A diﬀusion constant *d* in the
    equation *u~t~* = *du~xx~* will lead to the same solution with *t*
    replaced by *dt*, when we write the equation as *�u/�*(*dt*) =
    *�*^2^*u/�x*^2^. The fundamental solution has *e*^−*x*^2*/*4*dt* and
    its Fourier transform has *e*^−*dk*^ *^t^*.

> Example 2 Suppose the initial temperature is a step function *u*(*x,*
> 0) = 0. Then for negative *x* and *u*(*x,* 0) = 1 for positive *x*.
> The discontinuity is smoothed out immediately, as heat ﬂows to the
> left. The integral in formula (10) is zero up to the jump:
>
> *u*(*x, t*) = [1]{.underline} 4*�t*
>
> ^�^ *e*−(*x* − *s*)^2^*/*4*t ds .* (11)
>
> 0
>
> No luck with this integral ! We can ﬁnd the area under a complete
> bell-shaped curve (or half the curve) but there is no elementary
> formula for the area under a piece of the curve. No elementary
> function has the derivative *e*^−*x*^ . That is unfortunate, since
> those integrals give *cumulative probabilities* and statisticians need
> them all the time. So they have been normalized into the error
> function and tabulated to high accuracy:

[2]{.underline}

> Error function erf(*x*) = �*�*
>
> *e*−*s*^2^
>
> *ds .* (12)
>
> The integral from −*x* to 0 is also erf(*x*). The normalization by
> 2*/*�*�* gives erf(√) = 1. We can p�ro [d]{.underline}uce this error
> function from the h�ea[t]{.underline} equation integral (11) by
> setting
>
> *S* = (*s* − *x*)*/* �4[*t*.]{.underline} Then *s* = 0 changes to *S*
> = −*x/* 4*t* as the lower lim�i[t o]{.underline}n the integral,

and *dS* = *ds/* 4*t*. Split into an integral from 0 to √, and from
−*x/* 4*t* to 0:

> �4*t* � �
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image28.png){width="0.10167213473315835in"
> height="5.0e-3in"} −*S*2 [1]{.underline} � � *[x]{.underline}* ��
>
> *u*(*x, t*) = �4*�t*
>
> −*x/*

*e*

�4*t*

> *dS* =

2

> 1 + erf
>
> �4*t*
>
> *.* (13)
>
> Good idea to check that this gives *u* = ^[1]{.underline}^ at *x* = 0
> (where the error function is zero).
>
> This is the only temperature we know exactly, by symmetry between left
> and right.

### Explicit Finite Diﬀerences {#explicit-finite-diﬀerences .unnumbered}

> The simplest ﬁnite diﬀerences are *forward* for *�u/�t* and *centered*
> for *�*^2^*u/�x*^2^:
>
> Each new value *U~j,n~*~+1~ is given explicitly by *U~j,n~* +
> *R*(*U~j~*~+1*,n*~ 2*U~j,n~* + *U~j,n~*~−1~). The crucial ratio for
> the heat equation *u~t~* = *u~xx~* is now *R* = �*t/*(�*x*)^2^.
>
> We substitute *U~j,n~* = *G^n^ e^ikj^*^�*x*^ to ﬁnd the growth factor
> *G* = *G*(*k,* �*t,* �*x*):
>
> One-step *G* = 1 + *R*(*eik*�*x* 2 + *e*−*ik*�*x*) = 1 + 2*R*(cos
> *k*�*x* 1) *.* (15)
>
> growth factor
>
> *G* is real, just as the exact one-step factor *e*^−*k*^ ^�*t*^ is
> real. Stability requires \|*G*\| ≈ 1. Again the most dangerous case is
> when the cosine equals −1 at *k*�*x* = *�*:
>
> �*t* 1
>
> Stability condition \|*G*\| = \|1 − 4*R*\| ≈ 1 which requires *R* =
> (�*x*)2 � 2 *.* (16)
>
> In many cases we accept that small time step �*t* and use this simple
> method. The accuracy from forward �*~t~* and centered �^2^ is \|*U* −
> *u*\| = *O*(�*t* + (�*x*)^2^). Those two error terms are comparable
> when *R* is ﬁxed.
>
> We could improve this one-step method to a multistep method. The
> "method of lines" calls an ODE solver for the system of diﬀerential
> equations (continuous in time, discrete in space). There is one
> equation for every meshpoint *x* = *jh*:
>
> *dU* �^2^ *U dU~j~ U~j~*~+1~ − 2*U~j~* + *U~j~*~−1~
>
> Method of Lines
>
> = =
>
> *dt* (�*x*)2 *dt*
>
> (�*x*)2
>
> *.* (17)
>
> This is a stiﬀ system, because its matrix *K* (second diﬀerence
> matrix) has a large condition number: *�*~max~(*K*)*/�*~min~(*K*) *N*
> ^2^. We could choose a stiﬀ solver like ode15s in MATLAB.

### Implicit Finite Diﬀerences {#implicit-finite-diﬀerences .unnumbered}

> A fully implicit method for *u~t~* = *u~xx~* computes �^2^ *U* at the
> new time (*n* + 1)�*t*:
>
> �*tUn* �2 *Un*+1 *Uj,n*+1 − *Uj,n Uj*+1*,n*+1 − 2*Uj,n*+1 +
> *Uj*−1*,n*+1
>
> Implicit
>
> = =
>
> �*t* (�*x*)2 �*t*

(�*x*)2

> *.* (18)
>
> The accuracy is still ﬁrst-order in time and second-order in space.
> But stability no longer depends on the ratio *R* = �*t/*(�*x*)^2^. We
> have *unconditional* stability, with a growth factor 0 *\< G* 1 for
> all *k*. Substituting *U~j,n~* = *G^n^e^ijk^*^�*x*^ into (18) and then
> canceling those terms from both sides leaves an extra *G* on the right
> side:
>
> *G* = 1 + *RG*(*eik*�*x* 2 + *e*−*ik*�*x*) leads to *G* =
> [1]{.underline} *.* (19)
>
> 1 + 2*R*(1 − cos *k*�*x*)
>
> The denominator is at least 1, which ensures that 0 *\< G* ≈ 1. The
> time step is controlled by accuracy, because stability is no longer a
> problem.
>
> There is a simple way to improve to second-order accuracy. *Center
> everything at step n* + ^[1]{.underline}^ . Average an explicit �^2^
> *U~n~* with an implicit �^2^ *U~n~*~+1~. This produces the
>
> 2 *x* *x*
>
> famous *Crank-Nicolson method* (like the trapezoidal rule):
>
> Crank-Nicolson [*Uj,n*+1 − *Uj,n*]{.underline} = 1 (�^2^ *U*
>
> \+ �^2^ *U*
>
> ) *.* (20)

�*t* 2(�*x*)2

> *x j,n*
>
> *x j,n*+1

Now the growth factor *G*, by substituting *U~j,n~* = *G^n^e^ijk^*^�*x*^
into (20), solves

> [*G* − 1]{.underline} = [*G* + 1]{.underline} (2 cos *k*�*x* − 2) *.*
> (21)
>
> Separate out the part involving *G*, write *R* for �*t/*(�*x*)^2^, and
> cancel the 2's:
>
> Unconditional stability *G* = [1 + *R*(cos *k*�*x* − 1)]{.underline}
> has *G* 1 *.* (22)
>
> 1 − *R*(cos *k*�*x* − 1)
>
> The numerator is smaller than the denominator, since cos *k*�*x* 1. We
> do notice that cos *k*�*x* = 1 whenever *k*�*x* is a multiple of 2*�*.
> Then *G* = 1 at those frequencies, so Crank-Nicolson does not give the
> strict decay of the fully implicit method. We
>
> could weight the implicit �^2^ *U~n~*~+1~ by *a \>* ^[1]{.underline}^
> and the explicit �^2^ *U~n~* by 1 − *a \<* ^[1]{.underline}^ , to
>
> give a whole range of unconditionally stable methods (Problem ).
>
> Numerical example

### Finite Intervals with Boundary Conditions {#finite-intervals-with-boundary-conditions .unnumbered}

> We introduced the heat equation on the whole line −√ *\< x \<* √. But
> a physical problem will be on a ﬁnite interval like 0 ≈ *x* ≈ 1. We
> are back to Fourier series (not Fourier integrals) for the solution
> *u*(*x, t*). And second diﬀerences bring back the great matrices *K,
> T, B, C* that depend on the boundary conditions:
>
> Absorbing boundary at *x* = 0: The temperature is held at *u*(0*, t*)
> = 0. Insulated boundary: No heat ﬂows through the left boundary if
> *u~x~*(0*, t*) = 0.
>
> If both boundaries are held at zero temperature, the solution will
> approach *u*(*x, t*) = 0 everywhere as *t* increases. If both
> boundaries are insulated as in a freezer, the solution will approach
> *u*(*x, t*) = *constant*. No heat can escape, and it is evenly
> distributed as
>
> *t* � √. This case still has the conservation law � 1 *u*(*x, t*) *dx*
> = constant.
>
> Example 3 (Fourier series solution) We know that *e^ikx^* is
> multiplied by *e*^−*k*^ *^t^* to give a solution of the heat equation.
> Then *u* = *e*^−*k*^ *^t^* sin *kx* is another solution (combining
>
> \+*k* with −*k*). With zero boundary conditions *u*(0*, t*) = *u*(1*,
> t*) = 0, the only allowed
>
> frequencies are *k* = *n�* (then sin *n�x* = 0 at both ends *x* = 0
> and *x* = 1). The complete solution is a combination of these
> exponential solutions with *k* = *n�*:
>
> Complete solution *u*(*x, t*) = � *b e*−*n*2*�*2*t* sin *n�x .* (23)
>
> *n*=1
>
> The Fourier sine coeﬃcients *b~n~* are chosen to match *u*(*x,* 0) = �
> *b~n~* sin *n�x* at *t* = 0.
>
> You can expect cosines to appear for insulated boundaries, where the
> slope (not the temperature) is zero. This gives exact solutions to
> compare with ﬁnite diﬀerence solutions. For ﬁnite diﬀerences,
> *absorbing boundary conditions produce the matrix K* (not *B* or *C*).
> The choice between explicit and implicit decides whether we have
> second diﬀerences −*KU* at time level *n* or level *n* + 1:
>
> Explicit method *U~n~*~+1~ − *U~n~* = −*RKU~n~* (24)
>
> Fully implicit *U~n~*~+1~ − *U~n~* = −*RKU~n~*~+1~ (25)
>
> Crank-Nicolson *U~n~*~+1~ − *U~n~* = − [1]{.underline} *RK*(*U~n~* +
> *U~n~*~+1~) *.* (26)
>
> The explicit stability condition is again *R* ≈ [1]{.underline}
> (Problem ). Both implicit meth-ods are unconditionally stable (in
> theory). The reality test is to try them in practice.
>
> An insulated boundary at *x* = 0 changes *K* to *T* . Two insulated
> boundaries produce *B*. Periodic conditions will produce *C*. The fact
> that *B* and *C* are singular no longer stops the computations. In the
> fully implicit method (*I* + *RB*)*U~n~*~+1~ = *U~n~*, the extra
> identity matrix makes *I* + *RB* invertible.
>
> The two-dimensional heat equation describes the temperature
> distribution in a plate. For a square plate with absorbing boundary
> conditions, the diﬀerence matrix *K* changes to *K*2D. The bandwidth
> jumps from 1 (triangular matrix) to *N* (when meshpoints are ordered a
> row at a time). Each time step of the implicit method now requires a
> serious computation. So implicit methods pay an increased price for
> stability, to avoid the explicit restriction �*t* ≈ [1]{.underline}
> (�*x*)^2^ + ^[1]{.underline}^(�*y*)^2^.

### Convection-Diﬀusion {#convection-diﬀusion .unnumbered}

> Put a chemical into ﬂowing water. It diﬀuses while it is carried along
> by the ﬂow. A diﬀusion term *d u~xx~* appears together with a
> convection term *c u~x~*. This is the simplest model for one of the
> most important diﬀerential equations in engineering:

\(27\)

> On the whole line −√ *\< x \<* √, the ﬂow and the diﬀusion don't
> interact. If the velocity is *c*, convection just carries along the
> diﬀusing solution to *h~t~* = *d h~xx~*:

Diﬀusing traveling wave *u*(*x, t*) = *h*(*x* + *ct, t*) *.* (28)

> Substituting into equation (27) conﬁrms that this is the solution
> (correct at *t* = 0):
>
> Chain rule *.* (29)
>
> Exponentials also show this separation of convection *e^ikct^* from
> diﬀusion *e*^−*dk*^2 *t*:
>
> Starting from *e*ikx *u*(*x, t*) = *e*−dk2t *e*ik(x + ct) *.* (30)
>
> Convection-diﬀusion is a terriﬁc model problem, and the constants *c*
> and *d* clearly have diﬀerent units. We take this small step into
> *dimensional analysis*:
>
> distance (distance)^2^
>
> Convection coeﬃcient *c*: Diﬀusion coeﬃcient *d*: (31)
>
> time time
>
> Suppose *L* is a typical length scale in the problem. *The Peclet
> number P e* = *cL/d* is dimensionless. It measures the relative
> importance of convection and diﬀusion. This Peclet number for the
> linear equation (27) corresponds to the *Reynolds number* for the
> nonlinear Navier-Stokes equations (Section ).
>
> In the diﬀerence equation, the ratios *r* = *c*�*t/*�*x* and 2*R* =
> 2*d*�*t/*(�*x*)^2^ are also dimensionless. That is why the stability
> conditions *r* ≈ 1 and 2*R* ≈ 1 were natural for the wave and heat
> equations. The new problem combines convection and diﬀusion, and the
> *cell Peclet number P* uses �*x/*2 as the length scale in place of
> *L*:
>
> *r c* �*x*
>
> Cell Peclet Number *P* = = *.* (32) 2*R* 2*d*
>
> We still don't have agreement on the best ﬁnite diﬀerence
> approximation! Here are three natural candidates (you may have an
> opinion after you try them):

1.  Forward in time, centered convection, centered diﬀusion

2.  Forward in time, upwind convection, centered diﬀusion

3.  Explicit convection (*centered or upwind* ), with implicit diﬀusion.

> Each method will show the eﬀects of *r* and *R* and *P* (we can
> replace *r/*2 by *RP* ):

1.  Centered explicit

> [*Uj,n*+1 − *Uj,n*]{.underline} = *c [Uj]{.underline}*[+1*,n* −
> *Uj*−1*,n*]{.underline} + *d*
>
> �2 *Uj,n*
>
> *.* (33)
>
> �*t* 2�*x* (�*x*)2
>
> Every new value *U~j,n~*~+1~ is a combination of three known values at
> time *n*:
>
> *U~j,n~*~+1~ = (1 − 2*R*)*U~j,n~* + (*R* + *RP* )*U~j~*~+1*,n*~ + (*R*
> − *RP* )*U~j~*~−1*,n*~ *.* (34)
>
> Those three coeﬃcients add to 1, and *U* = constant certainly solves
> equation (33). *If all three coeﬃcients are positive, the method is
> surely stable.* More than
>
> that, *oscillations cannot appear*. Positivity of the middle coeﬃcient
> requires *R* ≈ ~2~
>
> as usual for diﬀusion. Positivity of the other coeﬃcients requires
> \|*P* \| � 1. Of course *P* will be small when �*x* is small (so we
> have convergence as �*x* 0). In avoiding oscillations, the actual cell
> size �*x* is crucial to the quality of *U* .
>
> Figure 5.12 was created by Strikwerda \[59\] and Persson to show the
> oscillations for *P \>* 1 and the smooth approximations for *P \<* 1.
> Notice how the initial hat function is smoothed and spread and shrunk
> by diﬀusion. Problem ﬁnds the exact solution, which is moved along by
> convection. Strictly speaking, even the oscillations might pass the
> stability test \|*G*\| ≈ 1 (Problem ). But they are unacceptable.
>
> Figure 5.12: Convection-diﬀusion with and without numerical
> oscillations: *R* =
>
> , *r* = and .
>
> *[U]{.underline} [U]{.underline} [U]{.underline} [U]{.underline}* �^2^
> *U*

2.  Upwind convection = *c* + *d ^x^*

> �*t* �*x* (�*x*)2
>
> *.* (35)
>
> The accuracy in space has dropped to ﬁrst order. But the oscillations
> are eliminated whenever *r* + 2*R* ≈ 1. That condition ensures three
> positive coeﬃcients when (35) is solved for the new value
> *U~j,n~*~+1~:
>
> *U~j,n~*~+1~ = (*RP* + *R*)*U~j~*~+1*,n*~ + (1 − *RP* −
> 2*R*)*U~j,n~* + *RU~j~*~−1*,n*~ *.* (36)
>
> Arguments are still going, comparing the centered method 1 and the
> upwind method 2. The diﬀerence between the two convection terms,
> upwind minus centered, is ac-tually a diﬀusion term hidden in (35) !
>
> [*Uj*+1 − *Uj*]{.underline} [*Uj*+1 − *Uj*−1]{.underline}
> �[�*x*]{.underline} � [*Uj*+1 − 2*Uj* + *Uj*−1]{.underline}
>
> Extra diﬀusion − = *.* (37)
>
> So the upwind method has this extra numerical diﬀusion or "*artiﬁcial
> viscosity* " to kill oscillations. It is a non-physical damping. If
> the upwind approximation were included in Figure 5.12, it would be
> *distinctly below* the exact solution. Nobody is perfect.

3.  Implicit diﬀusion

> [*Uj,n*+1 − *Uj,n*]{.underline}
>
> = *c [Uj]{.underline}*[+1*,n* − *Uj,n*]{.underline}
>
> �2 *Uj,n*+1
>
> \+ *d ^x^*
>
> *.* (38)
>
> �*t* �*x* (�*x*)2
>
> MORE TO DO

### Problem Set 5.4 {#problem-set-5.4 .unnumbered}

1.  Solve the heat equation starting from a combination *u*(*x,* 0�) =
    *∂*(*x* + 1) − 2*∂*(*x*) +

2.  Integrating the answer to Problem 1 gives another solution to the
    heat equation:

> � *~x~*
>
> Show that *w*(*x, t*) = *u*(*X, t*) *dX* solves *w~t~* = *w~xx~ .*
>
> 0

Graph the initial function *w*(*x,* 0) and sketch the solution *w*(*x,*
1).

3.  Integrating once more solves the heat equation *h~t~* = *h~xx~*
    starting from *h*(*x,* 0) =

> *w*(*X,* 0) *dX* = *hat function*. Draw the graph of *h*(*x,* 0).
> Figure 5.12 shows the graph of *h*(*x, t*), shifted along by
> convection to *h*(*x* + *ct, t*).

4.  In convection-diﬀusion, compare the condition *R* ≈ [1]{.underline}
    *, P* ≈ 1 (for positive coef-ﬁcients in the centered method) with
    *r* + 2*R* 1 (for the upwind method). For which *c* and *d* is the
    upwind condition less restrictive, in avoiding oscillations ?

5.  The eigenvalues of the *n* by *n* second diﬀerence matrix *K* are
    *�~k~* = 2 − 2 cos *[^k�^]{.underline}* . The eigenvectors *y~k~* in
    Section 1.5 are discrete samples of sin *k�x*. Write the general
    solutions to the fully explicit and fully implicit equations (14)
    and (18) after *N* steps, as combinations of those discrete sines
    *y~k~* times powers of *�~k~*.

6.  Another exact integral involving *e*^−*x*^ ^*/*4*t*^ is

> � � *x e*−*x*2*/*4*t dx* = �−2*t e*−*x*2*/*4*t*�� = 2*t .*
>
> From (17), show that the temperature is *u* = �*t*
>
> starting from a ramp *u*(*x,* 0) = max(0*, x*).
>
> at the center point *x* = 0

7.  A ramp is the integral of a step function. So the solution of *u~t~*
    = *u~xx~* starting from a ramp (Problem 6) is the integral�o
    [f]{.underline} the solution starting from a step

> function (Example 2 in the text). Then *t* must be the total amount of
> heat
>
> that has crossed from *x \>* 0 to *x \<* 0 in Example 2 by time *t*.
> Explain each of those three sentences.
>
> *5.5. DIFFERENCE MATRICES AND EIGENVALUES* �c 2006 Gilbert Strang

# Diﬀerence Matrices and Eigenvalues

> This brief section collects together useful notes on ﬁnite diﬀerence
> matrices, and also ﬁnite element matrices. Certainly those special
> matrices *K, T, B, C* from the start of the book are the building
> blocks for approximations to *u~xx~* and *u~yy~*. Second derivatives
> and fourth derivatives lead to symmetric matrices. *First derivatives
> are antisymmetric*. They present more diﬃculties.
>
> A symmetric matrix has orthogonal eigenvectors. For those special
> matrices, the eigenvectors are discrete samples of sines and cosines
> and *e^ikx^*. The eigenvalues are
>
> real, and they often involve *e^ik^*^�*x*^ −2+*e*^−*ik*�*x*^. That is
> the discrete factor 2 cos *k*�*x*−2. Divided by (�*x*)^2^, it is close
> for small *k* to the factor −*k*^2^ from the second derivative of
> *e^ikx^*. *The von Neumann approach using e^ikx^ matches the
> eigenvectors of these*
>
> *matrices*, and the growth factors *G* match the eigenvalues.
>
> For a one-sided (upwind) diﬀerence, the matrix eigenvalues are not
> always reliable.
>
> For a centered diﬀerence they do follow von Neumann. Compare

�−1 1

⎡ � 0 1 ⎡

�^+^ = �

> −1 1
>
> ~0~ [1]{.underline} −1 0 −1
>
> � =

−1 1 2 −1 0 −1

−1 −1 0

> The eigenvalues of the triangular upwind matrix �^+^ are all −1
> (*useless*). The eigen-values of the antisymmetric �^0^ are guaranteed
> to be imaginary like the factor *ik* from the derivative of *e^ikx^*.
> The eigenvalues *�* = −1 for �^+^ do not make upwind diﬀerences
> useless. They only mean that the von Neumann test, which produces
> *e^ik^*^�*x*^ − 1, is better than relying on eigenvalues.
>
> As it stands, �^+^ is exactly in "*Jordan form*." The matrix has only
> one line of eigenvectors, not *n*. It is an extreme example of a
> nondiagonalizable (and somehow degenerate) matrix. If the diagonals of
> −1's and 1's are extended to inﬁnity, then Fourier and von Neumann
> produce vectors with components *e^ikj^*^�*x*^ and with eigen-values
> *e^ik^*^�*x*^ − 1. In summary: For normal matrices, eigenvalues are a
> reliable guide.
>
> For other constant-diagonal matrices, better to rely on von Neumann.
>
> Brieﬂy, the discrete growth factors *G* are exactly the eigenvalues
> when the matrices
>
> are called "*normal* " and the test is *AA*^T^ = *A*^T^*A* (for
> complex matrices take the conjugate transpose *A*�). This test is
> passed by all symmetric and antisymmetric
>
> and orthogonal matrices.

### Options for First Diﬀerences {#options-for-first-diﬀerences .unnumbered}

> Upwind elements Streamline diﬀusion DG
>
> Boundary conditions Convection-diﬀusion

# Nonlinear Flow and Conservation Laws

> Nature is nonlinear. The coeﬃcients in the equation *depend on the
> solution u*. In place of *u~t~* = *c u~x~* we will study *u~t~* +
> *uu~x~* = 0 and more generally *u~t~* + *f* (*u*)*~x~* = 0. These are
> "conservation laws" and the conserved quantity is the integral of *u*.
>
> The ﬁrst part of this book emphasized the balance equation: forces
> balance and currents balance. For steady ﬂow this was Kirchhoﬀ's
> Current Law: *ﬂow in equals ﬂow out*. The net ﬂow was zero. Now the
> ﬂow is *unsteady* ---the "mass inside" is changing. So a new *�/�t*
> term will enter the conservation law.
>
> There is "ﬂux" through the boundaries. In words, the rate of change of
> mass inside a region equals that incoming ﬂux. For an interval \[*a,
> b*\], the incoming ﬂux is the diﬀerence in ﬂuxes at the endpoints *a*
> and *b*:
>
> In applications, *u* can be a *density* (of cars along a highway). The
> integral of *u* gives the mass (number of cars) between *a* and *b*.
> This number changes with time, as cars ﬂow in at point *a* and out at
> point *b*. The ﬂux is density *u* times velocity *v*.
>
> The integral form is fundamental. We can get a diﬀerential form by
> allowing *b* to approach *a*. Suppose *b a* = �*x*. If *u*(*x, t*) is
> a smooth function, its integral over a distance �*x* will have leading
> term �*x u*(*a, t*). So if we divide equation (1) by �*x*, the limit
> as �*x* approaches zero is *�u/�t* = −*�f* (*u*)*/�x*:
>
> When *f* (*u*) = density *u* times velocity *v*(*u*), we can solve
> this single conservation law. For traﬃc ﬂow, the velocity *v*(*u*) can
> be measured (it will decrease as density increases). In gas dynamics
> there are also conservation laws for momentum and energy. The velocity
> *v* becomes another unknown, along with the pressure *p*. The Euler
> equations for gas dynamics in one space dimension include two
> additional equations:
>
> Conservation of momentum
>
> *� �*
>
> (*uv*) + (*uv*^2^ + *p*) = 0 (3)
>
> *�t �x*
>
> *� �*
>
> Conservation of energy (*E*) + (*Ev* + *Ep*) = 0 *.* (4)
>
> *�t �x*
>
> Systems of conservation laws are more complicated, but our scalar
> equation (2) al-ready has the possibility of shocks. A shock is a
> discontinuity in the solution *u*(*x, t*), where the diﬀerential form
> breaks down and we need the integral form (1).
>
> The other outstanding example, together with traﬃc ﬂow, is Burger's
> equation,
>
> 1 2

for *u* = velocity. The ﬂux *f* (*u*) is
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image29.png){width="6.833661417322835e-2in"
height="6.666666666666667e-3in"}*u* . The "inviscid" form has no *u* :

> *[�u]{.underline} [�]{.underline}* � *u*^2^ � *[�u]{.underline}
> [�u]{.underline}*
>
> When both the density and velocity are unknowns, these examples
> combine into *conservation of mass and conservation of momentum*.
> Typically we change density to *ν*. For small disturbances of a
> uniform density *ν*~0~, we could linearize the conservation laws and
> reach the wave equation (Problem ). But the Euler and Navier-Stokes
> equations are truly nonlinear, and we begin the task of solving them.
>
> We will approach conservation laws (and these examples) in three ways:

1.  By following characteristics until trouble arrives: they separate or
    collide

2.  By a special formula ( )

3.  By ﬁnite diﬀerence and ﬁnite volume methods, which are the practical
    choice.

### Characteristics {#characteristics .unnumbered}

> The one-way wave equation *u~t~* = *c u~x~* is solved by *u*(*x, t*) =
> *u*(*x* + *ct,* 0). Every initial value *u*~0~ is carried along a
> characteristic line *x* + *ct* = *x*~0~. Those lines are parallel when
> the velocity *c* is a constant.
>
> The conservation law *u~t~* = +*u u~x~* = 0 will be solved by *u*(*x,
> t*) = *u*(*x ut,* 0). Every initial value *u*~0~ = *u*(*x*~0~*,* 0) is
> carried along a characteristic line *x* − *u*~0~*t* = *x*~0~. Those
> lines are *not* parallel because their slopes depend on the initial
> value *u*~0~.
>
> Notice that the formula *u*(*x, t*) = *u*(*x* − *ut,* 0) involves *u*
> on both sides. It gives the solution "implicitly." If the initial
> function is *u*(*x,* 0) = 1 − *x*, for example, the formula must be
> solved for *u*:
>
> *u* = 1 − (*x* − *ut*) gives (1 − *t*)*u* = 1 − *x* and *u* = [1 −
> *x*]{.underline} *.* (5)
>
> This does solve Burger's equation, since the time derivative *u~t~* =
> (1 − *x*)*/*(1 − *t*)^2^ is equal to −*uu~x~*. The characteristic
> lines (with diﬀerent slopes) can meet. This is an extreme example,
> where all characteristics meet at the same point:
>
> *x* − *u*~0~*t* = *x*~0~ or *x* − (1 − *x*~0~)*t* = *x*~0~ which goes
> through *x* = 1*, t* = 1 (6)
>
> You see how the solution *u* = (1 − *x*)*/*(1 − *t*) becomes 0*/*0 at
> that point *x* = 1*, t* = 1. Beyond their meeting point, the
> characteristics cannot completely decide *u*(*x, t*).
>
> A more fundamental example is the Riemann problem, which starts from
> two constant values *u* = *A* and *u* = *B*. Everything depends on
> whether *A \> B* or *A \< B*. On the left side of Figure 5.13, with *A
> \> B*, *the characteristics meet*. On the right
>
> side, with *A \< B*, *the characteristics separate*. Both cases
> present a new (nonlinear) problem, when we don't have a single
> characteristic that is safely carrying the correct initial value to
> the point. This Riemann problem has *two* characteristics through the
> point, or *none*:
>
> Shock Characteristics *collide* (light goes red: speed drops from 60
> to 0)
>
> Fan Characteristics *separate* (light goes green: speed up from 0 to
> 60)
>
> The problem is how to connect *u* = 60 to *u* = 0, when the
> characteristics don't give the answer. A shock will be sharp breaking
> (drivers only see the car ahead in this model). A fan will be gradual
> acceleration.
>
> TO DO\...
>
> Figure 5.13: A shock when characteristics collide, a fan when they
> separate.
>
> For the conservation law *u~t~* + *f* (*u*)*~x~* = 0, the
> characteristics are *x* − *f [!]{.smallcaps}*(*u*~0~)*t* = *x*~0~.
>
> That line has the right slope to carry the constant value *u* =
> *u*~0~:
>
> *d*
>
> *dt u*(*x*~0~
>
> \+ *St, t*) = *S �u* + *�u* = 0 when *S* = *f [!]{.smallcaps}*(*u*)
> *.* (7)
>
> *�x �t*
>
> The solution until trouble arrives is *u*(*x, t*) = *u*(*x* − *f
> [!]{.smallcaps}*(*u*)*t,* 0).

### Shocks {#shocks .unnumbered}

> After trouble arrives, it will be the *integral form* that guides the
> choice of the correct solution *u*. If there is a jump in *u* (*a
> shock* ), that integral from tells where the jump must occur. Suppose
> *u* has diﬀerent values *u~L~* and *u~R~* at points *x~L~* and *x~R~*
> on the left and right sides of the shock:
>
> Integral form
>
> *[d]{.underline} ^x^*R
>
> *dt*
>
> *u dx* + *f* (*u~R~*) − *f* (*u~L~*) = 0 *.* (8)

*x*~L~

> If the position of the shock is *x* = *X*(*t*), we take *x~L~* and
> *x~R~* very close to *X*. The values of *u*(*x, t*) inside the
> integral are close to the constants *u~L~* and *u~R~*:
>
> *[d]{.underline}*
>
> (*x* − *x* ) *u* + (*x* − *X*) *u* � + *f* (*u* ) − *f* (*u* ) � 0 *.*
>
> *This gives the speed s* = *dX/dt of the shock curve*:
>
> For the Riemann problem, the left and right values *u~L~* and *u~R~*
> will be constants *A* and *B*. The shock speed *s* is the ratio
> between the jump \[ *f* \] = *f* (*B*) *f* (*A*) and the jump \[ *u*
> \] = *B A*. Since this ration gives a constant slope, the shock line
> is straight. For other problems, the characteristics are carrying
> diﬀerent values of *u* into the shock. So the shock speed *s* is not
> constant and the shock lines is curved.
>
> The shock gives the solution when characteristics collide. With *f*
> (*u*) = ^[1]{.underline}^ *u*^2^ in
>
> Burger's equation, the shock speed is halfway between *u~L~* and
> *u~R~*:
>
> 1 *u*^2^ − *u*^2^ 1
>
> Burger's equation Shock speed *s* =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} *[^R^ ^L^]{.underline}* =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image17.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} (*u~R~* + *u~L~*) *.* (10)
>
> 2 *u~R~* − *u~L~* 2
>
> The Riemann problem has *u~L~* = *A* and *u~R~* = *B*, and *s* is
> their average. Figure 5.14 shows how the integral form of Burger's
> equation is solved by the right placement of the shock.

### Fans {#fans .unnumbered}

> You might expect a similar picture (just ﬂipped) when *A \< B*.
> *Wrong*. The integral form is still satisﬁed, but it is also satisﬁed
> by a fan. The choice between shock and fan is made by the "entropy
> condition" that as *t* increases, *characteristics must go into the
> shock*. The wave speed is faster than the shock speed on the left, and
> slower on the right:
>
> Since Burger's equation has *f [!]{.smallcaps}*(*u*) = *u*, it only
> has shocks when *u~L~* is larger than *u~R~*. In the Riemann problem
> that means *A \> B*. In the opposite case, the smaller value *u~L~* =
> *A* has to be connected to *u~R~* = *B* by the fan in Figure 5.14:
>
> *x*
>
> Fan (or rarefaction) *u* =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.333880139982502e-2in"
> height="6.666666666666667e-3in"} for *At \< x \< Bt.* (12)
>
> *t*
>
> use ﬁg 6.28 p. 592 of IAM (reverse left and right ﬁgs)
>
> Figure 5.14: Characteristics collide in a shock and separate in a fan.
>
> Notice especially that in the traﬃc ﬂow problem, the velocity *v*(*u*)
> *decreases* as the density *u* increases. A good model is linear
> between *v* = *v*max at zero density and *v* = 0 at maximum density.
> Then the ﬂux *f* (*u*) = *u v*(*u*) is a downward parabola (concave
> instead of Burger's convex *u*^2^*/*2):
>
> Traﬃc speed
>
> � *[u]{.underline}* � �
>
> *u*2 �
>
> Typical values for a single lane of traﬃc show a maximum ﬂux of *f* =
> 1600 vehicles per hour, when the density is *u* = 80 vehicles per
> mile. This maximum ﬂow rate
>
> is attained when the velocity *f/u* is *v* = 20 miles per hour! Small
> comfort at that speed, to know that other cars are getting somewhere
> too.
>
> Problems and compute the solution when a light goes red (shock
> trav-els backward) and when a light goes green (fan moves forward).
> Please look at the ﬁgures, to see how the vehicle trajectories are
> entirely diﬀerent form the characteris-tics.
>
> A driver keeps adjusting the density to stay safely behind the car in
> front. (Hitting the car would give *u \<* 0.) We all recognize the
> frustration of braking and accelerating from a series of shocks and
> fans. This traﬃc crawl happens when the green light is too short for
> the shock to make it through.

### A Solution Formula for Burger's Equation {#a-solution-formula-for-burgers-equation .unnumbered}

> Let me comment on three nonlinear equations. They are useful models,
> quite special because each one has an exact solution formula:
>
> The conservation law can develop shocks. This won't happen in the
> second equation because the *u~xx~* viscosity term prevents it. That
> term can stay small when the solution is smooth, but it dominates when
> a wave is about to break. The proﬁle is steep but it stays smooth.
>
> As starting function for the conservation law, I will pick a point
> source: *u*(*x,* 0) =
>
> *∂*(*x*). We can guess a solution with a shock, and check the jump
> condition and entropy condition. Then we ﬁnd an exact formula when *�
> u~xx~* is included, by a neat change of variables that produces *h~t~*
> = *� h~xx~*. When we let *�* 0, the limiting formula solves the
> conservation law---and we can check that the following solution is
> correct.
>
> Solution with *u*(*x,* 0) = *�*(*x*) When *u*(*x,* 0) jumps upward, we
> expect a fan. When it drops we expect a shock. The delta function is
> an extreme case (very big jumps up and down, very close together!). So
> we look for a shock curve *x* = *X*(*t*) immediately in front of a
> fan!
>
> The total mass at the start is *∂*(*x*) *dx* = 1. This never changes,
> and already that locates the shock position *X*(*t*):
>
> *^X^ [x]{.underline} X*^2^
>
> Mass at time *t* = *dt* = = 1 so *X*(*t*) =
>
> 2*t .* (15)
>
> ~0~ *t* 2*t*

Does the drop in *u*, from *X/t* = �2*t/t* to zero, satisfy the jump
condition?

> *dX* �2 Jump \[ *u*^2^*/*2 \] *X*^2^*/*2*t*^2^ �2*t*
>
> Shock speed *s* =

*dt*

> = 2�*t*
>
> equals
>
> =
>
> Jump \[ *u* \]
>
> = *.*
>
> *X/t* 2*t*
>
> The entropy condition *u~L~ \> s \> u~R~* = 0 is also satisﬁed, and
> the solution ( ) looks good. It *is* good, but because of the delta
> function we check it another way.
>
> Begin with *u~t~* + *u u~x~* = *� u~xx~*, and solve that equation
> exactly. If *u*(*x*) is *�U/�x*, then integrating our equation gives
> *U~t~* + ^[1]{.underline}^ *U* ^2^ = *� U~xx~*. The initial value
> *U*~0~(*x*) is now
>
> 2 *x*
>
> a step function. Then the great change of variables *U* = −2*�* log
> *h* produces the heat

−*U*~0~(*x*)*/*2*�*

> equation *h~t~* = *� h~xx~* (Problem ). The initial value becomes
> *h*(*x,* 0) = *e* .
>
> Section 5.4 found the solution to the heat equation *u~t~* = *u~xx~*
> from any starting function
>
> *h*(*x,* 0) and we just change *t* to *�t*:
>
> ⎨ 1 � � −*U*~0~(*y*)*/*2*�* −(*x*−*y*)^2^ */*4*�t* ⎩
>
> *U* (*x, t*) = −2*�* log *h*(*x, t*) = −2*�* log �4*��t* −� *e e*
>
> *dy .* (16)
>
> It doesn't look easy to let *�* 0, but it can be done. That
> exponential has the form *e*^−*B*(*x,y*)*/*2*�*^ . This is largest
> when *B* is smallest. An asymptotic method called "steepest descent"
> shows that as *�* 0, the bracketed quantity in (16) approaches
>
> −*B*−min*/*2*�*
>
> *c e*
>
> in the limit:

. Taking its logarithm and multiplying by −2*�*, (16) becomes *U* =
*B*min

> lim *U* (*x, t*) = *B* = min�*U* (*y*) + [1]{.underline} (*x* −
> *y*)^2^�*.* (17)
>
> This is the solution formula for *U~t~* + ^[1]{.underline}^ *U* ^2^ =
> 0. Its derivative *u* = *U~x~* solves the
>
> 2 *x*
>
> conservation law *u~t~* + *u u~x~* = 0. By including the viscosity *�
> u~xx~* with *�* 0, we are
>
> ﬁnding the *u*(*x, t*) that satisﬁes the jump condition and the
> entropy condition.
>
> Example Starting from *u*(*x,* 0) = *∂*(*x*), its integral *U*~0~ is a
> step function. The minimum of *B* is either at *y* = *x* or at *y* =
> 0. Check each case:
>
> *U* (*t, x*) = *B*min = *min~y~* ⎨
>
> 0 (*y* ≈ 0) (*x* − *y*) ⎩

2

> 0 for *x* ≈ 0
>
> = *x*^2^*/*2*t* for 0 ≈ *x* ≈
>
> �2*t*
>
> 1 (*y \>* 0) 2*t* �
>
> �⎧1 for *x* √ 2*t*
>
> The result *u* = *dU/dx* is 0 or *x/t* or 0. This
> ag�r[ee]{.underline}s with our guess in equation ( )---a
>
> fan rising from 0 and a shock back to 0 at *x* = 2*t*.

# Level Sets and the Fast Marching Method

> The level sets of *f* (*x, y*) are the sets on which the function is
> constant. For example *f* (*x, y*) = *x*^2^ + *y*^2^ is constant on
> circles around the origin. Geometrically, a level plane *z* = constant
> will cut through the surface *z* = *f* (*x, y*) on a level set. One
> attractive feature of working with level sets is that their topology
> can change (pieces of the level set can separate or come together)
> just by changing the constant.
>
> Starting from one level set, the signed distance function *d*(*x, y*)
> is especially important. It gives the *distance* to the level set, and
> also th[e sign:]{.underline} typically *d \>* 0 outside and *d \<* 0
> inside. For the unit circle, *d* = *r* − 1 = *x*2 + *y*2 − 1 will be
> the signed distance function. In the mesh generation algorithm of
> Section 2. , it was convenient to describe the region by its distance
> function *d*(*x, y*).
>
> A fundamental fact of calculus: The gradient of *f* (*x, y*) is
> perpendicular to its level sets. Reason: In the tangent direction *t*
> to the level set, *f* (*x, y*) is not changing and (grad *f* ) · *t*
> is zero. So grad *f* is in the normal direction. For the function
> *x*^2^ + *y*^2^, the gradient [(2*x,* 2*y*]{.underline}) points
> outward from the circular level sets. The gradient of *d*(*x, y*) =
> *x*2 + *y*2 − 1 points the same way, and it has a special property:
> The gradient of a distance function is a unit vector. It is the *unit*
> normal *n*(*x, y*) to the level sets. For the circles,
>
> grad(� 1) = ( *x,*
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image30.png){width="8.667104111986002e-2in"
> height="6.666666666666667e-3in"}) and \| grad \|^2^ = *x* + *y* = 1
> *.* (1)
>
> *r r r*2 *r*2
>
> You could think of the level set *d*(*x, y*) = 0 as a wall of ﬁre.
> This ﬁrefront will move normal to itself. If it has constant velocity
> 1 then at time *T* the ﬁre will reach all points on the level set
> *d*(*x, y*) = *T* .
>
> That "wall of ﬁre" example brings out an important point when the zero
> level set has a corner (it might be shaped like a V). The points at
> distance *d* outside that set (the ﬁrefront at time *d*) will lie on
> lines parallel to the sides of the V, and also on a circular arc of
> radius *d* around the corner. For *d \<* 0 the V moves *inward*. It
> remains a V (with no smoothing of the corner).
>
> The central problem of the level set method is to propagate a curve
> like the ﬁrefront. A velocity ﬁeld *v* = (*v*~1~*, v*~2~) gives the
> direction and speed of each point for the movement. At time *t* = 0,
> the curve is the level set where *d*(*x, y*) = 0. At later times the
> curve is the zero level set of a function *�*(*x, y, t*). The
> fundamental level set equation in its ﬁrst form is
>
> *d�*
>
> \+ *v* · grad *�* = 0*,* with *�* = *d*(*x, y*) at *t* = 0 *.* (2)
>
> *dt*
>
> In our wall of ﬁre example, *v* would be the unit vector in the normal
> direction to the ﬁrefront: *v* = *n* = grad *�/*\| grad *�*\|. In all
> cases it is only the normal component *F* = *v* · *n* that moves the
> curve! Tangential movement (like rotating a circle around its center)
> gives no change in the curve as a whole. By rewriting *v* · grad *�*,
> the level
>
> set equation takes a second form that is more useful in computation:
>
> grad *� d�*
>
> *v* · grad *�* = *v* · \| grad *�*\| = *F* \| grad *�*\| leads to +
> *F* \| grad *�*\| = 0 *.* (3)
>
> \| grad *�*\| *dt*
>
> We only need to know the velocity ﬁeld *v* (and only its normal
> component *F* ) near the *current location* of the level curve--not
> everywhere else. We are propagating a curve. The velocity ﬁeld may be
> ﬁxed (easiest case) or it may depend on the local shape of the curve
> (nonlinear case). An important example is motion by mean curvature:
> *F* = −*�*. The neat property \| grad *�*\| = 1 of distance functions
> simpliﬁes the formulas for the normal *n* and curvature *�*:
>
> When � is a *n* = grad *�* becomes *n* = grad *�*
>
> distance \| grad *�*\| (4)
>
> function *�* = div *n* becomes *�* = div(grad *�*) = Laplacian of *�*
>
> But here is an unfortunate point for *t \>* 0. Constant speed (*F*
> = 1) in the normal direction does maintain the property \| grad *�*\|
> = 1 of a distance function. Motion by mean curvature, and other
> motions, will destroy this property. To recover the simple formulas
> (4) for distance functions, the level set method often reinitializes
> the problem---restarting from the current time *t*~0~ and computing
> the distance function *d*(*x, y*) to the current level set *�*(*x, y,
> t*~0~) = 0. This reinitialization was the Fast Marching Method, which
> ﬁnds distances from nearby meshpoints to the current level set.
>
> We describe this quick method to compute distances to meshpoints, and
> then discuss the numerical solution of the level set equation (3) on
> the mesh.

### Fast Marching Method {#fast-marching-method .unnumbered}

> The problem is to march outward, computing distances from meshpoints
> to the in-terface (the current level set where *�* = 0). Imagine that
> we know these distances for the grid points adjacent to the interface.
> (We describe fast marching but not the full algorithm of
> reinitialization.) The key step is to compute the distance to the
> *next nearest meshpoint*. Then the front moves further outward with
> velocity *F* = 1. When the front crosses a new meshpoint, it will
> become the next nearest and its distance will be settled next.
>
> So we accept one meshpoint at a time. Distances to further meshpoints
> are tenta-tive (not accepted). They have to be recomputed using the
> newly accepted meshpoint and its distance. The Fast Marching Method
> must quickly take these steps recur-sively:

1.  Find the tentative meshpoint *p* with smallest distance (to be
    > accepted).

2.  Update the tentative distances to all meshpoints adjacent to *p*.

> To speed up step 1, we maintain a binary tree of unaccepted meshpoints
> and their tentative distances. The smallest distance is at the top of
> the tree, which identiﬁes
>
> *p*. When that value is removed from the tree, others move up to form
> the new tree.
>
> Recursively, each vacancy is ﬁlled by the smaller of the two distance
> values below it. Then step 2 updates those values at points adjacent
> to *p*. These updated values may have to move (a little) up or down to
> reset the tree. In general, the updated values should be smaller (they
> mostly move up, since they have the latest meshpoint *p* as a new
> candidate in ﬁnding the shortest route to the original interface).
>
> The Fast Marching Method ﬁnds distances to *N* meshpoints in time
> *O*(*N* log *N* ). The method applies when the front moves *in one
> direction only*. The underlying equation is *F* \|�*T* \| = 1 (Eikonal
> equation with *F \>* 0). The front never crosses a point twice (and
> the crossing time is *T* ). If the front is allowed to move in both
> directions, and *F* can change sign, we need the initial value
> formulation (3).

### Lagrangian versus Eulerian {#lagrangian-versus-eulerian .unnumbered}

> A fundamental choice in analyzing and computing ﬂuid ﬂow is between
> Lagrange and Euler. For the minimizing function in optimization, they
> arrived at the same "Euler-Lagrange equation". In studying ﬂuids, they
> chose *very diﬀerent* approaches:
>
> Lagrange follows the path of each particle of ﬂuid. He moves.
>
> Euler sees which particles pass through each point. He sits.
>
> Lagrange is more direct. He "*tracks*" the front. At time zero, points
> on the front have positions *x*(0). They move according to vector
> diﬀerential equations *dx/dt* = *V* (*x*). If we mark and follow a
> ﬁnite set of points, equally spaced at the start, serious diﬃculties
> can appear. Their spacing can get very tight or very wide (forcing us
> to remove or add marker points). The initial curve can split apart or
> cross itself (changes of topology). The level set method escapes from
> these diﬃculties by going Eulerian.
>
> For Euler, the *x*-*y* coordinate system is ﬁxed. He "*captures*" the
> front implicitly, as a level set of *�*(*x, y, t*). When the
> computational grid is also ﬁxed, we are con-stantly interpolating to
> locate level sets and compute distance functions. Squeezing or
> stretching or tangling of the front appear as changes in *�*, not as
> disasters for the mesh.
>
> The velocity *v on the interface* determines its movement. When the
> level set method needs *v* at a meshpoint oﬀ the interface, a good
> candidate is the value of *v* at the nearest point on the interface.

### Upwind Diﬀerencing {#upwind-diﬀerencing .unnumbered}

> The level set ﬁnite diﬀerence method is properly developed in the
> books by its origina-tors: Sethian \[ \] and Osher and Fedkiw \[ \].
> Here we concentrate on an essential point:
>
> *upwind diﬀerencing*. *Recall* from Section 1. the three simplest
> approximations
>
> F, B, Cto the ﬁrst derivative *d�/dx*--*Forward*, *Backward*,
> *Centered* :
>
> F *�*(*x* + *h*) − *�*(*x*) B *�*(*x*) − *�*(*x* − *h*) C *�*(*x* +
> *h*) − *�*(*x* − *h*)
>
> *h h* 2*h*
>
> Which do we use in the simple convection equation *d�/dt* + *a d�/dx*
> = 0? Its true solution is *�*(*x* − *at,* 0). *The choice of ﬁnite
> diﬀerences depends on the sign of a*. The ﬂow moves left to right for
> *a \<* 0. Then the *backward* diﬀerence is natural---the "upwind"
> value *�*(*x*−*h, t*) on the left should contribute to *�*(*x,
> t*+�*t*). The downwind value *�*(*x* + *h, t*) on the right moves
> further downwind during the time step, and has no inﬂuence at *x*.
>
> When the movement of the solution (and the wind) is right to left
> (with *a \>* 0), then the *forward* diﬀerence will use the appropriate
> upwind value *�*(*x* + *h, t*) along with *�*(*x, t*), in computing
> the new *�*(*x, t* + �*t*).
>
> Notice the time-step limitation \|*a*\|�*t* � *h*. In time �*t*, the
> "wind" will bring the true value of *�* from *x* + *a*�*t* to the
> point *x*. If *a \>* 0 and ﬁnite diﬀerences reach upwind to *x* + *h*,
> that must be far enough to include information at *x* + *a*�*t*. So
> the *Courant-Friedrichs-Lewy condition* is *a*�*t* � *h*. The
> numerical waves must propagate at least as fast as the physical waves
> (and in the right direction!). Downwind diﬀer-encing is looking for
> that information on the wrong side of the point *x*, and is doomed to
> failure. Centered diﬀerencing in space is unstable for ordinary
> forward Euler.
>
> By careful choice of the right ﬁnite diﬀerences, Osher has constructed
> higher-order essentially non-oscillatory (ENO) schemes. A central idea
> in nonlinear problems, where the diﬀerential equation has multiple
> solutions (see Section ), is to choose the "*viscosity solution*."
> This physically correct solution appears in the limit as an extra
> *�u~xx~* diﬀusion term goes to zero. With good diﬀerencing the
> viscosity solution is the one that appears as �*x* � 0.
>
> At this point, the level set method does not appear in large
> production codes. In research papers it has successfully solved a
> great variety of diﬃcult nonlinear problems.
>
> Chapter 6
>
> Solving Large Systems

# Elimination with Reordering

> Finite elements and ﬁnite diﬀerences produce large linear systems *KU*
> = *F* . *The matrix K is extremely sparse*. It has only a small number
> of nonzero entries in a typical row. In "physical space" those
> nonzeros are tightly clustered---they come from neighboring nodes and
> meshpoints. But we cannot number *N* ^2^ nodes in a plane in any way
> that keeps all neighbors close together ! So in 2-dimensional
> problems, and even more in 3-dimensional problems, we meet three
> questions right away:

1.  How best to number the nodes

2.  How to use the sparseness of *K* (when nonzeros might be widely
    separated)

3.  Whether to choose direct elimination or an iterative method.

> That last point separates this section on elimination (where node
> order is important) from later sections on iterative methods (where
> preconditioning is crucial).
>
> To ﬁx ideas, we will create the *n* equations *KU* = *F* from
> Laplace's diﬀerence equation in an interval, a square, and a cube.
> With *N* unknowns in each direction, *K* has order *n* = *N* or *N*
> ^2^ or *N* ^3^. There are 3 or 5 or 7 nonzeros in a typical row of the
> matrix. Second diﬀerences in 1D, 2D, and 3D are shown in Figure 6.1.
>
> Along an inside row of the matrix, the entries add to zero. In two
> dimensions this is 4 1 1 1 1 = 0. This "zero sum" remains true for
> ﬁnite elements (the element shapes decide the exact numbers). It
> reﬂects the fact that *u* = 1 solves Laplace's equation and *U* =
> ones(*n,* 1) has diﬀerences equal to zero. The constant vector solves
> *KU* = 0 *except near the boundaries*. When a neighbor is a boundary
> point, its known value moves onto the right side of *KU* = *F* . Then
> that row of *K* is
>
> *not zero sum*. Otherwise *K* would be singular, if *K* ← ones(*n,* 1)
> = zeros(*n,* 1).

Using block matrix notation, we can create the 2D matrix *K*2D from the
familiar

*N* by *N* second diﬀerence matrix *K*. We number the nodes of the
square a row at

> �c 2006 Gilbert Strang

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image31.png){width="0.1430139982502187in"
height="0.1430139982502187in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image32.png){width="0.10500984251968504in"
height="0.10500984251968504in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image32.png){width="0.10500984251968504in"
height="0.10500984251968504in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image32.png){width="0.10500984251968504in"
height="0.10500984251968504in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image33.png){width="0.10500984251968504in"
height="0.10500984251968504in"}−1

> Tridiagonal *K*
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image34.png){width="0.13302274715660542in"
> height="0.13302384076990376in"}4
>
> Block Tridiagonal *K*2D *K*3D
>
> −1 2 −1 −1 −1
>
> *N* by *N* −1
>
> 2D : *N* ^2^ by *N* ^2^
>
> 3D : *N* ^3^ by *N* ^3^
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image31.png){width="0.14301946631671042in"
> height="0.14301946631671042in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image35.png){width="0.1050142169728784in"
> height="0.1050142169728784in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image36.png){width="0.1050142169728784in"
> height="0.1050142169728784in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image32.png){width="0.1050142169728784in"
> height="0.1050142169728784in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image37.png){width="0.1050142169728784in"
> height="0.1050142169728784in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image38.png){width="0.1050142169728784in"
> height="0.1050142169728784in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image39.png){width="0.1050142169728784in"
> height="0.1050142169728784in"}Figure 6.1: 3*,* 5*,* 7-point diﬀerence
> molecules for −*u~xx~,* −*u~xx~* − *u~yy~ ,* −*u~xx~* − *u~yy~* −
> *u~zz~*.
>
> a time (this "natural numbering" is not necessarily best). Then the
> 1's for the neighbors above and below are *N* positions away from the
> main diagonal of *K*2D.
>
> The 2D matrix in Figure 6.2a is *block tridiagonal with tridiagonal
> blocks*:
>
> � 2 −1 ⎡ � *K* + 2*I* −*I* ⎡
>
> *K* = � −1
>
> 2 −1
>
> ⎢ *K*2D = � −*I*
>
> *K* + 2*I* −*I*
>
> ⎢ (1)
>
> � −1
>
> 2 ⎣ �
>
> −*I K* + 2*I* ⎣
>
> Size *N* Elimination in this order: Size *n* = *N* ^2^
>
> Time *N* Bandwidth *w* = *N,* Space *nw* = *N* ^3^*,* Time *nw*^2^ =
> *N* ^4^
>
> The matrix *K*2D has 4's down the main diagonal. Its bandwidth *w* =
> *N* is the distance from the diagonal to the nonzeros in −*I*. Many of
> the spaces in between are ﬁlled during elimination! Then the storage
> space required for the factors in *K*2D = *LU* is of order *nw* = *N*
> ^3^. The time is proportional to *nw*^2^ = *N* ^4^, when *n* rows each
> contain *w* nonzeros, and *w* nonzeros below the pivot require
> elimination.
>
> Again, the operation count grows as *nw*^2^. Each elimination step
> uses a row of length *w*. There can be *nw* nonzeros to eliminate
> below the diagonal. If some entries stay zero inside the band,
> elimination could be faster than *nw*^2^---and this is our goal.
>
> Those counts are not impossibly large in many practical 2D problems
> (and we show how they can be reduced). The horrifying *N* ^7^ count
> will come for elimination on *K*3D. Suppose the 3D cubic grid is
> numbered a plane at a time. In each plane we see a 2D square, and
> *K*3D has blocks of order *N* ^2^ from those squares. With each square
> numbered as above, the blocks come from *K*2D and *I* = *I*2D:
>
> � *K*2D + 2*I* −*I* ⎡ 3D Size *n* = *N* ^3^
>
> *K*3D = −*I*
>
> �
>
> *K*2D + 2*I I*
>
> · · ·
>
> −*I K*2D + 2*I*
>
> Bandwidth *w* = *N* ^2^ Elimination space *N* ^5^ Elimination time *N*
> ^7^
>
> The main diagonal of *K*3D contains 6's, and "inside rows" have six
> −1's. Next to a face or edge or corner of the cube, we lose one or two
> or three of those −1's.
>
> From any node to the node above it, we count *N* ^2^ nodes. The *I*
> blocks are far from the main diagonal and the bandwidth is *w* = *N*
> ^2^. Then *nw*^2^ = *N*^7^.
>
> Fill-in Let me focus attention immediately on the key problem, when we
> apply elimination to sparse matrices. *The zeros "inside the band" may
> ﬁll in with nonze-ros*. Those nonzeros enter the triangular factors of
> *K* = *LL*^T^ (Figure 6.2a). When multiples of one pivot row are
> subtracted from other rows, a nonzero in that pivot row will infect
> all the others.
>
> Sometimes a matrix has a full row, from an equation like *U~j~* = 1
> (see Figure 6.3).
>
> That full row better come last !
>
> A good way to visualize the nonzero structure (sparsity structure) of
> *K* is by a graph. The rows of *K* are nodes in the graphs. A nonzero
> entry *K~ij~* produces an edge between nodes *i* and *j*. *The graph
> of K*2D *is exactly the mesh of unknowns*! Filling in a nonzero adds a
> new edge (a diagonal in our square graph). Watch how ﬁll-in happens in
> elimination:
>
> Suppose *a~ij~* is eliminated. A multiple of row *j* later is
> subtracted from the row *i*.
>
> If *a~jk~* is nonzero in row *j*, then *a*new becomes ﬁlled in row
> *i*:
>
> Matrix *a~jj~ a~jk~ a~jj~ a~jk~* Graph *j*
>
> *k i k*
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image40.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image41.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image40.png){width="9.101159230096238e-2in"
> height="9.101159230096238e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image41.png){width="9.101159230096238e-2in"
> height="9.101159230096238e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.101268591426072e-2in"
> height="9.101159230096238e-2in"}nonzeros *a~ij~* 0 −� 0 *a*new edges
> −� *j* Fill-in
>
> Kronecker product One good way to create *K*2D from *K* and *I* (*N*
> by *N*) is the kron(*A, B*) command. This replaces each number *a~ij~*
> by the block *a~ij~ B*. To take second diﬀerences in all columns at
> the same time, and all rows, use kron twice:
>
> This sum agrees with (1). Then a 3D box needs *K*2D and *I*2D =
> kron(*I, I*) in each plane. This easily adjusts to allow rectangles,
> with *I*'s of diﬀerent sizes. For a cube, take second diﬀerences
> inside all planes with *K*2D, plus diﬀerences in the *z*-direction:
>
> *K*3D = kron(*K*2D*, I*) + kron(*I*2D*, K*) has size (*N* ^2^)(*N*) =
> *N* ^3^ *.* (3)
>
> Here *K* and *K*2D and *K*3D of size *N* and *N* ^2^ and *N*^3^ are
> serving as *models of the type of matrices that we meet*. But we have
> to say that there are special ways to work with these particular
> matrices. The *x, y, z* directions are separable. We can use FFT-type
> methods in each direction. See Section 6. on *Fast Poisson Solvers*.
>
> MATLAB should know that the matrices are sparse ! If we create *I* =
> speye(*N* ) and *K* comes from spdiags as in Section 1.1, the kron
> command will preserve the sparse treatment. Before we describe
> reordering by minimum degree, allow me to display spy(*K*2D) plus ﬁll,
> and the reordered spy(*P K*2D*P* ^T^). *The latter will have much less
> ﬁll-in*. Your eye may not see this so clearly, but the count is
> convincing !
>
> Figure 6.2: (a) *K*2D is ﬁlled in by elimination. (b) A good
> reordering of *K*2D.

### Minimum Degree Algorithm {#minimum-degree-algorithm .unnumbered}

> We now describe a useful way to reorder meshpoints and equations in
> *K*2D *U* = *F* . The ordering achieves *approximate minimum degree*
> at each step---the number of nonzeros below the pivot is almost
> minimized. This is essentially the algorithm used in MATLAB's command
> *U* = *K*\\*F* , when *K* has been deﬁned as a sparse matrix. We list
> some of the functions from the sparfun directory:
>
> speye (sparse identity *I*) nnz (number of nonzero entries) find (ﬁnd
> indices of nonzeros) spy (visualize sparsity pattern) colamd and
> symamd (approximate minimum degree permutation of *K*)
>
> You can test and use the minimum degree algorithms without a careful
> analysis. The approximations are faster than the exact minimum degree
> permutations colmmd and symmmd. The speed (in two dimensions) and the
> roundoﬀ errors are quite acceptable.
>
> In the Laplace examples, the minimum degree ordering of nodes is
> irregular com-pared to "a row at a time." The ﬁnal bandwidth is
> probably not decreased. But many nonzero entries are postponed as long
> as possible ! That is the key.
>
> The diﬀerence is shown in the arrow matrix of Figure 6.3. Its minimum
> degree ordering (one nonzero below each pivot) produces large
> bandwidth, but *no ﬁll-in*. Elimination will only change the last row
> and column. The triangular factors *L* and *U* have all the same zeros
> as *A*, keeping the arrow. The space for storage stays at 3*n*, and
> elimination needs only *n* divisions and multiplications and
> subtractions. When a sparse matrix has a full row, *put it last*.
>
> � ← Faster ← ⎡
>
> Bandwidth � ←
>
> ← Slower ⎡
>
> ← ←
>
> � ← ← ⎢
>
> 6 and 3
>
> diagonals ← ←
>
> � ⎢
>
> best ← ←
>
> � ⎢
>
> ← ← ← ← ← ← ←
>
> � ⎢
>
> when ← ←
>
> �� ⎢⎣
>
> Fill-in
>
> �� ← ← F F ⎣
>
> −� ← ← ← ← ← ← ←
>
> entries
>
> ← F F ←
>
> Figure 6.3: Minimum degree (arrow matrix) defeats minimum bandwidth.
>
> The second ordering reduces the bandwidth from 6 to 3. But when row 4
> is used as the pivot row, the entries indicated by F are *ﬁlled in*.
> That lower quarter of *A* becomes full, with *n*^2^*/*8 nonzeros in
> each factor *L* and *U* . You see that the whole nonzero "proﬁle" of
> the matrix decides the ﬁll-in, not just the bandwidth.
>
> Here is another example, from the red-black ordering of a square grid.
> Color the gridpoints like a checkerboard. Then all four neighbors or a
> red point are black, and vice versa. If we number the red points
> before the black points, the *permuted K*2D has diagonal blocks of
> 4*I*:
>
> This pushes the 1's and the ﬁll-in into the last *N* ^2^*/*2 rows.
> Notice how *P* permutes the rows (the equations) and *P* ^T^ permutes
> the columns (the unknowns). Together they keep 4's on the main
> diagonal.
>
> Now the real thing. Minimum degree algorithms choose the (*k* + 1)st
> pivot column, after the ﬁrst *k* columns have been eliminated as usual
> below the diagonal. The algorithms look at the nonzeros in the lower
> right matrix of size *n* − *k*.
>
> *Symmetric case*: Choose the remaining meshpoint with the fewest
> neighbors.
>
> *Unsymmetric case*: Choose the remaining column with the fewest
> nonzeros.
>
> The component of *U* corresponding to that column is renumbered
> *k* + 1. So is the meshpoint in the ﬁnite diﬀerence grid. Of course
> elimination in that column will normally produce new nonzeros in the
> remaining columns. Some ﬁll-in is unavoidable. The algorithm keeps
> track of the new positions of nonzeros, and also the actual entries.
> It is the *positions* that decide the *ordering* of unknowns (the
> permutation of columns). Then the *entries* in *K* decide the
> *numbers* in *L* and *U* .
>
> The degree of a node is the number of connections to other nodes. This
> is the number of oﬀ-diagonal nonzeros in that column of *K*. In Figure
> 6.4 the corner nodes 1*,* 3*,* 4*,* 6 all begin with degree 2. The
> side nodes 2 and 5 have degree 3. *The degrees change as elimination
> proceeds* ! Nodes connected to the pivot become connected to each
> other---and that entry of the matrix ﬁlls in.
>
> You will see how a renumbering of meshpoints preserves the symmetry of
> *K*. The rows and columns are reordered in the same way. Then *P
> K*old*P* ^T^ = *K*new = *K*nTew.
>
> Example 1 Figure 6.4 shows a small example of the minimal degree
> ordering, for Laplace's 5-point scheme. The problem starts with six
> meshpoints (they would be connected to boundary points where *U* is
> known) and a 6 by 6 matrix. *K* has two 3 by 3 tridiagonal blocks from
> horizontal links, and two 3 by 3 blocks with −*I* from vertical links.
>
> The ﬁrst elimination step chooses row 1 as pivot row, because node 1
> has minimum degree 2. (Any degree 2 node could come ﬁrst, leading to
> diﬀerent elimination orders.) The pivot is P, the other nonzeros in
> that row are boxed. When row 1 operates on rows 2
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image42.png){width="9.101268591426072e-2in"
> height="9.101268591426072e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.101159230096238e-2in"
> height="9.101159230096238e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image21.png){width="9.101268591426072e-2in"
> height="9.101268591426072e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.101268591426072e-2in"
> height="9.101159230096238e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.101596675415573e-2in"
> height="9.101596675415573e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image21.png){width="9.101596675415573e-2in"
> height="9.101596675415573e-2in"}1 2 3 2 3
>
> 4 5 6 4 5 6
>
> Pivot on row 1 (degree = 2) Then pivot on row 3
>
> Pivots P
>
> Fill-in F
>
> Pivot row produces 0's and F's
>
> Figure 6.4: Minimum degree nodes 1 and 3 give pivots P. New diagonal
> edges 2--4 and 2--6 in the graph match the ﬁrst four entries F that
> are ﬁlled in by elimination.
>
> and 4, it changes six entries below it (left ﬁgure). *The two ﬁll-in
> entries marked by* F *change to nonzeros*. This ﬁll-in of the (2*,* 4)
> and (4*,* 2) entries corresponds to the dashed line connecting nodes 2
> and 4 in the graph.
>
> Elimination continues on the 5 by 5 matrix (and the graph with 5
> nodes). Node 2 still has degree 3, so it is not eliminated next. If we
> break the tie by choosing node 3, elimination using the new pivot P
> will ﬁll in the (2*,* 6) and (6*,* 2) positions. *Node 2 becomes
> linked to node 6 because they were both linked to the eliminated node
> 3*.
>
> The problem is reduced to 4 by 4, for the unknown *U* 's at the
> remaining nodes 2, 4, 5, 6. Problem asks you to take the next
> step---choose a minimum degree node and reduce the system to 3 by 3.
> Figure 6.5 shows the start of a minimum degree ordering for a larger
> grid. Notice how ﬁll-in (16 edges, 32 F's) increases the degrees.
>
> 7
>
> 4 3 �−
>
> 25 meshpoints
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image44.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image44.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image43.png){width="6.970581802274715e-2in"
> height="6.970581802274715e-2in"}1--4: degree 2
>
> 5--8: degree 3
>
> 8 6 17 to go −� degrees 4 and 5
>
> 1 5 2 at this stage
>
> Figure 6.5: Nodes connected to an eliminated node become connected to
> each other.
>
> Storing the Nonzero Structure = Sparsity Pattern
>
> A large system *KU* = *F* needs a fast and economical storage of the
> node connections (the positions *i, j* of nonzeros in the matrix). The
> internal list of edges and nonzero positions will change as
> elimination proceeds. Normally we don't see that list.
>
> Here we create the list for *N* = 4 by \[*i, j, s*\] = find(*K*). This
> has nnz(*K*) = 10:
>
> *i* = 1 2 1 2 3 2 3 4 3 4 *j* = 1 1 2 2 2 3 3 3 4 4
>
> *s* = 2 −1 −1 2 −1 −1 2 −1 −1 2
>
> The 10 entries are in *s*, so the ﬁfth nonzero has *i* = 3, *j* = 2,
> and *s* = *K*~32~ = 1. The positions *i, j* of nonzeros in *K* are in
> lexicographical order.
>
> You can see that the list *j* of column indices should be compressed.
> All we need are *pointers* to indicate when a new column appears on
> the list. In reality *j* is replaced by this short list of pointers to
> the list, including a last pointer to position 11 that signals the
> stop:
>
> point = 1 3 5 8 11 can be updated by perm(point)
>
> when columns are reordered.
>
> The sparse backslash command *U* = *K F* uses an approximate minimum
> degree algorithm. First it checks the nonzero pattern to see if row
> and column permuta-tions *P*~1~ and *P*~2~ can produce a block
> triangular form. The reordered system is *P*~1~*KP* ^T^(*P*~2~*U* ) =
> *P*~1~*F* :

⎡

Block triangular matrix *P*~1~*KP* = � ⎢ *.*

> 2 � 0 ⎣
>
> The reordered unknown *P*~2~*U* and the right-hand side *P*~1~*F* are
> similarly partitioned into *m* blocks. *Block back-substitution*
> starts with the smaller problem *B~mm~U~m~* = *F~m~*. Working upwards,
> we only deal with the blocks *B~ii~* on the diagonal (the smaller the
> better). Surprisingly often, a block triangular form is available.
>
> To preserve symmetry we need *P*~1~ = *P*~2~. In the positive deﬁnite
> case, the Cholesky command chol is preferred to lu, since useless row
> exchanges can be safely omitted. If diag(*K*) is positive, there is a
> chance (not a certainty !) of positive deﬁniteness. Backslash will try
> chol until it is forced to accept row exchanges.
>
> It is understood that MATLAB is not tuned for high performance. Use it
> for tests and experiments and adjustments. Established codes often
> turn to C^++^.

### Graph Separators {#graph-separators .unnumbered}

> Here is another approach to ordering, diﬀerent from minimum degree.
> The whole graph or mesh is separated into disjoint pieces by a cut.
> This separator goes through
>
> a small number of nodes or meshpoints. *It is a good idea to number
> the nodes in the separator last*. Elimination is relatively fast for
> the disjoint pieces *P* and *Q*. It only slows down at the end, for
> the (smaller) separator *S*.
>
> The meshpoints in *P* have no direct connections to *Q* (both are
> connected to the separator *S*). Numbered in that order, the "block
> arrow" stiﬀness matrix has two blocks of zeros. Its *K* = *LU*
> factorization looks like this:
>
> � *K*~P~ 0 *K*~PS~
>
> ⎡ � *L*P
>
> ⎡ � *U*P 0 *A* ⎡
>
> *K* = 0 *K*~Q~ *K*~QS~ *L* = 0 *L*~Q~ *U* = *U*~Q~ *B* (5)
>
> *K*~SP~ *K*~SQ~ *K*~S~ *X Y Z C*
>
> The zero blocks in *K* give zero blocks in *L* and *U* . The submatrix
> *K*~P~ produces *L*~P~ and *U*~P~. Then come the factors *L*~Q~*U*~Q~
> of *K*~Q~, followed by the connections through the separator. The
> major cost is often that last step, the solution of a fairly dense
> system. When the separator *S* has size *N*, a dense system costs *N*
> ^3^.
>
> A separator illustrates the key idea of domain decomposition: *Cut the
> problem into smaller pieces*. This is natural for structural analysis
> of an airplane: Solve separately for the wings and the fuselage. The
> smaller system for the separator (where the pieces meet) is like the
> third row of equation (5). This expresses the requirement that the
> unknown and its normal derivative (stress or ﬂux) match along the
> separator. We apologize that a full discussion of domain decomposition
> is impossible (see \[--\]).
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image45.png){width="7.70067804024497e-2in"
> height="7.70067804024497e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image46.png){width="7.70067804024497e-2in"
> height="7.70067804024497e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image47.png){width="0.11901137357830271in"
> height="0.11901137357830271in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image48.png){width="0.11901137357830271in"
> height="0.11901137357830271in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image45.png){width="7.70067804024497e-2in"
> height="7.70067804024497e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image46.png){width="7.70067804024497e-2in"
> height="7.70067804024497e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image49.png){width="0.11901574803149606in"
> height="0.11901574803149606in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image50.png){width="7.70100612423447e-2in"
> height="7.70100612423447e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image51.png){width="7.70100612423447e-2in"
> height="7.70100612423447e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image51.png){width="7.70100612423447e-2in"
> height="7.70100612423447e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image46.png){width="7.70100612423447e-2in"
> height="7.70100612423447e-2in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image45.png){width="7.70100612423447e-2in"
> height="7.70100612423447e-2in"}1 4 1 5 3
>
> *P Q*
>
> 3 5 2 6 4 *P S Q*

+-------------------+--------------------------------+-----------------+
| Arrow matrix      | > Separator comes last         | Blocks *P, Q*   |
+===================+================================+=================+
| (Figure 6.3)      | (Figure 6.4)                   | Separator *S*   |
+-------------------+--------------------------------+-----------------+

> Figure 6.6: A graph separator numbered last produces a block arrow
> matrix *K*.
>
> Figure 6.6 shows three examples, each with separators. The graph for a
> perfect arrow matrix has a one-point separator (very unusual). The
> 6-node rectangle has a two-node separator in the middle. Every *N* by
> *N* grid can be cut by an *N*-point separator (and *N* is much smaller
> than *N* ^2^).
>
> On a rectangular grid, the best cut is down the middle in the shorter
> direction. Our model problem on a square is actually the hardest ! A
> region shaped like a U (or maybe a radiator in 3D) might look diﬃcult.
> But actually it allows very short separators and fast elimination. A
> tree needs *no* ﬁll-in (Problem ).

### Nested Dissection {#nested-dissection .unnumbered}

> You could say that the numbering of *P* then *Q* then *S* is block
> minimum degree. But one cut with one separator will not come close to
> an optimal numbering. It is natural to extend the idea to a nested
> sequence of cuts. *P* and *Q* have their own separators at the next
> level. This nested dissection continues until it is not productive to
> cut further. It is a strategy of "divide and conquer."
>
> Figure 6.7 illustrates three levels of nested dissection on a 7 by 7
> grid. The ﬁrst separator is down the middle. Then two cuts go across
> and four cuts go down. Numbering the separators last within each
> stage, the matrix *K* of size 49 has arrows inside arrows inside
> arrows. The spy command will display the pattern of nonzeros.
>
> 1 7 43 28

+----------------------+-------+--------------------------+----------+
| > 1 to 9             |       | 22 to 30                 |          |
+======================+=======+==========================+==========+
| > 19 to 21           |       | 40 to 42                 | > *K* =  |
+----------------------+-------+--------------------------+----------+
| > 10 to 18           |       | 31 to 39                 |          |
+----------------------+-------+--------------------------+----------+
| 18                   | > 49  | > 39                     |          |
+----------------------+-------+--------------------------+----------+

> Figure 6.7: Three levels of separators. Still nonzeros in *K*, only in
> *L*.
>
> Separators and nested dissection show how numbering strategies are
> based on the graph of nodes. Edges between nodes correspond to
> nonzeros in the matrix *K*. The ﬁll-in created by elimination (entries
> F in *L* and *U* ) corresponds to adjacent edges in the graph. In
> practice, there has to be a balance between simplicity and optimality
> in the numbering---in scientiﬁc computing simplicity is a very good
> thing!
>
> Here are the complexity estimates for the Laplacian with *N* ^2^ or
> *N* ^3^ nodes:

+-------------------------------+-----------+--------+----------+-----+
| > Nested Separators           | > *n* =   | in 2D  | > *n* =  | >   |
|                               | > *N* ^2^ |        | > *N*    |  in |
|                               |           |        | > ^3^    | >   |
|                               |           |        |          |  3D |
+===============================+===========+========+==========+=====+
| > Space (nonzeros from        | > *N* ^2^ |        | > *N* 4  |     |
| > ﬁll-in)                     | > log *N* |        |          |     |
+-------------------------------+-----------+--------+----------+-----+
| > Time (ﬂops for elimination) | *N* 3     |        | > *N* 6  |     |
+-------------------------------+-----------+--------+----------+-----+

> In the last century, nested dissection lost out (too slow) on almost
> all applications. Now larger problems are appearing and the
> asymptotics eventually give nested dis-section an edge. All planar
> graphs have separators of size *n* into nearly equal pieces (*P* and
> *Q* have sizes at most 2*n/*3). Of course a new idea for ordering
> could still win. We don't recommend the older algorithm of (reverse)
> Cuthill-McKee.
>
> A reasonable compromise is the backslash command *U* = *K*\\*F* that
> uses a nearly minimum degree ordering in Sparse MATLAB.
>
> The text \[GL\] by George and Liu is the classic reference for this
> section on ordering of the nodes. The new book \[ ,2007\] by Davis has
> a superb description of his recent algorithms and how they are
> implemented (in MATLAB's backslash and in UMFPACK for sparse
> unsymmetric systems).

### Problem Set 6.1 {#problem-set-6.1 .unnumbered}

1.  Create *K*2D for a 4 by 4 square grid with *N* ^2^ = 3^2^ interior
    mesh points (so *n* = 9). Print out its factors *K* = *LU* (or its
    Cholesky factor *C* = chol(*K*) for the symmetrized form *K* =
    *C*^T^*C*). How many zeros in these triangular factors? Also print
    out inv(*K*) to see that it is full.

2.  As *N* increases, what parts of the *LU* factors of *K*2D are ﬁlled
    in ?

3.  Can you answer the same question for *K*3D? In each case we really
    want an estimate *cN ^p^* of the number of nonzeros (the most
    important number is *p*).

4.  Use the tic; \...; toc clocking command or the cpu command to
    compare the solution time for *K*2D*x* = random *f* in ordinary
    MATLAB and sparse MATLAB (where *K*2D is deﬁned as a sparse matrix).
    Above what value of *N* does the sparse routine *K*\\*f* win ?

5.  Compare ordinary vs. sparse solution times in the three-dimensional
    *K*3D*x* = random *f* . At which *N* does the sparse *K*\\*f* begin
    to win ?

6.  Incomplete *LU*

7.  Draw the next step after Figure 6.4 when the matrix has become 4 by
    4 and the graph has nodes 2--4--5--6. Which have minimum degree? Is
    there more ﬁll-in?

8.  Redraw the right side of Figure 6.4 if row number 2 is chosen as the
    second pivot row. Node 2 does not have minimum degree. Indicate new
    edges in the 5-node graph and new nonzeros F in the matrix.

9.  Order a tree to avoid all ﬁll-in.

10. Block triangular.

11. Suppose the unknowns *U~ij~* on a square grid are stored in an *N*
    by *N* matrix, and not listed in a vector *U* of length *N* ^2^.
    Show that the vector result of (*K*2D)*U* is now produced by the
    matrix *KU* + *UK*.

12. Elimination in minimum degree order is started for the square mesh
    in Fig-ure 6.5. How large do the degrees become as elimination
    continues? (You could try a large graph, giving systematics
    instructions for ties in the minimum degree.)

13. Experiment with the red-black permutation in equation ( ), to see
    how much ﬁll-in is produced by elimination. Is the red-black
    ordering superior to the original row-by-row ordering?

> *6.2. ITERATIVE METHODS* �c 2006 Gilbert Strang

# Iterative Methods

> New solution methods are needed when a problem *Ax* = *b* is too large
> and expensive for ordinary elimination. We are thinking of *sparse
> matrices A*, so that multiplications *Ax* are relatively cheap. If *A*
> has at most *p* nonzeros in every row, then *Ax needs at most pn
> multiplications*. Typical applications are to large ﬁnite diﬀerence or
> ﬁnite element equations, where we often write *A* = *K*.
>
> We are turning from elimination to look at iterative methods. There
> are really two big decisions, the preconditioner *P* and the choice of
> the method itself:

1.  A good preconditioner *P* is close to *A* but much simpler to work
    with.

2.  Options include *pure iterations* (6.2), *multigrid* (6.3), and
    *Krylov methods* (6.4), including the conjugate gradient method.

> Pure iterations compute each new *x~k~*~+1~ from *x~k~* − *P*
> ^−1^(*Ax~k~* − *b*). This is called "*stationary* " because every step
> is the same. Convergence to *x*~�~ = *A*^−1^*b*, studied below, will
> be fast when all eigenvalues of *M* = *I* − *P* ^−1^*A* are small. It
> is easy to suggest a preconditioner, but not so easy to suggest an
> excellent *P* (*Incomplete LU is a success*). The older iterations of
> Jacobi and Gauss-Seidel are less favored (but
>
> they are still important, you will see good points and bad points).
>
> Multigrid begins with Jacobi or Gauss-Seidel iterations, for the one
> job that they do well. They remove high frequency components (rapidly
> oscillating parts) to leave a smooth error. Then the central idea is
> to *move to a coarser grid* ---where the rest of the error can be
> destroyed. Multigrid is often dramatically successful.
>
> Krylov spaces contain all combinations of *b, Ab, A*^2^*b, . . .* and
> Krylov methods look for the best combination. Combined with
> preconditioning, the result is terriﬁc. When the growing subspaces
> reach the whole space R*^n^*, those methods give the exact solution
> *A*^−1^*b*. But in reality we stop much earlier, long before *n* steps
> are complete. The *conjugate gradient method* (*for positive deﬁnite
> A, and with a good preconditioner* ) has become truly important.
>
> The goal of numerical linear algebra is clear: Find a fast stable
> algorithm that uses the special properties of the matrix. We meet
> matrices that are symmetric or triangular or orthogonal or tridiagonal
> or Hessenberg or Givens or Householder. Those are at the core of
> matrix computations. The algorithm doesn't need details of the entries
> (which come from the speciﬁc application). By concentrating on the
> matrix structure, numerical linear algebra oﬀers major help.
>
> Overall, elimination with good numbering is the ﬁrst choice ! But
> storage and CPU time can become excessive, especially in three
> dimensions. At that point we turn from elimination to iterative
> methods, which require more expertise than *K*\\*F* . The next pages
> aim to help the reader at this frontier of scientiﬁc computing.

### Stationary Iterations {#stationary-iterations .unnumbered}

> We begin with old-style pure stationary iteration. The letter *K* will
> be reserved for "Krylov" so we leave behind the notation *KU* = *F* .
> The linear system becomes *Ax* =
>
> *b*. The large sparse matrix *A* is not necessarily symmetric or
> positive deﬁnite: Linear system *Ax* = *b* Residual *r~k~* = *b* −
> *Ax~k~* Preconditioner *P* � *A* The preconditioner *P* attempts to be
> close to *A* and still allow fast iterations. The
>
> Jacobi choice *P* = diagonal of *A* is one extreme (fast but not very
> close). The other
>
> extreme is *P* = *A* (too close). Splitting the matrix *A* gives a new
> form of *Ax* = *b*: Splitting *Px* = (*P* − *A*)*x* + *b .* (1) This
> form suggests an iteration, in which every vector *x~k~* leads to the
> next *x~k~*~+1~: Iteration *Px*~k+1~ = (*P* − *A*)*x*~k~ + *b .* (2)
>
> Starting from any *x*~0~, the ﬁrst step ﬁnds *x*~1~ from *P x*~1~ =
> (*P* − *A*)*x*~0~ + *b*. The iteration continues to *x*~2~ with the
> same matrix *P* , so it often helps to know its triangular factors
>
> in *P* = *LU* . Sometimes *P* itself is triangular, or *L* and *U* are
> approximations to the triangular factors of *A*. Two conditions on *P*
> make the iteration successful:

1.  The new *x~k~*~+1~ must be quickly computable. Equation (2) must be
    fast to solve.

2.  The errors *e~k~* = *x* − *x~k~* should approach zero as rapidly as
    possible.

> Subtract equation (2) from (1) to ﬁnd the error equation. It connects
> *e~k~* to *e~k~*~+1~: Error *P e~k~*~+1~ = (*P* − *A*)*e~k~* which
> means *e*~k+1~ = (*I* − *P* ^−1^*A*)*e*~k~ = *Me*~k~ *.* (3) The right
> side *b* disappears in this error equation. Each step multiplies the
> error
>
> vector *e~k~* by *M* . The speed of convergence of *x~k~* to *x* (and
> of *e~k~* to zero) depends
>
> entirely on *M* . *The test for convergence is given by the
> eigenvalues of M* :
>
> The largest eigenvalue (in absolute value) is the spectral radius
> *λ*(*M* ) = max \|*�*(*M* )\|. Convergence requires *λ*(*M* ) *\<* 1.
> The convergence rate is set by the largest eigen-value. For a large
> problem, we are happy with *λ*(*M* ) = *.*9 and even *λ*(*M* ) =
> *.*99.

When the initial error *e*~0~ happens to be an eigenvector of *M* , the
next error is

*e*~1~ = *Me*~0~ = *�e*~0~. At every step the error is multiplied by
*�*. *So we must have*

> \|*�*\| *\<* 1. Normally *e*~0~ is a combination of all the
> eigenvectors. When the iteration multiplies by *M* , each eigenvector
> is multiplied by its own eigenvalue. After *k* steps those multipliers
> are *�^k^*, and the largest is (*λ*(*M* ))*^k^* .
>
> If we don't use a preconditioner then *M* = *I* − *A*. All the
> eigenvalues of *A* must be inside a unit circle centered at 1, for
> convergence. Our second diﬀerence matrices *A* = *K* would fail this
> test (*I* − *K* is too large). The ﬁrst job of a preconditioner is to
> get the matrix decently scaled. Jacobi will now give *λ*(*I* −
> ^[1]{.underline}^ *K*) *\<* 1, and a really
>
> good *P* will do more.

+----------------------------------------+-----------------------------+
| > *6.2. ITERATIVE METHODS*             | �c 2006 Gilbert Strang      |
+========================================+=============================+
|                                        | Jacobi Iterations           |
+----------------------------------------+-----------------------------+
| > For preconditioner we ﬁrst propose a |                             |
| > simple choice:                       |                             |
+----------------------------------------+-----------------------------+

> Typical examples have spectral radius *λ*(*M*) = 1 − *cN* ^−2^, where
> *N* counts meshpoints in the longest direction. This comes closer and
> closer to 1 (too close) as the mesh is reﬁned and *N* increases. But
> Jacobi is important, it does part of the job.
>
> For our tridiagonal matrices *K*, Jacobi's preconditioner is just *P*
> = 2*I* (the diago-nal of *K*). The Jacobi iteration matrix becomes *M*
> = *I* − *D*^−1^*A* = *I* − ^[1]{.underline}^*K*:
>
> Iteration matrix

1

> *M* = *I* − *K*
>
> �0 1
>
> = �
>
> ⎡
>
> ⎢ *.* (4)

for a Jacobi step 2 2 1 0 1

1 0

> Here is *x*new from *x*old, in detail. You see how Jacobi shifts the
> oﬀ-diagonal entries of *A* to the right-hand side, and divides by the
> diagonal part *D* = 2*I*:
>
> 2*x*~1~ − *x*~2~ = *b*~1~
>
> �*x*1 ⎡new �
>
> *x*2 ⎡old �*b*1 ⎡
>
> −*x*~1~ + 2*x*~2~ − *x*~3~ = *b*~2~
>
> becomes � ⎢
>
> 1 *x*~1~ + *x*~3~ 1 *b*~2~
>
> =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image17.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} +
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} *.* (5)
>
> −*x*~2~ + 2*x*~3~ − *x*~4~ = *b*~3~ *x*~3~ 2 *x*~2~ + *x*~4~ 2 *b*~3~
>
> −*x*~3~ + 2*x*~4~ = *b*~4~ *x*~4~ *x*~3~ *b*~4~
>
> The equation is solved when *x*new = *x*old, but this only happens in
> the limit. The real question is the number of iterations to get close
> to convergence, and that depends on the eigenvalues of *M*. How close
> is *�*max to 1 ?
>
> *Those eigenvalues are simple cosines*. In Section 1.5 we actually
> computed all
>
> the eigenvalues *�*(*K*) = 2 − 2 cos( *[^j�^]{.underline}* ). Since
> *M* = *I* − ^[1]{.underline}^ *K*, we now divide those
>
> *N* +1 2
>
> eigenvalues by 2 and subtract from 1. The eigenvalues cos *jω* of *M*
> are less than 1 !
>
> 2 − 2 cos *jω �*
>
> Jacobi eigenvalues *�~j~*(*M*) = 1 − 2
>
> = cos *jω* with *ω* = *.* (6)
>
> *N* +1
>
> Convergence is safe (but slow) because \| cos *ω*\| *\<* 1. Small
> angles have cos *ω* � 1 − ^[1]{.underline}^ *ω*^2^.
>
> The choice *j* = 1 gives us the ﬁrst (and largest) eigenvalue of *M*:

[1]{.underline} *[�]{.underline}* ^2^

> Spectral radius *�*max(*M*) = cos *ω* � 1 − 2 *N* +1

*.* (7)

> *Convergence is slow for the lowest frequency.* The matrix *M* in (4)
> has the
>
> four eigenvalues cos *^[�]{.underline}^ ,* cos ^[2*�*]{.underline}^
> *,* cos ^[3*�*]{.underline}^ , and cos ^[4*�*]{.underline}^ (which is
> − cos *^[�]{.underline}^* ) in Figure 6.8.
>
> 5 5 5 5 5
>
> There is an important point about those Jacobi eigenvalues *�~j~*(*M*)
> = cos *jω*. The magnitude \|*�~j~*\| at *j* = *N* is the same as the
> magnitude at *j* = 1. This is not good for multigrid, where high
> frequencies need to be strongly damped. So weighted Jacobi has a
> valuable place, with a weighting factor *�* in *M* = *I* −
> *�D*^−1^*A*:

1

*�*

> *�*max = cos 5
>
> Jacobi

2

Jacobi weighted by *�* =

3

High frequency smoothing 1

3

> *�* 2*� �* 3*�* 4*� � ω*
>
> 5 5 2 5 5 − 1

3

> *�*min = cos

−1

> 4*�*
>
> 5 = −*�*max
>
> Figure 6.8: The eigenvalues of Jacobi's *M* = *I* −
> ^[1]{.underline}^*K* are cos *jω*, starting near *�* = 1 and ending
> near *�* = −1. Weighted Jacobi has *�* = 1 − *�* + *�* cos *jω*,
> ending near
>
> *�* = 1 − 2*�*. Both graphs show *j* = 1*,* 2*,* 3*,* 4 and *ω* =
> *[^�^]{.underline}* = *^[�]{.underline}^* (with *�* =
> ^[2]{.underline}^ ).
>
> *N*+1 5 3
>
> *Jacobi's iteration matrix M* = *I* −*D*^−1^*A changes to M* = *I*
> −*�D*^−1^*A.*
>
> The preconditioner is now *P* = *D/�*. Here are the eigenvalues
> *�*(*M*) when *A* = *K*:
>
> *�*
>
> Weighted *D* = 2*I* and *M* = *I* − 2 *A* and *� \<* 1
>
> Jacobi *�* (*M*) = 1 − *�* (2 − 2 cos *jω*) = 1 − *�* + *�* cos *jω.*
>
> \(8\)
>
> *j* 2
>
> The dashed-line graph in Figure 6.8 shows these values *�~j~*(*M*) for
> *�* = ^[2]{.underline}^ . This *�* is
>
> optimal in damping the high frequencies (*jω* between *�/*2 and *�*)
> by at least ^[1]{.underline}^
>
> *� �* 2 1

At *jω* =
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image52.png){width="9.833880139982502e-2in"
height="6.666666666666667e-3in"} *�*(*M*) = 1 − *�* + *�* cos
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image52.png){width="9.833880139982502e-2in"
height="6.666666666666667e-3in"} = 1 −
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image16.png){width="8.167104111986001e-2in"
height="6.666666666666667e-3in"} =
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image53.png){width="9.500546806649168e-2in"
height="6.666666666666667e-3in"}

2 2 3 3

1

At *jω* = *� �*(*M*) = 1 − *�* + *�* cos *�* = 1 −
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
height="6.666666666666667e-3in"} = −
![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.500546806649168e-2in"
height="6.666666666666667e-3in"}

3 3

> If we move away from *�* = ^[2]{.underline}^ , one of those
> eigenvalues will increase in magnitude. A weighted Jacobi iteration
> will be a good smoother within multigrid.
>
> In two dimensions the picture is essentially the same. The *N* ^2^
> eigenvalues of *K*2D are the sums *�*~j~ + *�*~k~ of the *N*
> eigenvalues of *K*. All eigenvectors are samples of sin *j�x* sin
> *k�y*. (In general, the eigenvalues of kron(*A, B*) are
> *�~j~*(*A*)*�~k~*(*B*). For kron(*K, I*) + kron(*I, K*), sharing
> eigenvectors means we can add eigenvalues.)
>
> Jacobi has *P* = 4*I*, from the diagonal of *K*2D. So *M* 2D = *I*2D −
> ^[1]{.underline}^*K*2D:
>
> 1 1 1
>
> *�~jk~*(*M* 2D) = 1 − 4 \[*�~j~*(*K*) + *�~k~*(*K*)\] = 2 cos *jω* + 2
> cos *kω .* (9)
>
> With *j* = *k* = 1, the spectral radius *�*~max~(*M*) = cos *ω* is the
> same 1 − *cN* ^−2^ as in 1D.

### Numerical Experiments {#numerical-experiments .unnumbered}

> The multigrid method grew out of the slow convergence of Jacobi
> iterations. You have to see how typical error vectors *e~k~* begin to
> decrease and then stall. For weighted Jacobi, the high frequencies
> disappear long before the low frequencies. Figure 6. shows a drop
> between *e*~0~ and *e*~−−~, and then very slow decay toward *e*~�~ =
> 0. We have chosen the second diﬀerence matrix *A* = *K*~500~ and
> started the iterations with the right-hand side *x*~0~ = *b* =
> rand(500*,* 1).
>
> This unacceptably slow convergence is hidden if we only look at the
> residual *r~k~* = *b* − *Ax~k~*. Instead of measuring the error *x* −
> *x~k~* in the solution, *r~k~* measures the error in the equation.
> That residual error *does* fall quickly. The key that led to multigrid
> is the rapid drop in *r* with such a slow drop in *e*.
>
> Figure 6.9: The residual *b* − *Ax* falls quickly but the solution
> error gets stalled.

### Gauss-Seidel and the Red-Black Ordering {#gauss-seidel-and-the-red-black-ordering .unnumbered}

> The Gauss-Seidel idea is to use the components of *x*new as soon as
> they are computed. This cuts the storage requirement in half, since
> *x*old is overwritten by *x*new. The preconditioner *P* = *D* + *L*
> becomes *triangular* instead of diagonal (still easy to use):
>
> Gauss-Seidel gives faster error reduction than ordinary Jacobi,
> because the Jacobi eigenvalues cos *jω* become (cos *jω*)^2^. The
> spectral radius is squared, so one Gauss-Seidel step is worth two
> Jacobi steps. The (large) number of iterations is cut in half,
>
> when the −1's below the diagonal stay with the 2's on the *left side*
> of *Px*new:
>
> � 0 ⎡new �*x*1 ⎡new �*x*2 ⎡old �*b*1 ⎡
>
> Gauss-Seidel
>
> new − *x*1 *x*2 *x*3 *b*2
>
> (*P* −*A*)*x*old + *b* � *x*2 ⎣ �*x*3 ⎣ � *x*4 ⎣ � *b*3 ⎣
>
> A new *x*~1~ comes from the ﬁrst equation, because *P* is triangular.
> Using *x*new in the second equation gives *x*new, which enters the
> third equation. Problem 1 shows that
>
> *x*new = (cos *jω*)^2^*x*old, with the correct eigenvector *x*old. All
> the Jacobi eigenvalues cos *jω* are squared for Gauss-Seidel, so they
> become smaller.
>
> Symmetric Gauss-Seidel comes from a double sweep, reversing the order
> of components to make the combined process symmetric. By itself, *I* −
> *P* ^−1^*A* is not symmetric for triangular *P* .
>
> A red-black ordering produces a neat compromise between Jacobi and
> Gauss-Seidel. Imagine that a two-dimensional grid is a *checkerboard*.
> Number the red nodes before the black nodes. The numbering will not
> change Jacobi's method (which keeps
>
> all of *x*old to create *x*new). But Gauss-Seidel will be improved. In
> one dimension,
>
> Gauss-Seidel updates all the even (red) components *x*~2*j*~ using
> known black values. Then it updates the odd (black) components
> *x*~2*j*+1~ using the new red values:
>
> *x* �− [1]{.underline} ⎤*x* + *x* + *b* ⎥ and then *x* �−
> [1]{.underline} ⎤*x* + *x* + *b* ⎥ *.* (11)
>
> In two dimensions, *x~i,j~* is red when *i* + *j* is even, and black
> when *i* + *j* is odd. Laplace's ﬁve-point diﬀerence matrix uses four
> black values to update each center value (red). Then red values update
> black, giving one example of *block Gauss-Seidel*.
>
> For line Gauss-Seidel, each row of grid values forms a block. The
> preconditioner
>
> *P* is *block triangular*. That is the right way to see *P* in 2D:

� 4*I* 0 �

> � *K*+2*I* 0 0 ⎡
>
> *P*red−black =
>
> −1's 4*I*
>
> and *P*line G−S = −*I K*+2*I* 0
>
> 0 −*I K*+2*I*
>
> A great feature is the option to compute all red values *in parallel*.
> They need only black values and can be updated in any order---there
> are no connections among red values (or within black values in the
> second half-step). For line Jacobi, the rows in 2D can be updated in
> parallel (and the plane blocks in 3D). Block matrix computations are
> eﬃcient.
>
> Overrelaxation (SOR) is a combination of Jacobi and Gauss-Seidel,
> using a factor *�* that almost reaches 2. The preconditioner is *P* =
> *D* +*�L*. (By *overcorrecting* from *x~k~* to *x~k~*~+1~, hand
> calculators noticed that they could ﬁnish in a few weeks.) My earlier
> book and many other references show how *�* is chosen to minimize the
> spectral
>
> radius *λ*(*M* ), improving *λ* = 1 − *cN* ^−2^ to *λ*(*M* ) = 1 −
> *cN* ^−1^. Then convergence is much faster (*N* steps instead of *N*
> ^2^, to reduce the error by a constant factor like *e*).

### Incomplete LU {#incomplete-lu .unnumbered}

> A diﬀerent approach has given much more ﬂexibility in constructing a
> good *P* . The idea is to compute an *incomplete LU factorization* of
> the true matrix *A*:
>
> The exact *A* = *LU* has ﬁll-in. So does Cholesky's *A* = *R*^T^*R*.
> Zero entries in *A* become nonzero in *L* and *U* and *R*. But *P* =
> *L*approx*U*approx can keep only the ﬁll-in entries F above a ﬁxed
> tolerance. The MATLAB commands for incomplete *LU* are
>
> \[ *L, U,* Perm \] = luinc(*A,* tol) or *R* = cholinc(*A,* tol) *.*
>
> If you set tol = 0, those letters inc have no eﬀect. This becomes
> ordinary sparse
>
> *LU* (and Cholesky for positive deﬁnite *A*). A large value of tol
> will remove all ﬁll-in.
>
> Diﬀerence matrices like *K*2D can maintain zero row sums by adding
> entries below tol to the main diagonal (instead of destroying those
> entries completely). This modiﬁed *ILU* is a success (mluinc and
> mcholinc). The variety of options, and especially the fact that the
> computer can decide automatically how much ﬁll-in to keep, has made
> incomplete *LU* a very popular starting point.
>
> In the end, *Px~k~*~+1~ = (*P* −*A*)*x~k~* +*b* is too simple ! Often
> the smooth (low frequency) errors decrease too slowly. *Multigrid will
> ﬁx this*. And pure iteration is choosing one particular vector in a
> "Krylov subspace." With relatively little work we can make a
>
> much better choice of *x~k~*. Multigrid methods and Krylov projections
> are the state of the art in today's iterative methods.

### Problem Set 6.2 {#problem-set-6.2 .unnumbered}

> 1 If *x*old = (cos *[^k�^]{.underline}* sin *[^k�^]{.underline} ,*
> cos^2^ *[^k�^]{.underline}* sin [^2*k�*^]{.underline} *, . . . ,*
> cos*^N^* *[^k�^]{.underline}* sin *^[Nk�]{.underline}^* ) show that

*N* +1

> *N* +1
>
> *N* +1
>
> *N* +1

*N* +1

> *N* +1
>
> the Gauss-Seidel iteration (10) is satisﬁed with *x*new = cos^2^
> *[^k�^]{.underline} x*old. This
>
> shows that *M* for Gauss-Seidel has *�* = cos^2^ *[^k�^]{.underline}*
> (squares of Jacobi eigenvalues).

# Multigrid Methods

> The Jacobi and Gauss-Seidel iterations produce smooth errors. The
> error vector *e* has its high frequencies nearly removed in a few
> iterations. But low frequencies are reduced very slowly. Convergence
> requires *O*(*N* ^2^) iterations---which can be unaccept-able. The
> extremely eﬀective multigrid idea is to change to a coarser grid, on
> which "smooth becomes rough" and low frequencies act like higher
> frequencies.
>
> On that coarser grid a big piece of the error is removable. *We
> iterate only a few times before changing from ﬁne to coarse and coarse
> to ﬁne*. The remarkable result is that multigrid can solve many sparse
> and realistic systems to high accuracy in a ﬁxed number of iterations,
> not growing with *n*.
>
> Multigrid is especially successful for symmetric systems. The key new
> ingredients are the (rectangular !) matrices *R* and *I* that change
> grids:

1.  A *restriction matrix R* transfers vectors from the ﬁne grid to the
    coarse grid.

2.  The return step to the ﬁne grid is by an *interpolation matrix I* =
    *I* ^h^ .

3.  The original matrix *A~h~* on the ﬁne grid is approximated by
    *A*~2h~ = *RA*~h~*I* on the coarse grid. You will see how this
    *A*~2*h*~ is smaller and easier and faster than *A~h~*. I will start
    with interpolation (a 7 by 3 matrix *I* that takes 3 *v*'s to 7
    *u*'s):

> � 1 ⎡ �*v*1*/*2 ⎡ �*u*1 ⎡
>
> Interpolation *Iv* = *u*
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} � ⎢ � ⎡
>
> ⎢ � ⎢
>
> *u* on the ﬁne (*h*) grid from 1 1 1 *v*1

� ⎢

> *v*~1~*/*2+*v*~2~*/*2 *u*~3~
>
> �
>
> 2 �*v*~2~ ⎣ = *v*~2~ ⎢ � ⎢ (1)
>
> *v* on the coarse (2*h*) grid 2
>
> ⎢ �
>
> values are the *u*'s.
>
> 1 1 *v*~3~ *v*~2~*/*2+*v*~3~*/*2 *u*~5~
>
> � 2⎣ � *v*3 ⎣ � *u*6 ⎣
>
> 1 *v*~3~*/*2 *u*~7~
>
> This example has *h* = ^[1]{.underline}^ on the interval 0 � *x* � 1
> with zero boundary conditions.
>
> The seven interior values are the *u*'s. The grid with 2*h* =
> ^[1]{.underline}^ has three interior *v*'s.
>
> Notice that *u*~2~*, u*~4~*, u*~6~ from rows 2, 4, 6 are the same as
> *v*~1~*, v*~2~*, v*~3~ ! Those coarse grid
>
> values *v~j~* are just moved to the ﬁne grid at the points *x* =
> ^[1]{.underline}^*,* ^[2]{.underline}^ *,* ^[3]{.underline}^ . The
> in-between

4 4 4

> values *u*~1~*, u*~3~*, u*~5~*, u*~7~ on the ﬁne grid are coming from
> *linear interpolation* between
>
> 0*, v*~1~*, v*~2~*, v*~3~*,* 0:

1

> Linear interpolation in rows 1, 3, 5, 7 *u*~2*j*+1~ = 2 (*v~j~* +
> *v~j~*~+1~) *.* (2)
>
> The odd-numbered rows of the interpolation matrix have entries
> ^[1]{.underline}^ and ^[1]{.underline}^ . We almost always use grid
> spacings *h,* 2*h,* 4*h, . . .* with the convenient ratio 2. Other
> matrices *I* are possible, but linear interpolation is easy and
> eﬀective. Figure 6.10a shows the new values *u*~2*j*+1~ (open circles)
> between the transferred values *u*~2*j*~ = *v~j~* (solid circles).

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image54.png){width="0.12301181102362205in"
height="0.12301181102362205in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image55.png){width="0.12301181102362205in"
height="0.12301181102362205in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image56.png){width="0.12301181102362205in"
height="0.12301181102362205in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image57.png){width="0.12301181102362205in"
height="0.12301181102362205in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image58.png){width="0.12301181102362205in"
height="0.12301290463692038in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image54.png){width="0.12301181102362205in"
height="0.12301181102362205in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image59.png){width="0.12301181102362205in"
height="0.12301181102362205in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image60.png){width="0.12301181102362205in"
height="0.12301181102362205in"}*u*~2~ = *v*~1~

> *vm* = 2+�2 sin [2*m�*]{.underline}
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image60.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image61.png){width="0.12249890638670166in"
> height="0.1225in"}
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image54.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image54.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image62.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image63.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image63.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image55.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image64.png){width="0.12301618547681539in"
> height="0.12301727909011373in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image64.png){width="0.12301618547681539in"
> height="0.12301727909011373in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image65.png){width="0.12301618547681539in"
> height="0.12301618547681539in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image66.png){width="0.12301618547681539in"
> height="0.12301727909011373in"}(a) Linear interpolation by *u* = *I^h^
> v* (b) Restriction by *R*^2*h*^*u* = ^[1]{.underline}^ (*I^h^* )^T^*u*
>
> 2*h h*
>
> 2 2*h*
>
> Figure 6.10: Interpolation to the *h* grid (7 *u*'s). Restriction to
> the 2*h* grid (3 *v*'s).
>
> When the *v*'s represent smooth errors on the coarse grid (because
> Jacobi or Gauss-Seidel has been applied on that grid), interpolation
> gives a good approximation to the errors on the ﬁne grid. A practical
> code can use 8 or 10 grids.
>
> The second matrix we need is a restriction matrix *R*^2h^. It
> transfers *u* on a ﬁne grid to *v* on a coarse grid. One possibility
> is the one-zero "injection matrix" that simply copies *v* from the
> values of *u* at the same points on the ﬁne grid. This ignores the
> odd-numbered ﬁne grid values *u*~2*j*+1~. Another possibility (which
> we adopt) is the full weighting operator *R* that comes from
> transposing *I^h^* .
>
> *Fine grid h to coarse grid* 2*h by a restriction matrix R*^2h^ =
> ^[1]{.underline}^(*I*^h^ )^T^

h 2 2h

� *u*1 ⎡

> Full weighting *Ru* = *v* 1 � 1 2 1 ⎡ �*u*3 ⎢ �*v*1 ⎡
>
> Fine grid *u* to coarse grid *v* 4 � 1 2 1 ⎣ � *u*4 ⎢ = � *v*2 ⎣ *.*
> (3)
>
> 1 2 1 *u*~5~ *v*~3~
>
> *u*~6~ *u*~7~
>
> The eﬀect of this restriction matrix is shown in Figure 6.10b. We
> intentionally chose the special case in which *u~j~* = sin(2*jω/*8) on
> the ﬁne grid (*open circles*). Then *v* on the coarse grid (*dark
> circles*) is also a pure sine vector. *But the frequency is doubled*
> (a full cycle in 4 steps). So a smooth oscillation on the ﬁne grid
> becomes "half as smooth" on the coarse grid, which is the eﬀect we
> wanted.

### Interpolation and Restriction in Two Dimensions {#interpolation-and-restriction-in-two-dimensions .unnumbered}

> Coarse grid to ﬁne grid in two dimensions from bilinear interpolation:
> Start with values *v~i,j~* on a square or rectangular coarse grid.
> Interpolate to ﬁll in *u~i,j~* by a sweep (interpolation) in one
> direction followed by a sweep in the other direction. We could allow
> two spacings *h~x~* and *h~y~*, but one meshwidth *h* is easier to
> visualize. A horizontal sweep along row *i* of the coarse grid (which
> is row 2*i* of the ﬁne grid) will
>
> ﬁll in values of *u* at odd-numbered columns 2*j* + 1 of the ﬁne grid:
>
> 1
>
> Horizontal sweep *u*~2*i,*2*j*~ = *v~i,j~* and *u*~2*i,*2*j*+1~ = 2
> (*v~i,j~* + *v~i,j~*~+1~) as in 1D. (4)
>
> Now sweep vertically, up each column of the ﬁne grid. Interpolation
> will keep those values (4) on even-numbered rows 2*i*. It will average
> those values to ﬁnd *u* = *I*2D *v* on the ﬁne-grid odd-numbered rows
> 2*i* + 1:

\(5\)

> The entries in the tall thin coarse-to-ﬁne interpolation matrix *I*2D
> are 1*,* ^[1]{.underline}^, and ^[1]{.underline}^
>
> The full weighting ﬁne-to-coarse restriction operator *R*2D is the
> *transpose I*2D^T^,
>
> multiplied by ^[1]{.underline}^. That factor is needed (like
> ^[1]{.underline}^ in one dimension) so that a constant
>
> vector of 1's will be restricted to a constant vector of 1's. (The
> entries along each row
>
> of the wide matrix *R* add to 1.) This restriction matrix has entries
> ^[1]{.underline}^*,* ^[1]{.underline}^, and ^[1]{.underline}^ and

4 8 16

> *each coarse-grid value v is a weighted average of nine ﬁne-grid
> values u*:
>
> Restriction matrix *R* = ^[1]{.underline}^ *I*^T^ 1/16
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}
>
> 1/8
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image41.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"} 1/16
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}Row *i, j* of *R* produces *v*~i,j~
> 1/8
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image21.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image49.png){width="0.11901137357830271in"
> height="0.11901137357830271in"}
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image40.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"} 1/8
>
> *v*~i,j~ uses *u*~2i,2j~ and 8 neighbors
>
> The nine weights add to 1 1/16
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image20.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"}
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image41.png){width="9.100831146106737e-2in"
> height="9.100831146106737e-2in"} 1/16 2*i*−1 2*i* 2*i*+1
>
> You can see how a sweep along each row with weights ^[1]{.underline}^
> *,* ^[1]{.underline}^*,* ^[1]{.underline}^, followed by a sweep

4 2 4

> down each column, gives the nine coeﬃcients in that "restriction
> molecule." Its
>
> matrix *R*2D is an example of a *tensor product* or *Kronecker
> product* kron(*R, R*). A 3 by 7 matrix *R* in one dimension becomes a
> 9 by 49 restriction matrix *R*2D in two dimensions.
>
> Now we can transfer vectors between grids. We are ready for the
> *geometric multigrid* method, when the geometry is based on spacings
> *h* and 2*h* and 4*h*. The idea extends to triangular elements (each
> triangle splits naturally into four similar triangles). The geometry
> can be more complicated than our model on a square.
>
> When the geometry becomes too diﬃcult, or we are just given a matrix,
> we turn (in the ﬁnal paragraph) to *algebraic multigrid*. This will
> imitate the multi-scale idea, but it works directly with *Au* = *b*
> and not with any underlying geometric grid.

### A Two-Grid V-Cycle (a v-cycle) {#a-two-grid-v-cycle-a-v-cycle .unnumbered}

> Our ﬁrst multigrid method only involves two grids. The iterations on
> each grid can use Jacobi's *I* − *D*^−1^*A* (possibly weighted by *�*
> = 2*/*3 as in the previous section) or Gauss-Seidel. For the larger
> problem on the ﬁne grid, iteration converges slowly to
>
> the low frequency smooth part of the solution *u*. *The multigrid
> method transfers the current residual r~h~* = *b* − *Au~h~ to the
> coarse grid*. We iterate a few times on that 2*h* grid, to approximate
> the coarse-grid error by *E*~2*h*~. Then interpolate back to *E~h~* on
> the ﬁne grid, make the correction to *u~h~* + *E~h~*, and begin again.
>
> This ﬁne-coarse-ﬁne loop is a two-grid V-cycle. We call it a v-cycle
> (small v).
>
> Here are the steps (remember, the error solves *A~h~*(*u* − *u~h~*) =
> *b~h~* − *A~h~u~h~* = *r~h~*):
>
> Steps 2-3-4 give the restriction-coarse solution-interpolation
> sequence that is the heart of multigrid. Recall the three matrices we
> are working with:

*A* = *A*~h~ = *original matrix*

*R* = 2h

> = *restriction matrix*
>
> *I* = *I*^h^ = *interpolation matrix .*
>
> Step 3 involves a fourth matrix *A*~2*h*~, to be deﬁned now. *A*~2*h*~
> is square and it is smaller than the original *A~h~*. In words, we
> want to "project" the larger matrix *A~h~* onto the coarse grid. There
> is a natural choice ! The variationally correct *A*~2*h*~ comes
> directly and beautifully from *R* and *A* and *I*:
>
> *The coarse grid matrix is A*~2h~ = *R*^2h^*A*~h~*I*^h^
>
> = *RAI.* (6)
>
> h 2h
>
> When the ﬁne grid has *N* = 7 interior meshpoints, the matrix *A~h~*
> is 7 by 7. Then the coarse grid matrix *RAI* is (3 by 7)(7 by 7)(7 by
> 3) = 3 by 3.
>
> Example In one dimension, *A* = *A~h~* might be the second diﬀerence
> matrix *K/h*^2^. Our
>
> ﬁrst example came from *h* =
>
> ^[1]{.underline}^. Now choose *h* =
>
> ^[1]{.underline}^, so that multigrid goes from ﬁve
>
> meshpoints inside 0 *\< x \<* 1 to two meshpoints (*I* is 5 by 2 and
> *R* is 2 by 5): The neat multiplication (we will use it again later)
> is *RA~h~* = *RK*~5~*/h*^2^:
>
> � 2 ⎡
>
> 1 � 1 2 1
>
> � 1 −1
>
> ⎢ � 0 2 0 −1 0 �

*RA* =

> 4 1 2 1 *h*2 �

−1 ⎢⎣

> = (2*h*)2 0 −1 0 2 0 *.* (7)
>
> A natural choice for *A*~2*h*~ on the coarse grid is
> *K*~2~*/*(2*h*)^2^ and multigrid makes this choice:
>
> [1]{.underline} � 2 −1 �
>
> Coarse grid matrix *A* = *RAI* = *.* (8)
>
> The reader will appreciate that the *I* ^T^*AI* rule preserves
> symmetry and positive deﬁniteness, when *A* has those properties. The
> rule arises naturally in Galerkin methods \[--,page --\], including
> the ﬁnite element method. Notice how the restriction operator *R* with
> the factor ^[1]{.underline}^ automatically adjusts 1*/h*^2^ to
> 1*/*(2*h*)^2^.
>
> Steps 1 and 5 are necessary, but they are really outside the essential
> multigrid idea. The smoother is step 1, the post-smoother is step 5.
> Those are normal iterations for which weighted Jacobi or Gauss-Seidel
> is satisfactory.
>
> The Errors *e~h~* and *E~h~*
>
> Suppose we solve the coarse grid equation exactly at step 3. Is the
> multigrid error correction *E~h~* then equal to the true ﬁne-grid
> error *e~h~* = *u* − *u~h~* ? No, that is too much to expect ! We have
> only solved the smaller problem on the coarse grid, not the full
> problem. But the connection between *E~h~* and *e~h~* is simple and
> crucial for understanding multigrid. We now track down the steps from
> *E* to *e*.
>
> *Four matrices multiply e*. At step 2, the residual *r* = *b* −
> *Au~h~* = *A*(*u* − *u~h~*) = *Ae*
>
> multiplies by *A*. The restriction is multiplication by *R*. The
> solution step 3 multiplies by *A*^−1^ = (*RAI*)^−1^. The interpolation
> step 4 multiplies by *I* to ﬁnd the correction
>
> 2*h* −1
>
> *E*. *Altogether, E is IA*21 *RA*h*e*:
>
> *E* = *I*(*RAI*)^−1^*RAe* and we call this *E* = *Se .* (9)
>
> When *I* is 5 by 2 and *R* is 2 by 5, that matrix *S* on the right
> side is 5 by 5. It can't be the identity matrix, since *RAI* and its
> inverse are only 2 by 2 (rank two). But *S* = *I*(*RAI*)^−1^*RA* has
> the remarkable property *S*^2^ = *S*. This says that *S is the
> identity matrix on its 2-dimensional column space*. (Of course *S* is
> the zero matrix on its 3-dimensional nullspace.) *S*^2^ = *S* is easy
> to check:
>
> *S*^2^ = (*I*(*RAI*)^−1^*RA*)(*I*(*RAI*)^−1^*RA*) = *S* because
> (*RAI*)^−1^*RAI* disappears. (10)
>
> So the multigrid correction *E* = *Se* is not the whole error *e*, *it
> is a projection of e*. The new error is *e* − *E* = *e* − *Se* = (*I*
> − *S*)*e*. *This matrix I* − *S is the two-grid operator. I* − *S*
> plays the same fundamental role in describing the multigrid steps 2--4
> that the usual *M* = *I* − *P* ^−1^*A* plays for each iteration in
> steps 1 and 5:
>
> v-cycle matrix = *I* − *S* iteration matrix = *I* − *P* ^−1^*A .*
>
> Example (continued). The 5 by 5 matrix *A~h~* = *K*~5~*/h*^2^ and the
> rectangular *I* and *R*

led in (8) to *A*~2*h*~ = *K*~2~*/*(2*h*)^2^. To ﬁnd *S* = *IA*^−1^*RA*
, we multiply (7) by *IA*^−1^:

*A*^−1^*RA*

> = � 0 1 0 0 0 �
>
> 2*h h*
>
> 2*h*
>
> � 0 1*/*2 0 0 0 ⎡
>
> � 0 1 0 0 0⎢
>
> Now multiply by *I* to ﬁnd *S*
>
> 0 0 0 1 0
>
> 0 0 0 1*/*2 0
>
> The eigenvalues of this *S* are 1*,* 1*,* 0*,* 0*,* 0. If you square
> *S*, you recover *S*^2^ = *S*. With its three columns of zeros, the
> nullspace of *S* contains all ﬁne-grid vectors of the form (*e*~1~*,*
> 0*, e*~3~*,* 0*, e*~5~). Those are vectors that don't appear on the
> coarse grid. If the error *e* had this form, then *E* = *Se* would be
> zero (no improvement from multigrid). *But we don't expect a large
> component of those high frequency vectors in e, because of the
> smoothing*.
>
> The column space of *S* contains column 2 = ( ^[1]{.underline}^ *,*
> 1*,* ^[1]{.underline}^ *,* 0*,* 0) and column 4 = (0*,* 0*,*
> ^[1]{.underline}^*,* 1*,* ^[1]{.underline}^).
>
> 2 2 2 2
>
> These are "mixed-frequency vectors." We do expect them to appear in
> *e*, because the
>
> smoothing step didn't remove them. But these are vectors for which *E*
> = *Se* = *e* and they are the errors that multigrid catches ! After
> step 4 they are gone.
>
> Let me say this in another way. Because *S*^2^ = *S*, the only
> eigenvectors are *�* = 0 and *�* = 1. (If *Su* = *�u* we always have
> *S*^2^*u* = *�*^2^*u*. Then *S*^2^ = *S* gives *�*^2^ = *�*.) Our
> example has *�* = 1*,* 1*,* 0*,* 0*,* 0. The eigenvalues of *I* −*S*
> are 0*,* 0*,* 1*,* 1*,* 1. The eigenvectors *e* reveal what multigrid
> is doing:
>
> *E* = *Se* = 0 In this case multigrid gives no improvement. The
> correction *E* added to *u~h~* in step 4 is zero. IN the example, this
> happens for errors *e* = (*e*~1~*,* 0*, e*~3~*,* 0*, e*~5~) that are
> zero on the coarse grid where step 3 is working.
>
> *E* = *Se* = *e* In this case multigrid is perfect. The correction
> *E~h~* added to *u~h~* in step 4 is the whole error *e~h~*. In the
> example, two eigenvectors of *S* for *�* = 1 are *e* = (1*,* 2*,* 2*,*
> 2*,* 1) and *e* = (1*,* 2*,* 0*,* −2*,* −1). Those have large
> low-frequency components. They oscillate up and down only once and
> twice. They are in the column space of
>
> *I*. They are no perfect sines, but an important part of the
> low-frequency error is caught and removed. The number of independent
> vectors with *Se* = *e* is the number of coarse gridpoints (here 2).
> That measures the *A*~2*h*~ problem that step 3 deals with. It is the
> rank of *S* and also *I*. The other 5 − 2 gridpoints account for the
> nullspace of *S*, where *E* = *Se* = 0 means no improvement from
> multigrid.
>
> Note The "high-frequency" vectors (*u*~1~*,* 0*, u*~3~*,* 0*, u*~5~)
> with *Su* = 0 are *not exactly* combinations of the last three
> discrete sines *y*~3~*, y*~4~*, y*~5~. The frequencies are mixed by
> *S*, as equations (18--19) will clearly show. The exact statements are
> *column space of S*
>
> *= column space of I* and *nullspace of S = nullspace of RA*. The
> mixing of frequencies does not aﬀect our main point: Iteration handles
> the high frequencies and multigrid handles the low frequencies.
>
> You can see that a perfect smoother followed by perfect multigrid
> (exact solution at step 3) would leave no error. In reality, this will
> not happen. Fortunately, a careful
>
> (not so simple) analysis will show that a multigrid cycle with good
> smoothing can reduce the error by a constant factor *λ* that is
> independent of *h*:
>
> →error after step 5→ � *λ* →error before step 1→ with *λ \<* 1 *.*
> (12)
>
> A typical value is *�* = ^[1]{.underline}^ . Compare with *λ* = *.*99
> for Jacobi alone. This is the
>
> Holy Grail of numerical analysis, to achieve a convergence factor *λ*
> (a spectral radius of the overall iteration matrix) that *does not
> move up to* 1 *as h* � 0. We can achieve a given relative accuracy in
> a ﬁxed number of cycles. Since each step of each cycle requires only
> *O*(*n*) operations on sparse problems of size *n*, multigrid is an
> *O*(*n*) algorithm. This does not change in higher dimensions.
>
> There is a further point about the number of steps and the accuracy.
> The user may want the solution error *e* to be as small as the
> discretization error (when the original diﬀerential equation was
> replaced by *Au* = *b*). In our examples with second diﬀerences, this
> demands that we continue until *e* = *O*(*h*^2^) = *O*(*N* ^−2^). In
> that case we need more than a ﬁxed number of v-cycles. To reach *λ^k^*
> = *O*(*N* ^−2^) requires *k* = *O*(log *N* ) cycles. Multigrid has an
> answer for this too.
>
> Instead of repeating v-cycles, or nesting them into V-cycles or
> W-cycles, it is better to use full multigrid: FMG cycles are described
> below. Then the operation count comes back to *O*(*n*) even for this
> higher required accuracy *e* = *O*(*h*^2^).

### V-Cycles and W-Cycles and Full Multigrid {#v-cycles-and-w-cycles-and-full-multigrid .unnumbered}

> Clearly multigrid need not stop at two grids. If it did stop, it would
> miss the remark-able power of the idea. The lowest frequency is still
> low on the 2*h* grid, and that part of the error won't decay quickly
> until we move to 4*h* or 8*h* (or a very coarse 512*h*).
>
> The two-grid v-cycle extends in a natural way to more grids. It can go
> down to coarser grids (2*h,* 4*h,* 8*h*) and back up to (4*h,* 2*h,
> h*). This nested sequence of v-cycles is a V-cycle (capital V). *Don't
> forget that coarse grid sweeps are much faster than ﬁne grid sweeps*.
> Analysis shows that time is well spent on the coarse grids. So the
> W-cycle that stays coarse longer (Figure 6.11b) is generally superior
> to a V-cycle.
>
> *h* 2*h* 4*h* 8*h*
>
> Figure 6.11: V-cycles and W-cycles and FMG use several grids several
> times. The full multigrid cycle in Figure 6.11c is asymptotically
> better than V or W.
>
> *Full multigrid starts on the coarsest grid*. The solution on the 8*h*
> grid is interpolated
>
> to provide a good initial vector *u*~4*h*~ on the 4*h* grid. A v-cycle
> between 4*h* and 8*h* improves it. Then interpolation predicts the
> solution on the 2*h* grid, and a deeper
>
> V-cycle makes it better (using 2*h,* 4*h,* 8*h*). Interpolation of
> that improved solution onto the ﬁnest grid gives an excellent start to
> the last and deepest V-cycle.
>
> The operation counts for a deep V-cycle and for full multigrid are
> certainly greater than for a two-grid v-cycle, but *only by a constant
> factor*. That is because the count is divided by a power of 2 every
> time we move to a coarser grid. For a diﬀerential equation in *d*
> space dimensions, we divide by 2*^d^*. The cost of a V-cycle (as deep
> as we want) is less than a ﬁxed multiple of the v-cycle cost:
>
> V-cycle cost *\<* 1 + [1]{.underline} +

2*d*

> [1]{.underline} ^2^
>
> 2*d*

2*d*

> \+ · · · v-cycle cost = 2*d* − 1 v-cycle cost *.* (13)
>
> Full multigrid is no more than a series of inverted V-cycles,
> beginning on a very coarse mesh. By the same reasoning that led to
> (13),
>
> 2*d* ⎦ 2*d* �2
>
> And the method works in practice. But good programming is required.

### Multigrid Matrices {#multigrid-matrices .unnumbered}

> For a 3-grid V-cycle, what matrix *S*~3~ corresponds to the 2-grid
> v-cycle projection *S* = *I*(*RAI*)^−1^*RA* ? No smoothing is involved
> here. *S* and *S*~3~ only project to coarser problems. By itself,
> *S*~3~ will not be a good solver without smoothers.
>
> To construct *A*~4*h*~, replace the matrix *A*~2*h*~ = *RAI* on the
> middle grid by using a coarse restriction *R~c~* = *R*^4*h*^ that
> transfers down to the 4*h* grid, and an interpolation *I~c~* =
> *I*^2*h*^ that comes back to 2*h*:
>
> Very coarse matrix *A*~4h~ = *R*~c~*A*~2h~*I*~c~ *.* (15)
>
> If *h* = ^[1]{.underline}^ , that product is (3 × 7)(7 × 7)(7 × 3).
> The 3 by 3 problem uses *A*~4*h*~ on the 4*h* = ^[1]{.underline}^ grid
> (with three interior unknowns). Then *S*~3~ = (*S*~3~)^2^ is the
> matrix that goes down two grids, solves the very coarse problem by
> *A*^−1^, and comes back up:
>
> *E*~3~ = *S*~3~*e* = Error removed *S*~3~ = *I^h^
> I*^2*h*^*A*^−1^*R*^4*h*^*R*^2*h*^*A .* (16)
>
> 2*h* 4*h* 4*h* 2*h h*
>
> The error that remains after an unsmoothed V-cycle will be (*I* −
> *S*~3~)*e*. On the *h* = ^[1]{.underline}^ grid, there are 15
> frequencies in the error *e*. Only the lowest 3 are (approximately)
> removed by *S*~3~*e*. We have only solved a 3 by 3 problem with
> *A*~4*h*~. It is the *smoothers*, on the ﬁne *h* grid and the middle
> 2*h* grid, that reduce the high and middle frequency errors in the
> solution.
>
> Note to myself: *S*~4*h*~ = *I~c~A*^−1^*R~c~A*~2*h*~ =
> *I~c~A*^−1^*R~c~RAI* = 7 × 7 has *I* on right instead
>
> of left. Still *S*^2^ = *S*~4*h*~.

### Numerical Experiments {#numerical-experiments-1 .unnumbered}

> The real test of multigrid eﬀectiveness is numerical ! Its *k*-step
> approximation *e~k~* should approach zero and the graphs will show how
> quickly this happens. An initial guess *u*~0~ includes an error
> *e*~0~. Whatever iteration we use, we are trying to drive *u~k~* to
> *u*, and *e~k~* to zero. The multigrid method jumps between two or
> more grids, so as to converge more quickly, and our graphs will always
> show the error on the ﬁne grid.
>
> We can work with the equation *Ae* = 0, whose solution is *e* = 0.
> Following \[--\], Figure 6. a displays an initial error with low and
> high frequencies:

1

> (*e*~0~)*~j~* = sin 4*jωh* + sin 20*jωh* with *h* = 32 *.*
>
> We draw continuous functions sin 4*ωx* and sin 20*ωx* rather than 31
> discrete values. Figure 6. b shows the error vector *e*~3~ after three
> ﬁne-grid sweeps of weighted Jacobi (with *�* = ^[2]{.underline}^ ). As
> expected, the high frequency component has greatly decayed. The error
> *e*~3~ = (*I* − *P* ^−1^*A*)^3^*e*~0~ is much smoother than *e*~0~.
> For our second diﬀerence matrix *A~h~* (better known as *K*), the
> Jacobi preconditioner from Section 6.2 simply has *P* ^−1^ =
> ^[1]{.underline}^ *�I*. We can ignore the factors *h*^2^ that divide
> *K* and *P* , because they
>
> cancel.

Figure 6.12: The initial error and the error *e*~3~ after three weighted
Jacobi relaxations.

> Now multigrid begins. The current ﬁne-grid residual is *r~h~* =
> −*A~h~e*~3~. After restric-tion to the coarse grid it becomes
> *r*~2*h*~. Three weighted Jacobi iterations on the coarse grid error
> equation *A*~2*h*~*E*~2*h*~ = *r*~2*h*~ start with the guess *E*~2*h*~
> = 0. That produces\...
>
> ADD V-CYCLE AND FMG EXPERIMENTS
>
> Figure 6.13: The ﬁne-grid error after 3 sweeps on the coarse grid (a)
> and then the ﬁne grid (b).

### Eigenvector Analysis {#eigenvector-analysis .unnumbered}

> The reader will recognize that one matrix (like *I* − *S* for a
> v-cycle) can describe each multigrid method. The eigenvalues of a full
> multigrid matrix would be nice to know, but they are usually
> impractical to ﬁnd. Numerical experiments build conﬁdence. Computation
> also provides a *diagnostic* tool, to locate where convergence is
> stalled and a change is needed (often in the boundary conditions). If
> we want a *predictive* tool, the best is modal analysis.
>
> The key idea is to watch the Fourier modes. In our example those are
> discrete sines, because of the boundary conditions *u*(0) = *u*(1) =
> 0. We will push this model problem all the way, to see what the
> multigrid matrix *I* − *S* does to those sine vectors.
>
> The ﬁnal result in (18--19) shows why multigrid works and it also
> shows how *pairs of frequencies are mixed*. The eigenvectors are
> mixtures of two frequencies.
>
> The frequencies that mix together are *k* and *N* + 1 − *k*. The
> discrete sines with those frequencies are *y~k~* and *Y~k~*:
>
> *y* = sin *[kω]{.underline} ,* sin [2*kω*]{.underline} *, . . .*
>
> *^k^ N*+1 *N*+1
>
> and *Y~k~*

= sin [(*N*+1−*k*)*ω*]{.underline} *,* sin [2(*N*+1−*k*)*ω*]{.underline}
*, . . . .*

*N*+1 *N*+1

> Where *y~k~* goes up and down *k* times, *Y~k~* does that *N* + 1 −
> *k* times.
>
> There is something neat you have to see. *Y*~k~ and *y*~k~ have the
> same compo-nents except for alternating signs ! Cancel *N*+1 with
> *N*+1 in those components of *Y~k~*:
>
> *Y* = sin *ω* − *[kω]{.underline} ,* sin 2*ω* − [2*kω*]{.underline} *,
> . .* = + sin *[kω]{.underline} ,* − sin [2*kω*]{.underline} *, . .*
>
> *^k^ N*+1 *N*+1 *N*+1 *N*+1
>
> \(17\)
>
> For our model problem with second diﬀerences, we can report the result
> of multiplying by *S* = *I*(*RAI*)^−1^*RA*. In fact the true multigrid
> matrix is *I* − *S*, to give the error *e* − *E* = (*I* − *S*) *e*
> that remains after steps 2, 3, 4. Seeing *I* − *S* is even better:
>
> Such beautiful formulas can't be expected in more complicated
> problems, and we seize this chance to make four key points:

1.  Low frequencies like *k* = 1*,* 2*,* 3 are greatly reduced by
    multigrid. The cosine in equation (18) will be near 1. The factor (1
    − cos *[^k�^]{.underline}* ) is very small, of order (*k/N*)^2^.
    This shows how multigrid is powerful in nearly killing the low
    frequencies. These are exactly the frequencies on which Jacobi and
    Gauss-Seidel will stall in the smoothing iterations.

2.  The pair of sines *y*~k~ and *Y*~k~ is mixed together by multigrid.
    We will see that the restriction *R* and interpolation *I* are
    responsible. Those are not like the square matrix *A*, which keeps
    frequencies separate (because the sines are its eigenvectors).
    Aliasing appears for rectangular matrices !

3.  The combinations *e* = *y*~k~ + *Y*~k~ are eigenvectors of *I* − *S*
    with *�* = 1. Just add equations (18) and (19), to get (*I* −
    *S*)*e* = *e*. Since *Y~k~* has the same components as *y~k~* with
    alternating signs, *y~k~* + *Y~k~* has the correct form (*e*~1~*,*
    0*, e*~3~*,* 0*, . . .*). Those are the vectors that we discovered
    earlier in the nullspace (*�* = 0) of *S*. They are not touched by
    *I* − *S* since *Se* = 0.

4.  The other eigenvectors of *I* −*S* are just *Sy*~k~. We know that
    (*I* −*S*)*Sy~k~* = 0 because *S* = *S*^2^. In our example with *N*
    = 5, the vectors *Sy*~1~ and *Sy*~2~ are multiples of (1*,* 2*,*
    2*,* 2*,* 1) and (1*,* 2*,* 0*,* −2*,* 1) that we found explicitly.
    Multigrid removes them from the error.

> According to (18), these vectors *Sy~k~* are combinations of *y~k~*
> and *Y~k~*. To ﬁnd a good combination, multiply (18) and (19) by (1 +
> cos *[^k�^]{.underline}* ) and (1 − cos *[^k�^]{.underline}* ). The
> right-
>
> hand sides are now the same and we subtract:
>
> *N* +1

*N* +1

> *S*� = *e*� (*I* − *S*)*e*� = (*I* − *S*) 1 + cos *[kω]{.underline} y*

*N*+1 *^k^*

> − 1 − cos *[kω]{.underline} Y*
>
> *N*+1 *^k^*

� = 0 (20)

> These mixtures *e*� in square brackets are completely killed (*�* = 0)
> by multigrid. A smooth error vector *e~h~* (after Jacobi iterations
> have reduced its high frequency components) has only small components
> along the eigenvectors *y~k~* + *Y~k~*. Multigrid doesn't touch those
> pieces (*�* = 1). The larger components along the *Z~k~* will die.

### The Restriction *R* Produces Aliasing {#the-restriction-r-produces-aliasing .unnumbered}

> To complete this analysis we have to see where and how a pair of
> frequencies is mixed. The aliasing comes from the restriction matrix
> *R* = *R~h~*, when both vectors *y^h^* and
>
> *Y ^h^* lead to multiples of the same output vector *y*^2*h*^:
>
> *Ry^h^* = ⎦[1]{.underline} − [1]{.underline} cos *[kω]{.underline}* �
> *y*^2*h*^ and *RY ^h^* = ⎦ [1]{.underline} [1]{.underline} cos
> *[kω]{.underline}* � *y*^2*h*^ *.* (21)
>
> *You see the aliasing by R*. We cannot hope to decide the input *y~k~*
> or *Y~k~* from these outputs. This is normal for a short wide matrix.
> (The matrix *R* is 3 by 7 and 2 by 5 in our examples.) The coarse mesh
> output has only about half as many components as the ﬁne mesh input.
>
> The transpose of *R* does the opposite. Where *R* mixes two inputs
> *y^h^* and *Y ^h^* into one output, the interpolation matrix *I* sends
> one input frequency on the coarse grid into a pair of frequencies on
> the ﬁne grid:
>
> 2 *I^h^ y*^2*h*^ = ⎦1 + cos *[kω]{.underline}* � *y^h^* − ⎦1 − cos
> *[kω]{.underline}* � *Y ^h^ .* (22)
>
> Interpolation of a smooth vector (low *k*) on a coarse grid will
> excite an oscillatory mode *Y ^h^* (high *k*) on the ﬁne grid. But
> those oscillations have small amplitude, because the cosine of
> *kω/*(*N*+1) is near 1.
>
> The key formulas (18) and (19) that describe multigrid come from
> assembling (21) for *R*, (22) for *I*, and the known eigenvalues for
> *A~h~* and *A*~2*h*~. I think the calculation of *S* in (11) shows
> this best. Its zero columns put *y~k~* + *Y~k~* in its nullspace. The
> nonzero columns in *S* come from the interpolation matrix *I*. So *Se*
> captures a part of the whole error *e*. *Multigrid solves a projection
> of the original problem*.
>
> Example completed It would be useless to repeat steps 2, 3, 4 with no
> smoothing in between. Nothing would change! The untouched vectors *e*
> = *y~k~* + *Y~k~* with (*I* − *S*)*e* = *e* will still be untouched.
> It is the smoothing matrix *M* = *I* − *P* ^−1^*A* that must reduce
> these errors.
>
> If we apply Jacobi with weight *w* = ^[2]{.underline}^ at steps 1 and
> 5, then *M* = *I* − ^[1]{.underline}^ *A*. The overall
>
> 3 3
>
> matrix for all steps 1 to 5 will be *M*(*I* − *S*)*M*. The eigenvalues
> of that matrix will decide
>
> the success (or not) of multigrid. To my amazement, the 5 by 5 matrix
> *M*(*I* − *S*)*M* has a *triple eigenvalue of* ^[1]{.underline}^ !
>
> 1
>
> The three eigenvalues *�* = 1 of *I* − *S* are reduced to *�* =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image67.png){width="9.500546806649168e-2in"
> height="6.666666666666667e-3in"} for *M* (*I* − *S*)*M* .
>
> 9
>
> The largest eigenvalue of *M* is *.*91---you see the value of
> multigrid. I hope you will try
>
> eig(*M* � *M* � (*I* − *S*) � *M* � *M*) with double smoothing (see
> Problems 9--12).

### Fourier Modal Analysis {#fourier-modal-analysis .unnumbered}

> Pure modal analysis neglects the boundaries completely. It assumes an
> inﬁnite grid ! The vectors *y~k~* in the example were sines because of
> the boundary conditions. When boundaries are gone, the *y~k~* are
> replaced by inﬁnitely long vectors *y*� coming from complex
> exponentials. Now there is a continuum of frequencies *�*:
>
> *y*� = (*. . . , e*^−2*i�*^*, e*^−*i�*^*,* 1*, e^i�^, e*^2*i�*^ *, . .
> .*) with − *ω* � *�* � *ω .* (23) We need inﬁnite matrices *K*~�~ to
> multiply these inﬁnite vectors. Second diﬀerences
>
> −1*,* 2*,* −1 appear on *all rows forever*. The key is that each
> *y~�~* is an eigenvector of *K*~�~,
>
> with eigenvalue *�* = 2 − 2 cos *�*:
>
> *K*~�~ *y*� = (2 − 2 cos *�*) *y*� because − *e^i�^*^(*n*+1)^ −
> *e^i�^*^(*n*−1)^ = −2 cos *� e^i�n^ .* (24)
>
> This tells us the action of *A~h~* = *K*~�~*/h*^2^. It also tells us
> about *A*~2*h*~, when the coarse mesh changes *h*^2^ to (2*h*)^2^ and
> *�* to 2*�*.
>
> The restriction matrix *R* still introduces aliasing. The frequencies
> that mix to-gether are now *�* and *�* + *ω*. Notice how increasing
> *�* by *ω* produces a factor *e^i�n^* = (−1)*^n^* with alternating
> signs. This is exactly what we saw for *y~k~* and *Y~k~*. This time it
> is *y*� − *y*�+rr that has all zeros in its even-numbered components.
>
> This pure Fourier analysis will go all the way to formulas for the
> inﬁnite (*I* − *S*)*y*� and (*I* −*S*)*y*�+rr , just like equations
> (18) and (19). In that ﬁnite case, those equations explained why
> multigrid succeeds. They do the same in the inﬁnite case.
>
> Let me emphasize why this pure modal analysis (with no boundaries and
> constant coeﬃcients) was mentioned. It allows Fourier to work freely.
> The diﬀerential equation div(*c*(*x, y*) grad *u*) = *f* (*x, y*) on a
> general region would lead to giant complications in the eigenvectors
> for multigrid---impossible to ﬁnd them. But if we ﬁx *c* = constant
> and ignore boundaries, those "interior eigenvectors" return to simple
> combinations of *y*� and *y*�+rr. That leaves diﬃculties associated
> with the boundary conditions, which Fourier doesn't easily resolve.

### Algebraic Multigrid {#algebraic-multigrid .unnumbered}

> We close this section with a few words about algebraic multigrid, when
> the problem comes as a system of equations *Au* = *b*. *There is no
> grid in the background*. We need to ﬁnd replacements for the key ideas
> on which geometric multigrid was based: *smooth vectors, connected
> nodes, coarse meshes*. Replacing the ﬁrst two is fairly easy,
> rescaling *A~h~* to *A*~2*h*~ on a (nonexistent) coarse mesh is less
> clear.

1.  Smooth vectors. In geometric multigrid these are vectors for which
    the norms of *u* and *Au* are comparable. That will be our
    indication of a smooth vector. High frequencies in *u* would be
    greatly ampliﬁed by *A* (just as the second derivative ampliﬁes sin
    *kt* by *k*^2^). For low frequencies, Multigrid works on smooth
    errors and Jacobi doesn't.

2.  Connected nodes. On a grid, neighboring nodes are reﬂected by a
    nonzero entry in *A*. When there is no grid, we look directly at the
    matrix. Its signiﬁcant nonzero entries *A~ij~* (magnitude greater
    than *�A~ii~*, say with *�* = ^[1]{.underline}^ ) tell us when

> we should think of the "nodes" *i* and *j* as being connected.

3.  Coarse subset of nodes. Each signiﬁcant entry *A~ij~* indicates that
    the value of *u~j~ strongly inﬂuences* the value of *u~i~*. Probably
    the errors *e~j~* and *e~i~* are comparable, when the error is
    smooth. We don't need both *i* and *j* in the "coarse set *C*" of
    nodes. On a grid they would be neighbors, not both in *C*.

> But if *i* is *not* in *C*, then every *j* that strongly inﬂuences *i*
> should either be in *C* or be strongly inﬂuenced by another *J* that
> *is* in *C*. This heuristic rule is discussed more fully in \[--\],
> with an algorithm for constructing *C*. (In general, too many coarse
> unknowns are better than too few.)
>
> The excellent book \[--\] also constructs the coarse-to-ﬁne
> interpolation matrix *I*. This starts with the errors *E~j~* for *j*
> in *C*, and leaves them unchanged. If *i* is not in *C*, the
> interpolated value *E~i~* at step 2 of multigrid will be a *weighted
> combination* of the *E~j~* that do have *j* in *C*. In our
> one-dimensional model problem, that weighted combination was the
> average of the two neighbors of *i*. That model problem certainly had
> a grid !
>
> The interpolating combination will give greatest weight to the *e~j~*
> for which *j* in *C* strongly inﬂuences *i*. But there may be smaller
> entries *A~ij~* that cannot be completely ignored. The ﬁnal decision
> on the weights for each interpolated value is more subtle than a
> simple average. Algebraic multigrid is more expensive than geometric
> multigrid, but it applies to a much wider range of sparse matrices *A*
> (and the software can control AMG without us). We still expect a
> "smoothing + multigrid" combination that is close to *O*(*n*) steps
> for an accurate solution of *Au* = *b*.
>
> Let me mention an important contrast between solid mechanics and ﬂuid
> mechan-ics. For solids, the original ﬁnite element grid is already
> relatively coarse. We are typically looking for "engineering accuracy"
> and we don't have ﬁne scale motions to resolve. Multigrid is not such
> a common choice for structural problems (elimination
>
> is simpler). Fluids do have ﬁne scales so that multigrid becomes a
> natural idea, not only numerically but physically. Of course ﬂuids
> don't generally present symmetric matrices, because of the convective
> terms, and ﬁnite element methods may require "upwind adjustments." The
> analysis of multigrid convergence becomes harder for ﬂuids, just when
> a multiscale approach becomes attractive.

### Problem Set 6.3 {#problem-set-6.3 .unnumbered}

1.  What is the 3 by 7 matrix *R*~injection~ that copies *v*~1~*,
    > v*~2~*, v*~3~ from *u*~2~*, u*~4~*, u*~6~ and ignores *u*~1~*,
    > u*~3~*, u*~5~*, u*~7~ ?

2.  Write down a 9 by 4 bilinear interpolation matrix *I* that uses the
    > four grid values at the corners of a square (side 2*h*) to produce
    > nine values at the (*h*) gridpoints. What constant should multiply
    > the transpose of *I* to give a one-element restriction matrix *R*
    > ?

3.  In Problem 2, the four small squares (side *h*) subdivide into 16
    > smaller squares (side *h/*2). How many rows and columns in the
    > interpolation matrix *I~h/~*~2~ ?

4.  If *A* is the 5-point discrete Laplace matrix (with −1*,* −1*,* 4*,*
    > −1*,* −1 on a typical row) what is a typical row of *A*~2*h*~ =
    > *RAI* using bilinear interpolation as in Problems 2--3 ?

5.  Suppose *A* comes from the 9-point stencil (8*/*3 surrounded by
    > eight entries of

> −1*/*3). What is now the stencil for *A*~2*h*~ = *RAI* ?

6.  Verify *Ry^h^* = ^[1]{.underline}^(1 + cos *[^k�^]{.underline}*
    > )*y*^2*h*^ in equation (23) for the linear restriction matrix

> *k* 2 *N* +1 *k*
>
> *R* applied to discrete sines *y^h^* with *k* � ^[1]{.underline}^ (*N*
> +1).
>
> *k* 2

7.  Show that *RY ^h^* = ^[1]{.underline}^ (−1−cos *[^k�^]{.underline}*
    > )*y*^2*h*^ in equation (23) for the "complementary"

> *k* 2 *N* +1 *k*
>
> discrete sines *Y ^h^* = *y~N~*~+1−*k*~. Now *N* + 1 − *k \>*
> ^[1]{.underline}^ (*N* +1).

8.  Verify equation (24) for linear interpolation applied to the
    > discrete sines *y^h^* with

> *k* � ^[1]{.underline}^ (*N* +1).

9.  With *h* = ^[1]{.underline}^ , use the 7 by 3 and 3 by 7 matrices
    > *I* and *R* in equations (1--2) to ﬁnd the 3 by 3 matrix *A*~2*h*~
    > = *RAI* with *A* = *K*~7~*/h*^2^.

10. Continue Problem 9 to ﬁnd the 7 by 7 matrix *S* =
    > *I*(*RAI*)^−1^*RA*. Verify that *S*^2^ = *S*, and that *S* has the
    > same nullspace as *RA* and the same column space as *I*. What are
    > the seven eigenvalues of *S* ?

11. Continue Problem 10 to ﬁnd (by MATLAB) the multigrid matrix *I* −
    > *S* and the presmoothed/postsmoothed matrix *MSM* , where *M* is
    > the Jacobi smoother

> *I* − *�D*^−1^*A* = *I* − ^[1]{.underline}^ *K*~7~ with *�* =
> ^[2]{.underline}^ . Find the eigenvalues of *MSM* !
>
> 3 3

12. Continue Problem 11 to ﬁnd the eigenvalues of *M* ^2^*SM* ^2^ with
    > two Jacobi smoothers (*�* = ^[2]{.underline}^ ) before and after
    > the grid changes.

13. With unweighted Jacobi (*�* = 1 and *M* = *I* − ^[1]{.underline}^
    > *K*~7~) ﬁnd *MSM* and its eigen-

> values. Is the weighting useful ?

14. Starting from *h* = ^[1]{.underline}^ and the second diﬀerence
    > matrix *A* = *K*~15~*/h*^2^, compute

> the projected 7 by 7 matrix *A*~2*h*~ = *RAI* and the doubly projected
> 3 by 3 matrix
>
> *A*~4*h*~ = *R~c~A*~2*h*~*I~c~*. Use linear interpolation matrices *I*
> and *I~c~*, and restriction matrices *R* = ^[1]{.underline}^ *I*^T^
> and *R~c~* = ^[1]{.underline}^ *I*^T^.
>
> 2 2 *c*

15. Use *A*~4*h*~ from Problem 14 to compute the projection matrix
    > *S*~3~ in (16). Verify that this 15 by 15 matrix has rank 3, and
    > that (*S*~3~)^2^ = *S*~3~.

16. The weighted Jacobi smoothers are *M~h~* = *I*~15~ −
    > ^[1]{.underline}^ *K*~15~ and *M*~2*h*~ = *I*~7~ −
    > ^[1]{.underline}^ *K*~7~. With MATLAB, compute the smoothed error
    > reduction matrix *V*~3~ and its eigenvalues:

> *V*~3~ = *M~h~IM*~2*h*~(*I*~7~ − *S*~2*h*~)*M*~2*h*~*RAM~h~ .*
>
> *S*~2*h*~ = *I~c~A*^−1^*R~c~A*~2*h*~ is the projection matrix for the
> v-cycle within the V-cycle.

17. Compute the (15 × 7)(7 × 3) linear interpolation matrix *I^h^
    > I*^2*h*^. What is the

> restriction matrix ?

# Krylov Subspaces and Conjugate Gradients

> Our original equation is *Ax* = *b*. *The preconditioned equation is
> P* ^−1^*Ax* = *P* ^−1^*b*. When we write *P* ^−1^, we never intend
> that an inverse will be explicitly computed. *P* may come from
> Incomplete *LU* , or a few steps of a multigrid iteration, or "domain
> decomposition." Entirely new preconditioners are waiting to be
> invented.
>
> *The residual is r*~k~ = *b* − *Ax*~k~*.* This is the error in *Ax* =
> *b*, not the error in *x*
>
> itself. An ordinary preconditioned iteration corrects *x~k~* by the
> vector *P* ^−1^*r~k~*:
>
> *P x~k~*~+1~ = (*P* − *A*)*x* + *b* or *P x~k~*~+1~ = *P x* + *r* or
> *x*~k+1~ = *x* + *P* ^−1^*r .* (1)
>
> In describing Krylov subspaces, I should work with *P* ^−1^*A*. For
> simplicity I will only write *A* ! I am assuming that *P* has been
> chosen and used, and the precondi-tioned equation *P* ^−1^*Ax* = *P*
> ^−1^*b* is given the notation *Ax* = *b*. The preconditioner is now
> *P* = *I*. Our new *A* is probably better than the original matrix
> with that name.
>
> With *x*~1~ = *b*, look ﬁrst at two steps of the pure iteration
> *x~j~*~+1~ = (*I* − *A*)*x~j~* + *b*: *x*~2~ = (*I* − *A*)*b* + *b* =
> 2*b* − *Ab x*~3~ = (*I* − *A*)*x*~1~ + *b* = 3*b* − 3*Ab* + *A*^2^*b.*
> (2)
>
> My point is simple but important: *x*~j~ *is a combination of b, Ab, .
> . . , A*^j−1^*b.*
>
> We can compute those vectors quickly, multiplying each time by a
> sparse *A*. Ev-ery iteration involves only one matrix-vector
> multiplication. Krylov gave a name to *all* combinations of those
> vectors, and he suggested that there might be better combinations than
> the particular choices *x~j~* in (2).
>
> Usually a diﬀerent combination will come closer to the desired *x* =
> *A*^−1^*b*.

### Krylov subspaces {#krylov-subspaces .unnumbered}

> The linear combinations of *b, Ab, . . . , A^j^*^−1^*b* form the *j*th
> Krylov subspace. This space depends on *A* and *b*. Following
> convention, I will write K~j~ for that subspace and K~j~ for the
> matrix with those basis vectors in its columns:
>
> Krylov matrix K~j~ Krylov subspace K
>
> = \[ *b Ab A*^2^*b . . . A*^j−1^*b* \] *.*
>
> = *all combinations of b, Ab, . . . , A*^j−1^*b*.

\(3\)

j

> Thus K~j~ is the column space of K~j~. We want to choose the *best
> combination* as our improved *x~j~* . Various deﬁnitions of "best"
> will give various *x~j~* . Here are four diﬀerent approaches to
> choosing a good *x~j~* in K~j~---this is the important decision:

1.  The residual *r~j~* = *b* − *Ax~j~* is orthogonal to K~j~ (Conjugate
    Gradients).

2.  The residual *r~j~* has minimum norm for *x~j~* in K~j~ (GMRES and
    MINRES).

3.  *r~j~* is orthogonal to a diﬀerent space K~j~(*A*^T^) (BiConjugate
    Gradients).

4.  The error *e~j~* has minimum norm (SYMMLQ).

> In every case we hope to compute the new *x~j~* quickly from the
> earlier *x*'s. If that step only involves *x~j~*~−1~ and *x~j~*~−2~
> (short recurrence) it is especially fast. Short recurrences happen for
> conjugate gradients and symmetric positive deﬁnite *A*. The BiCG
> method is a natural extension of short recurrences to unsymmetric *A*
> (using two Krylov spaces). A stabilized version called BiCGStab
> chooses *x~j~* in *A*^T^K~j~(*A*^T^).
>
> As always, computing *x~j~* can be very unstable until we choose a
> decent basis.

### Vandermonde Example {#vandermonde-example .unnumbered}

> To follow each step of orthogonalizing the basis, and solving *Ax* =
> *b* by conjugate gradients, we need a good example. It has to stay
> simple ! I am happy with this one:
>
> � 1 ⎡ � 1⎡ � 1⎡ � 1*/*1⎡

*A* = ��

> 3 ⎢⎣
>
> *b* = �� 1 ⎢⎣
>
> *Ab* = �� 3 ⎢⎣
>
> ~−1~ 1*/*2
>
> *A b* = � 1*/*3 ⎣ *.* (4)
>
> 4 1 4 1*/*4
>
> That constant vector *b* spans the Krylov subspace K~1~. Then *Ab*,
> *A*^2^*b*, and *A*^3^*b* are the other basis vectors in K~4~. They are
> the columns of K~4~, which we will name *V* :
>
> 1 1 1 1
>
> Vandermonde matrix K = *V* = 1 2 4 8 *.* (5)
>
> 1 3 9 27
>
> 1 4 16 64
>
> Those columns are constant, linear, quadratic, and cubic. The column
> vectors are independent but not at all orthogonal. The best measure of
> non-orthogonality starts by computing *inner products of the columns*
> in the matrix *V* ^T^*V* . When columns are orthonormal, their inner
> products are 0 or 1. (The matrix is called *Q*, and the inner products
> give *Q*^T^*Q* = *I*.) Here *V* ^T^*V* is far from the identity matrix
> !
>
> �

*V* ^T^*V* = ��

> 100 354
>
> 30 100 354 1300⎣
>
> 100 = 1^3^
>
> \+ 2^3^
>
> \+ 3^3^
>
> \+ 4^3^
>
> 100 354 1300 4890 1300 = 1^5^ + 2^5^ + 3^5^ + 4^5^
>
> The eigenvalues of this inner product matrix (*Gram matrix* ) tell us
> something im-portant. The extreme eigenvalues are *�*~max~ 5264 and
> *�*~min~ *.*004. Those are the squares of *α*~4~ and *α*~1~, the
> largest and smallest singular values of *V* . The key measure is their
> ratio *α*~4~*/α*~1~, the condition number of *V* :
>
> cond(*V* ^T^*V* ) 5264 10^6^

*.*004

> cond(*V* ) = *�*max

*�*min

> � 1000 *.*
>
> For such a small example, 1000 is a poor condition number. For an
> orthonormal basis with *Q*^T^*Q* = *I*, all eigenvalues = singular
> values = condition number = 1.
>
> We could improve the condition by rescaling the columns of *V* to unit
> vectors. Then *V* ^T^*V* has ones on the diagonal, and the condition
> number drops to 263. But when the matrix size is realistically large,
> that rescaling will not save us. In fact we could extend this
> Vandermonde model from constant, linear, quadratic, and cubic vectors
> to the functions 1*, x, x*^2^*, x*^3^. (*A* multiplies by *x*.) Please
> look at what happens !
>
> Continuous Vandermonde matrix *V~c~* = \[ 1 *x x*^2^ *x*^3^ \] *.* (6)
> Again, those four functions are far from orthogonal. The inner
> products in *V* ^T^*V~c~*

1, the integrals are

> 0

[1]{.underline} [1]{.underline} [1]{.underline} ⎡

> � ⎢
>
> Continuous inner products *Vc V~c~* = 1

�

> 1 *.* (7)
>
> ⎣
>
> The extreme eigenvalues of this Hilbert matrix are *�*~max~ � 1*.*5
> and *�*~min~ � 10^−4^. As always, those are the squares of the
> singular values *α*~max~ and *α*~min~ of *V~c~*. *The condition number
> of the power basis* 1*, x, x*^2^*, x*^3^ *is the ratio
> α*~max~*/α*~min~ 125. If you want a more impressive number (a
> numerical disaster), go up to *x*^9^. The condition number of the 10
> by 10 Hilbert matrix is *�*~max~*/�*~min~ � 10^13^, and 1*, x, . . . ,
> x*^9^ is a very poor basis.
>
> To reduce that unacceptably large number, Legendre orthogonalized the
> basis. He chose the interval from −1 to 1, so that even powers would
> be automatically orthogonal to odd powers. The ﬁrst *Legendre
> polynomials* are 1*, x, x*^2^ − [1]{.underline} *, x*^3^ −
> [3]{.underline} *x*.
>
> Our point is that the Vandermonde matrix example (as we follow it
> below) will be completely parallel to the famous functions of
> Legendre.
>
> In particular, the three-term recurrence in the Arnoldi-Lanczos
> orthogonal-ization is exactly like Legendre's classical three-term
> recurrence for his polynomials. They appear for the same reason---the
> symmetry of *A*.

### Orthogonalizing the Krylov Basis {#orthogonalizing-the-krylov-basis .unnumbered}

> The best basis *q*~1~*, . . . , q~j~* for the Krylov subspace K~j~ is
> orthonormal. Each new *q~j~* comes from orthogonalizing *t* =
> *Aq~j~*~−1~ to the basis vectors *q*~1~*, . . . , q~j~*~−1~ that are
> already chosen. The iteration to compute these orthonormal *q*'s is
> Arnoldi's method.
>
> This method is essentially the Gram-Schmidt idea (called *modiﬁed*
> Gram-Schmidt when we subtract the projections of *t* onto the *q*'s
> one at a time, for numerical

stability). We display one Arnoldi cycle for the Vandermonde example
that has

> �
>
> *b* = \[ 1 1 1 1 \] and *A* = diag(\[ 1 2 3 4 \]):
>
> *Arnoldi's orthogonalization of b, Ab, . . . , A*^n−1^*b*:

�

> 0 *q*~1~ = *b/*√*b*√; % Normalize *b* to √*q*~1~√ = 1 *q*~1~ = \[ 1 1
> 1 1 \] */*2
>
> for *j* = 1*, . . . , n* − 1 % Start computation of *q~j~*~+1~ �

1.  *t* = *Aq*~j~; % one matrix multiplication *Aq*~1~ = \[ 1 2 3 4 \]
    > */*2

> for *i* = 1*, . . . , j* % *t* is in the space K~j+1~

2.  *h*~ij~ = *q*^T^*t*; % *h~ij~q~i~* = projection of *t* on *q~i~
    > h*~11~ = 5*/*2

> *i* �

3.  *t* = *t* − *h~ij~q~i~*; % Subtract that projection *t* = \[ −3 −1 1
    > 3\] */*4

> end; % *t* is orthogonal to *q*~1~*, . . . , q~j~*

4.  *h*~j+1,j~ = √*t*√; % Compute the length of *t h*~21~ =

> �5*/*2
>
> ~�~ �

5.  *q*~j+1~ = *t/h~j~*~+1*,j*~; % Normalize *t* to √*q~j~*~+1~√ = 1
    > *q*~2~ = \[ −3 −1 1 3\] */* 20

> end % *q*~1~*, . . . , q~n~* are orthonormal
>
> You might like to see the four orthonormal vectors in the Vandermonde
> example. Those columns *q*~1~*, q*~2~*, q*~3~*, q*~4~ of *Q* are still
> constant, linear, quadratic, and cubic. I can also display the matrix
> *H* of numbers *h~ij~* that produced the *q*'s from the Krylov vectors
> *b, Ab, A*^2^*b, A*^3^*b*. (Since Arnoldi stops at *j* = *n* 1, the
> last column of *H* is not actually computed. It comes from a ﬁnal
> command *H*( : *, n*) = *Q* ^�^ *A Q*( : *, n*).) This *H* turns out
> to be *symmetric and tridiagonal*, and we will look for a reason.
>
> *Arnoldi's method for the Vandermonde example V gives Q and H*:
>
> � 1 −3 1 −1 ⎡ ��5*[/]{.underline}*2 �5*/*2 � ⎡
>
> *Q* = �� 1 −1 −1 3⎢⎣ *H* = ��

5*/*2 5*/*2

*.*80

*.*80

5[*/*2]{.underline}

> �*.*45⎢⎣
>
> 1 3 1 1
>
> 2 �20 2 �20
>
> *.*45 5*/*2
>
> Please notice that *H* is not upper triangular. The usual *QR*
> factorization of the original Krylov matrix K (which was *V* in our
> example) has this same *Q*, but Arnoldi does not compute *R*. Even
> though the underlying idea copies Gram-Schmidt (at every step
> *q~j~*~+1~ is a unit vector orthogonal to the previous *j* columns),
> there is a diﬀerence. The vector *t* that Arnoldi orthogonalizes
> against the previous *q*~1~*, . . . , q~j~* is *t* = *Aq~j~* . This is
> not column *j* + 1 of K, as in Gram-Schmidt. Arnoldi is factoring *AQ*
> !
>
> *Arnoldi factorization AQ* = *QH for the ﬁnal subspace* K~n~:
>
> � ⎡ � ⎡ � ⎡
>
> *AQ* = � *Aq*~1~
>
> · · ·
>
> *Aq~n~*
>
> ⎢ = � *q*1
>
> · · ·
>
> *qn* ⎢ �
>
> ⎢ *.* (8)
>
> � ⎣ � ⎣ � ⎣
>
> This matrix *H* is upper triangular plus one lower diagonal, which
> makes it "*upper Hessenberg*." The *h~ij~* in step 2 go down column
> *j* as far as the diagonal. Then
>
> *h~j~*~+1*,j*~ in step 4 is below the diagonal. We check that the ﬁrst
> column of *AQ* = *QH*
>
> (multiplying by columns) is Arnoldi's ﬁrst cycle that produces *q*~2~:
>
> Column 1 *Aq*~1~ = *h*~11~*q*~1~ + *h*~21~*q*~2~ which is *q*~2~ =
> (*Aq*~1~ − *h*~11~*q*~1~)*/h*~21~ *.* (9) That subtraction is step 3
> in Arnoldi's algorithm. The division by *h*~21~ is step 5.
>
> Unless more of the *h~ij~* are zero, the cost is increasing at every
> iteration. The vector updates in step 3 for *j* = 1*, . . . , n* − 1
> give nearly *n*^2^*/*2 updates and *n*^3^*/*2 ﬂops. A *short
> recurrence* means that most of these *h~ij~* are zero, and the count
> of ﬂoating point operations drops to *O*(*n*^2^). That happens when
> *A* = *A*^T^.

### Arnoldi Becomes Lanczos {#arnoldi-becomes-lanczos .unnumbered}

> The matrix *H* is symmetric and therefore tridiagonal when *A* is
> symmetric. This fact is the foundation of conjugate gradients. For a
> matrix proof, multiply *AQ* = *QH* by *Q*^T^. The left side *Q*^T^*AQ*
> is always symmetric when *A* is symmetric. Since *H* has only one
> lower diagonal, it has only one upper diagonal. This tridiagonal *H*
> has only three nonzeros in its rows and columns. So computing
> *q~j~*~+1~ only involves *q~j~* and *q~j~*~−1~:
>
> Arnoldi when *A* = *A*^T^ *Aq~j~* = *h~j~*~+1*,j*~ *q~j~*~+1~ +
> *h~j,j~ q~j~* + *h~j~*~−1*,j*~ *q~j~*~−1~ *.* (10) This is the
> *Lanczos iteration*. Each new *q~j~*~+1~ = (*Aq~j~* − *h~j,j~q~j~* −
> *h~j~*~−1*,j*~*q~j~*~−1~)*/h~j~*~+1*,j*~
>
> involves one multiplication *Aq~j~* , two dot products for *h*'s, and
> two vector updates.
>
> Allow me an important comment on the *symmetric eigenvalue problem Ax*
> = *�x*. We have seen that *H* = *Q*^T^*AQ* is tridiagonal, and *Q*^T^
> = *Q*^−1^ from the orthogonality *Q*^T^*Q* = *I*. The matrix *H* =
> *Q*^−1^*AQ* has the same eigenvalues as *A*:
>
> Same *� Hy* = *Q*^−1^*AQy* = *�y* gives *Ax* = *�x* with *x* = *Qy .*
> (11)
>
> It is much easier to ﬁnd the eigenvalues *�* for a tridiagonal *H*
> than for the original *A*.
>
> For a *large* symmetric matrix, we often stop the Arnoldi-Lanczos
> iteration at a tridiagonal *H~k~* with *k \< n*. The full *n*-step
> process to reach *H~n~* is too expensive, and often we don't need all
> *n* eigenvalues. So we compute the *k* eigenvalues of *H~k~* instead
> of the *n* eigenvalues of *H*. These computed *�*~1*k*~*, . . . ,
> �~kk~* (sometimes called Ritz values) can provide good approximations
> to the ﬁrst *k* eigenvalues of *A*. And we have an excellent start on
> the eigenvalue problem for *H~k~*~+1~, if we decide to take a further
> step.
>
> This Lanczos method will ﬁnd, approximately and iteratively and
> quickly, the leading eigenvalues of a large symmetric matrix. For its
> inner loop (the eigenvalues of the tridiagonal *H~k~*) we use the
> "*QR* method" described in section .

### The Conjugate Gradient Method {#the-conjugate-gradient-method .unnumbered}

> We return to iterative methods for *Ax* = *b*. The Arnoldi algorithm
> produced or-thonormal basis vectors *q*~1~*, q*~2~*, . . .* for the
> growing Krylov subspaces K~1~*,* K~2~*,* Now
>
> we select vectors *x~k~* in K~k~ that approach the exact solution to
> *Ax* = *b*.
>
> We concentrate on the *conjugate gradient method when A is symmetric
> positive deﬁnite*. Symmetry gives a short recurrence. Deﬁniteness
> prevents division by zero.
>
> The rule for *x~k~* in conjugate gradients is that the residual *r~k~*
> = *b Ax~k~* should be orthogonal to all vectors in K~k~. Since *r~k~*
> will be in K~k+1~, it must be a multiple of Arnoldi's next vector
> *q~k~*~+1~ ! Each residual is therefore orthogonal to all previous
> residuals (which are multiples of the previous *q*'s):
>
> Orthogonal residuals *r*^T^*r~k~* = 0 for *i \< k .* (12)
>
> The diﬀerence between *r~k~* and *q~k~*~+1~ is that the *q*'s are
> normalized, as in *q*~1~ = *b/*√*b*√.
>
> Similarly *r~k~*~−1~ is a multiple of *q~k~*. Then the diﬀerence *r~k~
> r~k~*~−1~ is orthogonal to each subspace K~i~ with *i \< k*. Certainly
> *x~i~ x~i~*~−1~ lies in that K~i~. So �*r* is orthogonal to earlier
> �*x*'s:
>
> (*x~i~* − *x~i~*~+1~)^T^(*r~k~* − *r~k~*~−1~) = 0 for *i \< k .* (13)
> These diﬀerences �*x* and �*r* are directly connected, because the
> *b*'s cancel in �*r*:
>
> *r~k~* − *r~k~*~−1~ = (*b* − *Ax~k~* ) − (*b* − *Ax~k~*~−1~) =
> −*A*(*x~k~* − *x~k~*~−1~) *.* (14) Substituting (14) into (13), *the
> updates* �*x are "A-orthogonal" or conjugate*: Conjugate directions
> (*x~i~* − *x~i~*~−1~)^T^*A*(*x~k~* − *x~k~*~−1~) = 0 for *i \< k .*
> (15)
>
> Now we have all the requirements. Each conjugate gradient step ends
> with a "search direction" *d~k~*~−1~ for the next update *x~k~* −
> *x~k~*~−1~. Steps 1 and 2 compute the correct multiple *�~k~d~k~*~−1~
> to move to *x~k~*. Using (14), step 3 ﬁnds the new *r~k~*. Steps 4 and
> 5 orthogonalize *r~k~* against the search direction just used, to ﬁnd
> the next *d~k~*.
>
> The constants *�~k~* in the search direction and *�~k~* in the update
> come from (12) and (13) for *i* = *k* −1. For symmetric *A*,
> orthogonality will be automatic for *i \< k* −1, as in Arnoldi. We
> have a "short recurrence" for the new *x~k~* and *r~k~*.
>
> Here is one cycle of the algorithm, starting from *x*~0~ = 0 and
> *r*~0~ = *b* and *d*~0~ = *r*~0~.
>
> Steps 1 and 3 involve the same matrix-vector multiplication *Ad*.
>
> Conjugate Gradient Method for Symmetric Positive Deﬁnite *A*
>
> Example: *A* = diag(\[ 1 2 3 4 \]) and *b* = \[ 1 1 1 1 \]^�^

1.  *�*~k~ = *r*^T^

> *r~k~*~−1~*/d*^T^
>
> *Ad~k~*~−1~ % Step length to next *x~k~ �*~1~ = 4*/*10 = 2*/*5

�

2.  *x*~k~ = *x~k~*~−1~ + *�~k~d~k~*~−1~ % Approximate solution *x*~1~ =
    > \[ 2 2 2 2 \] */*5

�

3.  *r*k = *rk*−1 − *�kAdk*−1

> \% New residual from (14)
>
> *r*~1~ = \[ 3 1
>
> −1 −3 \] */*5

4.  *�*~k~ = *r*^T^*r~k~/r*^T^

> *rk*−1
>
> \% Improvement this step
>
> *�*~1~ = 1*/*5
>
> *k k*−1 �

5.  *d*~k~ = *r~k~* + *�~k~d~k~*~−1~ % Next search direction *d*~1~ = \[
    > 4 2 0 −2 \] */*5

> The formulas for *�~k~* and *�~k~* are explained brieﬂy below---and
> fully by Trefethen-Bau \[--\] and Shewchuk \[--\] and many other good
> references.
>
> When there is a preconditioner *P* (to use even fewer CG steps for an
> accurate *x*), step 3 uses *P* ^−1^*A* and the inner products in steps
> 1 and 4 include an extra factor *P* ^−1^.

### Diﬀerent Viewpoints on Conjugate Gradients {#diﬀerent-viewpoints-on-conjugate-gradients .unnumbered}

> I want to describe the (same!) conjugate gradient method in two
> diﬀerent ways:

1.  It solves a tridiagonal system *Hy* = *f* recursively, for Arnoldi's
    *H*.

2.  It minimizes the energy ^[1]{.underline}^*x*^T^*Ax* − *x*^T^*b*
    recursively. This is important.

> How does *Ax* = *b* change to the tridiagonal *Hy* = *f* ? Those are
> connected by Arnoldi's orthonormal columns *q*~1~*, . . . , q~n~* in
> *Q*, with *Q*^T^ = *Q*^−1^ and *Q*^T^*AQ* = *H*:
>
> *Ax* = *b* is (*Q*^T^*AQ*)(*Q*^T^*x*) = *Q*^T^*b* which is *Hy* = *f*
> = (√*b*√*,* 0*, . . . ,* 0) *.* (16)
>
> Since *q*~1~ is *b/ b* , the ﬁrst component of *f* = *Q*^T^*b* is
> *q*^T^*b* = *b* . The other components of *f* are *q*^T^*b* = 0
> because *q~i~* is orthogonal to *q*~1~. The conjugate gradient method
> is implicitly computing the symmetric tridiagonal *H*. When the method
> ﬁnds *x~k~*, it also ﬁnds *y~k~* = *Q*^T^*x~k~* (but it doesn't say
> so). Here is the third step:
>
> Tridiagonal system *Hy* = *f*
>
> � *h*11 *h*12 ⎡ � ⎡ �√*b*√⎡
>
> Implicitly solved by CG *H*3*y*3 = *h*21 *h*22 *h*23 *y*3 = 0 *.* (17)
>
> *h*32 *h*33 0
>
> This is the equation *Ax* = *b projected by Q*~3~ onto the third
> Krylov subspace K~3~.
>
> These *h*'s never appear in conjugate gradients. We don't want to do
> Arnoldi too! It is the *LDL*^T^ factors of *H* that CG is somehow
> computing---two new numbers *�* and *�* at each step. Those give a
> fast update from *y~k~*~−1~ to *y~k~*. The iterates *x~k~* =
> *Q~k~y~k~* from conjugate gradients approach the exact solution *x~n~*
> = *Q~n~y~n~* which is *x* = *A*^−1^*b*.
>
> *Energy* By seeing conjugate gradients as an energy minimizing
> algorithm, we can extend it to nonlinear problems and use it in
> optimization. For our linear equation *Ax* = *b*, the energy is
> *E*(*x*) = ^[1]{.underline}^ *x*^T^*Ax* − *x*^T^*b*. Minimizing
> *E*(*x*) is the same as solving *Ax* = *b*, when *A* is positive
> deﬁnite---this was the main point of Section 1.6. The CG iteration
> minimizes *E*(*x*) on the growing Krylov subspaces.
>
> The ﬁrst subspace K~1~ is the line in the direction *d*~0~ = *r*~0~ =
> *b*. Minimization of the energy *E*(*x*) for the vectors *x* = *�b*
> produces the number *�*~1~:

1 2 T T

> *b*^T^*b*
>
> *E*(*�b*) =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} *� b*

2

> *Ab* − *�b*
>
> *b* is minimized at *�*~1~ = *b*T*Ab .* (18)

This *�*~1~ is the constant chosen in step 1 of the ﬁrst conjugate
gradient cycle.

> The gradient of *E*(*x*) = ^[1]{.underline}^*x*^T^*Ax* − *x*^T^*b* is
> exactly *Ax* − *b*. *The steepest descent*
>
> *direction at x*~1~ *is along the negative gradient, which is r*~1~ !
> This sounds like the perfect direction *d*~1~ for the next move. But
> the great diﬃculty with steepest descent is that this *r*~1~ can be
> too close to the ﬁrst direction *d*~0~. Little progress that way. So
> step 5 adds the right multiple *�*~1~*d*~0~, in order that the new
> *d*~1~ = *r*~1~ + *�*~1~*d*~0~ will be *A*-orthogonal to the ﬁrst
> direction *d*~0~.
>
> Then we move in this conjugate direction *d*~1~ to *x*~2~ = *x*~1~ +
> *�*~2~*d*~1~. This explains the name *conjugate gradients*. The pure
> gradients of steepest descent would be too nearly parallel, and we
> would take small steps across a valley instead of a good step to the
> bottom (the minimizing *x* in Figure 6.15). Every cycle of CG chooses
> *�~k~* to minimize *E*(*x*) in the new search direction *x* =
> *x~k~*~−1~ + *�d~k~*~−1~. The last cycle (if we go that far) gives the
> overall minimizer *x~n~* = *x* = *A*^−1^*b*.

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image68.png){width="2.2918449256342956in"
height="1.680472440944882in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image69.png){width="2.2918449256342956in"
height="1.680472440944882in"}

> Figure 6.14: Steepest descent vs. conjugate gradient.
>
> The main point is always this. When you have orthogonality, projection
> and minimizations can be computed one direction at a time.
>
> Example
>
> � 2 1 1 ⎡ � 3 ⎡ � 4 ⎡
>
> Suppose *Ax* = *b* is � 1 2 1 ⎣ � −1 ⎣ = � 0 ⎣ *.*
>
> 1 1 2 −1 0
>
> From *x*~0~ = (0*,* 0*,* 0) and *r*~0~ = *d*~0~ = *b* the ﬁrst cycle
> gives *�*~1~ = ^[1]{.underline}^ and *x*~1~ = ^[1]{.underline}^ *b* =
> (2*,* 0*,* 0).

The new residual is *r*~1~ = *b* − *Ax*~1~ = (0*,* −2*,* −2). Then the
CG algorithm yields

> [8]{.underline} � 2 ⎡ [8]{.underline}
>
> � 3 ⎡ −1
>
> *�*~1~ = 16 *d*~1~ = � −2 ⎣ *�*~2~ = 16 *x*~2~ = � −1 ⎣ = *A b* !
>
> −2 −1
>
> The correct solution is reached in two steps, where normally CG will
> take *n* = 3 steps. The reason is that this particular *A* has only
> two distinct eigenvalues 4 and 1. In that case *A*^−1^*b* is a
> combination of *b* and *Ab*, and this best combination *x*~2~ is found
> at cycle 2. The residual *r*~2~ is zero and the cycles stop
> early---very unusual.
>
> Energy minimization leads in \[ \] to an estimate of the converg�e[nce
> r]{.underline}ate for the

T

error *e* = *x* − *x~k~* in conjugate gradients, using the *A*-norm
√*e*√*~A~* = *e Ae*:

> ⎦�*�*max − �*�*min �*k*
>
> Error estimate √*x* − *x~k~*√*~A~* ≈ 2 � √*x* − *x*~0~√*~A~ .* (19)
>
> max + *�*min
>
> This is the best-known error estimate, although it doesn't account for
> any clustering of the eigenvalues of *A*. It involves only the
> condition number *�*~max~*/�*~min~. Prob-lem gives the "optimal" error
> estimate but it is not so easy to compute. That optimal estimate needs
> all the eigenvalues of *A*, while (19) uses the extreme eigenval-ues
> *�*~max~(*A*) and *�*~min~(*A*)---which in practice we can bound above
> and below.

### Minimum Residual Methods {#minimum-residual-methods .unnumbered}

> When *A* is not symmetric positive deﬁnite, CG is not guaranteed to
> solve *Ax* =
>
> *b*. We lose control of *d*^T^*Ad* in computing *�*. We will follow
> van der Vorst \[ \] in brieﬂy describing the *minimum norm residual*
> approach, leading to MINRES and GMRES.
>
> These methods choose *x~j~* in the Krylov subspace K~j~ so that *b
> Ax~j~* is minimal. The ﬁrst orthonormal vectors *q*~1~*, . . . , q~j~*
> go in the columns of *Q~j~* , so *Q*^T^*Q~j~* = *I*. As in (16) we set
> *x~j~* = *Q~j~y*, to express the solution as a combination of those
> *q*'s: using (8) is
>
> Norm of residual √*r~j~*√ = √*b* − *Ax~j~* √ = √*b* − *AQ~j~ y*√ =
> √*b* − *Q~j~*~+1~*H~j~*~+1*,j*~ *y*√*.* (20)
>
> Here I used the ﬁrst *j* columns of Arnoldi's formula *AQ* = *QH*.
> Since the *j*th column of *H* is zero after entry *j* + 1, we only
> need *j* + 1 columns of *Q* on the right side:

+----------------------------+---+----+-------+----+-----+----+------+
|                            |   |    | > �   | >  | *   | >  |      |
|                            |   |    | >     | ·. | h*1 |  ⎡ |      |
|                            |   |    | *h*11 | >  | *j* |    |      |
|                            |   |    |       |  · |     |    |      |
|                            |   |    |       | >  |     |    |      |
|                            |   |    |       |  · |     |    |      |
|                            |   |    |       | >  |     |    |      |
|                            |   |    |       | >  |     |    |      |
|                            |   |    |       |  . |     |    |      |
|                            |   |    |       | >  |     |    |      |
|                            |   |    |       |  . |     |    |      |
+============================+===+====+=======+====+=====+====+======+
| > First *j* columns of     |   |    |       |    | > . |    |      |
| > *QH* = ⎤ *q*~1~          |   |    |       |    | >   |    |      |
|                            |   |    |       |    | > . |    |      |
|                            |   |    |       |    | >   |    |      |
|                            |   |    |       |    | >   |    |      |
|                            |   |    |       |    |  *h |    |      |
|                            |   |    |       |    | jj* |    |      |
+----------------------------+---+----+-------+----+-----+----+------+
|                            | > | >  | > ⎥ � | >  |     | *  | > \( |
|                            |   | *q | >     |  . |     | .* | 21\) |
|                            | · | j* | *h*12 | >  |     |    |      |
|                            | > | +1 | >     |  . |     | >  |      |
|                            |   |    | > �   | >  |     | ⎢⎣ |      |
|                            | · |    |       |  . |     |    |      |
|                            | > |    |       |    |     |    |      |
|                            |   |    |       |    |     |    |      |
|                            | · |    |       |    |     |    |      |
+----------------------------+---+----+-------+----+-----+----+------+
|                            |   |    |       |    | > * |    |      |
|                            |   |    |       |    | hj* |    |      |
|                            |   |    |       |    | +1* |    |      |
|                            |   |    |       |    | ,j* |    |      |
+----------------------------+---+----+-------+----+-----+----+------+

> The norm in (20) is not changed when we multiply by *Q*^T^ . Our
> problem becomes:
>
> Choose *y* to minimize √*r~j~* √ = √*Q*^T^ *b* − *H~j~*~+1*,j*~ *y*√
> *.* (22)
>
> This is an ordinary least squares problem with only *j* + 1 equations
> and *j* unknowns.
>
> The right side *Q*^T^ *b* is (√*r*~0~√*,* 0*, . . . ,* 0) as in (16).
> The rectangular matrix *H~j~*~+1*,j*~ is
>
> Hessenberg in (21). We face a completely typical problem of numerical
> linear algebra:
>
> *Use zeros in H and Q*^T^ *b to ﬁnd a fast algorithm that computes y*.
> The two favorite
>
> algorithms for this least squares problem are closely related:
>
> MINRES *A* is symmetric (likely indeﬁnite, or we use CG) and *H* is
> tridiagonal.
>
> GMRES *A* is *not* symmetric and the upper triangular part of *H* can
> be full.
>
> In both cases we want to clear out that nonzero diagonal below the
> main diagonal of
>
> *H*. The natural way to do that, one entry at a time, is by "*Givens
> rotations*." These plane rotations are so useful and simple (the
> essential part is only 2 by 2) that we complete this section by
> explaining them.

### Givens Rotations {#givens-rotations .unnumbered}

> The direct approach to the least squares solution of *Hy* = *f*
> constructs the normal equations *H*^T^*Hy* = *H*^T^*f* . That was the
> central idea in Chapter 1, but you see what we lose. If *H* is
> Hessenberg, with many good zeros, *H* ^T^*H* is full. Those zeros in
> *H* should simplify and shorten the computations, so we don't want the
> normal equations.
>
> The other approach to least squares is by Gram-Schmidt. We factor *H*
> into orthogonal times upper triangular. Since the letter *Q* is
> already used, the or-thogonal matrix will be called *G* (after
> Givens). The upper triangular matrix is *G*^−1^*H*. The 3 by 2 case
> shows how a rotation in the 1--2 plane can clear out *h*~21~:
>
> −1 � cos *λ* sin *λ* 0 ⎡ � *h*~11~ *h*~12~ ⎡ � � � ⎡
>
> *G*21 *H* = �− sin *λ* cos *λ* 0 ⎣ � *h*~21~ *h*~22~ ⎣ = � 0 � ⎣ *.*
> (23)
>
> 0 0 1 0 *h*~32~ 0 �
>
> That bold zero entry requires *h*~11~ sin *λ* = *h*~21~ cos *λ*, which
> determines the rotation angle *λ*. A second rotation *G*^−1^, in the
> 2-3 plane, will zero out the 3*,* 2 entry. Then
>
> −1 −1
>
> *G*32 *G*21 *H* is a square upper triangular matrix *U* above a row of
> zeros!
>
> The Givens orthogonal matrix is *G*~21~*G*~32~ but there is no reason
> to do this multi-plication. We use each *G~ij~* as it is constructed,
> to simplify the least squares problem. Rotations (and all orthogonal
> matrices) leave the lengths of vectors unchanged:
>
> √*Hy* − *f* √ = √*G*^−1^*G*^−1^*Hy* − *G*^−1^*G*^−1^*f* √ = √ �*U* �
> *y* − �*F* � √ *.* (24)
>
> This length is what MINRES and GMRES minimize. The row of zeros below
> *U* means that the last entry *e* is the error---we can't reduce it.
> But we get all the other entries exactly right by solving the *j* by
> *j* system *Uy* = *F* (here *j* = 2). This gives the best least
> squares solution *y*. Going back to the original problem of minimizing
> the residual √*r*√ = √*b* − *Ax~j~* √, the best *x~j~* in the *j*th
> Krylov space is *Q~j~ y*.
>
> For non-symmetric *A* (GMRES rather than MINRES) the recurrence is not
> short. The upper triangle in *H* can be full, and *step j becomes
> expensive*. Possibly it is inaccurate as *j* increases. So we may
> change "full GMRES" to GMRES(*m*), which restarts the algorithm every
> *m* steps. It is not so easy to choose a good *m*. But GMRES is an
> important algorithm for unsymmetric *A*.

### Problem Set 6.4 {#problem-set-6.4 .unnumbered}

1.  When the tridiagonal *K* is preconditioned by *P* = *T* (second
    diﬀerence matrix with *T*~11~ = 1) show that *T* ^−1^*K* = *I* +
    *λe*^T^ with *e*^T^ = \[ 1 0 *. . .* 0 \]. Start from

> 1 1
>
> *K* = *T* + *e*~1~*e*^T^. Then *T* ^−1^*K* = *I* + (*T*
> ^−1^*e*~1~)*e*^T^. Verify that *T* ^−1^*e*~1~ = *β* from:
>
> 1

� 1 −1

> 1
>
> ⎡ � *N* ⎡ � 1 ⎡
>
> *T λ* = *e*1 = ��� −1 2 −1
>
> ⎢ � *N* −1 ⎢ = � 0 ⎢ *.*

−1 2 ⎣ �

> 1 ⎣ � 0 ⎣
>
> Second diﬀerences of this linear vector *β* are zero. Multiply *I* +
> *βe*^T^ times
>
> *I* − (*βe*^T^)*/*(*N* + 1) to establish that this is the inverse
> matrix *K* ^−1^*T* .

2.  For the model of a square grid with separator down the middle,
    create the reordered matrix *K* in equation (4). Use spy(*K*) to
    print its pattern of nonzeros.

3.  Arnoldi expresses each *Aq~j~* as *h~j~*~+1*,j*~*q~j~*~+1~ +
    *h~j,j~q~j~* + + *h*~1*,j*~*q*~1~. Multiply by *q*^T^ to ﬁnd
    *h~i,j~* = *q*^T^*Aq~j~* . *If A is symmetric* this is
    (*Aq~i~*)^T^*q~j~* . Explain why (*Aq~i~*)^T^*q~j~* = 0 for *i \< j*
    1 by expanding *Aq~i~* into *h~i~*~+1*,i*~*q~i~*~+1~ + +
    *h*~1*,i*~*q*~1~. We have a *short recurrence if A* = *A*^T^ (only
    *h~j~*~+1*,j*~ and *h~j,j~* and *h~j~*~−1*,j*~ are nonzero).

4.  (This is Problem 3 at the matrix level) The Arnoldi equation *AQ* =
    *QH* gives

> *H* = *Q*^−1^*AQ* = *Q*^T^*AQ*. Therefore the entries of *H* are
> *h~ij~* = *q*^T^*Aq~j~* .

(a) Which Krylov space contains *Aq~j~* ? What orthogonality gives
    > *h~ij~* = 0 when

> *i \> j* + 1 ? Then *H* is upper Hessenberg.

(b) If *A*^T^ = *A* then *h~ij~* = (*Aq~i~*)^T^*q~j~* . Which Krylov
    space contains *Aq~i~* ? What orthogonality gives *h~ij~* = 0 when
    *j \> i* + 1 ? Now *H* is tridiagonal.

```{=html}
<!-- -->
```
5.  Test the pcg(*A,* ) MATLAB command on the 1*,* 2*,* 1 second
    diﬀerence matrix *A* = *K*. As preconditioner use *P* = *T* , when
    *T*~11~ = 1.

6.  If *K* = \[ *b Ab . . . A^n^*^−1^*b* \] is a Krylov matrix with *A*
    = *A*^T^, why is the inner product matrix *K*^T^*K* a Hankel matrix
    ? This means constant entries down each *antidiagonal* (the opposite
    of Toeplitz). Show that (*K* ^T^*K*)*~ij~* depends on *i* + *j*.

7.  These are famous names associated with linear algebra (and a lot of
    other mathematics too). All dead. Write one sentence on what they
    are known for.

+--------------+---------------------+---------------+-----------------+
| > Arnoldi    | > Gram              | > Jacobi      | > Schur         |
+==============+=====================+===============+=================+
| > Cholesky   | > Hadamard          | > Jordan      | > Schwartz      |
+--------------+---------------------+---------------+-----------------+
| > Fourier    | > Hankel            | > Kronecker   | > Seidel        |
+--------------+---------------------+---------------+-----------------+
| > Frobenius  | > Hessenberg        | > Krylov      | > Toeplitz      |
+--------------+---------------------+---------------+-----------------+
| > Gauss      | > Hestenes-Stiefel  | > Lanczos     | > Vandermonde   |
+--------------+---------------------+---------------+-----------------+
| > Gershgorin | > Hilbert           | > Markov      | > Wilkinson     |
+--------------+---------------------+---------------+-----------------+
| > Givens     | > Householder       | > Schmidt     | > Woodbury      |
+--------------+---------------------+---------------+-----------------+

> solution: Jacobi (matrices), Gauss (elimination, numerical
> integration), Lanczos \[-1,2,-1 with q_1=(1,0,-)\], zeros of
> cosines/convergence rate?, Another q_1? Berresford.

# The Saddle Point Stokes Problem

> So far the matrix *C* has been diagonal---no trouble to invert. This
> section jumps to a ﬂuid ﬂow problem that is still linear (simpler than
> Navier-Stokes). But now *C* ^−1^ represents the positive deﬁnite
> Laplacian (−�) in the continuous problem, and it is a ﬁnite diﬀerence
> or ﬁnite element discretization in the matrix problem. The matrix
> *C*^−1^ is sparse, but *C* itself involves a serious boundary value
> problem.
>
> In this case we don't reduce the computation all the way to
> *A*^T^*CA*! Instead we stay with the sparse matrix whose blocks are
> *C*^−1^, *A*, *A*^T^, and 0. This is an *indeﬁnite* matrix, with that
> zero block on its diagonal. The solution *v, p* is a *saddle point*.
>
> This section also discusses the preconditioning of indeﬁnite systems
> (not only Stokes).

### The Stokes Problem {#the-stokes-problem .unnumbered}

> The unknowns in the two-dimensional Stokes problem are the velocity
> components in *v* = (*v*~1~(*x, y*)*, v*~2~(*x, y*)) and the pressure
> *p*(*x, y*). The ﬂow is *incompressible* so the velocity vector is
> constrained by div *v* = 0. Therefore *A*^T^ is (minus) the divergence
> and *A* must be the gradient. Notice the diﬀerent letters in our
> framework (*u* is changed to *p*, *w* is changed to *v*, and *b* is
> changed to *f* ):

pressure *p*(*x, y*) div *v* = 0

> *A* = gradient
>
> � *v* = *Ce*
>
> *e* = *f* − grad *p*
>
> *A*^T^ = −divergence
>
> � velocity *v*(*x, y*)
>
> Figure 6.15: The three-step *A*^T^*CA* framework for the Stokes
> problem.
>
> The real novelty is in *e* = *C*^−1^*v* = (−�*v*~1~*,* −�*v*~2~). The
> Stokes problem asks us to ﬁnd a velocity vector *v* and a pressure *p*
> that solve −�*v* = *f* − grad *p* and div *v* = 0:
>
> *�*^2^*v*~1~
>
> − *�x*2 +
>
> *�*^2^*v*~2~
>
> − *�x*2 +

*�v*~1~

> *�*^2^*v*~1~
>
> *�y*2
>
> *�*^2^*v*~2~
>
> *�y*2
>
> *�v*~2~
>
> *[�p]{.underline}*
>
> \+ = *f*~1~(*x, y*)
>
> *�x*
>
> *[�p]{.underline}*
>
> \+ = *f*~2~(*x, y*)
>
> *�y*
>
> (1a)
>
> (1b)
>
> \+
>
> *�x �y*
>
> = 0 (1c)
>
> This describes slow viscous ﬂow. It is not for aeronautics! The full
> Navier-Stokes equations have extra nonlinear terms from the motion of
> the underlying ﬂuid. The Stokes problem could come into its own in
> biological applications, not for large-scale blood ﬂow in the heart
> but for small-scale movements in capillaries (or even in cells). This
> linear problem is simpler than Navier-Stokes, and needs to be
> understood ﬁrst. We keep it simple by omitting discussion of the
> boundary conditions.
>
> In the language of optimization, the pressure *p*(*x, y*) is the
> Lagrange multiplier that imposes the incompressibility constraint div
> *v* = 0 when the energy is minimized: Minimize �� �\| grad *v*~1~\|2 +
> \| grad *v*~2~\|2 − 2*f* · grad *v*� *dx dy* subject to div *v* = 0
> *.*
>
> The Lagrangian *L*(*v, p*) adds *λL/λv* = 0 and *λL/λp* = 0 are
> exactly the Stokes equations (1). Chapter 6 will develop this
> primal-dual block form to ﬁnd the saddle point of *L*---here we only
> need to know *A* and *C*.
>
> The key point is that we do not eliminate *v* to reach *K* =
> *A*^T^*CA*, because *C* is *the inverse of the Laplacian*. It is
> diagonal only in frequency space, not in physical *x, y* space. The
> Stokes problem stays in its block form (1) with two unknowns *v* and
> *p*:
>
> Block form (continuous) *A*T 0 *p* = − div 0 *p* = 0 *.* (2)
>
> In the discrete case, that block matrix will be symmetric but
> *indeﬁnite* (as usual). It will have positive and also negative
> eigenvalues and pivots (positive pivots from *C*^−1^, negative pivots
> from *A*^T^*CA*). Finite elements for velocity *v* and pressure *p*
> have to be carefully matched to ensure that the discrete problem has a
> good solution. The approximating polynomials are often *one degree
> higher* for *v* than for *p*.

### The Inf-Sup Condition {#the-inf-sup-condition .unnumbered}

> Restricting a positive deﬁnite operator *K* to a subspace (by a
> projection *P* ) never destroys positive deﬁniteness. All eigenvalues
> of *P KP* ^T^ lie safely between *�*~min~(*K*) and *�*~max~(*K*). But
> an indeﬁnite operator has a *negative �*~min~, so this interval
> includes zero: not safe! We must take particular care that the block
> matrix is safely invertible.
>
> These mixed problems, or saddle point problems, are partly positive
> and partly negative. The new requirement for a bounded inverse is an
> *inf-sup condition* (also known as a Babuska-Brezzi condition): For
> every *p* there must be a *v* so
>
> that
>
> *v*^T^*Ap* √ *∂* �*v*T*C*−1*v p*T*p* for a ﬁxed *∂ \>* 0 *.* (3)
>
> This "compatibility" of velocities and pressures produces
> (*A*^T^*CA*)^−1^ 1*/∂*^2^.
>
> Condition (3) will immediately fail if there is a nonzero pressure *p*
> with *Ap* = 0. In the discrete case, this means that *A* must have
> full column rank. Otherwise the
>
> last columns of the block matrix in (2) are not independent, and the
> block matrix is not invertible. In particular, the rectangular *A*
> cannot be short and wide.
>
> More exactly, the lower bound (3) on *v*^T^*Ap* requires that a
> nonzero pressure *p* may not be orthogonal to every *A*^T^*v*. The
> space of all *A*^T^*v*'s must have *at least* the dimension of the
> space of *p*'s. Thinking of *A*^T^ as divergence, this indicates why
> the velocity ﬁnite elements are often one polynomial degree above the
> pressure ﬁnite elements. But dimensions of spaces are not suﬃcient to
> conﬁrm that (3) is actually true. Each choice of ﬁnite elements for
> *v* and *p* requires its own analysis.
>
> Now we explain the highlighted statement after equation (3):
> *A*^T^*CA* is bounded
>
> below by *∂*^2^ and ≥(*A*^T^*CA*)^−1^≥ ≈ 1*/∂*^2^ when the inf-sup
> condition holds. Begin by
>
> introducing *w* = *C*^−1*/*2^*v*. The continuous and discrete
> Laplacians, both called *C*^−1^, have positive deﬁnite square roots
> *C*^−1*/*2^ (never to be computed). Then (3) reads:
>
> *w*T*C*1*/*2*Ap*
>
> For every *p* there must be a *w* so that √ *∂*≥*p*≥ *.* (4)
>
> ≥*w*≥
>
> This is where we take the maximum over all *w* (the *sup*). On the
> left, the maximum of *w*^T^*z/*≥*w*≥ is exactly ≥*z*≥. This is
> attained when *w* = *z* (then the cosine is one).

+---------------------------------+---+----------------------+--------+
| > Since (4) has *z* =           |   |                      |        |
| > *C*^1*/*2^*Ap*, this best     |   |                      |        |
| > choice of *w* reduces (3) to  |   |                      |        |
+=================================+===+======================+========+
| > 1*/*2                         |   |                      | \(5\)  |
| >                               |   |                      |        |
| > For every *p,* ≥*z*≥ = ≥*C    |   |                      |        |
| > Ap*≥ √ *∂*≥*p*≥ *.*           |   |                      |        |
+---------------------------------+---+----------------------+--------+
| > Square both sides, and        |   |                      |        |
| > minimize their ratio over all |   |                      |        |
| > *p* (the *inf* ). The         |   |                      |        |
| > inequality                    |   |                      |        |
+---------------------------------+---+----------------------+--------+
| > 1*/*2 2 2 2                   | > | > *p*^T^*A*^T^*CAp*  | \(6\)  |
| >                               |   | > √ *∂*^2^*p*^T^*p*  |        |
| > ≥*C Ap*≥ √ *∂* ≥*p*≥          | o |                      |        |
|                                 | r |                      |        |
+---------------------------------+---+----------------------+--------+

> is tightest at the lowest eigenvector and eigenvalue, where
> *A*^T^*CAp* = *∂*^2^*p*. The largest eigenvalue of (*A*^T^*CA*)^−1^ is
> 1*/∂*^2^. The matrix is symmetric so its norm is also 1*/∂*^2^.
>
> A key goal in replacing (*A*^T^*CA*)^−1^ 1*/∂*^2^ by the inf-sup
> condition is to work with *C*^−1^ and not *C*. We can apply (3) to the
> continuous problem (it holds, so Stokes is well-posed). We can also
> test (3) on subspaces *V~h~* and *P~h~* of ﬁnite element trial
> functions. It is a *compatibility condition*: for every pressure
> *p~h~* in *P~h~*, there must be a velocity *v~h~* in *V~h~* satisfying
> (3). If and when this is established, with a bound *∂~h~* that stays
> away from zero, the mixed ﬁnite element method will be stable.
>
> *Correction to p*^T^*p*: Finite elements are functions *p~h~*(*x, y*),
> not just vectors *v* and
>
> *p*. So inner products and norms of *v~h~* and *p~h~* come from
> integrals and not sums. The *L*^2^ norm of a pressure trial function
> *p~h~* = *p~j~ α~j~*(*x, y*) is connected to the discrete coeﬃcient
> vector *p* through a positive deﬁnite "pressure mass matrix" *Q*:
>
> ≥*p~h~*≥ = �� (*p~h~*) *dx dy* = *p~i~p~j~* �� *α~i~α~j~ dx dy* = *p
> Qp .* (7)
>
> The correct inf-sup condition (3) changes *p*^T^*p* to *p*^T^*Qp*.
> When satisﬁed for the ﬁnite elements 3*,* 5*,* 8 in the list below,
> the inequality (6) involves *p*^T^*Qp*:
>
> Correction to (6) *p*^T^*A*^T^*CAp* √ *∂*^2^*p*^T^*Qp* (8)
>
> This makes *Q* (or even its diagonal part) a simple and useful
> candidate as precondi-tioner. Not the best, but it is directly
> available and it scales the problem correctly.

### Testing the Inf-Sup Condition {#testing-the-inf-sup-condition .unnumbered}

> The inf-sup condition can be delicate. The books by Brezzi-Fortin and
> Elman-Silvester-Wathen are excellent references. From the latter book
> we report on typical results, writing *P*~0~*, P*~1~*, P*~2~ for
> constant, linear, and quadratic polynomials on triangles, and *Q*~0~*,
> Q*~1~*, Q*~2~ for constant, bilinear, and biquadratic elements on
> quadrilaterals:

1.  Velocities in *P*~1~, pressures in *P*~0~: failure

2.  Velocities in *P*~1~, pressures in *P*~1~: failure

3.  Velocities in *P*~2~, pressures in *P*~1~: success

4.  Velocities in *Q*~1~, pressures in *Q*~1~: failure

5.  ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
    > height="0.17701771653543308in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
    > height="0.17701771653543308in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701662292213474in"
    > height="0.17701771653543308in"}Velocities in *Q*~2~, pressures in
    > *Q*~1~: success (Figure 6.17)

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
height="0.17701771653543308in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
height="0.17701771653543308in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
height="0.17701662292213474in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
height="0.17701662292213474in"}

> Figure 6.16: *Q*~2~ velocities • and *Q*~1~ pressures ≤: failure on
> one square, success on two.
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
> height="0.17701662292213474in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701771653543308in"
> height="0.17701662292213474in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image70.png){width="0.17701662292213474in"
> height="0.17701662292213474in"}For *Q*~2~ *Q*~1~ on one square, *A* is
> 2 by 4 (four pressures, two equations div *v* = 0 at the center).
> There will surely be non-constant solutions to *Ap* = 0: failure.
>
> For two squares, *A* is 6 by 6 (six pressures, div *v* = 0 at three
> internal nodes). Only a constant pressure solves *Ap* = 0, and this
> *hydrostatic solution* is removed by the boundary conditions (like
> grounding a node, here a better choice would be *p dx dy* = 0). A
> related "serendipity" element is also successful, by removing the
>
> node inside the square and the *x*^2^*y*^2^ term in the velocities.
> That leaves 8 nodes matching 8 terms in the polynomial.
>
> The list of element pairs also includes pressures *P*~−1~ and *Q*~−1~
> that are *not contin-uous* between elements (this is permitted since
> delta functions don't appear):

6.  Velocities in *P*~2~, pressures in *P*~−1~: failure

7.  Velocities in *Q*~2~, pressures in *Q*~−1~: failure

8.  Velocities in *Q*~2~, pressures in *P*~−1~: success

9.  Velocities in *Q*~1~, pressures in *Q*~0~: failure (Figure 6.18)

> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image71.png){width="0.21902121609798775in"
> height="0.21902121609798775in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image71.png){width="0.21902121609798775in"
> height="0.21902121609798775in"}In each square
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image71.png){width="0.21902121609798775in"
> height="0.21902121609798775in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image71.png){width="0.21902121609798775in"
> height="0.21902121609798775in"}*v* = *a* + *bx* + *cy* + *dxy* in
> *Q*~1~ *p* = *constant* in *Q*~0~
>
> Figure 6.17: Bilinear velocities , mode).
>
> constant pressures ≤ (unstable checkerboard
>
> The failure of *Q*~1~ *Q*~0~ is especially important. *Q*~0~ means a
> constant pressure in each square. This is the simplest pair of
> elements that are *conforming* (no delta functions in grad *v* because
> *Q*~1~ elements *a* + *bx* + *cy* + *dxy* are continuous across
> edges).

Four squares are not stable because that pressure vector *p* = (1*,*
1*,* 1*,* 1) satisﬁes

*Ap* = 0. More squares don't help---this checkerboard pattern with
"white squares

> = 1" and "black squares = −1" continues to be a spurious mode
> satisfying *Ap* = 0. The columns of *A*, even after *p* = constant is
> removed, are still not independent.
>
> This *Q*~1~ *Q*~0~ element is so simple and potentially useful that it
> is often *stabilized* by relaxing the incompressibility equation
> *A*^T^*v* = 0. We insert a new anti-checkerboard matrix −*�E*, exactly
> chosen to eliminate (1*,* −1*,* 1*,* −1) from the nullspace!
>
> � −1 ⎤ �� 1 −1 1 −1 ⎡⎢
>
> Stabilized The block matrix becomes *C A* with *E* = �−1 1 −1 1 ⎢ *.*

*A*^T^ −*�E*

> � 1 −1 1 −1 ⎣
>
> Our zero block is replaced by the negative semideﬁnite matrix −*�E*.
> Elimination leaves −*A*^T^*CA* − *�E* in that block, which is more
> strongly negative. The *Q*~1~ − *Q*~0~ construction is now uniformly
> invertible, since *E* times the checkerboard *p* is not zero.
>
> In this special case we know the guilty *p*. In other cases *E* is
> constructed with only the constant pressure in its nullspace (which
> isn't harmful). The new *�E* is taken small enough so that its
> positive eigenvalues roughly match those of *A*^T^*CA*. The zero
> eigenvalue of *A*^T^*CA* (produced by the checkerboard pressure)
> becomes positive.

### Solving the Discrete Saddle Point Problem {#solving-the-discrete-saddle-point-problem .unnumbered}

> Don't forget that this is the fundamental problem of scientiﬁc
> computing!
>
> �*C*−1 *A* ⎤ �*w* ⎤ � *b* ⎤
>
> In this section, *w* has become *v* and *u* is *p*. In earlier
> sections, when *C* was a diagonal matrix (small-block diagonal, in a
> multidimensional problem), the reduction to *A*^T^*CA* was very
> reasonable. Now the Stokes problem illustrates that *C* ^−1^ can be
> sparse (coming from ﬁnite diﬀerences or ﬁnite elements) while *C* is
> full. In that case
>
> we may prefer to compute with the sparse block form, even though its
> matrix is not at all positive deﬁnite like *A*^T^*CA*.
>
> A direct method (elimination) is appropriate up to *n* = 10^4^ or
> 10^5^. It will be used in most problems! Of course an indeﬁnite matrix
> may require row exchanges to avoid small pivots. A good code will
> decide that without our intervention.
>
> The pivoting can be organized using 2 by 2 blocks, or we may reorder
> the unknowns as in Section to keep the *L* and *U* factors as sparse
> as possible. If we eliminate in the original order, subtracting
> *A*^T^*C* times one block row from the other, then
>
> T
>
> −*K* = −*A CA* will appear as the Schur complement in the lower right
> block.
>
> For very large systems, a direct method demands too much computation
> (and memory). We'll look brieﬂy at iterative methods, remembering that
> the conjugate gradient method expects positive deﬁniteness. It could
> be used with *A*^T^*CA*, but it is not safe for the indeﬁnite problem.
> Each CG step applies *A*^T^*CA* (possibly preconditioned) to a vector.
> The matrix-vector multiplications *Ap* and *A*^T^*v* are fast. In
> between, multiplying by *C* amounts to solving the system *C* ^−1^*v*
> = *Ap*. In practice this will be two linear systems for the velocity
> components *v*~1~ and *v*~2~, with the same Laplace matrix---two
> "Poisson solves" at each step. This is not impossible but some inner
> iteration like multigrid is likely to be used.
>
> A number of iterative methods compute both *v* and *p*, based on the
> block form:

1.  The Uzawa method has *C*^−1^*v^k^*^+1^ = *f* − *Ap^k^* and
    > *p^k^*^+1^ = *p^k^* + *�A*^T^*v^k^*^+1^

2.  Penalty methods are described in Chapter on optimization

3.  The augmented Lagrangian method is presented in detail by
    > Glowinski-Le Tallec.

> These and more are discussed by Quarteroni-Valli for the Stokes
> problem. They all involve the "Poisson solve" associated with *C*. We
> turn instead to a closer look at *preconditioners for the general
> saddle point problem*, whether it arises in ﬂuid ﬂow or optimization
> or network analysis or elsewhere.

### Preconditioning Saddle Point Problems {#preconditioning-saddle-point-problems .unnumbered}

> The basic methods for large sparse indeﬁnite problems are MINRES and
> GMRES (symmetric and nonsymmetric). Our focus here is on constructing
> a good precondi-tioner.
>
> When we only know the matrix entries in *C*^−1^ and *A*, the code will
> have to construct a good preconditioner "blindly" from that
> information. Recall the funda-mental dividing line mentioned in the
> preface, to be *given a matrix or given a problem*. When we know the
> underlying problem (like Stokes), we can devise a preconditioner by
> hand. There is a similar separation between algebraic multigrid and
> geometric multigrid (the computer thinks or we do).
>
> Look ﬁrst at the saddle point matrix *M* and its block factorization
> *M* = *LDL*^T^:
>
> *M* = *A*^T^ 0 = *A*^T^*C I* 0 −*A*^T^*CA* 0 *I .* (10)
>
> *m n m n m n m n*
>
> *M*^−1^ clearly involves *C* and (*A*^T^*CA*)^−1^ from the inverse of
> that middle matrix. Our preconditioners will keep this *m, n* block
> structure. To come close to *M* ^−1^, as precon-ditioners are intended
> to do, we could approximate the blocks of *M* and invert or we could
> directly approximate *C* and (*A*^T^*CA*)^−1^.
>
> Three approximations to *M* are suggested by Elman-Silvester-Wathen:
>
> � *C*�−1 *A*⎤ ⎥*C*�−1 0 ⎦ ⎥*C*�−1 *A* ⎦
>
> Preconditioners *P*~1~ = *A*T
>
> *P*~2~ = *P*~3~ =
>
> 0 0 *K*
>
> 0 *K*�
>
> The matrix *A* (often relatively simple) is kept unchanged. *C*�
> approximates the Poisson
>
> A key point about *P*~2~ and *P*~3~: If *C*� = *C* and *K*� = *K*,
> then *P*2 *M* has only *three*
>
> diﬀerent eigenvalues and *P* ^−1^*M* has only the eigenvalue *�* = 1.
> In this case. In that case MINRES and GMRES converge in three or two
> steps. So those changes from *P*~1~ add very few iterations. Wathen
> begins with simple suggestions for the preconditioner *P* −1:

1.  Replace the Poisson solver *C* by a single multigrid cycle *C*

2.  Replace *K*^−1^ by four conjugate gradient steps preconditioned by
    > *Q* or diag(*Q*).

> The multigrid cycle applies a basic iteration on ﬁne and also coarse
> meshes, to reduce both high and low frequencies in the error residual
> (Section ). The matrix *Q* that preconditions *K* is the pressure mass
> matrix in (7). Its energy *p*^T^*Qp* gives a lower (and also upper)
> bound to *p*^T^*Kp*. Usually diag(*Q*) also has this "equispectral
> property", scaling the system correctly even if the approximation to
> *K* is not really close.
>
> *C*� and *K*� are deﬁned algorithmically by multigrid and
> preconditioned conjugate

### Nonsymmetric Problems and Model Reduction {#nonsymmetric-problems-and-model-reduction .unnumbered}

> We move now toward problems more general than Stokes. They might be
> associated with the Navier-Stokes equations (div *v* is still zero)
> and its linearizations. In that case *C* will be unsymmetric, from the
> ﬁrst derivative terms in the linearization. *Convection joins
> diﬀusion* (also in many problems from chemical engineering).
>
> A key point is the relative strength of those two terms, inertia
> versus viscosity. It is measured by the Reynolds number Re =
> (density)(velocity)(distance)/(viscosity).
>
> Stokes ﬂow is the limiting case Re = 0 for high viscosity and low
> velocity. The high speed Euler equation *dv/dt* = − grad *p* + *F* is
> at the other extreme Re � →.
>
> Beyond computational ﬂuid dynamics are other diﬀerential equations
> with their own constraints, and then all the algebraic problems of
> constrained optimization. Our discussion is moving from "given a
> problem" toward "given a matrix." The constraints make it a saddle
> point matrix---possibly unsymmetric, with *A*^T^ changed to *B*. We
> look to preconditioners of the same general forms, as a guide.
>
> Always the key is an approximate inverse to the *Schur complement*
> −*K* = −*BCA*:
>
> Elimination reduces *B* 0 to 0 −*BCA* = 0 −*K .* (11)
>
> Normally *K* will be dense. If it is also large, we look at iterative
> methods. Multigrid for *C* will become *algebraic multigrid*
> \[Briggs-McCormick-van Hensen\]. The approx-imation is constructed
> directly from the matrix, not using the diﬀerential equation that may
> be in the background.
>
> For *K* = *BCA*, a "black box" approach to preconditioning is
> suggested in \[ \]: Reduce *C* to a smaller model matrix *C*,
> satisfying
>
> *AC*˜ � *CA* and then *K* = *BAC* � *BCA.* (12)
>
> Notice that *C* is *m* by *m* (large) while *C* is *n* by *n*. The
> model reduction *CA* = *AC*
>
> will not be exactly solvable (more equations than unknowns). The
> meaning of � is to

*AC*� � *C A*, since the saddle point problem gives us *C* and not *C*.

### Advection-Diﬀusion Problems {#advection-diﬀusion-problems .unnumbered}

> The Stokes problem involves the Laplacian −�*v*. The corresponding
> matrix *C* ^−1^ is "essentially symmetric." Perfect symmetry holds in
> the interior and could only be lost at the boundary (it shouldn't be).
> Now, linearizing the *v* · grad *v* term in the Navier-Stokes equation
> produces a ﬁrst derivative "advection" term, and symmetry is deﬁnitely
> lost.
>
> Chapter 7
>
> Optimization and Minimum Principles

# Two Fundamental Examples

> Within the universe of applied mathematics, optimization is often a
> world of its own. There are occasional expeditions to other worlds
> (like diﬀerential equations), but mostly the life of optimizers is
> self-contained: *Find the minimum of F* (*x*~1~*, . . . , x*~n~)*.*
> That is not an easy problem, especially when there are many variables
> *x~j~* and many constraints on those variables. *Those constraints may
> require Ax* = *b or x~j~* √ 0 *or*
>
> *both or worse*. Whole books and courses and software packages are
> dedicated to this
>
> problem of *constrained minimization*.
>
> I hope you will forgive the poetry of worlds and universes. I am
> trying to emphasize the importance of optimization---a key component
> of engineering mathematics and scientiﬁc computing. This chapter will
> have its own ﬂavor, but it is strongly connected to the rest of this
> book. To make those connections, I want to begin with two speciﬁc
> examples. If you read even just this section, you will see the
> connections.

### Least Squares {#least-squares .unnumbered}

> Ordinary least squares begins with a matrix *A* whose *n* columns are
> independent. The rank is *n*, so *A*^T^*A* is symmetric positive
> deﬁnite. The input vector *b* has *m* components, the output *u* has
> *n* components, and *m \> n*:
>
> Then *e* is perpendicul�ar to columns 1*,* 2*, . . . , n* of *A*.
> Write those zero inner products
>
> �c 2006 Gilbert Strang
>
> as (column)^T^(*e*) = 0 to ﬁnd *A*^T^*Au* = *A*^T^*b*:
>
> � (column 1)^T^ ⎡ � �0⎡ *A*T*e* = 0
>
> � . ⎢⎣ � *e*⎡ = � . ⎢
>
> is *A*^T^(*b* − *Au*�) = 0
>
> \(2\)
>
> (column *n*)^T^ � ⎣ � . ⎣
>
> *A*^T^*Au* = *A*^T^*b .*
>
> Graphically, Figure 7.1 shows *Au* as the *projection of b*. It is the
> combination of columns of *A* (the point in the column space) that is
> nearest to *b*. We studied least squares in Section 2.3, and now we
> notice that a second problem is solved at the same time.
>
> This second problem (*dual problem*) does not project *b* down onto
> the column space. Instead it projects *b* across onto the
> perpendicular space. In the 3D picture, that space is a line (its
> dimension is 3 2 = 1). In *m* dimensions that perpendicular subspace
> has dimension *m n*. *It contains the vectors that are perpendicular
> to all columns of A*. The line in Figure 7.1 is the nullspace of
> *A*^T^.
>
> One of the vectors in that perpendicular space is *e* = projection of
> *b* ! Together, *e*
>
> and *u* solve the two linear equations that express exactly what the
> ﬁgure shows:
>
> We took this chance to write down three names for these very simple
> but so funda-mental equations. I can quickly say a few words about
> each name.
>
> Primal-Dual The primal problem is to minimize ∞*Au* − *b*∞2 . This
> produces *u*. The dual problem is to minimize ∞*w* − *b*∞2 , under the
> condition that *A*^T^*w* = 0. This produces *e*. We can't solve one
> problem without solving the other. They are solved
>
> together by equation (3), which ﬁnds the projections in both
> directions.
>
> Saddle Point The block matrix *S* in those equations is not positive
> deﬁnite !
>
> Saddle point matrix (4)
>
> The ﬁrst *m* pivots are all 1's, from the matrix *I*. When elimination
> puts zeros in place of *A*^T^, *it puts the negative deﬁnite*
> −*A*^T^*A into the zero block*.
>
> Multiply row 1 by *A*^T^ � *I* 0 � � *I A*� �*I A* �
>
> Subtract from row 2 −*A*^T^ *I A*^T^ 0 = 0 −*A*^T^*A .* (5)
>
> That elimination produced *A*^T^*A* in the (2*,* 2) block (the "Schur
> complement"). So the ﬁnal *n* pivots will all be negative. *S* is
> indeﬁnite, with pivots of both signs.
>
> *S* doesn't produce a pure minimum or maximum, positive or negative
> deﬁnite. It leads to a saddle point (*u*�*, e*). When we get up more
> courage, we will try to draw this.
>
> Kuhn-Tucker These are the names most often associated with equations
> like (3) that solve optimization problems. Because of an earlier
> Master's Thesis by Karush, you often see "KKT equations." In
> continuous problems, for functions instead of vectors, the right name
> would be "Euler-Lagrange equations." When the constraints include
> inequalities like *w* 0 or *Bu* = *d*, Lagrange multipliers are still
> the key. For those more delicate problems, Kuhn and Tucker earned
> their fame.
>
> Nullspace of *A*^T^ Nullspace of *A*^T^*C*

*e* = *b* − *Au*

*e b*

*Au* = *orthogonal*

projection of *b*

> replacements Column space of *A* = alrlevpelcatcoerms e*A*nt*u*s
>
> Figure 7.1: Ordinary and weighted least squares: min ∞*b* − *Au*∞2 and
> ∞*Wb* − *WAu*∞2 .

### Weighted Least Squares {#weighted-least-squares .unnumbered}

> This is a small but very important extension of the least squares
> problem. It involves the same rectangular *A*, and a square weighting
> matrix *W* . Instead of *u* we write *u~W~* (this best answer changes
> with *W* ). You will see that the symmetric positive deﬁnite
> combination *C* = *W* ^T^*W* is what matters in the end.
>
> No new mathematics, just replace *A* and *b* by *WA* and *Wb*. The
> equation has become
>
> *A*^T^*W* ^T^*WA u* ^T^ ^T^
>
> T T T
>
> �*~W~* = *A W Wb* or *A CA u*�*~W~* = *A Cb* or *A C*(*b*−*A u*�*~W~*
> ) = 0*.* (7)
>
> In the middle equation is that all-important matrix *A*^T^*CA*. In the
> last equation, *A*^T^*e* = 0 has changed to *A*^T^*Ce* = 0. When I
> made that change in Figure 7.1, I lost the 90^�^ angles. The line is
> no longer perpendicular to the plane, and the projections are no
> longer orthogonal. We are still splitting *b* into two pieces, *Au~W~*
> in the column space and *e in the nullspace of A*^T^*C*. The equations
> now include this *C* = *W* ^T^*W* :
>
> *e* is "*C*-orthogonal" *e* + *Au* = *b*
>
> to the columns of *A A*^T^
>
> *W*

*Ce* = 0

> \(8\)
>
> With a simple change, the equations (8) become symmetric ! Introduce
> *w* = *Ce*
>
> and *e* = *C*^−1^*w* and shorten *u*~W~ to *u*:
>
> This weighted saddle point matrix replaces *I* by *C*^−1^ (still
> symmetric):
>
> *C A m* rows
>
> Saddle point matrix *S* = *A*T 0 *n* rows
>
> Elimination produces *m* positive pivots from *C*^−1^, and *n*
> negative pivots from −*A*^T^*CA*:
>
> �*C*−1 *A*� �*w* � � *b* � �*C*−1 *A* � �*w* � � *b* �
>
> *A*^T^ 0 *u*
>
> = 0 �−−� 0 −*A*^T^*CA u*
>
> = −*A*^T^*Cb .*
>
> \(10\)
>
> The "Schur complement" that appears in the 2*,* 2 block becomes
> *A*^T^*CA*. We are back to *A*^T^*CAu* = *A*^T^*Cb* and all its
> applications.
>
> Two more steps will ﬁnish this overview of optimization. We show how a
> diﬀerent vector *f* can appear on the right side. The bigger step is
> also taken by our second example, coming now. *The dual problem (for w
> not u) has a constraint*. At ﬁrst it was *A*^T^*e* = 0, now it is
> *A*^T^*w* = 0, and in the example it will be *A*^T^*w* = *f* .
>
> *How do you minimize a function of e or w when these constraints are
> enforced* ? Lagrange showed the way, with his multipliers.

### Minimizing with Constraints {#minimizing-with-constraints .unnumbered}

> The second example is a line of *two springs and one mass*. The
> function to minimize is the energy in the springs. The constraint is
> the balance *A*^T^*w* = *f* between internal forces (in the springs)
> and the external force (on the mass). I believe you can see in Figure
> 7.2 the fundamental problem of constrained optimization. The forces
> are drawn as if both springs are stretched with forces *f \>* 0,
> pulling on the mass. Actually spring 2 will be compressed (*w*~2~ is
> negative).
>
> As I write those words---*spring*, *mass*, *energy*, *force
> balance*---I am desperately hoping that you won't just say "this is
> not my area." Changing the example to another area of science or
> engineering or economics would be easy, the problem stays the same in
> all languages.
>
> All of calculus trains us to minimize functions: Set the derivative to
> zero! But the basis calculus course doesn't deal properly with
> constraints. We are minimizing an energy function E(*w*~1~*, w*~2~),
> but we are constrained to stay on the line *w*~1~ − *w*~2~ = *f* .
>
> *What derivatives do we set to zero*?
>
> A direct approach is to solve the constraint equation. Replace *w*~2~
> by *w*~1~ *f* . That seems natural, but I want to advocate a diﬀerent
> approach (which leads to the same result). Instead of looking for
> *w*'s that satisfy the constraint, the idea of Lagrange is
>
> **\...\.....**
>
> **.**

spring 1 **. .**

**.**

> Internal energy in the springs
>
> �force *w*1 *E*(*w*) = *E*~1~(*w*~1~) + *E*~2~(*w*~2~)
>
> Balance of internal/external forces
>
> *w*~1~ − *w*~2~ = *f* (*the constraint* )
>
> external force
>
> **.** force *w*~2~
>
> **.**
>
> **.**
>
> Constrained optimization problem

spring 2

> **.**. **..** *Minimize E*(*w*) *subject to w*~1~
>
> **.**
>
> − *w*~2~ = *f*
>
> **.. .**
>
> Figure 7.2: Minimum spring energy *E*(*w*) subject to balance of
> forces.
>
> to *build the constraints into the function*. Rather than removing
> *w*~2~, we will add a new unknown *u*. It might seem surprising, but
> this second approach is better.
>
> With *n* constraints on *m* unknowns, Lagrange's method has *m*+*n*
> unknowns. The idea is to add a Lagrange multiplier for each
> constraint. (Books on optimization
>
> call this multiplier *�* or *�*, we will call it *u*.) Our Lagrange
> function *L* has the constraint *w*~1~ − *w*~2~ − *f* = 0 built in,
> and multiplied by −*u*:
>
> Calculus can operate on *L*, by setting derivatives (*three partial
> derivatives*!) to zero:
>
> Kuhn-Tucker
>
> Notice how the third equation *�L/�u* = 0 automatically brings back
> the constraint---because it was just multiplied by −*u*. If we add the
> ﬁrst two equations to eliminate *u*, and substitute *w*~1~ − *f* for
> *w*~2~, we are back to the direct approach with one unknown.
>
> But we don't want to eliminate *u*! That Lagrange multiplier is an
> important number with a meaning of its own. In this problem, *u* is
> the displacement of the mass. In economics, *u* is the selling price
> to maximize proﬁt. In all problems, *u* measures the sensitivity of
> the answer (the minimum energy *E*min) to a change in
>
> the constraint. We will see this sensitivity *dE*min*/df* in the
> linear case.

### Linear Case {#linear-case .unnumbered}

> The force in a linear spring is proportional to the elongation *e*, by
> Hooke's Law
>
> *w* = *ce*. Each small stretching step requires work =
> (force)(movement) = (*ce*)(�*e*).
>
> Then the integral ^1^*ce*^2^ that adds up those small steps gives the
> energy stored in the
>
> spring. We can express this energy in terms of *e* or *w*:
>
> 1 2 1 *w*^2^
>
> Energy in a spring *E*(*w*) =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image72.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"} *c e* =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image73.png){width="0.3016852580927384in"
> height="6.666666666666667e-3in"} *.* (12)
>
> 2 2 *c*
>
> Our problem is to minimize a quadratic energy *E*(*w*) subject to a
> linear balance
>
> equation *w*~1~ − *w*~2~ = *f* . This is the model problem of
> optimization.
>
> We want to solve this model problem by geometry and then by algebra.
>
> Geometry In the plane of *w*~1~ and *w*~2~, draw the line *w*~1~
> *w*~2~ = *f* . Then draw the ellipse *E*(*w*) = *E*~min~ that *just
> touches this line*. The line is tangent to the ellipse. A smaller
> ellipse from smaller forces *w*~1~ and *w*~2~ will not reach the
> line---those forces will not balance *f* . A larger ellipse will not
> give minimum energy. This ellipse touches the line at the point
> (*w*~1~*, w*~2~) that minimizes *E*(*w*).
>
> replacements
>
> *E*(*w*) = *E*min

(*w*~1~*, w*~2~)

*w*~1~ *\>* 0

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image74.png){width="2.9730752405949255in"
height="2.4556747594050745in"}tension in spring 1

> � 1 l and � *u* l perpendicular to
>
> *w*~2~ *\<* 0 compression in spring 2
>
> Figure 7.3: The ellipse *E*(*w*) = *E*~min~ touches *w*~1~ − *w*~2~ =
> *f* at the solution (*w*~1~*, w*~2~).
>
> At the touching point in Figure 7.3, the perpendiculars (1*,* 1) and
> (*u, u*) to the line and the ellipse are parallel. The perpendicular
> to the line is the vector (1*,* −1) from the partial derivatives of
> *w*~1~ − *w*~2~ − *f* . The perpendicular to the ellipse
>
> is (*�E/�w*~1~*, �E/�w*~2~), from the gradient of *E*(*w*). By the
> optimality equations (11a)
>
> and (11b), this is exactly (*u,* −*u*). Those parallel gradients at
> the solution are the algebraic statement that the line is tangent to
> the ellipse.
>
> Algebra To ﬁnd (*w*~1~*, w*~2~), start with the derivatives of
> *w*^2^*/*2 *c*~1~ and *w*^2^*/*2 *c*~2~:

1 2

> *�E w*~1~ *�E w*~2~
>
> Energy gradient = and = *.* (14)
>
> *�w*~1~ *c*~1~ *�w*~2~ *c*~2~
>
> Equations (11a) and (11b) in Lagrange's method become *w*~1~*/c*~1~ =
> *u* and *w*~2~*/c*~2~ = −*u*. Now the constraint *w*~1~ − *w*~2~ = *f*
> yields (*c*~1~ + *c*~2~)*u* = *f* (*both w*'s *are eliminated* ):
>
> Substitute *w*~1~ = *c*~1~*u* and *w*~2~ = −*c*~2~*u.* Then (*c*~1~ +
> *c*~2~)*u* = *f .* (15)
>
> I don't know if you recognize *c*~1~ + *c*~2~ as our stiﬀness matrix
> *A*^T^*CA* ! This problem is so small that you could easily miss *K* =
> *A*^T^*CA*. The matrix *A*^T^ in the constraint equation *A*^T^*w* =
> *w*~1~ − *w*~2~ = *f* is only 1 by 2, so *the stiﬀness matrix K is* 1
> *by* 1:
>
> *A*^T^ = ⎤1 −1⎥ and *K* = *A*^T^*CA* = ⎤1 −1⎥ �*c*1 � � 1� = ⎤*c*~1~ +
> *c*~2~ ⎥ *.* (16)
>
> The algebra of Lagrange's method has recovered *Ku* = *f* . Its
> solution is the movement *u* = *f/*(*c*~1~+*c*~2~) of the mass.
> Equation (15) eliminated *w*~1~ and *w*~2~ using (11a) and (11b). Now
> back substitution ﬁnds those energy-minimizing forces:
>
> Spring forces *w*~1~
>
> [*c*~1~*f *]{.underline}
>
> = *c*~1~*u* =
>
> and *w*~2~
>
> = −*c u* = [−*c*2*f *]{.underline} *.* (17)
>
> *c*~1~ + *c*~2~ *c*~1~ + *c*~2~
>
> Those forces (*w*~1~*, w*~2~) are on the ellipse of minimum energy
> *E*~min~, tangent to the line:

*E*(*w*) =

> 1 *w*^2^
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image75.png){width="0.3000174978127734in"
> height="6.666666666666667e-3in"} +
>
> 1 *w*^2^
>
> 1 *c*~1~*f* ^2^ 1 *c*~2~*f* ^2^ 1 *f* ^2^
>
> = + = = *E*~min~ *.* (18)
>
> 2 *c*~1~ 2 *c*~2~ 2 (*c*~1~ + *c*~2~)^2^ 2 (*c*~1~ + *c*~2~)^2^ 2
> *c*~1~ + *c*~2~
>
> This *E*~min~ must be the same minimum value ^1^ *f* ^T^*K*^−1^*f* as
> in Section . It is.
>
> We can directly verify the mysterious fact that *u* measures the
> sensitivity of *E*~min~
>
> to a small change in *f* . Compute the derivative *dE*~min~*/df* :
>
> *[d]{.underline}* 1 *f* ^2^ *[f]{.underline}*
>
> Lagrange multiplier = Sensitivity = = *u .* (19)
>
> *df* 2 *c*~1~ + *c*~2~ *c*~1~ + *c*~2~
>
> This sensitivity is linked to the observation in Figure 7.3 that one
> gradient is *u* times the other gradient. From (11a) and (11b), that
> stays true for nonlinear springs.

### A Speciﬁc Example {#a-speciﬁc-example .unnumbered}

> I want to insert *c*~1~ = *c*~2~ = 1 in this model problem, to see the
> saddle point of *L* more clearly. The Lagrange function with built-in
> constraint depends on *w*~1~ and *w*~2~ and *u*:
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.272747156605424e-2in"
> height="3.2283464566929135e-3in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.272747156605424e-2in"
> height="3.2283464566929135e-3in"}*L* = 1*w*^2^ + 1*w*^2^ − *uw*~1~ +
> *uw*~2~ + *uf .* (20)
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.272747156605424e-2in"
> height="3.2283464566929135e-3in"} 1
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.272747156605424e-2in"
> height="3.2283464566929135e-3in"} 2
>
> 2 2
>
> The equations *�L/�w*~1~ = 0 and *�L/�w*~2~ = 0 and *�L/�u* = 0
> produce a beautiful symmetric saddle-point matrix *S*:
>
> *�L/�w*~1~ = *w*~1~ − *u* = 0 � 1 0 −1 ⎡ � *w*~1~ ⎡ � 0 ⎡
>
> *�L/�u* = −*w*~1~ + *w*~2~ = *f* −1 1 0 *u f*
>
> Is this matrix *S* positive deﬁnite ? *No*. It is invertible, and its
> pivots are 1*,* 1*,* −2. That −2 destroys positive deﬁniteness---it
> means a saddle point:
>
> � 1 0 −1 ⎡ � 1 0 −1 ⎡ � 1 ⎡

Elimination � 0 1 1 ⎣ −� � 1 1 ⎣ with *L* = � 0 1 ⎣ *.*

> −1 1 0 −2 −1 1 1
>
> On a symmetric matrix, elimination equals "completing the square." The
> pivots 1*,* 1*,* −2 are outside the squares. The entries of *L* are
> inside the squares:
>
> [1]{.underline} *w*^2^ + [1]{.underline} *w*^2^ − *uw*~1~ + *uw*~2~ =
> [1]{.underline} ⎤1(*w*~1~ − *u*)^2^ + 1(*w*~2~ + *u*)^2^ − 2(*u*)^2^⎥
> *.* (22)
>
> The ﬁrst squares (*w*~1~ *u*)^2^ and (*w*~2~ + *u*)^2^ go "upwards,"
> but 2*u*^2^ goes down. This gives a saddle point SP = (*w*~1~*,
> w*~2~*, u*) in Figure 7.4.
>
> The eigenvalues of a symmetric matrix have the same signs as the
> pivots, and the same product (which is det *S* = −2). Here the
> eigenvalues are *�* = 1*,* 2*,* −1.

**. .**

> 2
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image76.png){width="8.102034120734908e-2in"
> height="8.102034120734908e-2in"}*L* = 2 \[(*w*~1~ − *u*) + (*w*~2~ +
> *u*) − 2*u* \] + *uf*

�

> Four dimensions make it a squeeze

[(*c*~1~*f,* −*c*~2~*f, f* )]{.underline}

> Saddle point SP = (*w*~1~*, w*~2~*, u*) =
>
> *c*~1~ + *c*~2~
>
> Figure 7.4: (*w*~1~−*u*)^2^ and (*w*~2~+*u*)^2^ go up, −2*u*^2^ goes
> down from the saddle point SP.

### The Fundamental Problem {#the-fundamental-problem .unnumbered}

> May I describe the full linear case with *w* = (*w*~1~*, . . . ,
> w~m~*) and *A*^T^*w* = (*f*~1~*, . . . , f~n~*) ? The problem is to
> minimize the total energy *E*(*w*) = ^1^ *w*^T^*C*^−1^*w* in the *m*
> springs. The *n* constraints *A*^T^*w* = *f* are built in by Lagrange
> multipliers *u*~1~*, . . . , u~n~*. Multiplying
>
> the force balance on the *k*th mass by −*u~k~* and adding, all *n*
> constraints are built into the dot product *u*^T^(*A*^T^*w* − *f* ).
> For mechanics, we use a minus sign in *L*:
>
> Lagrange function *L*(*w, u*) = [1]{.underline} *w*^T^*C*^−1^*w* −
> *u*^T^(*A*^T^*w* − *f* ) *.*
>
> \(23\)
>
> To ﬁnd the minimizing *w*, set the *m* + *n* ﬁrst partial derivatives
> of *L* to zero:
>
> Kuhn-Tucker *�L/�w* = *C*^−1^*w Au* = 0 (24a)
>
> optimality
>
> equations *�L/�u* = −*A*^T^*w* + *f* = 0 (24b)
>
> This is the main point, that Lagrange multipliers lead exactly to the
> linear equations *w* = *CAu* and *A*^T^*w* = *f* that we studied in
> the ﬁrst chapters of the book. By using *u* in the Lagrange function
> *L* and introducing *e* = *Au*, we have the plus signs that
>
> appeared for springs and masses:
>
> *e* = *Au w* = *Ce f* = *A*^T^*w* =≤ *A*^T^*CAu* = *f .*
>
> Important Least squares problems have *e* = *b* − *Au* (minus sign
> from voltage drops). Then we change to +*u* in *L*. The energy *E* =
> ^[1]{.underline}^*w*^T^*C*^−1^*w* − *b*^T^*w* now has a term involving
> *b*. When Lagrange sets derivatives of *L* to zero, he ﬁnds *S* !
>
> *�L/�w* = *C*^−1^*w* + *Au* − *b* = 0
>
> �*C*−1 *A* � �*w* � � *b* �

or

> *�L/�u* = *A*^T^*w* − *f* = 0
>
> *A*^T^ 0
>
> *u* = *f*
>
> . (25)
>
> This system is my top candidate for the fundamental problem of
> scientiﬁc computing.
>
> You could eliminate *w* = *C*(*b Au*) *but I don't know if you
> should*. If you do it,
>
> *K* = *A*^T^*CA* will appear. Usually this is a good plan:

### Duality and Saddle Points {#duality-and-saddle-points .unnumbered}

> We minimize the energy *E*(*w*) but we do *not* minimize Lagrange's
> function *L*(*w, u*). It is true that *�L/�w* and *�L/�u* are zero at
> the solution. But the matrix of second derivatives of *L* is not
> positive deﬁnite. The solution *w, u* is a saddle point. It is a
> minimum of *L* over *w*, and at the same time it is a maximum of *L*
> over *u*. A saddle point has something to do with a horse. . . It is
> like the lowest point in a mountain range, which is also the highest
> point as you go across.
>
> The *minimax theorem* states that we can minimize ﬁrst (over *w*) or
> maximize ﬁrst (over *u*). Either order leads to the unique saddle
> point, given by *�L/�w* = 0 and *�L/�u* = 0. The minimization removes
> *w* from the problem, and it corresponds exactly to eliminating *w*
> from the equations (11) for "ﬁrst derivatives = 0." Every step will be
> illustrated by examples (linear case ﬁrst).
>
> Allow me to use the *A, C, A*^T^ notation that we already know, so I
> can point out the fantastic idea of duality. The Lagrangian is *L*(*w,
> u*) = ^[1]{.underline}^*w*^T^*C*^−1^*w* − *u*^T^(*A*^T^*w* − *f* ),
> leaving out *b* for simplicity. We compare minimization ﬁrst and
> maximization ﬁrst:
>
> Minimize over *w �L/�w* = 0 when *C*^−1^*w* − *Au* = 0. Then *w* =
> *CAu* and
>
> *L* = − [1]{.underline} (*Au*)^T^*C*(*Au*) + *u*^T^*f* . This is to be
> maximized.
>
> Maximize over *u* Key point: *L*~max~ = +→ if *A*^T^*w* =≥ *f* .
> Minimizing over *w*
>
> will keep *A*^T^*w* = *f* to avoid that +→. Then *L* =
> ^[1]{.underline}^ *w*^T^*C*^−1^*w*.
>
> The maximum of a linear function like 5*u* is +→. But the maximum of
> 0*u* is 0.
>
> Now come the two second steps, maximize over *u* and minimize over
> *w*. Those are the dual problems. Often one problem is called the
> "primal" and the other is its "dual"---but they are reversible. Here
> are the two dual principles for linear springs:

1.  Choose *u* to maximize − [1]{.underline} (*Au*)^T^*C*(*Au*) +
    > *u*^T^*f* . Call this function −*P* (*u*).

2.  Choose *w* to minimize ^1^ *w*^T^*C*^−1^*w* keeping the force
    > balance *A*^T^*w* = *f* .

> Our original problem was 2. In the language of mechanics, we were
> minimizing the complementary energy *E*(*w*). Its dual problem is 1.
> This minimizes the potential energy *P* (*u*), by maximizing *P*
> (*u*). Most ﬁnite element systems choose that "dis-placement method."
> They work with *u* because it avoids the constraint *A*^T^*w* = *f* .
>
> The dual problems 1 and 2 involve the same inputs *A, C, f* but they
> look entirely diﬀerent. *Equality between minimax*(*L*) *and
> maximin*(*L*) *gives the duality principle and the saddle point* :
>
> Duality of 1 and 2 max ( *P* (*u*)) = min *E*(*w*) *.* (27)
>
> all *u A*T*w* = *f*
>
> That is the big theorem of optimization---the maximum of one problem
> equals the minimum of its dual. We can ﬁnd those numbers, and see that
> they are equal, because the derivatives are linear. Maximizing *P*
> (*u*) will minimize *P* (*u*), which is the problem we solved in
> Chapter 1. Write *u*^�^ and *w*^�^ for the minimizer and maximizer:

1.  *P* (*u*) = ^[1]{.underline}^ *u*^T^*A*^T^*CAu* − *u*^T^*f* is
    > *P*~min~ = − [1]{.underline} *f* ^T^(*A*^T^*CA*)^−1^*f* when
    > *u*^�^ = (*A*^T^*CA*)^−1^*f*

2.  *E*(*w*) = ^1^ *w*^T^*C*^−1^*w* is *E*~min~ = ^1^ *f*
    > ^T^(*A*^T^*CA*)^−1^*f* when *w*^�^ = *CAu*^�^.

> 2 2
>
> So *u*^�^ = *K*^−1^*f* and *w*^�^ = *CAu*^�^ give the saddle point
> (*w*^�^*, u*^�^) of *L*. This is where
>
> *E*min = −*P*min.

### Problem Set 7.1 {#problem-set-7.1 .unnumbered}

1.  Our model matrix *M* in (21) has eigenvalues *�*~1~ = 1*, �*~2~ =
    2*, �*~3~ = 1:

> �*C*−1 *A*� � 1 0 −1⎡
>
> *M* = *A*T 0 = � 0 1 1⎣
>
> −1 1 0
>
> The trace 1 + 1 + 0 down the diagonal of *M* equals the sum of *�*'s.
> Check that det *M* = product of *�*'s. Find eigenvectors *x*~1~*,
> x*~2~*, x*~3~ of unit length for those eigenvalues 1*,* 2*,* −1. The
> eigenvectors are orthogonal!

2.  The quadratic part of the Lagrangian *L*(*w*~1~*, w*~2~*, u*) comes
    > directly from *M*:

> 1 ⎤ ⎥ � 1 0 −1 ⎡ �*w*~1~ ⎡ 1 � 2 2 �

![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image72.png){width="8.167104111986001e-2in"
height="6.666666666666667e-3in"} *w*~1~ *w*~2~

2

> *u* � 0 1 1⎣ �*w*~2~ ⎣ = 2
>
> *w*1 + *w*2 − 2*uw*~1~ + 2*uw*~2~ *.*

−1 1 0 *u*

> Put the unit eigenvectors *x*~1~*, x*~2~*, x*~3~ inside the squares
> and *�* = 1*,* 2*,* −1 outside:
>
> *w*^2^ + *w*^2^ − 2*uw*~1~ + 2*uw*~2~ = 1( )^2^ + 2( )^2^ − 1( )^2^
> *.*
>
> The ﬁrst parentheses contain (1*w*~1~ − 1*w*~2~ + 0*w*~3~)*/*�2
> because *x*~1~ is (1*,* −1*,* 0)*/*�2. Compared with (22), these
> squares come from orthogonal eigenvector directions.
>
> We are using *A* = *Q*�*Q*^T^ instead of *A* = *LDL*^T^.

3.  *Weak duality* Half of the duality theorem is max *P* (*u*) min
    > *E*(*w*). This is surprisingly easy to prove. Show that *P* (*u*)
    > is *always smaller* than *E*(*w*), for every *u* and *w* with
    > *A*^T^*w* = *f* .

1 T

− 2 *u*

*A*^T^*CAu* + *u*^T^

> 1 T

*f* ← 2 *w C*

^−1^*w* whenever *A*^T^

*w* = *f .*

> Set *f* = *A*^T^*w*. Verify that (right side) − (left side) =
>
> *CAu*) √ 0.
>
> [1]{.underline} (*w* − *CAu*)^T^*C*^−1^(*w* −
>
> Equality holds and max( *P* ) = min(*E*) when *w* = *CAu*. That is
> equa-tion (11)!

4.  Suppose the lower spring in Figure 7.2 is not ﬁxed at the bottom. A
    > mass at that end adds a new force balance constraint *w*~2~ *f*~2~
    > = 0. Build the old and new constraints into the Lagrange function
    > *L*(*w*~1~*, w*~2~*, u*~1~*, u*~2~) to minimize the energy
    > *E*~1~(*w*~1~) + *E*~2~(*w*~2~). Write down *four equations* like
    > (11a)--(11c): partial derivatives of *L* are zero.

5.  For spring energies *E*~1~ = ^1^*w*^2^*/c*~1~ and *E*~2~ = ^1^
    > *w*^2^*/c*~2~, ﬁnd *A* in the block form

> 2 1 2 2
>
> *C*^−1^ *A w* 0 *w*~1~ *u*~1~ *f*~1~ *A*T 0 *u* = *f* with *w* = *w*2
> *, u* = *u*2 *, f* = *f*2 *.*
>
> Elimination subtracts *A*^T^*C* times the ﬁrst block row from the
> second. With
>
> *c*~1~ = *c*~2~ = 1, what matrix −*A*^T^*CA* enters the zero block?
> Solve for *u* = (*u*~1~*, u*~2~).

6.  Continuing Problem 5 with *C* = *I*, write down *w* = *CAu* and
    > compute the energy *E*~min~ = ^1^*w*^2^ + ^1^ *w*^2^. Verify that
    > its derivatives with respect to *f*~1~ and *f*~2~

> 2 1 2 2
>
> are the Lagrange multipliers *u*~1~ and *u*~2~ (sensitivity analysis).
>
> Solutions 7.1

4.  The Lagrange function is *L* = *E*~1~(*w*~1~) + *E*~2~(*w*~2~) −
    > *u*~1~(*w*~1~ − *w*~2~ − *f*~1~) − *u*~2~(*w*~2~ − *f*~2~). Its
    > ﬁrst partial derivatives at the saddle point are

+-------+---------+---------------------------------------------------+
| >     | > =     | > *dE*~1~                                         |
|  *�L* |         | >                                                 |
|       |         | > (*w*~1~) − *u*~1~ = 0                           |
| *�    |         | >                                                 |
| w*~1~ |         | > *dw*                                            |
+=======+=========+===================================================+
| >     | > =     | > *dE*~2~                                         |
|  *�L* |         | >                                                 |
|       |         | > (*w*~2~) + *u*~1~ − *u*~2~ = 0                  |
| *�    |         | >                                                 |
| w*~2~ |         | > *dw*                                            |
+-------+---------+---------------------------------------------------+
| >     | > =     | > −(*w*~1~ − *w*~2~ − *f* ) = 0                   |
|  *�L* |         |                                                   |
+-------+---------+---------------------------------------------------+
| > *�  |         |                                                   |
| u*~1~ |         |                                                   |
+-------+---------+---------------------------------------------------+
| >     | > =     | > −(*w*~2~ − *f*~2~) = 0 *.*                      |
|  *�L* |         |                                                   |
+-------+---------+---------------------------------------------------+
| > *�  |         |                                                   |
| u*~2~ |         |                                                   |
+-------+---------+---------------------------------------------------+

*C*−1 *A*

5.  *A*T 0

> � *c*−1
>
> = ��� −1
>
> −1 −1 0 ⎡
>
> ~2~ 1 −1 ⎢⎢
>
> 0 −1

+----------------------+----------+------+--------------------+------+
| > With *C* = *I*     |          |      |                    |      |
| > elimination leads  |          |      |                    |      |
| > to                 |          |      |                    |      |
+======================+==========+======+====================+======+
| �*I*                 | > *A* �  | >    | > − *A A* = − � 2  | > −1 |
|                      | >        | with | >                  | > �  |
| 0                    | > T      |      | > T                | >    |
|                      | >        |      |                    |  *.* |
|                      | > −*A A* |      | −1                 | >    |
|                      |          |      |                    | > 1  |
+----------------------+----------+------+--------------------+------+
| > The equation\...   |          |      |                    |      |
+----------------------+----------+------+--------------------+------+

# Calculus of Variations

> One theme of this book is the relation of equations to minimum
> principles. *To minimize P is to solve P [t]{.smallcaps}* = 0. There
> may be more to it, but that is the main
>
> point. For a quadratic *P* (*u*) = ^[1]{.underline}^*u*^T^*Ku u*^T^*f*
> , there is no diﬃculty in reaching
>
> *P [t]{.smallcaps}* = *Ku* − *f* = 0. The matrix *K* is symmetric
> positive deﬁnite at a minimum.

In a continuous problem, the "derivative" of *P* is not so easy to ﬁnd.
The unknown

*u*(*x*) is a function, and *P* (*u*) is usually an integral. Its
derivative *�P/�u* is called the

> *ﬁrst variation*. *The* "*Euler-Lagrange equation* " *�P/�u* = 0 *has
> a weak form and a strong form*. For an elastic bar, *P* is the
> integral of ^[1]{.underline}^ *c*(*u [t]{.smallcaps}*(*x*))^2^ − *f*
> (*x*)*u*(*x*).
>
> The equation *�P/�u* = 0 is linear and the problem will have boundary
> conditions:
>
> Our goal in this section is to get beyond this ﬁrst example of
> *�P/�u*.
>
> The basic idea should be simple and it is: *Perturb u*(*x*) *by a test
> function*
>
> *v*(*x*). Comparing *P* (*u*) with *P* (*u* + *v*), the linear term in
> the diﬀerence yields *�P/�u*. *This linear term must be zero for every
> admissible v* (*weak form*). This program carries ordinary calculus
> into the calculus of variations. We do it in several steps:

1.  One-dimensional problems *P* (*u*) = � *F* (*u, u [t]{.smallcaps}*)
    *dx*, not necessarily quadratic

2.  Constraints, not necessarily linear, with their Lagrange multipliers

3.  Two-dimensional problems *P* (*u*) = �� *F* (*u, u~x~, u~y~*) *dx
    dy*

4.  Time-dependent equations in which *u [t]{.smallcaps}* = *du/dt*.

> At each step the examples will be as familiar (and famous) as
> possible. In two dimensions that means Laplace's equation, and minimal
> surfaces in the nonlinear case. In time-dependent problems it means
> Newton's Laws, and relativity in the nonlinear case. In one dimension
> we rediscover the straight line and the circle.
>
> This section is also the opening to *control theory* ---the modern
> form of the calculus of variations. Its constraints are diﬀerential
> equations, and Pontryagin's maximum principle yields solutions. That
> is a whole world of good mathematics.
>
> *Remark* To go from the strong form to the weak form, *multiply by v
> and integrate*. For matrices the strong form is *A*^T^*CAu* = *f* .
> The weak form is *v*^T^*A*^T^*CAu* = *v*^T^*f* for all *v*.
>
> For functions with *Au* = *u [t]{.smallcaps}*, this exactly matches �
> *cu [t]{.smallcaps}v [t]{.smallcaps} dx* = � *fv dx* above.

### One-dimensional Problems {#one-dimensional-problems .unnumbered}

> The basic problem is to minimize *P* (*u*) with a boundary condition
> at each end:

� ~1~ *[t]{.smallcaps}*

> *P* (*u*) = *F* (*u, u* ) *dx* with *u*(0) = *a* and *u*(1) = *b .*

0

> The best *u* defeats every other candidate *u*+*v* that satisﬁes these
> boundary conditions. Then (*u* + *v*)(0) = *a* and (*u* + *v*)(1) =
> *b* require that *v*(0) = *v*(1) = 0. When *v* and
>
> *v [t]{.smallcaps}* are small the correction terms come from *�F/�u*
> and *�F/�u [t]{.smallcaps}*. They don't involve
>
> *v*^2^:
>
> Inside the integral *F* (*u* + *v, u [t]{.smallcaps}* + *v
> [t]{.smallcaps}*) = *F* (*u, u [t]{.smallcaps}*) + *v
> [�F]{.underline}* + *v [t]{.smallcaps} [�F]{.underline}* + · · ·

� 1 � *[�F]{.underline}*

> *�u �u [t]{.smallcaps} [t]{.smallcaps} [�F]{.underline}* �
>
> That integrated term is the "ﬁrst variation". We have already reached
> *�P/�u*:

*[�P]{.underline}* � 1 � *[�F]{.underline} [t]{.smallcaps}
[�F]{.underline}* �

> This is the equation for *u*. The derivative of *P* in each direction
> *v* must be zero. Otherwise we can make *�P/�u* negative, which would
> mean *P* (*u* + *v*) *\< P* (*u*): *bad*.
>
> The strong form looks for a single derivative which---if it is
> zero---makes all these directional derivatives zero. It comes from
> integrating *�P/�u* by parts:
>
> � 1 � *[�F]{.underline} [d]{.underline}* � *[�F]{.underline}* �� �
> *[�F]{.underline}* �1
>
> The boundary term vanishes because *v*(0) = *v*(1) = 0. To guarantee
> zero for *every*
>
> *v*(*x*) in the integral, the function multiplying *v* must be zero
> (strong form):
>
> Example Find the shortest path *u*(*x*) between two points (0*, a*)
> and (1*, b*).
>
> By Pythagoras, (*dx*)2 + (*du*)2 is a short step on the path. So *P*
> (*u [t]{.smallcaps}*) = 1 + (*u [t]{.smallcaps}*)2 *dx* is the length
> of the path between the points. This square root *F* (*u
> [t]{.smallcaps}*) depends only on *u [t]{.smallcaps}* and *�F/�u* = 0.
> The derivative *�F/�u [t]{.smallcaps}* brings the square root into the
> denominator:
>
> *[�F]{.underline}* � 1 *[t]{.smallcaps} u [t]{.smallcaps}*
>
> If the quantity multiplying *v [t]{.smallcaps}* is a constant, then
> (3) is satisﬁed. The integral is certain to be zero because *v*(0) =
> *v*(1) = 0. The strong form *forces �F/�u [t]{.smallcaps}* to be
>
> constant: the Euler-Lagrange equation (2) is

*[d]{.underline}* � *[�F]{.underline}* �

> *d u [t]{.smallcaps} u [t]{.smallcaps}*

− *dx �u [t]{.smallcaps}*

> = − *dx* �1 + (*u [t]{.smallcaps}*)2 = 0 or �1 + (*u
> [t]{.smallcaps}*)2
>
> = *c .* (4)
>
> *That integration is always possible when F depends only on u* �
> (*�F/�u* = 0). It leaves the equation *�F/�u [t]{.smallcaps}* = *c*.
> Squaring both sides, *u* is seen to be *linear* :

(*u [t]{.smallcaps}*)^2^

> = *c*^2^(1 + (*u*

*[t]{.smallcaps}*)2) and *u [t]{.smallcaps}*

> *c*
>
> = �1 − *c*2

*c*

> and *u* = �1 − *c*2 *x* + *d .* (5)
>
> replacementTs he constants *c* and *d* are chosen to match *u*(0) =
> *a* and *u*(1) = *b*. *The shortest curve connecting two points is a
> straight line*. No surprise! The length *P* (*u*) is a minimum, not a
> maximum or a saddle point, because the second derivative *F
> [tt]{.smallcaps}* is positive.
>
> *x* *x*
>
> typical perturbation *v*(*x*) area below arc is *A*
>
> Figure 7.5: Shortest paths from *a* to *b*: straight line and circular
> arc (constrained).

### Constrained Problems {#constrained-problems .unnumbered}

> Suppose we cannot go in a straight line because of a constraint. When
> the constraint is *u*(*x*) *dx* = *A*, we look for *the shortest curve
> that has area A below it* :
>
> � ~1~ � *[t]{.smallcaps}* � ~1~
>
> Minimize *P* (*u*) = 1 + (*u* )2 *dx* with *u*(0) = *a, u*(1) = *b,
> u*(*x*) *dx* = *A .*
>
> 0 0
>
> The area constraint should be built into *P* by a Lagrange
> multiplier---here called *m*. The multiplier is a number and not a
> function, because there is one overall constraint rather than a
> constraint at every point. The Lagrangian*L* builds in *u dx* = *A*:
>
> Lagrangian *L*(*u, m*) = *P* + (multiplier)(constraint) = � (*F* +
> *mu*) *dx* − *mA .*
>
> The Euler-Lagrange equation *�L/�u* = 0 is exactly like *�P/�u* = 0 in
> (2):
>
> [*�*(*F* + *mu*)]{.underline} *[d]{.underline}* � [*�*(*F* +
> *mu*)]{.underline} �
>
> *d u [t]{.smallcaps}*
>
> *�u* − *dx �u [t]{.smallcaps}*
>
> = *m* − *dx* �1 + (*u [t]{.smallcaps}*)2 = 0 *.* (6)
>
> Again this equation is favorable enough to be integrated:

*u [t]{.smallcaps}*

> *mx* − �1 + (*u [t]{.smallcaps}*)2
>
> = *c* which gives *u [t]{.smallcaps}*
>
> *mx c*
>
> = �1 − (*mx* − *c*)2 *.*
>
> After one more integration we reach the equation of a circle in the
> *x*-*u* plane:
>
> *u*(*x*) = [−1]{.underline} 1 (*mx c*)2 + *d* and (*mx c*)^2^ + (*mu
> d*)^2^ = 1 *.* (7)
>
> *m*
>
> *The shortest path is a circular arc*! It goes high enough to enclose
> area *A*.
>
> The three numbers *m, c, d* are determined by the conditions *u*(0) =
> *a, u*(1) = *b*, and
>
> *u dx* = *A*. The arc is drawn in Figure 7.5 (and *m* is negative).
>
> We now summarize the one-dimensional case, allowing *F* to depend also
> on *u [tt]{.smallcaps}*. That introduces *v [tt]{.smallcaps}* into the
> weak form and needs *two* integrations by parts to reach
>
> the Euler-Lagrange equation. When *F* involves a varying coeﬃcient
> *c*(*x*), the form of the equation does not change, because it is *u*
> and not *x* that is perturbed.
>
> Applications are everywhere, and we mention one (of many) in sports.
> What angle is optimal in shooting a basketball? The force of the shot
> depends on the launch angle---line drives or sky hooks need the most
> push. The force is minimized at 45^�^ if the ball leaves your hand ten
> feet up; for shorter people the angle is about 50^�^. What is
> interesting is that the same angle solves a second optimization
> problem: to have the largest margin of error and still go through the
> hoop.
>
> The condition is *P [t]{.smallcaps}* = 0 in basketball (one shot) and
> *�P/�u* = 0 in track---where the strategy to minimize the time *P*
> (*u*) has been analyzed for every distance.

### Two-dimensional Problems {#two-dimensional-problems .unnumbered}

> In two dimensions the principle is the same. The starting point is a
> quadratic *P* (*u*), without constraints, representing the potential
> energy over a plane region *S*:
>
> � � J *c* � *�u* �2 *c* � *�u* �2 �

Minimize *P* (*u*) = 2 *�x* + 2 *�y* − *f* (*x, y*) *u*(*x, y*) *dx dy
.*

*S*

> If this energy has its minimum at *u*(*x, y*), then *P* (*u* + *v*) →
> *P* (*u*) for every *v*(*x, y*). We mentally substitute *u* + *v* in
> place of *u*, and look for the term that is linear in *v*. That term
> is the ﬁrst variation *�P/�u*, which must be zero for every *v*(*x,
> y*):
>
> This is the equation of virtual work. It holds for all admissible
> functions *v*(*x, y*), and it is the weak form of Euler-Lagrange. The
> strong form requires as always an integration by parts (Green's
> formula), in which the boundary conditions take care of the boundary
> terms. Inside *S*, that integration moves derivatives away from
> *v*(*x, y*):
>
> Integrate by parts � � �− *[�]{.underline}* �*c [�u]{.underline}* � −
> *[�]{.underline}* �*c [�u]{.underline}* � − *f* � *v dx dy* = 0 *.*
> (9)

*�x �x*

*S*

> *�y �y*
>
> Now the strong form appears. This integral is zero for every *v*(*x,
> y*). By the "funda-mental lemma" of the calculus of variations, the
> term in brackets is forced to be zero everywhere:
>
> Strong form − *[�]{.underline}* �*c [�u]{.underline}* � −
> *[�]{.underline}* �*c [�u]{.underline}* � = *f* (*x, y*) throughout
> *S* . (10)
>
> This is the Euler-Lagrange equation *A*^T^*CA* = *f* , or *c u* = *f*
> . For constant *c* it is Poisson. If the *y* variable is removed, we
> are back to a one-dimensional rod.
>
> With no extra eﬀort we can go backwards to *P* (*u*) from any linear
> equation:

*�*^2^*u �*^2^*u �*^2^*u*

> Second-order equation *a �x*2 + 2*b �x�y* + *c �y*2
>
> = 0 *.* (11)
>
> When *a, b*, and *c* are constant, the corresponding quadratic
> "energy" is
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image17.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"}1 �� J � *�u* �~2~ � *�u* � � *�u* �
> �*�u* �~2~�
>
> If we minimize *P* we expect to reach (11) as its Euler equation. But
> there is more to it than that. To *minimize P* it should be *positive
> deﬁnite*. Inside the integral is
>
> an ordinary 2 by 2 quadratic *au*^2^ + 2*bu~x~u~y~* + *cu*^2^. The
> test for positive-deﬁniteness
>
> *x y*
>
> is still *ac \> b*^2^, as it was in Chapter 1. (We can make *a \>* 0
> in advance.) That test
>
> decides whether or not equation (11) can be solved with arbitrary
> boundary values on *u*(*x, y*).
>
> In this positive deﬁnite case the equation is called "elliptic" and
> minimization is justiﬁed. There are three fundamental classes of
> partial diﬀerential equations:
>
> Laplace's equation *u~xx~* + *u~yy~* = 0 is elliptic, with *a* = *c* =
> 1 producing the identity matrix. The heat equation *u~xx~ u~t~* = 0 is
> parabolic, with *b* = *c* = 0; the matrix is singular and its
> determinant is zero. That parabolic borderline between elliptic and
> hyperbolic needs help from lower-order terms. The wave equation
> *u~xx~* − *u~tt~* = 0 has *a* = 1 and *c* = −1. It asks for initial
> values---two conditions on part of the boundary and no conditions on
> another part, instead of one condition everywhere.
>
> Here we stay with elliptic equations and minima of *P* (*u*). *The
> boundary con-ditions can specify u*, *or they can specify the normal
> component w* · *n*. Comparing (8) with (9), the boundary term comes
> from Green's formula in Sec-tion :
>
> � � *c*≥*u* · ≥*v dx dy* = − � � (≥ · (*c*≥*u*))*v dx dy* + � (*c*≥*u*
> · *n*)*v ds .* (12)
>
> *S S C*
>
> Both sides equal �� *fv dx dy*; that is the weak form. The ﬁrst term
> on the right
>
> yields the strong form div(*c* grad *u*) = *f* (*x, y*). A zero
> integral over the boundary *c* in (12) will be achieved by the
> boundary conditions. Strictly speaking, the boundary conditions on
> *u*(*x, y*) are part of the strong form.
>
> There are two ways to make this boundary integral of (*c*≥*u* ·
> *n*)*v* safely zero. If boundary values *u* = *u*~0~ are given, and
> *u* + *v* shares those values, then *v* = 0 on the boundary. That
> kills the integral. When *u* is not given and *v* is free, we must
> impose the natural boundary condition *c*≥*u* · *n* = *w* · *n* = 0.
>
> A natural condition on *w* goes with *A*^T^. The essential condition
> *u* = *u*~0~ goes with *A*.

### The Minimal Surface Problem {#the-minimal-surface-problem .unnumbered}

> Now we are ready for *nonlinear* partial diﬀerential equations. The
> corresponding energy will not be a quadratic *P* (*u*). It will be the
> exact energy *E*(*u*), from which *P* originally came as an
> approximation. If there is a thin membrane covering the set *S*---like
> a soap bubble---then stretching this membrane requires energy. The
> energy is proportional to the *surface area of the soap bubble*. In
> the right units the material constant will be *c* = 1, and the problem
> is to *minimize the surface*
>
> *area E*(*u*):
>
> �� J � *�u* �~2~ � *�u* �~2~�1*/*2
>
> *S*
>
> When *u* = 0, the bubble is ﬂat. The expression in brackets reduces
> to 1. That is the minimum if *u* = 0 is admissible. But suppose the
> bubble is created on a piece of wire that goes around *S* at a varying
> height *u*~0~(*x, y*). The bubble has to stick to the wire, so the
> trivial solution *u* = 0 is not allowed. The bent wire imposes a
> boundary condition *u* = *u*~0~(*x, y*) at the edge of *S*, and the
> *minimal surface problem* is to ﬁnd the smallest area *E*(*u*).
> Physically, surface tension makes the area a minimum.

The test for a minimum is still *E*(*u*) *E*(*u* + *v*). To compute the
term *�E/�u*

that is linear in *v*, look at the part *A* from *u* alone, and the
correction *B* involving *v*:

> � *[�u]{.underline}* �~2~ � *[�u]{.underline}* �~2~
>
> *[�u �v]{.underline} [�u �v]{.underline}*
>
> *A* = 1 + + and *B* = 2 + 2 + *O*(*v*^2^) *.*
>
> *�x �y �x �x �y �y*
>
> For small *v*, the square root is �*A* + *B* = �*A* + *B/*2�*A* + · ·
> · . Integrate both sides:
>
> *E*(*u* + *v*) = *E*(*u*) + � �
>
> [1]{.underline} *[�u �v]{.underline} [�u �v]{.underline}*
>
> �*A �x �x* + *�y �y*
>
> *dx dy* + · · · *.* (14)
>
> Now *�E/�u* is exposed. It is the integral in (14) and it is zero.
> That is the weak form of the minimal surface equation. Because of the
> square root of *A*, it is not linear in
>
> *u*. (It is always linear in *v*; that is the whole point of the ﬁrst
> variation!) Integrating by parts to remove the derivatives from *v*
> produces the Euler equation in its strong

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 2%" />
<col style="width: 13%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>form:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Minimal surface equation</p>
</blockquote></td>
<td><p><em><u>�</u></em></p>
<blockquote>
<p>− <em>�x</em></p>
</blockquote></td>
<td><blockquote>
<p>�</p>
</blockquote></td>
<td><blockquote>
<p><u>1 <em>�u</em></u></p>
<p>�<em>A �x</em></p>
</blockquote></td>
<td><blockquote>
<p>�</p>
</blockquote></td>
<td><blockquote>
<p><em><u>�</u></em></p>
<p>− <em>�y</em></p>
</blockquote></td>
<td><blockquote>
<p>�</p>
</blockquote></td>
<td><blockquote>
<p><u>1 <em>�u</em></u></p>
<p>�<em>A �y</em></p>
</blockquote></td>
<td><blockquote>
<p>�</p>
</blockquote></td>
<td><blockquote>
<p>= 0 <em>.</em></p>
</blockquote></td>
<td><blockquote>
<p>(15)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This is not easy to solve, because of the�s [q]{.underline}uare root
> in the denominator. For nearly
>
> ﬂat bubbles, linearization approximates *A* by 1. *The result is
> Laplace's equation*.
>
> Perhaps it is only natural that the most important nonlinear equation
> in geometry should reduce to the most important linear equation, but
> still it is beautiful.

### Nonlinear Equations {#nonlinear-equations .unnumbered}

> The shortest distance and minimal surface problems are typical of the
> general case. The variational problem starts with an integral *E* = *F
> dx dy*. Then *F* depends on *x* and *y* and *u* and derivatives like
> *�u/�x*:
>
> *F* = *F* (*x, y, u, D*~1~*u, D*~2~*u, . . .*) *.*
>
> For an elastic bar there was only *D*~1~*u* = *�u/�x*. For a soap
> bubble there is also
>
> *D*~2~*u* = *�u/�y*. Higher derivatives are allowed, and we can think
> of *u* itself as *D*~0~*u*.
>
> The comparison of *E*(*u*) with the nearby *E*(*u* + *v*) starts from
> an ordinary expan-sion like *F* (*u* + *v*) = *F* (*u*) + *F
> [t]{.smallcaps}*(*u*)*v* + *O*(*v*^2^). When *F* depends on several
> derivatives
>
> of *u*, this expansion has more terms from *F* (*x, y, D*~0~*u* +
> *D*~0~*v, D*~1~*u* + *D*~1~*v, . . .*):
>
> Inside the integral *F* (*u* + *v*) = *F* (*u*) + � *[�F]{.underline}
> D v* + · · · *.* (16)

*We take the derivatives of F with respect to u and u~x~ and any other
D~i~u*.

> The weak form involving *v* deals with those linear terms: (integral=
> 0 for all *v*). The strong form lifts each derivative *D~i~* from *v*
> and puts it (as *D*^T^) onto the part
>
> involving *u*:
>
> Weak to Strong � � � *[�F]{.underline}* � (*D v*)*dx dy* −� � �
> �*D*^T^ � *[�F]{.underline}* �� *v dx dy*
>
> The transpose is *D*^T^ = *D~i~* for derivatives of odd order (with an
> odd number of integrations by parts and minus signs). For even
> derivatives *D*^T^ = +*D~i~*.
>
> Buried inside the calculus of variations is the real source of
> *A*^T^*CA*! The derivatives *D~i~u* give *Au*. Their "transposes"
> *D*^T^ give *A*^T^. In between, *C is normally nonlinear*. But when
> *F* is a pure quadratic ^[1]{.underline}^ *c*(*Du*)^2^, then
> *D*^T^*�F/�Du* becomes *D*^T^(*cDu*)---which is exactly the linear
> *A*^T^*CAu* the we know so well.

Example 1 *F* = *u*^2^ + *u*^2^ + *u*^2^ + *u*^2^ + *u*^2^ + *u*^2^ =
(*D*~0~*u*)^2^ + · · · + (*D*~5~*u*)^2^

> The derivatives of *F* (a pure quadratic) are 2*u,* 2*u~x~,* 2*u~y~, .
> . . ,* 2*u~yy~*. They are derivatives with respect to *u* and *u~x~*
> and the other *D~i~u*, *not* with respect to *x*!
>
> Weak form 2 � � \[*uv* + *u~x~v~x~* + *u~y~v~y~* + *u~xx~v~xx~* +
> *u~xy~v~xy~* + *u~yy~v~yy~* \] *dx dy* = 0 *.*
>
> We integrate every term by parts to give the strong form (times *v*):
>
> Strong form 2 \[*u* − *u~xx~* − *u~yy~* + *u~xxxx~* + *u~xyxy~* +
> *u~yyyy~*\] = 0 *.*
>
> This is linear because *F* is quadratic; the minus signs come with odd
> derivatives in *F* .
>
> Example 2 *F* = (1 + *u*^2^)^1*/*2^ or *F* = (1 + *u*^2^ +
> *u*^2^)^1*/*2^
>
> *x x y*
>
> The derivatives with respect to *u~x~* and *u~y~* bring the square
> root into the denominator. The shortest path equation and the minimal
> surface equation are
>
> − *[d ux]{.underline}* = 0 and − *[�]{.underline}* �
> *[ux]{.underline}* � − *[�]{.underline}* � *[uy]{.underline}* � = 0
> *.*
>
> Every term ﬁts into the pattern of *A*^T^*CA*, and the framework
> becomes nonlinear:
>
> *[�F]{.underline} e* = *Au* no−nl�inear *w* = *C*(*e*) = *�e*
>
> leads to *A*^T^*w* = *A*^T^*C*(*Au*) = *f .*

### Nonlinear *C*(*Au*) from Nonquadratic Energies {#nonlinear-cau-from-nonquadratic-energies .unnumbered}

> That last line was worth a chapter of words. It is the shortest path
> to nonlinear equilibrium equations. In a linear spring, *w* = *ce* is
> proportional to *e*. The internal
>
> strain energy is *F* = � *ce de* = ^[1]{.underline}^ *ce*^2^. *In a
> nonlinear spring the constitutive*
>
> *law is w* = *C*(*e*). The relation of force to stretching, or current
> to voltage, or ﬂow
>
> to pressure, is no longer a straight line *Ce*. We need parentheses in
> *C*(*e*)!
>
> The energy density is still *F* = *C*(*e*) *de* = force times
> movement. Minimizing the total energy (integrate *F* to ﬁnd *E*) still
> gives the equilibrium equation:
>
> The energy *P* (*u*) = � \[*F* (*Au*) − *fu*\] *dx* is minimized when
> *A*^T^*C*(*Au*) = *f .*
>
> The ﬁrst variation of *E* leads to \[*C*(*Au*)(*Av*) *fv*\] *dx* = 0
> for every *v* (weak form). Then *A*^T^*C*(*Au*) = *f* is the Euler
> equation (strong form).
>
> For the nonlinear equivalent of positive deﬁniteness, *the function
> C*(*e*) *should be increasing*. The line *w* = *ce* had a constant
> slope *c \>* 0. Now that slope *C [t]{.smallcaps}* = *dC/de*
>
> is changing---but it is still positive. That makes the energy *E*(*u*)
> a convex function. The Euler equation is elliptic---we have a minimum.
>
> An example is the *power law w* = *C*(*e*) = *e^p^*^−1^ with *p \>* 1.
> The energy density is its integral *F* = *e^p^/p*. The stretching is
> *e* = *Au* = *du/dx*. The equilibrium equation is *A*^T^*C*(*Au*) =
> (−*d/dx*)(*du/dx*)^*p*−1^ = *f* . This is linear for *p* = 2.
> Otherwise nonlinear.

### Complementary Energy {#complementary-energy .unnumbered}

> The complementary energy is a function of *w* instead of *e*. It
> starts with the *inverse constitutive law e* = *C*^−1^(*w*)---in our
> example *e* = *w*^1*/*(*p*−1)^. The strain *e* comes from the stress
> *w*; the arrow in our framework is reversed. Graphically, we are
> looking at Figure 7.6a from the side. *The area under that curve is
> the complementary*
>
> *energy density F* ≈(*w*) = *C*^−1^(*w*) *dw*. The twin equations come
> from *F* and *F* ≈:
>
> *�F �F* ≈
>
> Constitutive Laws *w* = *C*(*e*) = and *e* = *C*^−1^(*w*) = *.* (17)
>
> *�e �w*
>
> The symmetry is perfect and the dual minimum principle applies to
> *Q*(*w*) = *F* ≈(*w*) *dx*:
>
> The complementary energy *Q*(*w*) is a minimum subject to *A*^T^*w* =
> *f* (*x*) *.*
>
> A Lagrange multiplier *u*(*x*) takes *Q* to *L*(*w, u*) = \[*F* ≈(*w*)
> *uA*^T^*w* + *uf* \] *dx*, with the constraint *A*^T^*w* = *f* built
> in. Its derivatives recover the two equations of equilibrium, now
> nonlinear:
>
> *�L/�w* = 0 is *C*^−1^(*w*) − *Au* = 0
>
> *�L/�u* = 0 is *A*^T^*w* = *f .*

The ﬁrst equation gives *w* = *C*(*Au*) and then the second is
*A*^T^*C*(*Au*) = *f* .

> replacements
>
> *w*
>
> *F* (*w*)

*F* ≈(*e*)

*w*

> *e* = *C*^−1^(*w*)
>
> *w* = *C*(*e*)
>
> replacem*e* ents *e*
>
> area *F* + *F* ≈ of rectangle is *ew*

*C*(*e*)

> Figure 7.6: The graphs of *w* = *C*(*e*) and *e* = *C*^−1^(*w*), and
> their areas *F* ≈ and *F* .
>
> Since these nonlinear things are in front of us, why not take the last
> step? It is
>
> never seen in advanced calculus, but there is nothing so incredibly
> diﬃcult. It is the direct link between *F* and *F* ≈, known as the
> *Legendre-Fenchel transform* :
>
> *F* ≈(*w*) = max \[*ew* − *F* (*e*)\] and *F* (*e*) = max \[*ew* − *F*
> ≈(*w*)\] *.* (18)
>
> For the ﬁrst maximum, diﬀerentiate with respect to *e*. That brings
> back *w* = *�F/�e*, which is the correct *C*(*e*). The maximum itself
> is *F* ≈ = *e�F/�e* − *F* . The ﬁgures show graphically that the areas
> satisfy *F* ≈ = *ew* − *F* on the curve and *ew* − *F \< F* ≈ oﬀ the
> curve. So the maximum of *ew* − *F* is *F* ≈ as desired.
>
> Similarly, the second maximum in (18) leads to *e* = *�F* ≈*/�w*. That
> is the con-
>
> stitutive law in the other direction, *e* = *C*^−1^(*w*). The whole
> nonlinear theory is there, provided the material laws are
> conservative---the energy in the system should be constant. This
> conservation law seems to be destroyed by dissipation, or more
> spectacularly by ﬁssion, but in some ultimate picture of the universe
> it must remain true.
>
> *F will be the Lagrangian and F* ≈ *is the Hamiltonian*. The equations
> *mu~tt~* + *cu~t~* + *ku* = 0 and *u~xx~* = *u~t~* include friction
> and damping and diﬀusion, but we hesitate to stretch our framework
> that far. Feynman's wonderful lectures made "least action" the
> starting point for physics, and the next paragraphs.
>
> The Legendre transform reappears at full strength in constrained
> optimization. There *F* and *F* ≈ are more general convex functions
> (with nonnegative second deriva-tives) and *we recognize that F* ^��^
> *is F* . Here we compute *F* ≈(*w*) for the power law
>
> and verify that it agrees with the integral of *C* ^−1^(*w*).
>
> Example Find *F* ≈(*w*) for the power law *F* (*e*) = *e^p^/p* (*e \>*
> 0 and *w \>* 0 and *p \>* 1) Diﬀerentiating *ew F* (*e*) gives *w
> e^p^*^−1^ = 0. Then the conjugate *F* ≈(*w*) in (18) is *w^q^/q*:
>
> *F* = *ew* [1]{.underline} *ep* = *w*1*/*(*p*−1)*w* [1]{.underline}
> *wp/*(*p*−1) = [*p* − 1]{.underline} *wp/*(*p*−1) = [1]{.underline}
> *wq . p p p q*
>
> *F* ≈(*w*) = *w^q^/q* is also a power law, with *dual exponent q* =
> *p/*(*p* 1). This matches the area under *C*^−1^(*w*) =
> *w*^1*/*(*p*−1)^, because integration will increase that exponent to
> 1 + 1*/*(*p* − 1) = *q*. The symmetric relation between the powers is
> *p*^−1^ + *q*^−1^ = 1.

### Dynamics and Least Action {#dynamics-and-least-action .unnumbered}

> Fortunately or unfortunately, the world is not in equilibrium. The
> energy stored in springs and beams and nuclei and people is waiting to
> be released. When the external forces change, the equilibrium is
> destroyed. Potential energy is converted to kinetic energy, the system
> becomes dynamic, and it may or may not ﬁnd a new steady state.
>
> When the system is conservative, the transients will not grow or
> decay. The energy changes from potential to kinetic to potential to
> kinetic, but the total energy *K* + *P* remains constant. It is like
> the earth around the sun or a child on a frictionless swing. The force
> *dP/du* is no longer zero, and the system oscillates. The problems are
> dynamic instead of static.
>
> To describe the motion we need an equation or a variational principle.
> Numerically we mostly work with equations (Newton's laws and
> conservation laws). This section derives those laws from the
> *principle of least action* :
>
> It is better to claim only that *�A/�u* = 0---the path is always a
> stationary point but not in every circumstance a minimum. We have a
> diﬀerence of energies, and positive deﬁniteness can be lost (a saddle
> point). Laplace's equation will be overtaken by the wave equation.
> First come three examples to show how the *global law* of least action
> (the variational principle of least action) produces Newton's *local
> law F* = *ma*.
>
> Example 3 A ball of mass *m* is attracted by the Earth's gravity

The only degree of freedom is the ball's height *u*(*t*). The energies
are *K* and *P* :

> [1]{.underline} � *[du]{.underline}* �2
>
> The action is *A* = � ( ^[1]{.underline}^ *m*(*u [t]{.smallcaps}*)^2^
> − *mgu*) *dt*. Then *�A/�u* follows from the rules of this
>
> section---with the time variable *t* replacing the space variable *x*.
> The true path *u* is compared to its neighbors *u* + *v*. The linear
> part of *A*(*u* + *v*) *A*(*u*) gives the ﬁrst variation *�A/�u* = 0:
>
> *[�A]{.underline}* � *t*1 *[t]{.smallcaps} [t]{.smallcaps}*
>
> That is the weak form of Newton's law. You recognize the momentum *mu
> [t]{.smallcaps}* as the
>
> derivative of ^[1]{.underline}^ *m*(*u [t]{.smallcaps}*)^2^ with
> respect to the velocity *u [t]{.smallcaps}*. The strong form is the
> Euler
>
> equation:
>
> Newton's law − �*m* � − *mg* = 0 which is *ma* = *F .* (19)

*[d]{.underline} [du]{.underline}*

*dt dt*

The action integral is minimized by the path that follows Newton's law.

> The 3-step framework of applied mathematics is not changed. The place
> of *A* is taken by *d/dt* and *A*^T^ is *d/dt*. The material constant
> is *m* and the external force is *f* = *mg*. The balance between
> *A*^T^*CAu* and *f* is Newton's law---a balance of inertial forces
> instead of mechanical forces. Figure 7.7 identiﬁes the variables as
> the velocity and momentum.
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image71.png){width="0.21904746281714785in"
> height="0.2190463692038495in"}*du dp*
>
> *v* = *f* = **. .**
>
> *dt dt* **.. ..**
>
> **. ..**
>
> **. ..**
>
> �

�

> *p* = *mv*
>
> Figure 7.7: Newton's law for a ball. A pendulum also ﬁts the
> framework.
>
> Example 4 A simple pendulum with mass *m* and length *l*
>
> The state variable *u* is the angle *�* from the vertical. The height
> *l l* cos *�* still enters the potential energy and the velocity is
> *v* = *l d�/dt*:
>
> [1]{.underline} � *[d�]{.underline}* �2
>
> In this problem the equation will no longer be linear. *K* is
> quadratic but *P* involves cos *�*. The Euler equation follows the
> rule for an integral *F* (*�, � [t]{.smallcaps}*) *dt*, with *F* = *K*
> − *P* :
>
> − � � = 0 or − *mgl* sin *�* − �*ml*^2^ � = 0 *.*
>
> Euler *[�F]{.underline} [d]{.underline} [�F]{.underline}
> [d]{.underline} [d�]{.underline}*
>
> This is the equation of a simple pendulum. The mass cancels out;
> clocks keep time!
>
> *d*^2^*� g*
>
> Pendulum equation

*dt*2

> \+
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.500437445319335e-2in"
> height="6.666666666666667e-3in"} sin *�* = 0 *.* (20)
>
> *l*
>
> When the angle is small and sin *�* is approximated by *�*, the
> equation becomes linear. The period changes a little. A linear clock
> keeps time, but not the right time.
>
> Example 5 A vertical line of springs and masses has *Mu
> [tt]{.smallcaps}* + *Ku* = 0
>
> The potential energy in the springs is *P* =
> ^[1]{.underline}^*u*^T^*A*^T^*CAu*. The kinetic energy has
> ^[1]{.underline}^ *m~i~*(*du~i~/dt*)^2^
>
> 2 2
>
> from each mass. Then *K* − *P* goes into the action integral, and
> there is an Euler equa-
>
> tion *�A/�u~i~* = 0 for each mass. In matrix form this is the basic
> equation of mechanical engineering:
>
> Undamped oscillation *Mu [tt ]{.smallcaps}*+ *A*^T^*CAu* = 0 *.*
>
> *M* is the diagonal mass matrix and *A*^T^*CA* is the positive deﬁnite
> stiﬀness matrix. The system oscillates around equilibrium and the
> total energy *K* + *P* is constant.
>
> Example 6 Waves in an elastic bar---*a continuum of masses and
> springs*. The action integral in this continuous case has an integral
> instead of a sum:
>
> � *t*1 � 1 J 1 � *du* �2 1 �*du* �2�

The Euler-Lagrange rules for *�A/�u* = 0 cover this case of a double
integral:

> Wave equation
>
> *[�A]{.underline} [�]{.underline}*

= −

> �*m[�u]{.underline}* � − *[�]{.underline}* �−*c[�u]{.underline}* � = 0
> *.*
>
> That is the wave equation *mu~tt~* = *cu~xx~*. With constant density
> *m* and elastic constant
>
> *c*, the wave speed is *c/m*---faster when the bar is stiﬀer and
> lighter.
>
> Staying with the calculus of variations, there are two important
> comments:

1.  When *u* is independent of time (no motion), the kinetic energy is
    > *K* = 0 and the least action principle reduces to *�P/�u* = 0. The
    > dynamic problem goes back to the static problem of *A*^T^*CAu* =
    > *f* , without a time derivative.

2.  The dual variable *w*, from all the evidence, should be found in its
    > usual place in Figure 7.7. It is the *momentum p* = *mv* = *m
    > du/dt*. We can rewrite *K*:

> The kinetic energy *K* = 1 *mv*^2^ becomes 1 *p*^2^ *.*
>
> 2 2*m*
>
> That is the "complementary" kinetic energy, expressed in terms of *p*
> instead of *v*. Note that *m* moves to the denominator, just as *c*
> did in the elastic energy *w*^2^*/*2*c*. Hamilton found the right
> total energy, using the momentum *p* and the displacement
>
> *u*. Those variables (not the velocity!) are at the primal and dual
> corners of our framework:
>
> Hamiltonian *H* = *K* + *P* =
>
> 1 *p*^2^ + *mgu .* (21)
>
> 2*m*
>
> The Hamiltonian *H*(*p, u*) takes us directly to the equations of
> motion:
>
> This is the essence of classical mechanics. It is tied to Hamilton and
> not to Newton. For that reason it survived the revolution brought by
> Einstein. We will see that *H* has a relativistic form and even a
> quantum mechanical form. Comparing a falling ball with an oscillating
> spring, the key diﬀerence in *H* is between *u* and *u*^2^:
>
> 1 1 1
>
> (ball) *H* = *p*^2^ + *mgu* (spring) *H* = *p*^2^ +
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image15.png){width="8.167104111986001e-2in"
> height="6.666666666666667e-3in"}*cu*^2^
>
> 2*m* 2*m* 2

Hamilton's equations *�H/�p* = *u [t]{.smallcaps}* and *�H/�u* = −*p
[t]{.smallcaps}* yield Newton's Laws:

> (ball) (spring)
>
> = *u [t]{.smallcaps}* and *mg* = −*p [t]{.smallcaps},* or *mu
> [tt]{.smallcaps}* = −*mg*
>
> = *u [t]{.smallcaps}* and *cu* = *p [t]{.smallcaps},* or *mu
> [tt]{.smallcaps}* + *cu* = 0 *.*
>
> *m*
>
> The mass passes through equilibrium at top speed (all energy in *K*).
> The force reverses to slow it down and stop it (all energy in *P* ).
> In the *u p* plane (*the phase plane*) the motion stays on the energy
> surface *H* = constant, which is the ellipse in Fig. 7.8. Each
> oscillation of the spring is a trip around the ellipse.
>
> With more springs there are 2*n* axes *u*~1~*, . . . , u~n~, p*~1~*, .
> . . , p~n~* and the ellipse becomes an ellipsoid. Hamilton's equations
> are *�H/�p~i~* = *du~i~/dt* and *�H/�u~i~* = *dp~i~/dt*.
>
> They lead again to *Mu [tt]{.smallcaps}* + *Ku* = 0, and to the wave
> equation in the continuous case.
>
> momentum *p*(*t*)

2

> 1 2 3 4
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image77.png){width="0.4050557742782152in"
> height="0.1050142169728784in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image77.png){width="0.4050557742782152in"
> height="0.1050142169728784in"}![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image77.png){width="0.40510279965004375in"
> height="0.10502624671916011in"}**.**
>
> **.**
>
> .**\...\...\...**
>
> **.. .**
>
> **. .**
>
> 3 Phase plane
>
> height
>
> **\...\...**
>
> **\...\...**
>
> **\.....**
>
> **.**
>
> **. .. .**
>
> **\...\...**
>
> **\...\...**

**. . .**

> **.. .**
>
> 1 *u*(*t*) **.**

**.**

> **\...\...**
>
> **.**
>
> **\...\.....**
>
> **.**

all *P*

**\... .**

> 4 **.**
>
> all *K*

�

> all *K*
>
> Figure 7.8: 1 tension 2 motion 3 compression 4 motion: Constant energy
> *H* = *K* +*P* .

### Relativity and Quantum Mechanics {#relativity-and-quantum-mechanics .unnumbered}

> These few paragraphs are an attempt, by a total amateur, to correct
> the action inte-gral by the rules of relativity. Feynman's lectures
> propose the term *mc*^2^ 1 (*v/c*)2 in the Lagrangian *K P* . At *v* =
> 0 we see Einstein's formula *e* = *mc*^2^ for the energy in a mass *m*
> at rest. It becomes part of the potential energy *P* .
>
> As the velocity increases from zero there is also a part corresponding
> to *K*. For small *x* the square root of 1 [−]{.underline} *x* is
> approximately 1 − [1]{.underline} *x*, which linearizes the problem
>
> and brings back Newton's ^1^*mv*^2^---just as linearizing the minimal
> surface equation
>
> brought back Laplace. Relativity mixes together *K* and *P* !
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image78.png){width="0.2666929133858268in"
> height="6.666666666666667e-3in"}2 � 2 � 1 *v*2 �
>
> Now, trusting in duality, we look for the conjugate function *F* ≈ in
> the Hamiltonian. It will be a function of *p*, not *v*. The ﬁrst step
> is to ﬁnd that momentum *p*. Before

relativity, *F* was ^[1]{.underline}^*mv*^2^ and its derivative was *p*
= *mv*. Always *p* is *�F/�v*:

> *�F mv*
>
> Momentum *p* =

*�v*

> = �1 − (*v/c*)2 *.* (24)
>
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image79.png){width="0.4067541557305337in"
> height="0.10502187226596675in"}This becomes inﬁnite as *v* approaches
> the speed of light. According to (18), *F* ≈ is
>
> Hamiltonian *F* ≈(*p*) = max \[*pv* − *F* (*v*)\] = *mc*^2^�1 +
> (*p/mc*)2 *.* (25)
>
> This maximum occurs at (24)---which we solved for *v* and substituted
> into *pv* − *F* (*v*).
>
> The new Hamiltonian *F* ≈ is again Einstein's energy *e* = *mc*^2^
> when the system is at rest. As *p* increases from zero, the next
> contribution is Newton's *p*^2^*/*2*m*:
>
> ≈ 2 � 1 *p*^2^ � *p*^2^
>
> Newton found the low-order term in the energy *F* ≈ that Einstein
> computed exactly! Perhaps the universe is like a minimal surface in
> space-time. To Laplace and Newton it looked ﬂat (linearized), but to
> Einstein it became curved.
>
> It is risky to add anything about quantum mechanics, which works with
> proba-bilities. It is a mixture of diﬀerential equations
> (Schr¨odinger) and matrix equations (Heisenberg). The event at which
> *�A/�u* = 0 almost always occurs. Feynman gave each possible
> trajectory of the system a phase factor *e^iA/h^* multiplying its
> probability amplitude. The small number *h* (Planck's constant) means
> that a slight change in the action *A* completely alters the phase.
> There are strong canceling eﬀects from nearby paths unless *the phase
> is stationary*. In other words *�A/�u* = 0 at the most probable path.
>
> This prediction of "stationary phase" applies equally to light rays
> and particles. Optics follows the same principles as mechanics, and
> light travels by the fastest route: *least action becomes least time*.
> If Planck's constant could go to zero, the deterministic principles of
> least action and least time would appear and the path of least action
> would be not only probable but certain.

# Problem Set 7.2 {#problem-set-7.2 .unnumbered}

1.  What are the weak form and the strong form of the linear beam
    > equation---the Euler equation for *P* = \[ ^[1]{.underline}^
    > *c*(*u [tt]{.smallcaps}*)^2^ − *fu*\] *dx*?

2.  Minimizing *P* = (*u [t]{.smallcaps}*)^2^*dx* with *u*(0) = *a* and
    > *u*(1) = *b* also leads to the straight line through these points.
    > Write down the weak form and the strong form.

3.  Find the Euler equations (strong form) for

> \(a\) � \[(*u [t]{.smallcaps}*)^2^ + *e^u^*\] *dx* (b) � *uu
> [t]{.smallcaps} dx* (c) � *x*^2^(*u [t]{.smallcaps}*)^2^*dx*

4.  If *F* (*u, u [t]{.smallcaps}*) is independent of *x*, as in almost
    > all our examples, show from the Euler equation and the chain rule
    > that *H* = *u [t]{.smallcaps}�F/�u [t]{.smallcaps} F* is constant.
    > This is dual to the fact that *�F/�u [t]{.smallcaps}* is constant
    > when *F* is independent of *u*.

5.  If the speed is *x* the travel time of a light ray is

> 1 1
>
> *T* =
> ![](book/images/Gilbert Strang MIT Computational Science and Engineering (1)/media/image18.png){width="9.333880139982502e-2in"
> height="6.666666666666667e-3in"} 1 + (*u*
>
> ~0~ *x*

t)  2 *dx* with *u*(0) = 0 and *u*(1) = 1 *.*

    a.  From equation *�T /�u* = 0 what quantity is constant (Snell's
        > law)?

    b.  Can you integrate once more to ﬁnd the optimal path *u*(*x*)?

```{=html}
<!-- -->
```
6.  With the constraints *u*(0) = *u*(1) = 0 and *u dx* = *A*, show that
    > the minimum value of *P* = (*u [t]{.smallcaps}*)^2^*dx* is
    > 12*A*^2^. Introduce a multiplier *m*, solve the Euler

> equation for *u*, and verify that *A* = −*m/*24. Then the derivative
> *dP/dA* = 24*A* equals the multiplier −*m* as the sensitivity theory
> predicts.

7.  For the shortest path constrained by � *u dx* = *A*, what is unusual
    about the

> solution in Fig. 7.5 as *A* becomes large?

8.  Suppose the constraint is *u dx A*, with inequality allowed. Why
    > does the solution remain a straight line as *A* becomes small?
    > Where does the multiplier *m* remain? This is typical of
    > inequality constraints: either the Euler equation is satisﬁed or
    > the multiplier is zero.

9.  Suppose the constrained problem is r[eversed, a]{.underline}nd we
    *maximize* the area *P* =

*u dx* subject to ﬁxed length *I* = 1 + (*u [t]{.smallcaps}*)2 *dx*,
with *u*(0) = *a* and *u*(1) = *b*.

a.  Form the Lagrangian and solve its Euler equation for *u*.

b.  How is the multiplier *M* related to *m* in the text?

c.  When do the constraints eliminate all functions *u*?

```{=html}
<!-- -->
```
10. Find by calculus the shortest broken-line path between (0*,* 1) and
    > (1*,* 1) that goes ﬁrst to the horizontal axis *y* = 0 and bounces
    > back. Show that the best path treats this axis like a mirror:
    > angle of incidence = angle of reﬂection.

11. The principle of maximum entropy selects the probability
    > distribution that max-imizes *H* = − *u* log *u dx*. Introduce
    > Lagrange multipliers for the constraints *u dx* = 1 and *xu dx* =
    > 1*/a*, and ﬁnd by diﬀerentiation an equation for *u*. On the
    > interval 0 *\< x \<* ∗ show that the most likely distribution is
    > *u* = *ae* .

12. If the second moment *x*^2^*u dx* is also known show that Gauss wins
    > again: the maximizing *u* is the exponential of a quadratic. If
    > only *u dx* = 1 is known, the most likely distribution is *u* =
    > constant. The *least* information comes when only one outcome is
    > possible, say *u*(6) = 1, since *u* log *u* is then identically
    > zero.

13. A helix climbs around a cylinder with *x* = cos *�, y* = sin *�, z*
    = *u*(*�*):

> its length is *L* = � �*dx*2 + *dy*2 + *dz*2 = � �1 + (*u
> [t]{.smallcaps}*)2 *d� .*
>
> Show that *u [t]{.smallcaps}* = constant satisﬁes Euler's equation.
> The helix is regular.

14. Multiply the nonlinear equation −*u [tt]{.smallcaps}* + sin *u* = 0
    > by *v* and integrate the ﬁrst term by parts to ﬁnd the weak form.
    > What integral *P* is minimized by *u*?

15. Find the Euler equations (strong form) for

1 *�*^2^*u* ^2^

a.  *P* (*u*) = 2 *�x*2

> \+ 2 �
>
> *�*^2^*u* ^2^

\+

*�x�y*

> *�*^2^*u* ^2^
>
> *�y*2
>
> *dx dy*

b.  *P* (*u*) = 1 � � (*yu*^2^ + *u*^2^) *dx dy* (c) *E*(*u*) = �
    > *u*�1 + (*u [t]{.smallcaps}*)2 *dx*

> \(d\) *P* (*u*) = [1]{.underline} � � (*u*^2^ + *u*^2^) *dx dy* with �
> � *u*^2^ *dx dy* = 1.

16. Show that the Euler equations for these integrals are the same:

> *�*^2^*u �*^2^*u*
>
> *�x*2 *�y*2 *dx dy* and
>
> � � �
>
> *�*^2^*u* ^2^

*�x�y*

> *dx dy*
>
> Presumably the two integrals are equal if the boundary conditions are
> zero.

17. Sketch the graph of *p*^2^*/*2*m* + *mgu* = constant in the *u p*
    > plane. Is it an ellipse, parabola, or hyperbola? Mark the point
    > where the ball reaches maximum height and begins to fall.

18. Draw a second spring and mass hanging from the ﬁrst. If the masses
    are *m*~1~*, m*~2~

> and the spring constants are *c*~1~*, c*~2~, the energy is
>
> *H* = *K* + *P* = [1]{.underline} *p*^2^ + [1]{.underline} *p*^2^ +
> [1]{.underline} *c u*^2^ + [1]{.underline} *c* (*u* − *u* ) *.*

2*m*~1~ ^1^

> 2*m*~2~ ^2^
>
> 2 1 1
>
> 2 2 2 1
>
> Find the four Hamilton's equations *�H/�p~i~* = *du~i~/dt, �H/�u~i~* =
> *dp~i~/dt*, and the matrix equation *Mu [tt]{.smallcaps}* + *Ku* = 0.

19. The Hamiltonian for a pendulum (with *u* = *�*) is *H* =
    > *p*^2^*/*2*m* + *mgl*(1 cos *u*). Write out Hamilton's
    > equations (22) and eliminate *p* to ﬁnd the equation of a
    > pendulum.

20. Verify that the energy ^[1]{.underline}^ *e*^T^*Ce* and the
    > complementary energy ^[1]{.underline}^ *w*^T^*C*^−1^*w* are

> conjugate. As in equation (18), this means that ^[1]{.underline}^
> *w*^T^*C*^−1^*w* = max\[*e*^T^*w*− [1]{.underline} *e*^T^*Ce*\].
