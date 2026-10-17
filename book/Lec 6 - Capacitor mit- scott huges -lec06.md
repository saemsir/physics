# Lec 6 - Capacitor mit- scott huges -lec06

> Source: `Lec 6 - Capacitor mit- scott huges -lec06.pdf`  
> Pages: 9


## Page 1

Scott Hughes
17 February 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 6:
Capacitance
6.1
Capacitance
Suppose that I have two chunks of metal. A charge +Q is on one of these chunks, −Q is
on the other (so that the system is neutral overall). Each chunk will be at some constant
potential. What is the potential diﬀerence between the two chunks of metal?
+Q
−Q
2
1
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
Whatever the potential diﬀerence V ≡φ2 −φ1 = −
R 2
1⃗E · d⃗s turns out to be, it must of
course turn out to be independent of the integration path. In fact, as we can show with a
little thought, the potential diﬀerence V must be proportional to the geometry. This means
that the potential diﬀerence (or “voltage”) between the two chunks must take the form
V = (Horribly messy constant depending on geometry) × Q .
The horrible mess that appears in this proportionality law depends only on geometry. In
other words, it will depend on the size and shape of the two metal chunks, their relative
orientation, and their separation. It does not depend on their charge.
This constant is deﬁned as 1/C, where C is the Capacitance of this system. A system like
this is then called a capacitor. The 1/ may seem a bit wierd; the point is that one usually
writes the capacitance formula in a diﬀerent way: we put
Q = CV .
A key thing to bear in mind when using this formula is that Q refers to the charge separation
of the system. In other words, when I say that a capacitor is charged up to some level Q,
54


## Page 2

Figure 1: Q = CV .
I mean that I have put +Q on one part of the capacitor, −Q on the other. The capacitor
as a whole remains neutral!! I emphasize this now because I often ﬁnd students are some-
what confused by this point, particularly when we start thinking about circuits that have
capacitors in them.
6.1.1
Why are the charge and voltage proportional?
The real concern here is, how do we know that when we say double the charge on the
capacitor, the charge doesn’t move around and cause the dependence to be more complicated?
The simple answer is the principle of superposition: whenever we double the amount of
charge, the ﬁelds that these charges create simply double. Hence, the potential diﬀerence
(which is just the line integral of the ﬁeld) must also double.
There’s an implied assumption here, though: we are assuming that there is enough charge
smeared out on the “plates” of the capacitor to uniformly cover them. Imagine we just had
one electron on the minus plate, and one electron “hole” on the plus plate. If we just doubled
the charge, the electron on the - plate indeed might move somewhere else. This situation
could be messy!
Fortunately, in every situation that is of practical interest, the assumption that the plates
are evenly coated with a charge excess is a good one. This is because the elementary charge
is so small — even if there’s just a tiny tiny amount of charge — say 10−12 Coulombs —
that means we’ve got something like 6 million excess electrons.
6.1.2
Units of capacitance
In SI units, we measure charge in Coulombs and potential in Volts, so the unit of capacitance
is the Coulomb/Volt. This combination is given a special name: the Farad, or F.
In cgs units, we measure charge in esu and potential in esu/cm. The unit of capacitance
is thus just the centimeter! This is actually kind of cool: objects that are big (have lots of
55


## Page 3

centimeters) tend to have a big capacitance.
It’s important to know how to convert between these two units: when we are computing
capacitance from the system’s characteristics, cgs units are nice, since it’s just a matter of
getting the geometry right. But SI units are used almost exclusively in circuits.
1 cm
=
1.11 × 10−12 F
≃
1 pF .
“pF” means “picofarad” — one trillionth of a Farad. Capacitors typically come in micro-
farads or picofarads; this is because (as we shall see in a moment) a Farad turns out to be
an enormous amount of capacitance.
6.2
Some examples
6.2.1
Isolated sphere
We take a sphere of radius R and put a charge Q on it. Its potential (relative to inﬁnity) is
V = Q/R. The sphere’s capacitance is therefore
Csphere = R .
When we began discussing the notion of capacitors, we talked about the potential diﬀerence
between two conductors. In this case, the second conductor is a “virtual” plate at inﬁnity.
There’s one spherical capacitor that we use all the time: the earth. It has a radius (and
hence a capacitance) of 6.4×108 cm. This is so large that we can eﬀectively take charge from
or dump charge onto the earth without changing its electrical potential at all. Converting,
the earth has a capacitance Cearth = 0.0007 Farad — enormous, but still signiﬁcantly smaller
than a Farad!
The fact that we can dump charge onto or take charge from the earth without changing
its potential appreciably means that it is often convenient to deﬁne the earth as the reference
point for computing potential. Many circuits take advantage of this by hooking directly to
“ground” — a lead that runs into the earth. That “grounded lead” is then deﬁned, by
convention, as potential zero. (Students educated in the remnants of the British Empire
may have learned to call a circuit that is grounded “earthed”.)
56


## Page 4

6.2.2
Parallel plates
Consider a pair of plates, each with area A and separated by a distance s.
Area A
s
Charge −Q
Charge +Q
If the plates are close together (s ≪
√
A), we can approximate the ﬁeld between these plates
as those coming from a pair of inﬁnite planes:
+
=
positive
negative
2πσ
2πσ
away from
towards
plate
plate
4πσ between plates
0   outside plates
Summing an inﬁnite plane with charge density σ = +Q/A and σ = −Q/A we ﬁnd
E = 4πσ = 4πQ/A
between the plates, and zero outside of the plates. The ﬁeld points from the positive plate
to the negative plate, so the potential diﬀerence from the negative to the positive plate is
V = −
Z pos
neg⃗E · d⃗s = 4πσ
Z s
0 ds = 4πQs
A
.
Rewriting this in the form Q = CV , we read oﬀthe capacitance:
Cplates = A
4πs .
57


## Page 5

This is an area divided by a length, so it has the correct units.
It’s pretty important to know about capacitance in SI units, since most circuit elements
are discussed using things like Volts and Farads rather than statvolts and centimeters. Con-
verting is easy: we just need to remember that the electric ﬁeld in general has a factor of k
(the constant from Coulomb’s law) attached to it. Hence, the voltage V likewise picks up
this factor; rearranging to solve for the capacitance, we ﬁnd
Cplates = 1
k
A
4πs .
In cgs units, k = 1, so this rather trivially reduces to what we had before. In SI units,
k = 1/4πϵ0, and we ﬁnd
Cplates = ϵ0 A
s
.
Whenever you work out a formula for capacitance in cgs units, you can easily convert to SI
by multiplying by 1/k = 4πϵ0.
6.2.3
Nested shells
Return to the example discussed last lecture: a pair of nested spherical shells,
R
R
Q
Q1
1
2
2
The potential diﬀerence we found in this case was
∆φ = V = Q2
R2
−Q2
R1
.
Set Q2 = Q = −Q1:
∆φ = V = Q
µ 1
R2
−1
R1
¶
.
Rearranging into the form Q = CV , we ﬁnd
C =
R1R2
R1 −R2
.
58


## Page 6

Note that if R1 is just barely larger than R2, this gives the same result as the parallel plate
formula: putting R1 = R2 + s, we ﬁnd
C
=
R2
2 + R2 s
s
≃
R2
2
s
s ≪R2
=
4πR2
2
4πs
=
A
4πs .
On the second to last line, we’ve used the fact that 4πR2
2 is the surface area of the sphere.
6.3
Energy stored in a capacitor
Suppose we are charging up a capacitor. At some intermediate point in the process, there is
a charge +q on one plate, −q on the other. We move a charge dq from the negative charge to
the positive charge. It takes work to do this: we are forcing a positive charge in the direction
opposite to what it “wants” to do. The amount of work we do moving this charge is
dW
=
V (q) dq
=
q
C dq .
Integrating this to a total charge separation of Q, we ﬁnd that the work that is done charging
up the capacitor is
W
=
Z Q
0
q
C dq
=
1
2
Q2
C .
This is the energy stored that is stored in the capacitor:
U = 1
2
Q2
C = 1
2CV 2 .
We’ve used Q = CV in the second equality.
It’s useful to carefully re-examine this formula for the case of the parallel plate capacitor:
we put C = A/4πs, and note that the charge Q = EA/4π, where E is the electric ﬁeld
between the plates. Then,
U
=
1
2
Q2
C
=
1
2
E2A2
16π2
4πs
A
=
E2
8π As .
The last line is the energy density of the electric ﬁeld between the plates times the volume
of that region.
59


## Page 7

6.4
Dielectrics
The capacitors we’ve discussed here are somewhat artiﬁcial: the space between their plates
is taken to be empty. In the real world, the normal situation is that this space is ﬁlled with
something — air, plastic, paper, compressed leprechauns, whatever. The “stuﬀ” that ﬁlls
this space interacts with the electric ﬁeld, and can have an important impact on the the
properties of the capacitor.
The basic idea can be understood fairly simply. The key point is that many materials
are polarizable: they are made out of molecules that, though neutral overall, have a net
excess of + charge at one end and an excess of −charge at the other. This means that each
molecule looks like a little electric “dipole” — a distribution whose total charge is zero, but
that shows non-trivial charge separation. Normally, the polar character of these molecules
is unimportant — the random, mostly thermal motion of the molecules means that at any
moment there is no net polarization to a big mass of them. If we take a block of such material
and slide it between two parallel plates, it looks (roughly) like this:
+
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
−
−
Suppose we now charge up these plates, so that there is an electric ﬁeld between them.
We leave these plates with ﬁxed charge. All of these little dipoles will now want to line up
— the + ends will align with the negatively charged plate, and vice versa:
By lining up in this way, they will tend to reduce the electric ﬁeld between the plates
— the ﬁeld due to the charges on the plates themselves is superposed upon a ﬁeld pointing
in the opposite direction due to the alignment of the dipoles. For an enormous number
of molecules, the reduction in the applied electric ﬁeld can be summarized using a single
number:
Fixed charge situation:
Ewith dielectric = Ewithout dielectric/K .
The number K is called the dielectric constant; it’s something we can measure and catalog
for various substances. Table 10.1 of Purcell lists a whole bunch; the values range from
K ≃1 for air to K ≃80 for water. (Water has a huge dielectric constant because of the
charge distribution associated with its bent molecules.) For us, the value of K is always
greater than or equal to one.
60


## Page 8

+
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
−
−
−
−
−
−
−
−
+
+
+
+
+
+
Since the electric ﬁeld is reduced by K, the voltage between the plates is likewise reduced.
For the parallel plate capacitor and in cgs units, we have
V with dielectric = 4πQs
KA .
Invoking the deﬁnition of the capacitance, we ﬁnd
Cwith dielectric = KA
4πs = KCwithout dielectric .
It’s worth thinking for a moment about what the dielectric does in some speciﬁc circum-
stances. Suppose I have a capacitor C whose plates have been charged up to some ﬁxed
charge Q. This is easily done by hooking a capacitor up to a voltage source V (e.g., a bat-
tery) and then removing the source — the capacitor will then hold the charge Q = CV . If
I insert a dielectric between the plates, the capacitance increases; since the charge is ﬁxed,
the voltage must decrease:
Fixed charge:
V new =
Q
Cnew =
Q
KCorig = V orig
K
.
Suppose instead I take the capacitor and hold it at ﬁxed voltage. This is also easy to do —
we hook up our capacitor to a voltage source and just leave it there. The capacitance again
increases, which means the charge must increase:
Fixed voltage:
Qnew = CnewV = KCorigV = KQorig .
The “extra” charge is actually pulled from the voltage source. Note that in this circumstance
the electric ﬁeld between the plates does not decrease when we insert the dielectric! However,
it takes more charge to hold this ﬁeld than it does without the dielectric — the dielectric
“wants” to reduce the electric ﬁeld; the voltage source needs to supply more charge to “ﬁght”
this tendency.
61


## Page 9

To wrap this section up, consider the capacitance in SI units. With a dielectric, it is
given by
Cwith dielectric
=
Kϵ0A
s
≡
ϵA
s .
The combination Kϵ0 ≡ϵ is called the permittivity of the dielectric. When K = 1, the
permittivity is just ϵ0, the permittivity of “free space” (meaning “empty space”).
In practice, people don’t usually describe dielectrics using permittivity — the dielectric
constant K is much more useful. However, you do encounter the term sometimes; and, it
helps to explain why ϵ0 is called the permittivity of free space.
62
