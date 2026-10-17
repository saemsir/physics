# Lec 5 - Fields and potentials around conductors The electrostatic uniqueness theorem - scott huges mit- lec 5

> Source: `Lec 5 - Fields and potentials around conductors The electrostatic uniqueness theorem - scott huges mit- lec 5.pdf`  
> Pages: 8


## Page 1

Scott Hughes
15 February 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 5:
Fields and potentials around conductors
The electrostatic uniqueness theorem
5.1
Conductors
For much of the rest of this class, we will be concerned with processes that involve conductors:
materials in which it is easy for charges to move around. We will discuss conductors in some
depth when we discuss currents; for now, we will just summarize a few of their properties.
Among the best conductors are metals — silver, gold, copper, aluminum, etc. The atoms
of these metals form a crystalline structure in which electrons can easily hop around from
atom to atom. Although a chunk of metal is neutral overall, we can visualize it as being
made of lots of positive charges that are nailed in place, paired up with lots of negative
charges (electrons) that are free to move around. In isolation, the negative charges will sit
close to the positive charges, so that the metal is not only neutral overall, but also largely
neutral everywhere (no local excess of positive or negative charge). Under the inﬂuence of
some external ﬁeld, the electrons are free to move around.
Some materials conduct OK, but are not as good as metals. For example, salty water
has lots of charges that are free to move around under the inﬂuence of an⃗E ﬁeld. However,
since these charges — usually sodium and chlorine ions — are far more massive than an
electron, and they do not ﬂow in a crystaline structure, salty water is not a very high quality
conductor. Another example is graphite: the somewhat unusual bond structure of graphite
makes it a fairly good conductor, but only in certain directions.
At the opposite end of the spectrum are insulators: materials in which the electrons are
bound quite tightly to the constituent molecules and hence have essentially no freedom to
move. Insulators are typically made from organic materials such as rubber or plastic, or
from crystals formed from strong covalently bounded molecules, such as quartz or glass.
The eﬀectiveness of a substance as a conductor is quantiﬁed by its resistivity, a number
that expresses how well it resists the ﬂow of current. We will revisit this quantity in about a
week when we discuss currents in detail; for now, suﬃce to say that small resisitivity means
a good conductor. In SI units, resistivity is measured in “Ohm-meters” (usually written
Ω-m); in cgs units, resistivity turns out to be measured in seconds. Here are a few example
values:
46


## Page 2

Material
Resistivity (Ω-m)
Resistivity (sec)
Silver
1.6 × 10−8
1.8 × 10−17
Copper
1.7 × 10−8
1.9 × 10−17
Gold
2.4 × 10−8
2.6 × 10−17
Iron
1.0 × 10−7
1.1 × 10−16
Sea water
0.2
2.2 × 10−10
Polyethylene
2.0 × 1011
220
Glass
∼1012
∼103
Fused quartz
7.5 × 1017
8.3 × 108
As you can see, the resistivity of ordinary materials varies over an enormous range,
reﬂecting the very diﬀerent electronic properties of materials around us.
5.2
Electric ﬁelds and conductors
For the rest of this lecture, we will assume that conductors are materials that have an inﬁnite
supply of charges that are free to move around. (This of course just an idealization; but, it
turns out to be an extremely good one. Real conductors in fact behave very similar to this
limit.) From this, we can deduce a few important facts about conductors and electrostatic
ﬁelds:
• There is no electric ﬁeld inside a conductor. Why? Suppose we bring a plus
charge near a conductor. For a very short moment, there will be an electric ﬁeld inside
the conductor. However, this ﬁeld will act on and move the electrons, which are free
to move about. The electrons will move close to the plus charge, leaving net positive
charge behind. The conductor’s charges will continue to move until the “external”⃗
E-ﬁeld is cancelled out — at that point there is no longer an⃗E-ﬁeld to move them, so
they stay still.
+
+
+
+
+
−−
−−
Figure 1: Conductor near an external charge. The charges in the conductor very quickly
rearrange themselves to cancel out the external ﬁeld.
A more accurate statement of this rule is “After a very short time, there is no
electric ﬁeld inside a conductor”. How short a time is it? Recall that in cgs units,
47


## Page 3

resistivity (which tells us how good/bad something conducts electricity) is measured
in seconds. It turns out that the time it takes for the charges to rearrange themselves
to cancel out the external⃗E-ﬁeld is just about equal to this resistivity. For metals,
this is a time that is something like 10−16 −10−17 seconds. This is so short that we
can hardly complain that the original statement isn’t precise enough!
• The electric potential within a conductor is constant. Proof: the potential
diﬀerence between any two points⃗a and⃗b inside the conductor is
φb −φa
=
−
Z⃗b⃗
a⃗E · d⃗s
=
0
since⃗E = 0 inside the conductor.
Hence, for any two points⃗a and⃗b inside the
conductor, φb = φa.
• Net charge can only reside on the surface of a conductor. This is easily proved
with Gauss’s law: make a little Gaussian surface that is totally contained inside the
conductor. Since there is no⃗E-ﬁeld inside the conductor,
H⃗E · d⃗A is clearly zero for
your surface. Since that is equal to the charge the surface contains, there can be no
charge.
We will discuss the charge on the conductor’s surface in a moment.
• Any external electric ﬁeld lines are perpendicular to the surface. Another
way to put this is that there is no component of electric ﬁeld that is tangent to the
surface. We prove this by contradiction: suppose that a component of the⃗E-ﬁeld were
tangent to the surface. If that were the case, then charges would ﬂow along the surface.
They would continue to ﬂow until there was no longer any tangential component to
the⃗E-ﬁeld. Hence, this situation cannot exist: even if it exists momentarily, it will
rapidly (within 10−17 seconds or so) correct itself.
• The conductor’s surface is an equipotential. This follows from the fact that the⃗
E-ﬁeld is perpendicular to the surface. We do a line integral of⃗E on the surface; the
path is perpendicular to the ﬁeld; so the diﬀerence in potential between any two points
on the surface is zero.
A few important corollaries follow from these rules.
• Corollary 1: Consider a conductor with a hollowed out region. If there is no charge
in this hollow, then the potential φ there is constant. It follows that the electric ﬁeld
−⃗∇φ inside the hollow is zero.
We will prove this carefully shortly. For now, we can motivate this proof by noting
that the surface of the conductor must be an equipotential. Since there is no charge
anywhere on the inside, the interior potential must obey Laplace’s equation, ∇2φ = 0.
Solutions to Laplace’s equation can have no local maxima or minima. The only solution
that has some proscribed constant value on an exterior boundary and has no local
maxima or minima is one that is constant.
48


## Page 4

φ = constant
E = 0
+
−
−
+
+
+
+
+
+
+
−
−
−
−
−
−
By putting things inside a conducting box, it is shielded from any external electric ﬁeld.
Such an arrangement is known as a Faraday cage. Although it is beyond the scope of
this course to prove this, Faraday cages work pretty well even when the external ﬁelds
vary in time, as long as they don’t vary too quickly.
• Corollary 2: suppose we put a charge q inside this hollow. There must be an induced
layer of surface charge on the wall of the hollow; the total amount of induced charge
in this layer is qind = −q.
q
+
−
−
−
−
−
−
−
Figure 2: Gaussian surface: dashed line enclosing hollow and induced negative charge.
To prove this, use Gauss’s law.
We draw a Gaussian surface that lies inside the
conductor. The⃗E-ﬁeld there is zero, so the total electric ﬂux must be zero. This
ﬂux equals 4π times the total charge contained by the surface, which is q plus the
induced charge:
I⃗
E · d⃗A
=
0
=
4π(q + qind)
→qind
=
−q .
49


## Page 5

You should be able to prove with another well chosen Gaussian surface that the con-
ductor has another layer of charge on its outer surface with total magnitude +q.
• Corollary 3: The induced charge density on any surface is given by |⃗E|/4π, where⃗E
is the electric ﬁeld right next to the surface. This follows from the rule that whenever
there is a surface charge layer, the electric ﬁeld changes with ∆E = 4πσ. Since the
ﬁeld inside the conductor is zero, ∆E = |⃗E|.
5.3
The uniqueness theorem
Suppose we know that some region contains a charge density ρ(⃗r). Suppose we also know
the value of the electronstatic potential φ(⃗r) value on the boundary of this region. The
uniqueness theorem then guarantees that there is only one function φ(⃗r) which describes the
potential in that region. This means that no matter how we ﬁgure out φ’s value — guessing,
computer aided numerical computation, demonic invocation — the function φ we ﬁnd is
guaranteed to be the one we want.
We prove this theorem by assuming it is not true: we assume that two functions, φ1(⃗r)
and φ2(⃗r), both satisfy Poisson’s equation:
∇2φ1(⃗r)
=
−4πρ(⃗r)
∇2φ2(⃗r)
=
−4πρ(⃗r) .
Both of these functions must satisfy the boundary condition: we must have φ1(⃗r) = φ2(⃗r) =
φB(⃗r) on the boundary of our region.
By the principle of superposition, any combination of the potentials φ1(⃗r) and φ2(⃗r) must
be a perfectly valid potential. (It’s not the potential that describes our region, but it still
is valid as far as the general laws of physics are concerned.) Let’s look in particular at
φ3(⃗r) = φ2(⃗r) −φ1(⃗r). First, what is the boundary condition for φ3? Since φ1 = φ2 on the
boundary, we must have φ3 = 0 there. Next, apply the Laplacian to φ3:
∇2φ3
=
∇2 (φ2 −φ1)
=
∇2φ2 −∇2φ1
=
4πρ −4πρ = 0 .
The potential φ3 thus satisﬁes Laplace’s equation. This means that it can have no local
maxima or minima inside its boundary. But, on the boundary, its value is zero! The only
function which is zero on a boundary and has no local maxima or minima is one which
is zero everywhere in the region: φ3(⃗r) = 0. This means that φ1(⃗r) = φ2(⃗r) — our initial
assumption, that at least two potentials satisﬁed Poisson’s equation in the region with the
given boundary condition, was wrong. Hence the solution for φ(⃗r) is unique. Putting it
concisely, we have proved the uniqueness theorem: An electrostatic potential φ(⃗r) is
completely determined within a region once its value is known on the region’s
boundary.
This is good news: it gives us license to be lazy.
50


## Page 6

5.4
Some conductor examples
5.4.1
Example 1: Randomly shaped conductor
A chunk of conductor with a hollowed out core has charge placed on it until its potential
(relative to inﬁnity) is φ0. What is the potential inside the core?
Surface potential φ0
φ = ?
Answer: the potential inside the core — indeed, everywhere inside the conductor’s surface
— must be φ0. Why? φ(⃗r) = φ0 is a solution that satisﬁes the boundary condition, and it
obviously satisﬁes Laplace’s equation (since φ0 is a constant). By the uniqueness theorem,
that’s all we need.
5.4.2
Example 2: Nested concentric spherical shells
A pair of thin, conducting, nested spherical shells with radii R2 and R1 carry charges Q2
and Q1 respectively. What is the potential of the inner sphere? What is the potential of the
outer sphere? What is the potential at r = 0? (Set the zero of the potential at inﬁnity.)
R
R
Q
Q1
1
2
2
51


## Page 7

Let’s do the potential of the outer sphere ﬁrst: it must be
φ1 = Q1 + Q2
R1
.
This should hopefully be almost obvious — if not, apply Gauss’s law outside the outer sphere
and note that it looks just like a point charge of Q1 + Q2 at the origin.
To get the potential of the inner sphere, we use
φ2 −φ1
=
−
Z R2
R1⃗
E · d⃗s
=
−
Z R2
R1
Q2
r2 dr
=
Q2
R2
−Q2
R1
→φ2
=
Q2
R2
+ Q1
R1
.
By the uniqueness theorem, the potential at r = 0 — indeed, for any r ≤R2 — must be φ2.
5.4.3
Example 3: Point charge and ﬂat plane conductor
.
Suppose we hold a point charge Q a distance d above an inﬁnite, ﬂat plane conductor.
The potential on the conductor is ﬁxed at zero1. What is the potential everywhere above
the conductor?
+
−
−
−
−
−
−
−
A priori, this looks nasty: the point charge induces minus charge on the conductor, which
makes things really complicated. What do we do?
1This is easily done by hooking it up to ground. “Ground” eﬀectively means an inﬁnite supply of plus
and minus charges. If we deﬁne ground as our reference potential, φ = 0, then anything hooked up to it will
also be at φ = 0.
52


## Page 8

Uniqueness theorem to the rescue. It doesn’t matter how we ﬁnd the potential, as long as
we do so in a way that satisﬁes the boundary condition: the potential must be φ = 0 on the
conductor, and the electric ﬁeld must be purely vertical in the conductor’s plane. A diﬀerent
conﬁguration which produces the exact same potential above the plane is the following one:
+
−
We’ve eliminated the plane entirely, and introduced a minus charge a distance d below the
conductor’s surface. This ﬁctitious charge is called an image charge. With this conﬁguration,
the plane right between the two charges (where the conductor’s surface is located) will be at
φ = 0 (superposition: each point is equidistant from both charges, which are of opposite sign).
Also the ﬁeld is purely vertical at that plane (horizontal components cancel by symmetry).
The potential satisﬁes the boundary condition; it satisﬁes Laplace’s equation; therefore, by
the uniqueness theorem it is THE solution.
The solution is of course complete nonsense in the region below the conductor’s surface.
But we don’t care! That region was not part of the study anyway.
53
