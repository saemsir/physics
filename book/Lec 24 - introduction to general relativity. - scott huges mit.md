# Lec 24 - introduction to general relativity. - scott huges mit

> Source: `Lec 24 - introduction to general relativity. - scott huges mit.pdf`  
> Pages: 6


## Page 1

Scott Hughes
12 May 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 24:
A (very) brief introduction to general relativity.
24.1
Gravity?
The Coulomb interaction between two point charges looks essentially identical to the grav-
itational interaction between two masses. Does this mean that everything we have done so
far can also be used to describe gravitational interactions (perhaps with some slight modiﬁ-
cations)?
The answer to this turns out to be almost — but not quite. To understand what this
means in detail, we need to do a little bit of background work. The key point to be made
here is that Maxwell’s equations and electricity and magnetism are relativistically correct:
all of E&M “knows about” special relativity, in the sense that the equations make sense
in any frame of reference. (When we transform reference frames, we modify the⃗E and⃗B
ﬁelds according to those relativistic transformation laws we all learned to love ages ago.
However, the new ﬁelds still satisfy Maxwell equations.) This is NOT the case for gravity!
Signiﬁcant modiﬁcations need to be made to make gravity relativistic. What we end up with
is Einstein’s theory of general relativity. In this lecture we will look at some basic properties
of general relativity.
To begin, we need to introduce a bit of notation.
24.2
4-vectors
Since space and time are uniﬁed in relativity, it doesn’t make much sense to treat them
separately. Accordingly, many concepts are described using 4-vectors, quantities that are
essentially just like the vectors we’ve known and loved since kindergarten, but with an extra
“timelike” component. For example, the position 4-vector is written
xµ = (ct, x, y, z) .
The way to read this is that µ is an index, ranging from 0 to 3: x0 = xµ=0 = ct; x1 = xµ=1 = x;
x2 = xµ=2 = y; x3 = xµ=3 = z. Whenever you see an x with a number superscript, it means
the index — it does NOT mean take it to a higher power! This system can be a little
confusing when you ﬁrst encounter it.
That the “timelike component of position” is time makes perfect sense. What do we
get when we try to make something like momentum into a 4-vector? It turns out that the
“timelike component of momentum” is the energy:
pµ = (E/c, px, py, pz) .
We’ll introduce a few other 4-vectors before we’re done here.
220


## Page 2

24.2.1
Invariant interval
Back on Pset 6, we showed that the quantity
∆s2 = −c2∆t + ∆x2 + ∆y2 + ∆z2
is invariant: all inertial observers agree on its value. This can be written this in terms of a
quantity called the metric:
∆s2 =
3
X
µ=0
3
X
ν=0
gµν∆xµ∆xν
where the metric tensor gµν can be represented as a 4 × 4 matrix:
gµν =





−1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
1




.
This relation is usually written using the Einstein summation convention: repeated indices
are assumed to be summed from 0 to 3.
In this convention, the invariant interval then
becomes
∆s2 = gµν∆xµ∆xν .
We will use this notation from now on.
24.2.2
Covariant versus contravariant
The 4-vectors that we have introduced so far are, technically speaking, written in terms of
contravariant components. Using the metric, we deﬁne a new version of our 4-vector:
xµ
≡
gµνxν
=
(−ct, x, y, z) .
The eﬀect is just to change the sign of the timelike component.
It should be noted that there is no physics in this operation. The diﬀerence between
“index up” (contravariant) and “index down” (covariant) is just needed to make sure that
the math works out right. In particular, in writing down quantities that matter for physics,
you typically end up summing over repeated indices. When we do this, the index has to be
down on one quantity and up on the other.
24.2.3
Derivatives
Finally, one handy notational deﬁnition: we write
∂µ ≡
∂
∂xµ ,
∂µ ≡
∂
∂xµ
.
There’s absolutely nothing deep about this! However, it makes certain quantities look nice.
Notice that ∂0 = (1/c)∂/∂t = −∂0.
221


## Page 3

24.3
Electric & magnetic ﬁelds?
Can we make a 4-vector that incorporates electric and magnetic ﬁelds? With a little thought,
we see that the answer to this has to be no — the three components of electric ﬁelds and
the three components of magnetic ﬁelds are 6 separate numbers. A 4-vector — pretty much
by deﬁnition! — only has 4 separate numbers.
What we can do is make a 4-vector out of the magnetic vector potential. We use the
electrostatic scalar potential as the time component, and ﬁnd
Aµ = (φ, Ax, Ay, Az) .
(Note that in cgs, φ and⃗A have the same units.) How do we get ﬁelds from this potential?
We take a derivative! The one that we want turns out to be
F µν ≡∂Aν
∂xµ
−∂Aµ
∂xν
.
This tensor contains EXACTLY the quantities that we want! When we write out the tensor
Fµν, we see that its components are given by
F µν =





0
Ex
Ey
Ez
−Ex
0
Bz
−By
−Ey
−Bz
0
Bx
−Ez
By
−Bx
0




.
The tensor is often called the Faraday tensor.
Although it’s not so simple to see where this one comes from, there’s a second tensor we
can construct in a similar manner, often just called the Dual Faraday tensor:
∗F µν =





0
Bx
By
Bz
−Bx
0
−Ez
Ey
−By
Ez
0
−Ex
−Bz
−Ey
Ex
0





We’ll discuss the point of introducing this “dual” form in just a moment.
A second 4-vector we can naturally make is for the source: we combine the vector current
density with charge density ρ to make
Jµ = (ρc, Jx, Jy, Jz) .
Using this, we can write Maxwell’s equations in a very simple form:
∂νF µν = 4π
c Jµ ,
∂∗
µF µν = 0 .
Expand one example: The F µν equation for µ = 0. Then,
∂F 0ν
∂xν = 4π
c J0
∂F 0x
∂x
+ ∂F 0y
∂y
+ ∂F 0z
∂z
= 4π
c (cρ)
∂Ex
∂x + ∂Ey
∂y + ∂Ez
∂z = 4πρ
−→⃗
∇·⃗E = 4πρ
222


## Page 4

If you expand and combine the F µν equation for µ = 1, 2, 3, you get
−1
c
∂⃗E
∂t +⃗∇×⃗B = 4π
c⃗J
−→⃗
∇×⃗B = 1
c
∂⃗E
∂t + 4π
c⃗J .
Likewise, the µ = 0 part of the ∗F µν equation gives us⃗
∇·⃗B = 0 ;
the µ = 1, 2, 3 parts give us⃗
∇×⃗E = −1
c
∂⃗B
∂t .
24.4
General relativity
We’ve now got enough background that we can now sketch the general theory of relativ-
ity. Without going into too much detail the key quantity we need to describe gravity in a
relativistic manner is the metric: our starting point is the equation
ds2 = gµνdxµdxν .
Rather than being constant, as it was in special relativity, the metric is a varying function
in general relativity. This turns out to mean that spacetime has curvature. All of gravity is
encoded in the mathematics of this curvature.
The metric plays the same role for gravity that the 4-vector Aµ plays in electricity and
magnetism — think of it as a “potential” for gravity. The equivalent of Maxwell’s equations
are the Einstein Field Equations:
Gµν = 8πG
c4 Tµν .
Some explanation of this equation is in order. On the right-hand side, the tensor Tµν —
called the “stress-energy tensor” — describes the ﬂow of 4-momentum. This tensor plays a
role in these equations analogous to that of J µ in Maxwell’s equations. A component Tµν
describes the ﬂow of the µ component of 4-momentum in the ν direction, in the same way
that Jµ describes the ﬂow of charge in the µ direction. For example, T00 describes the ﬂow of
the zero component of 4-momentum into the time direction; this turns out to be the energy
density. Components like T0x describe the ﬂow of energy in the x direction. This is related
to the mass density ρm and the velocity with which mass ﬂows.
The tensor Gµν is, in general, an enormous mess: it is found by applying a 2nd order,
coupled nonlinear diﬀerential operator to the metric gµν. The key thing to note is that,
roughly speaking, it corresponds to two derivatives of the metric. Thus Einstein’s equations
are of the form “two derivatives of the potential (metric) equals the source”, exactly as
Maxwell’s equations are.
223


## Page 5

24.4.1
Gravitational “forces”
Before moving on, we should talk about gravitational forces. In electricity and magnetism,
the force that operates upon charges is⃗
FE&M = q
h⃗
E + (⃗v/c) ×⃗B
i
.
In general relativity, it turns out that there is no such thing as a gravitational force! Instead,
what happens is that bodies move along a trajectory of extremal time. To understand what
this means, go back to the deﬁnition of the invariant interval:
ds2 = gµνdxµdxν .
For a body following a trajectory through spacetime, ds2 = −c2dτ 2, where τ describes the
time as measured on a clock on that body. The path that the body follows through spacetime
and the gravitational “forces” that act on it are found by working out the extremum of the
total time τ that accumulates during its travels. The details of that calculation are somewhat
beyond 8.022 — suﬃce it to say that it is a well-founded calculation.
An analogy helps to explain what is going on. Suppose we’re on a ﬂight from Boston to
Tokyo. To save fuel, we want the trip to be as short as possible. The shortest path between
two points is a straight line. But, on a round globe, what does “straight line” really mean?
We go back to the old fashioned deﬁnition we learned in kindergarten: a “straight line” is
the path which gives the shortest distance between two points. This is why a ﬂight from
Boston to Tokyo might actually go over the North Pole.
On a map, this ﬂight might look crazy — it looks like you’re bending the trajectory of
the plane in as stupid a way possible. A person who believes in the reality of maps — as
opposed to the reality of the earth — might say that the reason for this crazy trajectory is
that “forces” act on the plane in such a way that the path over the North Pole is “easier”
to follow than a simple logical “straight” line (straight according to the map, that is).
In general relativity, gravitational “forces” are like the ﬁctional forces to which our map
worshipper ascribes the airplane’s trajectory.
24.5
A special metric
It turns out that the spacetime metric outside of a rotating body is given by
ds2 = −(1 + 2Φ)(c2dt2) + (dx −βxdt)2 + (dy −βydt)2 + (dz −βzdt)2 .
(Strictly speaking, this is an approximate result, only holding under certain conditions —
namely that the body can’t be too dense, and that its internal velocities must be much less
than the speed of light.) The quantities βx, βy, and βz are components of a vector⃗β that
has units of velocity.
If we run this metric through our procedure to ﬁnd maximal time, we ﬁnd that the “force”
that acts on a body is given by
md2⃗x
dt2 = m⃗g + m(⃗v/c) ×⃗H ,
where⃗
g = −⃗∇Φ ,⃗
H
=⃗
∇×⃗β .
224


## Page 6

Notice that this force law looks EXACTLY like an electromagnetic force! In general relativity,
the gravitational force looks just like the normal Newtonian force — encapsulated in the
gravitational ﬁeld⃗g — is supplemented by a gravitomagnetic force arising from a ﬁeld⃗H
that acts just like a magnetic ﬁeld.
If we run this metric through Einstein’s ﬁeld equations, we ﬁnd⃗
∇·⃗g
=
−4πGρm
(Gravitational Gauss’s law)⃗
∇·⃗H
=
0⃗
∇×⃗g
=
0⃗
∇×⃗H
=
−16πG⃗Jm
c
(Gravitational Ampere’s law)
where⃗
Jm
=
ρm⃗v .
The equations which ﬁx the gravitational ﬁelds⃗g and⃗H look almost EXACTLY like Maxwell’s
equations! There are some important diﬀerences. Notice that the signs are reversed compared
to the Maxwell equations. This is because gravity is always an attractive force. If the force
between two masses were repulsive, we would ﬁnd a + sign for the⃗∇·⃗g. There is also a
factor of 4 diﬀerence on the Ampere’s law. This is harder to explain; it is related to the fact
that the gravitational “potential” is a 2 index tensor, rather than a 1 index vector.
This analogy continues. If we move a gyroscope with an angular momentum vector⃗s
through this spacetime, it precesses: the vector feels a torque according to
d⃗s
dt = 1
2⃗s ×⃗H
— an equation that is very similar to the torque felt by a magnetic dipole in a magnetic
ﬁeld,⃗τ =⃗m ×⃗B.
These relativistic eﬀects are ordinarily quite small and don’t play much of an important
role. Nonetheless, they are not zero. Last year, NASA launched a satellite to try to measure
this “gravitomagnetic precession”.
This satellite, called Gravity Probe B1 consists of an
extremely precise and sensitive gyroscope that very slowly changes the direction of its angular
momentum due to the gravitomagnetic ﬁeld induced by earth’s rotation. The net eﬀect
accumulated eﬀect is about 41 milliarcseconds (1.1 × 10−5 degrees) per year. It’s quite an
amazing technological feat to be able to measure such a puny eﬀect!
These eﬀects play a much more robust role when gravitational ﬁelds and rotation speeds
are stronger. In this case, the metric we used above is not really all that accurate. At
least qualitatively, however, this picture of a Newtonian-like gravitational ﬁeld⃗g and a
gravitomagnetic ﬁeld⃗H, remains useful. The extra “force” arising from the gravitomagnetic
ﬁelds are extremely strong and important! We look for such eﬀects when we study objects in
orbit around neutron stars and black holes — we use this gravitomagnetic eﬀect as a means
of learning about things in the universe.
1Gravity Probe A tested the fact that clocks run slow in gravitational ﬁelds.
225
