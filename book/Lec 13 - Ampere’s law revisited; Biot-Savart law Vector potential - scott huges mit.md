# Lec 13 - Ampere’s law revisited; Biot-Savart law Vector potential - scott huges mit

> Source: `Lec 13 - Ampere’s law revisited; Biot-Savart law Vector potential - scott huges mit.pdf`  
> Pages: 8


## Page 1

Scott Hughes
29 March 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 13:
Ampere’s law revisited; Biot-Savart law
Vector potential
13.1
Return to the magnetic ﬁeld
13.1.1
What we did before
Let’s quickly recap the major facts we’ve gone over regarding the magnetic ﬁeld. A charge
q moving with velocity⃗v in a magnetic ﬁeld⃗B feels a force⃗
F = q⃗v
c ×⃗B .
Magnetic ﬁelds arise from ﬂowing currents. The integral of⃗B along a closed path C the is
related to the current enclosed by the path by Ampere’s law:
I
C⃗B · d⃗s = 4π
c Iencl .
If we apply this law to a long wire we ﬁnd⃗
B(r) = 2I
cr
ˆφ .
where r is the distance to the wire and ˆφ is related to the direction in which the current ﬂows
by the right-hand rule: point your right-hand thumb in the direction in which the current
ﬂows and ˆφ curls around in the direction of your ﬁngers.
By placing many long wires next to each other and invoking superposition, we found the
magnetic ﬁeld of a sheet of current:
L
x
θ
y
In the limit of L →∞, but holding the current per unit length in the sheet K ≡I/L
constant, we found that⃗
B = +2πK
c
ˆx
119


## Page 2

above the plane, and⃗
B = −2πK
c
ˆx
below the plane.
The key observation here is that the change in the magnitude of the
magnetic ﬁeld as we cross the current is given by
|∆⃗B| = 4πK
c
.
This should be reminiscent of the change in electric ﬁeld when we cross a sheet of charge,
|∆⃗E| = 4πσ.
Taking the divergence of the wire’s⃗B-ﬁeld, we ﬁnd⃗
∇·⃗B = 0 .
Although we have only shown this holds for a speciﬁc example, this rule holds for all magnetic
ﬁelds that arise from currents. Physically, it tells us that — as far we can tell — there is no
such thing as an isolated magnetic charge. The smallest “chunks” of magnetic ﬁeld that we
can ﬁnd come in a dipole conﬁguration, with “north” and “south” poles. We never ﬁnd an
isolated “north” pole, with radial ﬁeld lines.
13.1.2
Ampere’s law revisited
Using Stoke’s theorem, we can rewrite the line integral of the⃗B ﬁeld in terms of its curl:
I
C⃗B · d⃗s =
Z
S(⃗∇×⃗B) · d⃗a .
S is any surface bounded by the curve C. This is a nice result, since the current enclosed by
C is given by an integral through the same surface S:
Iencl =
Z
S⃗J · d⃗a .
Putting these two results together, Ampere’s law becomes
Z
S(⃗∇×⃗B) · d⃗a = 4π
c
Z
S⃗J · d⃗a
Z
S
µ⃗
∇×⃗B −4π
c⃗J
¶
· d⃗a = 0 .
We ﬁnally obtain
−→⃗∇×⃗B = 4π
c⃗J .
This last equation is also called Ampere’s law — it expresses the same physics as
H
C⃗B ·d⃗s =
4πI/c, but in diﬀerential rather than integral form. If we had been doing this analysis in SI
units rather than cgs, we would have ended up with
−→⃗∇×⃗B = µ0⃗J .
120


## Page 3

It’s worthwhile to pause at this moment and collect the various divergence and curl
equations for⃗E and⃗B that we have so far:⃗
∇·⃗E
=
4πρ ,⃗
∇·⃗B = 0⃗
∇×⃗E
=
0 ,⃗
∇×⃗B = 4π
c⃗J .
These are Maxwell’s equations for static ﬁelds and steady currents. They are what you see
on the t-shirts whenever all time derivatives go to zero. Their SI versions are⃗
∇·⃗E
=
ρ/ϵ0 ,⃗
∇·⃗B = 0⃗
∇×⃗E
=
0 ,⃗
∇×⃗B = µ0⃗J .
13.2
The vector potential
13.2.1
Deﬁnition
Recall that for static electric ﬁelds, we have⃗
E = −⃗∇φ .
We motivated this rule from arguments based on work and energy — namely, that the
potential diﬀerence between any two points is just the work it takes (per unit charge) to
move a charge between those two points. However, it has an important and useful side
eﬀect: it “guarantees” that our electric ﬁelds are curl free:⃗
∇×⃗E = 0
since⃗
∇×⃗∇f = 0
for any scalar function f.
Can we do anything similar with the magnetic ﬁeld? In this case, the equation which we
would like to enforce is the rule⃗
∇·⃗B = 0 .
Can we pick a form of⃗B that guarantees this equation holds? Well, obviously, or I wouldn’t
have wasted the time to type this up: as you proved on Pset 3, the divergence of the curl of
any function is zero. This suggests that we can write⃗B as the curl of some vector function⃗
A:⃗
∇×⃗A =⃗B .
The function⃗A is called the “vector potential”.
The key thing to bear in mind is that
it is introduced to enforce the rule⃗∇·⃗B = 0, in the same way that⃗E = −⃗∇φ enforces⃗
∇×⃗E = 0. Unlike the scalar potential φ, however,⃗A has no connection to work or energy.
For our purposes at least, its only use is to facilitate some of our calculations1.
1It turns out to have a very real physical meaning in quantum mechanics, though.
121


## Page 4

13.2.2
Non-uniqueness
In electrostatics, we were able to prove a uniqueness theorem: once boundary conditions
were set, there was one — and only one — potential for a given charge distribution, meaning
that for every⃗E ﬁeld there was only one potential φ.
This is not the case for the vector potential! It is actually the case that an inﬁnite number
of vector potential functions correspond to a particular magnetic ﬁeld⃗B. Consider a uniform
magnetic ﬁeld:⃗B = B0ˆz. Our only requirement on the vector potential⃗A is that its curl
reproduce this ﬁeld. In other words, we need
Bx
=
∂Az
∂y −∂Ay
∂z = 0
By
=
∂Ax
∂z −∂Az
∂x = 0
Bz
=
∂Ay
∂x −∂Ax
∂y = B0 .
One vector potential which satisﬁes these conditions is⃗
A = xB0ˆy .
Another is⃗
A = −yB0ˆx .
Still another is given by combining these:⃗
A = −1
2yB0ˆx + 1
2xB0ˆy .
These are all valid choices. Given this freedom, it might seem like there’s no point in selecting
any particular solution. In fact, we end up taking the opposite viewpoint: Since any one of
these solutions is valid, let’s pick the one that is — in some manner that we must specify —
particularly convenient. In the next subsection, we describe a particular choice that allows
us to write down an equation that looks a lot like Poisson’s equation, but that holds for⃗A.
13.2.3
Poisson’s equation for⃗A
When we plugged the deﬁnition⃗E = −⃗∇φ into Gauss’s law,⃗∇·⃗E = 4πρ, we ended up with
Poisson’s equation,
∇2φ = −4πρ .
What happens if we plug⃗∇×⃗A =⃗B into Ampere’s law,⃗∇×⃗B = 4π⃗J/c? First, we need to
work out the curl of the curl: with a fair amount of tedious algebra you should be able to to
show that⃗
∇×⃗∇×⃗A =⃗∇
³⃗
∇·⃗A
´
−∇2⃗A .
This is in principle a horrible mess. However, we can take advantage of the non-uniqueness
of⃗A to simplify it. We have the freedom to choose our⃗A in such a way that it has no
divergence:⃗
∇·⃗A = 0 .
122


## Page 5

This is called a “gauge choice”. Some of you will study this notion in far greater detail in
future courses. For now, you simply need to take away the notion that the non-uniqueness
of⃗A gives us enough freedom to tinker around until the condition⃗∇·⃗A = 0 is guaranteed to
be met. (It still leaves us a lot of freedom. You can easily verify that all three of the choices
for⃗A we wrote down in the previous subsection satisfy⃗∇·⃗A = 0.)
Imposing this condition, we then have⃗
∇×⃗∇×⃗A = −∇2⃗A .
Let’s now plug this into Ampere’s law: we have⃗
∇×⃗B
=
4π
c⃗J⃗
∇×⃗∇×⃗A
=
4π
c⃗J
−→∇2⃗A
=
−4π
c⃗J .
This is kind of a goofy equation. In cartesian coordinates, it is best understood component
by component. Basically, it means that each component of⃗A is related to a component of⃗
J by the Laplacian operator:
∇2Ax
=
−4π
c Jx
∇2Ay
=
−4π
c Jy
∇2Az
=
−4π
c Jz .
Let’s look back at electrostatics again for a moment. Poisson’s equation, ∇2φ = −4πρ,
has as its solution the general equation for potential,
φ =
Z
V
ρ dV
r
.
Our Poisson equation for the vector potential is the exact same thing, provided we replace
φ with⃗A and ρ with⃗J/c:⃗
A = 1
c
Z
V⃗
J dV
r
.
For a current I ﬂowing in a wire, this equation becomes⃗
A = I
c
Z
along wire
d⃗l
r ,
where d⃗l points along the wire.
123


## Page 6

13.3
The Biot-Savart law
Using the last result we derived — the vector potential of wire — we can work out another
very important result. By taking the curl of that vector potential, we derive the magnetic
ﬁeld of a wire:⃗
B
=⃗
∇× I
c
Z
along wire
d⃗l
r
=
I
c
Z
along wire⃗∇× d⃗l
r .
We can take the “⃗∇×” under the integral since the limits of integration do not change when
we take the derivative. Next, we use⃗
∇× d⃗l
r =
µ1
r
¶⃗
∇× d⃗l +⃗∇
µ1
r
¶
× d⃗l .
(This follows from stuﬀyou did on pset 3.)⃗∇× d⃗l = 0 since d⃗l is a just a diﬀerential length
along the wire, and⃗∇(1/r) = −ˆr/r2. We ﬁnd⃗
∇× d⃗l
r = d⃗l × ˆr
r2
where we’ve used⃗a×⃗b = −⃗b×⃗a to get rid of the minus sign. We thus ﬁnally can write down
the magnetic ﬁeld of the wire:⃗
B = I
c
Z
along wire
d⃗l × ˆr
r2
.
This result is known as the Biot-Savart formula for the magnetic ﬁeld. It plays roughly the
same role in determining the magnetic ﬁeld from a current that Coulomb’s law plays setting
the electric ﬁeld from charges.
124


## Page 7

13.3.1
Field of a ring of current
The Biot-Savart law allows us to work out the magnetic ﬁeld of an interesting special case:
a ring of current.
θ
z
Take the ring to have radius R, and consider a current of magnitude I circulating as shown.
What is the magnitude and direction of the current a point z above the ring’s center?
Set up Biot-Savart:⃗
B = I
c
Z
around ring
d⃗l × ˆr
r2
.
The distance r is easy — r =
√
z2 + R2. Likewise, the magnitude |d⃗l| is easy — |d⃗l| = Rdφ,
where φ is an angle around the perimeter of the ring. The cross product d⃗l × ˆr is a little bit
trickier. A good way to understand it is to consider a special case: when z = 0, d⃗l × ˆr points
in the vertical ˆz direction. Moving away from this case, we see that it always points along
ˆz, but is reduced by a factor of sin θ in general:⃗
B
=
I
c
Z 2π
0
R sin θ dφ
R2 + z2 ˆz
=
I
c
Z 2π
0
R2 dφ
(R2 + z2)3/2 ˆz
=
2πI
c
R2
(R2 + z2)3/2 ˆz .
Notice that the direction, ˆz, could have been predicted by the right-hand rule: curl your
ﬁngers of your right hand in the direction of the current, and your thumb points along the
ﬁeld. Note also that it points in the same direction above and below the loop.
13.3.2
The solenoid
Suppose we stack a bunch of rings like this on top of one another. What is the magnetic
ﬁeld at the center of the cylinder that we make?
We answer this by adding up the magnetic ﬁelds from many rings. Let the total height
of the stack be L. Further, let the total amount of current circulating through all of the
125


## Page 8

rings be I. The total current per unit length ﬂowing through the stack is thus K = I/L.
The contribution to the magnetic ﬁeld from a height z above the center and from a ring of
thickness dz is then
d⃗B
=
2π
c
I dz
L
R2
(R2 + z2)3/2 ˆz
=
2Kπ
c
R2 dz
(R2 + z2)3/2 ˆz
The total magnetic ﬁeld is given by integrating this over z:⃗
B = 2πK
c
ˆz
Z L/2
−L/2
R2 dz
(R2 + z2)3/2 .
This integral turns out to be quite easy to do: since
Z L/2
−L/2
R2 dz
(R2 + z2)3/2 =
2L
√
L2 + 4R2
the answer is just⃗
B = 4πK
c
L
√
L2 + 4R2 ˆz
→4πKˆz
c
as L →∞.
This conﬁguration is known as a “solenoid”. The last formula (the L →∞limit) is accurate
enough (provided L ≫R) that it is often used even for ﬁnite length solenoids.
This value turns out to describe the magnetic ﬁeld throughout the interior for L ≫R!
Note that the value is exactly what we got for change of ﬁeld when we cross a current sheet:
in a very long solenoid, there is no ﬁeld on the outside, but it suddenly jumps to 4πK/c on
the inside. Because of this, solenoids play a role with for magnetic ﬁelds similar that played
by parallel plate capacitors for electric ﬁelds: they are devices which “contain” the ﬁeld in
some isolated region.
In practice, solenoids are constructed by wrapping wires around a tube to make a cylin-
drical geometry. If we can wrap our wires n times per unit length (for example, we may have
n = 10 turns/cm), then K = nI.
126
