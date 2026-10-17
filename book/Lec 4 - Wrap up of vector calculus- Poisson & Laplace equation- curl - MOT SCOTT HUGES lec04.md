# Lec 4 - Wrap up of vector calculus- Poisson & Laplace equation- curl - MOT SCOTT HUGES lec04

> Source: `Lec 4 - Wrap up of vector calculus- Poisson & Laplace equation- curl - MOT SCOTT HUGES lec04.pdf`  
> Pages: 12


## Page 1

Scott Hughes
10 February 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 4:
Wrap up of vector calculus:
Poisson & Laplace equations; curl
4.1
Summary: Vector calculus so far
We have learned several mathematical operations which fall into the category of vector
calculus. In Cartesian coordinates, these operations can be written in very compact form
using the following operator:⃗
∇≡ˆx ∂
∂x + ˆy ∂
∂y + ˆz ∂
∂z .
The ﬁrst vector calculus operation we learned is the gradient. It converts the electric
potential into the electric ﬁeld:⃗
E
=
−grad φ
=
−⃗∇φ .
The second operation is the divergence, which relates the electric ﬁeld to the charge density:
div⃗E = 4πρ .
Via Gauss’s theorem (also known as the divergence theorem), we can relate the ﬂux of any
vector ﬁeld⃗F through a closed surface S to the integral of the divergence of⃗F over the
volume enclosed by S:
I
S⃗F · d⃗A =
Z
V div⃗F dV .
This follows from the deﬁnition of the divergence:
div⃗F = lim
V →0
H
S⃗F · d⃗A
V
.
34


## Page 2

4.2
Divergence in Cartesian coordinates
So far, we’ve only deﬁned the divergence as a particular limit. We now want to develop a
concrete calculation showing its value. To do so, consider an inﬁnitesimal cube with sides
∆x, ∆y, and ∆z, centered on the coordinate x, y, z:
(x,y,z)
x
y
z
∆
∆z
∆y
x
[The large dot in the center of this cube is only there to mark the coordinate (x, y, z) — it
doesn’t mean anything else.] We take this region to be ﬁlled with a vector ﬁeld⃗F. To begin,
we want to compute the ﬂux of⃗F over this cube. Let’s look at the ﬂux over just the z faces
(the top and bottom):
∆Φz
=
Z
top & bottom⃗F · d⃗A
≃
∆x∆y [Fz (x, y, z + ∆z/2) −Fz (x, y, z −∆z/2)] .
Since the cube is taken to be very small (indeed, we will soon take the limit ∆x, ∆y, ∆z →0),
we approximate the integral. Notice that the contribution from the bottom face (z −∆z/2)
enters with a minus sign, consistent with that face pointing down.
Now, to evaluate the function under the integrand, we make a Taylor expansion about z:
∆Φz
≃
∆x∆y
"
Fz (x, y, z) + ∆z
2
∂Fz
∂z
#
−∆x∆y
"
Fz (x, y, z) −∆z
2
∂Fz
∂z
#
≃
∆x∆y∆z∂Fz
∂z .
Repeating this exercise to ﬁnd the ﬂuxes through the other four sides, we ﬁnd
∆Φx
≃
∆x∆y∆z∂Fx
∂x
∆Φy
≃
∆x∆y∆z∂Fy
∂y .
35


## Page 3

We now have enough information to evaluate the divergence of⃗F:
div⃗F
=
lim
V →0
R⃗F · d⃗A
V
=
lim
∆x,∆y,∆z→0
∆x∆y∆z (∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z)
∆x∆y∆z
=
∂Fx
∂x + ∂Fy
∂y + ∂Fz
∂z
≡⃗
∇·⃗F .
On the last line, we’ve taken advantage of the fact that we can think of the gradient operator
as a vector. In Cartesian coordinates, the divergence is nothing more than combination of
derivatives one ﬁnds by taking the dot product of this operator with a vector ﬁeld. It should
be strongly emphasized at this point, however, that this only works in Cartesian coordinates.
In spherical coordinates or cylindrical coordinates, the divergence is not just given by a dot
product like this!
4.2.1
Example: Recovering ρ from the ﬁeld
In Lecture 2, we worked out the electric ﬁeld associated with a sphere of radius a containing
uniform charge density ρ:⃗
E(r)
=
4
3πρrˆr
r ≤a
=
4πρa3/3
r2
ˆr
r > a .
Recall that we found this by applying the integral form of Gauss’s law. Breaking it up into
Cartesian components, we have for r ≤a
Ex
=
4
3πρx
Ey
=
4
3πρy
Ez
=
4
3πρz ;
for r > a,
Ex
=
4πρa3x/3
(x2 + y2 + z2)3/2
Ey
=
4πρa3y/3
(x2 + y2 + z2)3/2
Ez
=
4πρa3z/3
(x2 + y2 + z2)3/2 .
(We used the facts that rˆr = xˆx + yˆx + zˆz, and ˆr/r2 = rˆr/r3 in here.)
OK, let’s now evaluate⃗∇·⃗E. For r ≤a, we have
∂Ex
∂x = ∂Ey
∂y = ∂Ez
∂z = 4
3πρ ,
36


## Page 4

so⃗
∇·⃗E = 4
3πρ + 4
3πρ + 4
3πρ = 4πρ
exactly as advertised! The region r > a is a bit messier:
∂Ex
∂x
=
∂
∂x
4πρa3x/3
(x2 + y2 + z2)3/2
(1)
=
4πρa3
3
"
1
(x2 + y2 + z2)3/2 −
3x2
(x2 + y2 + z2)5/2
#
.
(2)
Repeating for y and z components and adding, we have⃗
∇·⃗E
=
4πρa3
3
"
3
(x2 + y2 + z2)3/2 −3x2 + 3y2 + 3z2
(x2 + y2 + z2)5/2
#
(3)
=
4πρa3
3
"
3
(x2 + y2 + z2)3/2 −
3
(x2 + y2 + z2)3/2
#
(4)
=
0 .
(5)
Since there is no charge in the exterior region — ρ = 0 for r > a — this is exactly what⃗
∇·⃗E should give.
4.3
Laplacian operator and Poisson’s equation
The div and grad operations can be combined to make an equation that relates the potential
φ to the charge density ρ:
div grad φ = −4πρ .
In Cartesian coordinates, this takes a very nice, simple form:⃗
∇· (⃗∇φ) = −4πρ
or
∇2φ = −4πρ .
The operator ∇2 is, in Cartesian coordinates, exactly what’d you expect taking⃗∇and
dotting it into itself:
∇2 = ∂2
∂x2 + ∂2
∂y2 + ∂2
∂z2 .
The equation ∇2φ = −4πρ is called Poisson’s equation; the operator ∇2 is called the “Lapla-
cian”.
37


## Page 5

For a two dimensional function φ(x, y), the Laplacian tells us about the average curvature
of the function. Let’s look at a couple of examples. First, take a potential that is a bowl-like
paraboloid in the x −y plane:
φ(x, y) = a
4

x2 + y2
,
which has the appearance
-2
-1
0
1
2 -2
-1
0
1
2
0
0.5
1
1.5
2
-2
-1
0
1
For this function, ∇2φ = ∂2φ/∂x2 + ∂2φ/∂y2 = a — the function has positive curvature
everywhere, reﬂected by the fact that the bowl-like function curls up everywhere. There is
a minimum at x = 0, y = 0.
38


## Page 6

4.4
Laplace’s equation
Second, look at a potential that has a hyperboloidal shape in the plane:
φ(x, y) = a
4

x2 −y2
.
This function has the appearance
-2
-1
0
1
2 -2
-1
0
1
2
-1
-0.5
0
0.5
1
-2
-1
0
1
In this case, we ﬁnd ∇2φ = ∂2φ/∂x2 + ∂2φ/∂y2 = 0. The average curvature of this function
is zero — it curves up in x, and down in y. There is no minimum (or maximum) in this
case, only a saddle point at x = 0, y = 0.
The case ∇2φ = 0 — that is, the charge density ρ = 0 — is a special case of Poisson’s
equation called Laplace’s equation. Laplace didn’t just attach his name to Poisson’s equation
in this special case out of some kind of greedy spite. The two equations really merit separate
treatment and diﬀerent names, since their solutions (and methods for solving them) have
rather diﬀerent properties. (Indeed, Laplace was Poisson’s teacher; the Laplace equation
predates Poisson’s by several decades.)
4.5
Earnshaw’s Theorem
A potential that satisﬁes Laplace’s equation has a very important property: if ∇2φ = 0 in
some region, then φ has no local minimum (or maximum) in that region. For there to be a
minimum, a function must have positive second derivative in every possible direction. This
just isn’t possible if
∂2φ
∂x2 + ∂2φ
∂y2 + ∂2φ
∂z2 = 0 .
Suppose we manage to locate a place where φ has a minimum in the x direction and a
minimum in the y direction. We know, then, that ∂2φ/∂x2 > 0 and ∂2φ/∂y2 > 0. The only
way for φ to satisfy Laplace’s equation is if ∂2φ/∂z2 < 0. This location is a minimum in x
and y, but it is not a minimum in z. The best we can do is ﬁnd a saddle point, a location
that is a minimum along two directions, but a maximum along the third.
The non-existence of minima for regions in which ρ = 0 has an important physical
consequence: it means that it is impossible to hold a charge in stable equilibrium with
39


## Page 7

electrostatic ﬁelds. Any object that is in stable equilibrium must be at a minimum of its
potential energy.
Since the potential energy of a charge in an electrostatic ﬁeld is just
U = qφ, it follows that stable equilibrium requires a minimum in the electric potential. Such
a minimum just isn’t possible when ρ = 0 — we must have ∇2φ = 0. This result goes under
the name Earnshaw’s Theorem.
This means that any conﬁguration make out of pure point charges cannot be stable. For
example, if we glue positive charges to the corners of a cube, it is impossible to stably hold
any kind of charge inside that cube:
All the forces cancel out on a charge at the exact center — but, if we displace it just slightly
away from the center, it will rapidly fall out of equilibrium and come shooting out of the
cube. This result was very disturbing to scientists in the late 19th and early 20th centuries,
since it implied that atoms could not be stable — the electron should fall into the proton after
a few microseconds. It wasn’t until we developed an understanding of quantum mechanics
that the stability of matter made any sense.
4.6
The curl
We wrap up this lecture with the ﬁnal instrument in our vector calculus arsenal. We begin
by thinking about the line integral of a vector ﬁeld⃗F around some closed loop C:
C
This quantity is called the circulation Γ of⃗F:
Γ =
I
C⃗F · d⃗s .
40


## Page 8

We now bridge the contour C with a new path B. Doing so we make two new loops C1
and C2. C1 is built from an open loop Co
1 and the path B going upwards; C2 is built from
an open loop Co
2 and the path B going downwards:
Co
1
Co
2
B
B
C1
C2
Now, we manipulate the integral in a manner similar to what we did when we derived the
divergence:
Γ
=
Z
Co
1⃗
F · d⃗s +
Z
Co
2⃗
F · d⃗s
=
Z
Co
1⃗
F · d⃗s +
Z
Co
2⃗
F · d⃗s +
Z
B⃗F · d⃗s +
Z
B⃗F · (−d⃗s)
=
 Z
Co
1⃗
F · d⃗s +
Z
B⃗F · d⃗s
!
+
 Z
Co
2⃗
F · d⃗s −
Z
B⃗F · d⃗s
!
=
I
C1⃗
F · d⃗s +
I
C2⃗
F · d⃗s
≡
Γ1 + Γ2 .
The key bit to this analysis is that when we cut a big contour in half, we end up with a
path going in one direction on the new “bridging” contour, and in the opposite direction on
the other side. Hence, everytime we do this, we get “internal” contours that cancel out, and
what’s left is equivalent to the original big contour.
We now repeatedly break up the contour into lots of little bits:
I
C⃗F · d⃗s =
big
X
i=1
I
Ci⃗
F · d⃗s ,
or
Γ =
big
X
i=1
Γi .
41


## Page 9

As we keep breaking the object up, we end up covering the area enclosed by the contour
with a grid of little circulation cells:
C
and so the total circulation must be proportional to the area that the contour encloses. We
thus deﬁne a vector called the curl of⃗F:
curl⃗F · ˆn = lim
A→0
H
C⃗F · d⃗s
A
.
The area A is bounded by the contour C. The curl is thus circulation of⃗F per unit A, in the
limit in which A goes to zero. Notice that the curl is a vector: it points in the direction ˆn
which is normal to the surface. We deﬁne this direction with the right hand rule: curl your
right-hand ﬁngers in the direction of C’s circulation, and your thumb deﬁnes ˆn.
As with the divergence, an important theorem is connected to the curl. We start with
its deﬁnition, and then do the breaking up into little bits:
Γ =
I
C⃗F · d⃗s
=
big
X
i=1
I
Ci⃗
F · d⃗s
=
big
X
i=1
Ai
H
Ci⃗F · d⃗s
Ai
=
big
X
i=1
Aicurl⃗F · ˆn
=
big
X
i=1
curl⃗F · (Ai ˆn)
=
I
A curl⃗F · d⃗A .
In words, the circulation of a vector ﬁeld⃗F over a closed contour C equals the ﬂux of the
curl of⃗F through the surface bounded by C. This rule is known as Stoke’s theorem.
Suppose our vector ﬁeld⃗F is just an electrostatic ﬁeld,⃗E. We already know that
I
C⃗E · d⃗s = 0
for any contour C since the electric force is conservative. It follows from this that
curl⃗E = 0
This is an important point, which is worth emphasizing: a “good” electrostatic ﬁeld has no
curl.
42


## Page 10

4.7
The curl in Cartesian coordinates
Consider a square lying in a plane parallel to the y−z plane, with sides ∆y and ∆z, centered
on the coordinate (x, y, z). This square is immersed in a vector ﬁeld⃗F. Using this square,
let’s work out what the curl must be.
x
y
z
y
∆
z
∆
(x,y,z)
a
b
c
d
We approximate the integral along the 4 legs as follows:
Z b
a⃗F · d⃗s
=
Fy(x, y, z −∆z/2)∆y ≃
"
Fy(x, y, z) −∆z
2
∂Fy
∂z
#
∆y
Z c
b⃗F · d⃗s
=
Fz(x, y + ∆y/2, z)∆z ≃
"
Fz(x, y, z) + ∆y
2
∂Fz
∂y
#
∆z
Z d
c⃗F · d⃗s
=
Fy(x, y, z + ∆z/2)(−∆y) ≃−
"
Fy(x, y, z) + ∆z
2
∂Fy
∂z
#
∆y
Z a
d⃗F · d⃗s
=
Fz(x, y −∆y/2, z)(−∆z) ≃−
"
Fz(x, y, z) −∆y
2
∂Fz
∂y
#
∆z .
Adding these together, we have
I
abcd⃗F · d⃗s =
 ∂Fz
∂y −∂Fy
∂z
!
∆y∆z ,
which tells us that
h
curl⃗F
i
x
=
lim
∆z,∆y→0
H
abcd⃗F · d⃗s
∆z∆y
=
 ∂Fz
∂y −∂Fy
∂z
!
.
This is the x component of the curl because, by right-hand rule, that is the orientation of
the square.
43


## Page 11

If we repeat this exercise for squares oriented parallel to the x −y planes and the x −z
planes, we ﬁnd
h
curl⃗F
i
y
=
 ∂Fx
∂z −∂Fz
∂x
!
h
curl⃗F
i
z
=
 ∂Fy
∂x −∂Fx
∂y
!
.
There’s a nice trick that we can use to work out these two components: we use cyclic
permutation to ﬂip around the axes. This means we just cyclic the labels, which is equivalent
to rotating the axes around. To get
h
curl⃗F
i
y, take the answer for
h
curl⃗F
i
x, and permute
the coordinate indices: x becomes y, y becomes z, z becomes x. Do it one more time, and
you’ve got the answer for
h
curl⃗F
i
z.
Putting all of this together, we have
curl⃗F
=
 ∂Fz
∂y −∂Fy
∂z
!
ˆx +
 ∂Fx
∂z −∂Fz
∂x
!
ˆy +
 ∂Fy
∂x −∂Fx
∂y
!
ˆz
=⃗
∇×⃗F .
Just as the divergence is nicely expressed using the gradient operator and the dot product,
the curl is nicely expressed using the gradient operator and the cross product.
4.8
Wrap up and summary
That was a lot of math. Let’s summarize all of these results:
4.8.1
Gauss’s theorem
dA
F
surface S
enclosing
V
volume
I
S⃗F · d⃗A =
Z
V div⃗FdV
The surface S is the boundary of the volume V .
44


## Page 12

4.8.2
Stokes’s law
                                                                                                                                                          

























































































































































bounding
surface S
curve C
I
C⃗F · d⃗s =
Z
S curl⃗F · d⃗A .
The curve C is the boundary of the surface S.
4.8.3
Gradient theorem
We only discussed this in detail for the electric potential, but the following rule holds for
any1 scalar function:
f(⃗b) −f(⃗a) =
Z⃗b⃗
a⃗∇f · d⃗s .
This holds for any path from the point⃗a to⃗b:
pointb
ds
pointa
grad
curve C
f
We will use these results many times as this course progresses.
1Except for some really bizarre ones which we will never encounter in this class.
45
