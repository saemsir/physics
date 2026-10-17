# Lec 7 - Current, continuity equation, resistance, Ohm’s law. - scoot huges lec07

> Source: `Lec 7 - Current, continuity equation, resistance, Ohm’s law. - scoot huges lec07.pdf`  
> Pages: 9


## Page 1

Scott Hughes
24 February 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 7:
Current, continuity equation, resistance, Ohm’s law.
7.1
Electric current: basic notions
The term “electric current” is used to describe the charge per unit time that ﬂows through a
region. In cgs units, current is measured in esu/sec, naturally enough. In SI units, current is
measured in Coulombs/sec, which is given the name Ampere (or amp). It is very important
to know how to convert between these units! Amps are used to describe currents FAR more
often than esu/sec: 1 ampere = 2.998 × 109 esu/sec.
Suppose we have a swarm of charges, all with the same charge q. The number density of
these charges is some value n (i.e., there are n charges per unit volume). Suppose further
that all of these charges are moving with velocity⃗u. How much current is ﬂowing through
an area⃗A?
To ﬁgure this out, we need to calculate how many of the charges pass through the area⃗
A in time ∆t. This number is given by the number of charges that ﬁt into the oblique prism
sketched below:
θ
u
A
u∆t
The number of charges in this prism is its volume, |⃗A||⃗u∆t| cos θ, times the number
density. The number of charges that pass through the area in time ∆t is
∆N = n(|⃗u|∆t)(|⃗A|) cos θ = n⃗u ·⃗A∆t .
The total charge that passes through is q times this number:
∆q = qn⃗u ·⃗A∆t ,
so that the current I = ∆q/∆t must be
I = qn⃗u ·⃗A .
63


## Page 2

This form of the current motivates the deﬁnition of the current density⃗J:⃗
J = qn⃗u = ρ⃗u .
For this (admittedly artiﬁcial) example of all charges streaming in the same direction with
the same velocity⃗u, the current density is just the charge density ρ ≡nq times that velocity.
The current is then given by I =⃗J ·⃗A.
Caution: bear in mind that the current density is a current per unit area: charge/(time
× area). This is hopefully obvious by dimensional analysis: charge density is charge/(length
cubed); velocity is length/time; hence current density is charge/(time × length squared).
7.2
Electric current: more details
Some of the details assumed above are obviously fairly artiﬁcial.
We make them more
realistic one by one. First, rather than having a single kind of charge that is free to move,
a material might have a bunch of diﬀerent charges that can carry current. For example,
ocean water conducts electricity largely because of the freely moving sodium and chlorine
ions. Other materials dissolved in the ocean contribute a bit as well. Each variety of charge
may have its own charge, number density, and velocity. Let the subscript k label diﬀerent
charge “species” — e.g., k = 1 could refer to electrons, k = 2 to chlorine ions, etc. The total
current density comes from combining them all together:⃗
J =
X
k
qknk⃗uk =
X
k
ρk⃗uk .
Note, via this formula, the equivalence between positive and negative charges we get by
ﬂipping the velocity direction: a positive charge moving with⃗uk contributes the same amount
to the overall current density as a negative charge moving with −⃗uk.
Next, the assumption that all charges of species k are moving with the exact same velocity⃗
uk is pretty obviously ludicrous. A current of 1 amp corresponds to (for example) 6.24×1018
electrons per second streaming past. There’s no way every single one of those electrons has
the exact same velocity! So, in our formula for⃗J, we replace⃗uk with its value averaged over
all the charges:
⟨⃗uk⟩= 1
Nk
Nk
X
i=1
(⃗uk)i ,
where Nk is the total number of charge carriers of species k, and (⃗uk)i is the velocity of the
ith charge in species k (admittedly, not the sanest looking equation in the universe). The
current density is thus given by⃗
J =
X
k
qknk⟨⃗uk⟩=
X
k
ρk⟨⃗uk⟩.
(Note: Purcell gives a somewhat diﬀerent formula for⃗J built from the averaged velocity. I
ﬁnd his formula to be rather confusing; it took me half an hour to connect what he does
with my own understanding of current density and averages. De mortuis nil nisi bonum.)
Finally, we do not expect in general to encounter nice, simple, uniform surfaces through
which our current ﬂows.
Not surprisingly, we generalize to an integral: the current —
charge/time — passing through some general surface S is given by
I =
Z
S⃗J · d⃗A .
We can thus think of total current as the ﬂux of current density through a surface.
64


## Page 3

7.3
Charge conservation and continuity
Suppose the current ﬂows through a closed surface:
S
J
J
J
J
J
In this case, there must be charge piling up inside (or departing from) the volume V enclosed
by the surface S:
I
S⃗J · d⃗A = −∂
∂tQ(contained by S) .
The minus sign in this equation comes from our convention on assigning direction to the area
element d⃗A — since d⃗A points out,⃗J · d⃗A is negative if the current density points inward,
and is positive if the current density points outward. Since inward corresponds to a gain of
charge (and vice versa) we clearly need a minus sign for the physics to make sense.
Using our skill at vector calculus, we can manipulate this equation as follows:
I
S⃗J · d⃗A =
Z
V
³⃗
∇·⃗J
´
dV ,
where V is the volume enclosed by S. This is just Gauss’s theorem. We also have
Q(enclosed by S) =
Z
V ρ dV .
Putting this together we have
Z
V
³⃗
∇·⃗J
´
dV
=
−∂
∂t
Z
V ρ dV
=
−
Z
V
∂ρ
∂t dV
→
Z
V
Ã⃗
∇·⃗J + ∂ρ
∂t
!
dV
=
0 .
65


## Page 4

This equation is guaranteed to hold only if⃗
∇·⃗J + ∂ρ
∂t = 0 .
This result is known as the continuity equation: it guarantees conservation of electric charge
in the presence of currents. It also tells us that when currents are steady — no time variation,
so that ∂ρ/∂t = 0 — we must have⃗∇·⃗J = 0.
7.4
Ohm’s law
Electric ﬁelds cause charges to move. It stands to reason that an electric ﬁeld applied to
some material will cause currents to ﬂow in that material.
For an amazingly wide range of materials, an empirical rule called Ohm’s law gives the
following relation between current density and applied electric ﬁeld:⃗
J = σ⃗E .
In other words, the current density is directly proportional to the electric ﬁeld. The constant
of proportionality σ is called the material’s conductivity.
CAUTION: the symbol σ stands for BOTH conductivity AND surface charge
density!!!! This can be annoying, but is a convention that we are stuck with, sadly. You
should always know from the context of a given equation the physical meaning of a particular
σ. Even more sadly, there are times when both meanings of σ need to be used simultaneously.
In such a case, I suggest using subscripts to distinguish the two symbols — e.g., σc gives the
conductivity, σq is surface charge density.
66


## Page 5

Ohm’s law comes in two ﬂavors. The version already given,⃗J = σ⃗E, can be thought of as
the “local” or “microscopic” version. It tells me about the relation between current density
and ﬁeld at any given point in some material. To understand the second version, consider
current ﬂowing in some chunk of material. The material is perfectly homogeneous, meaning
that the conductivity is σ throughout the chunk. It is of length L, and has a cross-section
area A:
L
A
We put this material in a uniform electric ﬁeld⃗E. Let’s orient this ﬁeld parallel to the
material’s long axis. Then, the potential diﬀerence or “voltage” between its two ends is
V = EL.
At every point in the chunk’s interior, Ohm’s law holds: J = σE (dropping the vector
signs since everything points along the long axis). Since E is constant everywhere, and since
the chunk is homogeneous, this value of J holds everywhere. The total current ﬂowing past
any point must be I = JA. We now look for a relationship between the current I and the
voltage V :
J
=
σE
I
A
=
σV
L
→V
=
I
µ L
σA
¶
≡
IR .
The formula V = IR is the “global” or “macroscopic” form of Ohm’s law: it is entirely
equivalent to J = σE, but involves quantities which are integrated over the macroscopic
extent of our conducting material. The quantity in parentheses is deﬁned as the resistance
R of the chunk of material:
R ≡L
σA ≡ρL
A .
In this context, the symbol ρ ≡1/σ is the resistivity of the material. Sadly, this is yet
another example of overusing symbols — be careful not to confuse ρ as resistivity with ρ as
charge density. The key thing to note about the resistance is that it goes proportional to
the length of a material, and inversely proportional to the cross-sectional area.
67


## Page 6

Units: In SI units, resistance is measured in Ohms, which is just a special name for
Volts/Amperes. In cgs units, the voltage is measured in esu/cm, and the current in esu/sec,
so the resistance is measured in sec/cm, a rather odd unit. From this, we can infer the units
of resistivity and conductivity: resistivity is measured in Ohm-meters in SI units1, and in
seconds in cgs.
7.4.1
Example: Resistance of a spherical shell
We derived the formula for the resistance of a piece of material for a very simple geometry.
Similar calculations apply even if things are arranged in a gooﬁer way.
Suppose we have a pair of nested spheres; the space between them is ﬁlled with material
whose resistivity is ρ. The inner sphere is held at constant potential V ; the outer sphere is
grounded, so that its potential is zero. The radius of the inner sphere is a; that of the outer
sphere is b. The current ﬂows steadily — there is no charge piling up anywhere. What is
the resistance of this shell?
V
b
a
We want to use Ohm’s law in microscopic form, J = σE, express the ﬁeld in terms of V ,
the current density in terms of a current I, and then read oﬀthe resistance R. To do that,
we need to know the potential at any point between the plates. By spherical symmetry, the
potential must clearly have the form φ = C/r + D, for some constants C and D. We have
the boundary conditions that at r = a, φ = V ; at r = b, φ = 0:
V
=
C
a + D
0
=
C
b + D .
With a bit of eﬀort, we solve these equations to ﬁnd
C
=
V
ab
b −a
D
=
−V
a
b −a .
1In practice, this unit is rarely used. The unit Ohm-cm is used much more often.
68


## Page 7

Now, we use E = −∂φ/∂r to ﬁnd
E = V
r2
ab
b −a .
So, we now know the electric ﬁeld. Note this points radially.
How much current passes through a shell of radius r somewhere between a and b? We
must have
I = 4πr2 J .
Note that this current must be constant! There is no charge piling up, so the same total
charge per unit time passs through any given shell of radius r.
Now, we impose the microscopic form of Ohm’s law:
I
=
(4πr2)(σE)
=
(4πr2)σ V
r2
ab
b −a
=
4πσab
b −a V .
Rearranging to put this in the form V = IR, putting ρ = 1/σ, we read oﬀthe resistance of
the shell:
R = ρ(b −a)
4πab
.
7.4.2
Example: Variation of σ
What happens if σ is not a constant? The answer is set by requiring that the current ﬂow
be steady. Consider two conductors of conductivity σ1 and σ2 fused together:
E1
σ1
E2
σ2
Area A
The current must be the same in each half:
I = JA = σ1E1A = σ2E2A .
This can only be true if the electric ﬁeld is diﬀerent in each material. The electric ﬁeld thus
suddenly jumps as we cross from one side of the junction to the other, which means that
there must be a layer of surface charge σq at the boundary2:
σq = 1
4π (E2 −E1) =
I
4πA
µ 1
σ2
−1
σ1
¶
.
Whenever the conductivity varies, there is a possibility that, in the steady state, some charge
accumulates somewhere. This is necessary to maintain steady current ﬂow.
2Here’s where the overuse of the symbol σ really gets annoying. Sorry.
69


## Page 8

7.5
A closer look at Ohm’s law
Ohm’s law, on the face of it, makes no sense. It tells us that under an applied electric ﬁeld,
we get a steady current density. Since⃗J = qn⃗u (considering only one current carrier), this
means that the electric ﬁeld is causing currents to move at constant velocity.
This should bug you! Electric ﬁelds cause forces; forces cause accelerations. Why don’t
the charges just accelerate like mad?
The answer is that the charges are in a medium — the conductor — that prevents them
from moving freely. The motion is essentially like that in a viscous medium. The situation
is much closer to a sky diver in free fall — after a short period of acceleration, the charges
reach “terminal velocity”, and essentially ride along at that velocity from then on. This
“terminal velocity” is what appears in the current density formula.
The cause of this eﬀectively viscous motion is (roughly) the many collisions that the
charge carriers experience as they ﬂow through the conductor. The charge carriers accelerate
like hell for a short time, smash into something, get directed in some random direction, charge
like hell again, and repeat3. The net averaged behavior is a uniform drift.
More concretely, let’s look at how the momentum of charge carriers accumulate in a
conductor.
Consider a single charge ﬁrst.
Suppose at t = 0 a collision just occurred.
Its momentum following this collision⃗p = m⃗u0, where⃗u0 is the random velocity it has
following the collision. The electric ﬁeld acting on this charge changes its momentum over
a time interval t by imparting an impulse ∆⃗p = q⃗Et. The total momentum of this particle,⃗
p = m⃗u0 + q⃗Et, thus grows linearly with time until the next collision occurs, at which point
the clock is reset and we repeat.
Now consider a whole swarm of N of these charges. The average momentum of a member
of this ensemble is
m⟨⃗u⟩= 1
N
N
X
i=1
³
m⃗ui + q⃗Eti
´
.
The velocity⃗ui is the random velocity imparted to charge i following its last collision; ti is
the time interval for that charge since that collision. If N is a large number, the ﬁrst term
must be extremely close to zero. Why? We’re adding up a enormous number of randomly
oriented vectors! The result of such addition is always a number that is very, very close to
zero, provided N is large4. What remains is
m⟨⃗u⟩= q⃗E
N
N
X
i=1
ti ≡q⃗Eτ ,
where
τ ≡1
N
N
X
i=1
ti
is the average time between collisions. This turns out to be a property of the material; this,
then, is what causes an imposed electric ﬁeld to lead to uniform velocity.
3If you’ve ever driven through Los Angeles during rush hour, you’ve experienced the life of a charge
carrier in a conductor.
4A careful analysis of this kind of addition shows that there is some error incurred by assuming that the
vectors sum to precisely zero. However, that error is of order 1/
√
N. As long as N is very large — which
is the case for any good conductor, where N is of order Avogadro’s number — these small errors are not
important. Those of you who take 8.044 will learn more about this.
70


## Page 9

Notice that from this derivation, we can just read oﬀthe conductivity:⃗
J
=
nq⟨⃗u⟩= nq

q⃗Eτ
m

= σ⃗E
→σ
=
nq2τ
m
.
If we have multiple charge carriers, we ﬁnd
σ =
X
k
nkq2
kτk
mk
.
71
