# Lec 3 -  Electric field energy. Potential; Gradient. Gauss’s law revisited; divergence. - MIT SCOTT HUGES

> Source: `Lec 3 -  Electric field energy. Potential; Gradient. Gauss’s law revisited; divergence. - MIT SCOTT HUGES.pdf`  
> Pages: 11


## Page 1

Scott Hughes
8 February 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 3:
Electric field energy.
Potential; Gradient.
Gauss’s law revisited; divergence.
3.1
Energy in the ﬁeld
Suppose we take our spherical shell of radius r, with charge per unit area σ = q/4πr2, and
squeeze it. How much work does it take to do this squeezing? To answer this, we need to
know how much pressure is being exerted by the shell’s electric ﬁeld on itself. Pressure is
force/area; σ is charge/area; force is charge times electric ﬁeld. Hence, our intuitive guess is
that the pressure should be
Pguess
=
(electric ﬁeld)(charge/area)
=
4πσ2 .
(We have used the fact that the electric ﬁeld just at the surface of the shell is 4πσ.)
This is almost right, but contains a serious ﬂaw. To understand the ﬂaw, note that the
electric ﬁeld we used here, E = 4πσ, includes contributions from all of the charge on the
sphere — including the charge that is being acted upon by the ﬁeld. We must therefore be
overcounting in some sense — a chunk of charge on the sphere cannot act upon itself.
It’s not too hard to ﬁx this up. Imagine pulling a little circular disk out of the sphere:
The correct formula for the pressure will be given by
P
=
(electric ﬁeld in hole)(charge/area on disk)
=
(electric ﬁeld in hole)σ .
We just need to ﬁgure out the electric ﬁeld in the hole. Fortunately, there’s a clever argument
that spares us the pain of a hideous integral: we know that the ﬁeld of the hole plus the ﬁeld
of the disk gives us the ﬁeld of the sphere:
Ehole + Edisk
=
Esphere
=
4πσ
Just outside the sphere
=
0
Just inside the sphere.
23


## Page 2

What’s Edisk? Fortunately, we only need to know this very close to the disk itself: from the
calculations we did in Lecture 2, we have
Edisk
=
+2πσ
Outer side of disk
=
−2πσ
Inner side of disk.
We’re now done:
Ehole = 2πσ
(Pointing radially outward)
which means that the pressure is
P = 2πσ2 .
(Purcell motivates the factor of 1/2 diﬀerence by pointing out that one gets the pressure by
averaging the ﬁeld at r over its discontinuity — the ﬁeld is 0 at radius r −ϵ, it is 4πσ at
r + ϵ. This argument is totally equivalent, and is in fact based upon Purcell problem 1.29.)
Now that we know the pressure it is easy to compute the work it takes to squeeze:
dW
=
F dr
=
P 4πr2 dr
=
2πσ2 dV .
On the last line, we’ve used the fact that when we compress the shell by dr, we have squeezed
out a volume dV = 4πr2 dr. Now, using E = 4πσ, we can write this formula in terms of the
electric ﬁeld:
dW
=
E2
8π dV .
The quantity E2/8π is the energy density of the electric ﬁeld itself. (In SI units, we would
have found ϵ0E2/2.) It shows up in this work calculation because when we squeeze the shell
we are creating new electric ﬁeld: the shell from r −dr to r suddenly contains ﬁeld, whereas
it did not before. We had to put dW = (energy density) dV amount of work into the system
to make that ﬁeld.
3.2
Electric potential diﬀerence
I move a charge q around in an electric ﬁeld⃗E. The work done by me as I move this charge
from position⃗a to⃗b is given by
Uba
=
Z⃗b⃗
a⃗Fme · d⃗s
=
−
Z⃗b⃗
a⃗Fq · d⃗s
=
−q
Z⃗b⃗
a⃗E · d⃗s .⃗
Fme is the force that I exert. By Newton’s 3rd, this is equal and opposite to the force Fq that
the electric ﬁeld exerts on the charge. This is why we ﬂip the sign going from line 1 to line
24


## Page 3

2. Make sure you understand this logic — that sign ﬂip is an important part of stuﬀwe’re
about to deﬁne! On the last line, we’ve expressed this in terms of the electric ﬁeld. Recall
that one of the things we learned about electric ﬁelds is that they generate conservative
forces. This means that this integral must be independent of the path we take from⃗a to⃗b.
We’ll return to this point later.
Since the work we do is proportional to the charge, we might as well divide it out. Doing
so, we deﬁne the electric potential diﬀerence between⃗a and⃗b:
φba = −
Z⃗b⃗
a⃗E · d⃗s .
This function has a simple physical interpretation: it is the work that I must do, per
unit charge, to move a charge from⃗a to⃗b. Its units are energy/charge: erg/esu in cgs,
Joule/Coulomb in SI. Both of these combinations are given special names: the cgs unit of
potential is the statvolt, the SI unit is the Volt.
3.3
Electric potential
Let’s say we ﬁx the position⃗a and consider the electric potential diﬀerence between⃗a and
a variety of diﬀerent points⃗r.
Since the point⃗a is ﬁxed, we can speak of the electric
potential φ(⃗r) relative to the reference point⃗a. The language we use here is very important
— “potential” (as opposed to “potential diﬀerence”) only makes sense provided we know
what is the reference point. All potentials are then deﬁned relative to that reference point.
In a large number of cases, it is very convenient to take the reference point⃗a to be at
inﬁnity. (We’ll discuss momentarily when it is not convenient to do so.) In this case, the
electric potential at⃗r is
φ(⃗r) = −
Z⃗r
∞⃗E · d⃗s .
Suppose⃗E arises from a point charge q at the origin:
φ(⃗r)
=
−
Z⃗r
∞⃗E · d⃗s
=
−
Z r
∞
q
r2dr
=
q
r .
Note that using this formula the potential diﬀerence has a very simple form:
φba
=
−
Z⃗b⃗
a⃗E · d⃗s .
=
q
b −q
a
=
φ(⃗b) −φ(⃗a) .
As the name suggests, the potential diﬀerence is indeed just the diﬀerence in the potential
between the two points.
25


## Page 4

By invoking superposition, we can generalize these formulas very simply: Suppose we
have N point charges. Using inﬁnity as our reference point, the potential at some point P
is given by
φ(P) =
N
X
i=1
qi
ri
,
where ri is the distance from P to the ith charge. We can further generalize this to continuous
distributions: for a charge density ρ distributed through a volume V ,
φ(P)
=
Z
V
ρ dV
r
,
where r is the distance from a volume element dV to the ﬁeld point; for surface charge
density σ distributed over an area A,
φ(P)
=
Z
A
σ dA
r
;
for a line charge density λ distributed over a length L,
φ(P)
=
Z
L
λ dl
r
.
3.4
An important caveat
There is one massive caveat that must be borne in mind when using these formulas: they
ONLY work if it is OK to set the reference point to inﬁnity. That, in turn only
works if the charge distribution itself is of ﬁnite size. As a counterexample, consider an
inﬁnite line charge, with charge per unit length λ. Using Gauss’s law, it is simple to show
that the electric ﬁeld of this charge distribution is given by⃗
E = 2λ
r ˆr ,
where ˆr points out from the line charge, and r is the distance to the line. Let’s ﬁrst work
out the potential diﬀerence between two points r1 and r2 away from the line:
φ21
=
−
Z r2
r1⃗
E · d⃗s
=
−2λ
Z r2
r1
dr
r
=
2λ ln (r1/r2) .
Suppose we make r1 our reference point. Now, look what happens as we let this reference
point approach inﬁnity — the potential diverges! For a charge distribution like this, the ﬁeld
does not fall oﬀquickly enough as a function of distance for inﬁnity to be a useful reference
point. In cases like this, we need to pick some other reference point. In such a situation, it
is crucial that you make clear what you have picked.
26


## Page 5

3.5
Energy of a charge distribution
If we can use inﬁnity as a reference point, then we can write down a formula for the energy
of a charge distribution that is sometimes quite handy. From an earlier lecture, we worked
out the formula
U = 1
2
X
i
X
j̸=i
qiqj
rij
.
A useful way to rearrange this formula is as follows:
U
=
1
2
X
i
qi
X
j̸=i
qi
rij
=
1
2
X
i
qiφ(ri) .
On the second line, we have used the fact that the quantity under the second sum is just
the electric potential of all the charges except qi, evaluated at qi’s location.
Now, we take a continuum limit: we put qi →ρ dV and let the sum become an integral.
We ﬁnd
U = 1
2
Z
ρφ dV .
This formula is entirely equivalent to other formulas we worked out for the energy of a charge
distribution. Bear in mind, though, that we have implicitly assumed that the potential goes
to zero inﬁnitely far from the charge distribution!
3.6
Field from the potential
Consider the potential diﬀerence between the point⃗r and⃗r + ∆⃗r:
∆φ
=
−
Z⃗r+∆⃗r⃗
r⃗
E · d⃗s
≃
−⃗E(⃗r) · ∆⃗r .
Now, expand the vectors in Cartesian coordinates:
∆φ
≃
−(Exˆx + Eyˆy + Ezˆz) · (∆xˆx + ∆yˆy + ∆zˆz)
≃
−Ex ∆x −Ey ∆y −Ez ∆z .
Dividing, taking the limit ∆→0, and invoking the deﬁnition of the partial derivative, we
ﬁnd
Ex = −∂φ
∂x ,
Ey = −∂φ
∂y ,
Ez = −∂φ
∂z ;
or⃗
E
=
−ˆx∂φ
∂x −ˆy∂φ
∂y −ˆz∂φ
∂z
≡
−⃗∇φ .
27


## Page 6

On the last line we have deﬁned the gradient operator,⃗
∇= ˆx ∂
∂x + ˆy ∂
∂y + ˆz ∂
∂z .
The electric ﬁeld is thus given by the gradient of the potential. You will sometimes see this
written⃗E = −grad φ.
28


## Page 7

3.7
The gradient and equipotentials
We’ve deﬁned a mathematical operation which we named the gradient. What exactly is it?
To get some intuition, let’s imagine a one dimensional potential, φ(x). The gradient is given
by⃗∇φ = ˆx dφ/dx. Bearing in mind that the derivative is the function’s slope, the gradient
appears to tell us the direction in which the function changes, and the rate of that change.
A 1-D example is simple, but also a touch silly. Let’s try a 2-D example: put φ(x, y) =
sin(x) sin(y). This potential looks like
-2
0
2
-2
0
2
-1
-0.5
0
0.5
1
-2
0
2
It is simple to calculate this potential’s gradient:⃗∇φ = ˆx cos(x) sin(y) + ˆy sin(x) cos(y).
This vector ﬁeld looks like
-3
-2
-1
0
1
2
3
-3
-2
-1
0
1
2
3
Notice the way the little arrows are pointing. Our intuition from the silly 1-D example is
exactly right: the gradient points in the direction in which the function increases fastest.
At the minima of the function (upper left, lower right), the gradient points out. At the
maxima (upper right, lower left), the gradient points in. A simple way to summarize this
29


## Page 8

is to remember that the gradient always points “uphill”. Bearing in mind that the electric
ﬁeld is the negative gradient of φ, we can say that the electric ﬁeld points “downhill”.
Another useful concept we can build from these plots is the notion of an equipotential
surface. As the name suggests, an equipotential surface is just a surface along which the
potential takes some constant value. For our 2-D example, the equipotential “surfaces” are
really curves in the x −y plane:
-3
-2
-1
0
1
2
3
-3
-2
-1
0
1
2
3
We can deduce one further important property of equipotential surfaces. By deﬁnition,
the potential is constant on them, so they deﬁne the directions along which the potential does
not change at all. The gradient, by contrast, deﬁnes the direction along which the potential
changes the most! If you think about this for a moment, it becomes clear the gradient must
be exactly perpendicular to equipotential surfaces. Since the electric ﬁeld is −⃗∇φ, it follows
that the electric ﬁeld is also exactly perpendicular to equipotentials. A very handy way of
putting this is to say that electric ﬁeld lines are orthogonal to equipotential surfaces.
(If you are a hiker and you have ever used a topographic map, much of this should seem
quite familiar. The contours of a topo map label surfaces of constant height, which is exactly
related to the gravitational potential. If you move perpendicular to the contour lines, you
are moving along the steepest slope possible — desperately scrambling up, or rather quickly
tumbling down.)
3.8
Divergence
The gradient which we just learned about is the ﬁrst and simplest mathematical operation
in vector calculus. We’re going to continue this theme for a little while, exploring several
vector calculus operations which we will use exhaustively in this course.
To set up the next vector calculus operation, let’s return to the notion of ﬂux. Suppose
we’ve got some vector ﬁeld⃗F, and we want to calculate its ﬂux Φ through a closed surface
S:
Φ =
I
S⃗F · d⃗A .
30


## Page 9

S
Now, we do something that may seem kind of silly: we cut the volume into two pieces.
S
S
1
2
o
o
S1
S2
Snew
Snew
S2
S1
o
o
(For clarity, the two halves on the right are drawn separated. We really leave the two pieces
right next to each other.) Before calculating, let’s make sure we understand what the various
surfaces in this diagram mean. On the left, we have the surfaces So
1 and So
2. These are just
the top-right and bottom-left halves of the “old” surface S. Note that these are not closed
surfaces. On the right, we still have So
1 and So
2; in addition, we have a pair of surfaces labeled
Snew. These surfaces are exactly the same area but are oriented in opposite directions. S1
and S2 are the closed surfaces surrounding the two halves of the blob.
OK, so what’s the ﬂux in this case? It must be exactly the same, Φ, since everything’s
still the same as far as the ﬁeld⃗F is concerned. But the way we calculate it is diﬀerent:
Φ
=
I
S⃗F · d⃗A
=
Z
So
1⃗
F · d⃗A +
Z
So
2⃗
F · d⃗A
=
Z
So
1⃗
F · d⃗A +
Z
So
2⃗
F · d⃗A +
Z
Snew⃗
F · d⃗A −
Z
Snew⃗
F · d⃗A
=
ÃZ
So
1⃗
F · d⃗A +
Z
Snew⃗
F · d⃗A
!
+
ÃZ
So
2⃗
F · d⃗A +
Z
Snew⃗
F · (−d⃗A)
!
=
I
S1⃗
F · d⃗A +
I
S2⃗
F · d⃗A
≡
Φ1 + Φ2 .
31


## Page 10

Let’s go through this carefully. On the second line, we have just broken the closed surface
S into the two open surfaces So
1 and So
2. On the third line, we have added and subtracted
an integral over Snew. On the fourth line, we’ve gathered these terms together in a special
way. This special way shows that the combined surfaces are just the closed surfaces S1 and
S2. On the sixth line, we deﬁne these two integrals as Φ1 and Φ2.
We can keep dividing this volume up into smaller and smaller subvolumes; everytime we
do so, there will be facing surfaces whose orientations will cancel each other out. This allows
us to break the total ﬂux up into contributions that come from the surfaces of all these little
subvolumes:
Φ =
big
X
i=1
Φk .
Since we can keep chopping it up into little volumes, the total ﬂux should be proportional
to the volume. This motivates the deﬁnition of the divergence:
div⃗F = lim
V →0
H
S⃗F · d⃗A
V
.
In words, the divergence is what you get when you compute the ﬂux through the surface S
bounding a volume V , divided by V , in the limit in which V goes to zero.
3.9
Gauss’s theorem and Gauss’s law
Now that we have deﬁned the divergence, we are set to prove a very important theorem. We
start with this equation again,
Φ =
big
X
i=1
Φk ,
but now we write out the integrals:
Z
S⃗F · d⃗A
=
N
X
i=1
I
Si⃗
F · d⃗Ai
=
N
X
i=1
Vi
H
Si⃗F · d⃗Ai
Vi
=
N
X
i=1
Vi div⃗F
=
Z
V div⃗F dV .
In words, the ﬂux of a vector function⃗F through a closed surface S equals the integral of
div⃗F over the volume enclosed by S. This is called Gauss’s theorem.
As a concrete example, let’s take⃗F to be the electric ﬁeld⃗E. We thus have
I
S⃗E · d⃗A =
Z
V div⃗E dV .
32


## Page 11

However, we proved a while ago that
I
S⃗E · d⃗A
=
4πQ(inside S)
=
4π
Z
V ρ dV .
Combining these, we have
Z
V div⃗E dV = 4π
Z
V ρ dV ,
or
Z
V
³
div⃗E −4πρ
´
dV = 0 .
This equation is only true for all volumes V only if
div⃗E = 4πρ
This equation also expresses Gauss’s law, only in diﬀerential (rather than integral) form.
Learn it well! In SI units, in keeping with the rule that the electric ﬁeld carries a factor
1/4πϵ0, this formula becomes
div⃗E = ρ/ϵ0
(SI) .
33
