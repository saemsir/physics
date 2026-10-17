# Lec 1 - Couloumb’s law; Superposition; Electric energy- Mit-Scott Huges

> Source: `Lec 1 - Couloumb’s law; Superposition; Electric energy- Mit-Scott Huges.pdf`  
> Pages: 10


## Page 1

Scott Hughes
1 February 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 1:
Introduction; Couloumb’s law; Superposition; Electric energy
1.1
Fundamental forces
The electromagnetic force is one of the four fundamental forces of physics. Let’s compare it
to the others to see where it ﬁts in the grand scheme of things:
Force
Range (cm)
Interaction
Exchange
“Strength”
particles
particles
Gravity
∞
All mass/energy
graviton (m = 0)
1
Weak
10−15
All elementary
weak bosons
1024
particles except
(m ∼100 × mproton)
photon & gluons
Electromagnetic
∞
All charges
photon (m = 0)
1035
Strong
10−13
quarks and gluons
gluons (m = 0)
1037
[The “strength” entries in this table reﬂect the relative magnitudes of the various forces as
they act on a pair of protons in an atomic nucleus. Note that MIT professor Frank Wilczek
shared the 2004 physics Nobel Prize with David Gross (now director of the Kavli Institute for
Theoretical Physics at UC Santa Barbara) and H. David Politzer (now professor of physics
at Caltech) for work that made possible our current understanding of the strong force.]
Let’s summarize the major characteristics of the electromagnetic force:
• Strong: It is the 2nd strongest of the fundamental forces — only the appropriately
named strong force (which binds quarks and nuclei together) beats it (and only at very
small distances).
• Long Range: As we’ll discuss soon, the electromagnetic force has the form F ∝1/r2,
just like gravity. This means it has inﬁnite range: it gets weaker with distance, but
just slowly enough that things really far away still feel it. Contrast this with the weak
force, which has the form F ∝exp(−r/RW)/r2, where RW ≃10−15 cm — it dies away
REALLY fast with r.
• Has 2 signs: It can attract and repel. Contrast this with gravity which only attracts.
• Acts on charge: More on this shortly.
The electromagnetic interaction plays an extremely important role in everyday life. The
forces that govern interactions between molecules in chemistry and biology (e.g., ionic forces,
van der Waals, hydrogen bonding) are all fundamentally electromagnetic in nature. A thor-
ough understanding of electromagnetism will carry you far in understanding the properties
of things you encounter in the everyday world. Add quantum mechanics and you’ve got
most of the tools needed to completely understand these things.
1


## Page 2

1.2
History of electromagnetism
Circa B.C. 500: Greeks discover that rubbed amber attracts small pieces of stuﬀ. (Note the
Greek word for amber: “ηλϵκτρoν”, or “electron”.) They also discover that certain iron rich
rocks from the region of Mαγνησια (Magnesia) attract other pieces of iron.
1730: Charles Francois du Fay noted that electriﬁcation seemed to come in two “ﬂavors”:
vitreous (now known as positive; example, rubbing glass with silk) and resinous (negative;
rubbing resin with fur)
1740: Ben Franklin suggested the “one ﬂuid” hypothesis: “positive” things have more charge
than “negative” things.
Suggested an experiment to Priestley to indirectly measure the
inverse square law...
1766: Joseph Priestley: did the suggested experiment, indirectly proving 1/r2 form of the
force law.
1773: Henry Cavendish: did Priestley’s experiment accurately:
F = k q1q1
r2+δ ,
|δ| < 1
50 .
(By the late 1800s, Maxwell was able to show that |δ| < 1/21600; by 1936 Plimpton and
Lawton were able to show |δ| < 2 × 10−9.)
1786: Charles-Augustin de Coulomb measured the electrostatic force and directly veriﬁed
the inverse square law.
1800: Count Alessandro Giuseppe Antonio Anastasio Volta invented the electric battery.
1820: Hans Chrstian Oersted and Andr´e-Marie Amp`ere establish connection between mag-
netic ﬁelds and electric currents
1831: Michael Faraday discovers magnetic induction
1873: James Clerk Maxwell uniﬁed electricity and magnetism into electromagnetism.
1887: Heinrich Hertz conﬁrms the connection between electromagnetism and radiation.
1905: Albert Einstein formulates the special theory of relativity, which (among other things)
clariﬁes the inter-relationship between electric and magnetic ﬁelds.
1.3
Electric charge
As stated above, the electromagnetic interaction acts on charges. This is really a tautological
statement: all we are doing is deﬁning “charge” as the property that the electromagnetic
interaction interacts with. We accept this and move on.
In nature, we ﬁnd that electric charge comes in discrete lumps or “quanta”. This was ﬁrst
measured by Robert Millikan in 1923 in his famous oil drop experiment. The smallest charge
we ever observe is the “elementary charge” e; it takes the value 1.602×10−19 Coulombs (one
of the units of charge we will use), or 4.803 × 10−10 esu (electrostatic units). The magnitude
of the electron’s charge and of the proton’s charge is e. The charges we encounter in nature
come in opposite signs. By convention, the electron has negative sign, the proton positive.
Charge is conserved: in any isolated system, the total charge cannot change. If it does
change, then the system is not isolated: charge either went somewhere or came in from
somewhere.
2


## Page 3

1.4
Coulomb’s law
Coulomb’s law tells us that the force between two charges is proportional to the product of
the two charges, inversely proportional to the distance between them, and points along the
vector pointing from one charge to the other:
Charge q2
r^
r
Charge q1
^21
12
The unit vector ˆr21 points toward 2 from 1; ˆr12 points toward 1 from 2. This means that
ˆr12 = −ˆr21. We write the distance to charge 2 from 1 as r21; this must be exactly the same
as the distance to charge 1 from 2, r12.
According to Coulomb’s law, the force that charge q2 feels due to charge q1 is given by⃗
F2 = kq1q2
r2
21
ˆr21
(We’ll discuss the constant k shortly. The key thing to note right now is that it is positive.)
Likewise, the force q1 feels due to charge q2 is⃗
F1
=
kq1q2
r2
12
ˆr12
=
−kq1q2
r2
12
ˆr21
=
−⃗F2 .
The force on q1 is equal but opposite to the force on q2. Newton would be pleased (3rd law).
It’s worth noting that we are assuming Coulomb’s law. Of course, this assumption is
justiﬁed because many many experiments have veriﬁed that this is the way the electric force
works. It’s kind of interesting, though, that pretty much this entire class follows from this
assumption. [Indeed, there are only three other “fundamental” assumptions that we will
need — superposition (discussed momentarily), special relativity, and the non-existence of
magnetic charge. All of 8.022 can be derived from these starting points!]
To illustrate Coulomb’s law, we have introduced all these subscripts and made it seem
like half of our time is going to be spent labeling charges, unit vectors, and distances. In
practice, though, the thing to note is that the force in both cases is along the vector from
one charge to the other. Its direction in both cases is repulsive if both charges have the same
sign; it is attractive if the charges are of opposite sign. Like charges repel; opposites attract.
3


## Page 4

1.5
Units
In electrodynamics, the choice of units we use matters: the basic equations actually have
slightly diﬀerent forms in diﬀerent system of units. Contrast this with mechanics, where⃗
F = m⃗a regardless of whether we measure length in units of meters, inches, furlongs, or
lightyears.
The system of units that is used by our textbook, and that is common in much physics
research (particularly theory) is the CGS unit system: length is measured in centimeters,
masses in grams, time in seconds.
In this system of units the constant k appearing in
Coulomb’s law is equal to 1. The cgs unit of charge is the esu, an acronym for the oh-so-
clever name electrostatic unit. It is deﬁned such that two charges of 1 esu each, separated
by 1 cm, feel a force of 1 dyne:
1 dyne = (1 esu)2
(1 cm)2 →1 esu = cm
q
dyne .
Another system of units that is commonly encountered is known as SI (for Syst`em Inter-
nationale) or MKS units. Engineers typically use SI units in their work. Lengths are mea-
sured in meters, masses in kilograms, time in seconds. Charges are measured in Coulombs,
abbreviated C. In this system of units the constant k in Coulomb’s law takes the value
k =
1
4πϵ0
where ϵ0 is yet another constant called the permittivity of free space. It takes the value
ϵ0 = 8.854 × 10−12 C2 N−1 m−2 .
The constant k then takes the value
k
=
8.988 × 109 N C−2m2
≃
9 × 109 N C−2m2
Note that the force between two 1 Coulumb charges held a meter apart is 9 billion Newtons!
1 Coulomb is an enormous amount of charge: 1 Coulomb = 2.998 × 109 esu. (The 2.998
is often approximated 3. Note that the speed of light’s value is 2.998 × 1010 cm/sec. The
equivalence of the numerical factors is not a coincidence!)
A common complaint in this class is that “no one uses cgs units, so why should we”?
This complaint is not really valid — people do in fact use cgs for a lot of things, as well as
even more bizarre variants of cgs units. (For example, in my research I work in a version
of cgs units in which both time and mass are measured in centimeters. In this system, the
speed of light c and the gravitational constant G are both equal to exactly 1. In some cases,
people actually mix units. The most commonly used unit for magnetic ﬁeld is the Gauss,
which is cgs — even if everything else is measured in SI. Never count on people to adopt a
logical system of anything!)
It is true, however, that cgs units are not encountered as often as SI units, so I understand
this annoyance. The harsh truth is that the best thing to do is to adapt, learn how to convert
between diﬀerent unit conventions, and deal with it. It’s actually good practice for being
a scientist or engineer — you’d be stunned how often people use what might be considered
nonstandard choices for things, especially if you have to dig back into older documents.
4


## Page 5

Here is a summary of how to convert various quantities between SI and CGS. In this table,
“3” is shorthand for 2.998. (More precisely, 2.99792458). “9” means “3” squared, or 8.988.
(More precisely, 8.9875517873681764.) In the vast majority of calculations, approximating
“3” as 3 and “9” as 9 is plenty accurate.
SI Units
CGS units
Energy
1 Joule
=
107 erg
Force
1 Newton
=
105 dyne
Charge
1 Coulomb
=
“3”×109 esu
Current
1 Ampere
=
“3”×109 esu/sec
Potential
“3”×102 Volts
=
1 statvolt
Electric ﬁeld
“3”×104 Volts/m
=
1 statvolt/cm
Magnetic ﬁeld
1 Tesla
=
104 gauss
Capacitance
1 Farad
=
“9”×1011 cm
Resistance
“9”×1011 Ohm
=
1 sec/cm
Inductance
“9”×1011 Henry
=
1 sec2/cm
1.6
Superposition
The principle of superposition is a fancy name for a simple concept: in electromagnetism,
forces add.
More concretely: suppose we have a number N of charges scattered in some region. We
want to calculate the force that all of these charges exert on some “test charge” Q. Label
q
q
q
q
q
q
q
1
2
3
4
5
6
7
Q
the ith charge qi; let ri be the distance from qi to Q. Let ˆri be the unit vector pointing from
qi to Q. The total force acting on Q is just the total found by summing the forces from each
individual charge qi:⃗
FQ
=
Qq1ˆr1
r2
1
+ Qq2ˆr2
r2
2
+ Qq3ˆr3
r2
3
+ . . .
=
N
X
i=1
Qqiˆri
r2
i
.
Since we know calculus, we can take a limiting description of this calculation.
Let’s
imagine that, in our swarm of charges, the number N becomes inﬁnitely large, the charges
5


## Page 6

all press together, and the whole thing goes over to a continuum. We describe this continuum
by the charge density or charge per unit volume ρ.
Imagine that we’ve got a big blob of charged goo with density ρ sitting somewhere. We
bring in our test charge Q close to it. How do we calculate the total force acting on the test
charge?
Q
Simple: we chop the blob up into little chunks of volume ∆V ; each such chunk contains
charge ∆q = ρ∆V . Suppose there are N total such chunks, and we label each one with some
index i. Let ˆri be the unit vector pointing from the ith chunk to the test charge; let ri be
the distance between chunk and test charge. The total force acting on the test charge is⃗
F =
N
X
i=1
Q(ρ∆Vi)ˆri
r2
i
This formula is really an approximation, since we probably can’t perfectly describe our blob
by a ﬁnite number of little chunks. The approximation becomes exact if we let the number
of chunks go to inﬁnity and the volume of each chunk go to zero — the sum then becomes
an integral:⃗
F =
Z
V
Q ρ dV ˆr
r2
.
If the charge is uniformly smeared over a surface, then we integrate a surface charge density
σ over the area of the surface:⃗
F =
Z
A
Q σ dA ˆr
r2
.
If the charge is uniformly smeared over a line, then we integrate a line charge density λ over
the length:⃗
F =
Z
L
Q λ dl ˆr
r2
.
(Note that the letter σ is the Greek equivalent for s, so it makes sense for a surface distribu-
tion. λ is the Greek equivalent for l, so it makes sense for a line distribution. ρ is the Greek
equivalent for r so it makes sense ... actually, it makes no sense at all. It was almost logical.)
A good portion of the calculations that we will do will be like this. Let’s look at an
example:
1.6.1
Example: Force on a test charge q due to a uniform line charge
A rod of length L has a total charge Q smeared uniformly over it. A test charge q sits a
distance a away from the rod’s midpoint. (Ignore the thickness of the rod.) What is the
electric force that the rod exerts on the test charge?
6


## Page 7

L
a
q
First, deﬁne a coordinate system: let the direction parallel to the rod be x, let the
perpendicular direction be y. Next, imagine dividing the rod up into little pieces of width
dx:
x
θ
dx
In drawing things this way, we have deﬁned x = 0 as the rod’s midpoint, so the rod runs
from x = −L/2 to x = L/2. We have also drawn the unit vector ˆr that points from the
piece of the rod to the test charge. Note that the unit vector’s direction changes as we slide
the piece dx from one end of the rod to the other. This is a very important thing to note:
the unit vector ˆr is a function, not just a constant. With trigonometry, it is simple to work
out what this function is:
ˆr = −ˆx sin θ −ˆy cos θ .
With a bit more trigonometry, we can write this as a function of x, the location of the chunk,
rather than of θ:
ˆr = −ˆx
x
√
a2 + x2 −ˆy
a
√
a2 + x2 .
Notice ﬁnally that
√
a2 + x2 is the distance from the element dx to the test charge.
7


## Page 8

Deﬁning λ = Q/L, the force that the test charge feels is given by a simple integral:⃗
F = −
Z L/2
−L/2 qλ
xˆx + aˆy
(a2 + x2)3/2 dx .
The horizontal (ˆx) component is obviously zero: for every element on the right of the
midpoint, there is an element on the left whose force magnitude is equal, but whose horizontal
component points in the opposite direction. You can prove this by doing the integral, but
it’s very healthy to understand the physics of this simple symmetry argument.
The remaining integral for the y component is now easy: using
Z
dx
(a2 + x2)3/2 =
x
a2√
a2 + x2 ,
we ﬁnd⃗
F
=
−
qλL
a
q
a2 + L2/4
ˆy
=
−
qQ
a
q
a2 + L2/4
ˆy .
This is a typical example of the kinds of integrations we will need to do (though most
will be more challenging than this simple case).
1.7
Energy of a system of charges
1.7.1
Work done moving charges
Suppose we have a charge Q sitting at the origin. How much work must we do to move a
charge q from radius r2 to radius r1? Let us ﬁrst do this assuming that q moves on a purely
radial path. The work that we do is given by integrating the force that we exert along this
path:
W =
Z⃗
Fus · d⃗s
What is Fus? It is opposite to the force that the charge Q exerts on q:⃗
Fus = −⃗FCoulomb = −Qqˆr
r2
.
We integrate this along a radial path, ds = dr ˆr, from r = r2 to r = r1:
W(r2 →r1)
=
Z⃗
Fus · d⃗s
=
−
Z r1
r2
Qq
r2 dr
=
Qq
r1
−Qq
r2
.
It is straightforward to prove that this result holds along any path. Suppose we come in
on a radial path to radius R, move in a circular arc through some angle θ, and then continue
on a new radial path to r1:
8


## Page 9

θ
1r
R
r2
The diﬀerential d⃗s in this case is still dr ˆr along the two radial paths, but it is R dθ ˆθ along
the angular segment (where ˆθ is a unit vector that points in the angular direction). The
integral thus becomes
W(r2 →r1)
=
Z⃗
Fus · d⃗s
=
−
Z R
r2
Qq
r2 dr −
Z θ
0
Qq
R2 (ˆr · ˆθ)(R dθ) −
Z r1
R
Qq
r2 dr
=
Qq
R −Qq
r2
+ 0 + Qq
r1
−Qq
R = Qq
r1
−Qq
r2
.
We end up with the exact same result because the contribution around the arc is zero: that
path is perpendicular to the force, so we do no work moving along that segment.
A corollary of this result is that the work we do is the same along ANY path that we
take from r2 to r1. Why? We can break up any path into radial segments and angular arcs,
in a similar manner to the above calculation. The angular segments don’t matter; the radial
segments will give us the same answers we’ve just derived.
A second corollary is that the electric force is conservative: any path that takes us from
r1 back to r1 does zero work (just plug r2 = r1 into the above result).
1.7.2
Work done to assemble a system of charges
How much work does it take to assemble a system of charges? With the calculations we just
did, answering this is easy.
Let’s clarify the question a bit: how much work does it take to move a charge q2 in from
inﬁnity until it is a distance r12 from a charge q1? This is really what we mean what we
ask how much energy it takes to assemble the system — we are asking what it takes to take
charges that are very far apart and bring them close together. Using the results we worked
out above, the answer is clearly
W(∞→r12)
=
q1q1
r12
≡
W12 .
This quantity can then be thought of as the energy content U of this system of charges:
U = W.
9


## Page 10

Now, how about if we bring in a third charge q3? This turns out to be easy using the
principle of superposition. To make it very clear what is going on, let’s go back to the
integral we have to do for the work: we bring the charge q3 in from inﬁnite distance until it
is a distance r13 from charge q1 and r23 from charge q2:
W(1+2)3
=
−
Z r13
∞
q1q3
r2 dr −
Z r23
∞
q2q3
r2 dr
=
q1q3
r13
+ q2q3
r23
=
W13 + W23 .
We add this to the work it took to bring q1 and q2 together to get the total work to assemble
this system:
W
=
W12 + W13 + W23
=
q1q2
r12
+ q1q3
r13
+ q2q3
r23
.
Again, this is the total energy content of the system: U = W.
We can generalize this to as many charges as we want; the resulting formulas rapidly get
pretty big. The key thing to note is that we are summing over pairs of charges in the system.
It is pretty simple to write down a formula that sums up the energy over pairs like this:
U = 1
2
N
X
j=1
N
X
k=1
j̸=k
qjqk
rjk
The requirement that j̸ = k makes sure that we only count over pairs of charges — if k = j,
we get nonsense in the formula. The factor of 1/2 out front is needed because the sums will
actually count each pair twice. (Try it out for a simple case, N = 2 or N = 3, to see.)
10
