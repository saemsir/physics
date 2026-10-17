# Lec 15 - Mutual and Self Inductance - mit scott huges

> Source: `Lec 15 - Mutual and Self Inductance - mit scott huges.pdf`  
> Pages: 10


## Page 1

Scott Hughes
7 April 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 15:
Mutual and Self Inductance.
15.1
Using induction
Induction is a fantastic way to create EMF; indeed, almost all electric power generation in
the world takes advantage of Faraday’s law to produce EMF and drive currents. Given the
deﬁning formula,
E = −1
c
dΦB
dt
where
ΦB =
Z
S⃗B · d⃗A
all that we need to do is set up some way to make a time varying magnetic ﬂux and we can
induce EMF and drive currents very happily.
Given the deﬁnition of magnetic ﬂux, there are essentially three ways that we can make it
vary and thereby create an EMF: we can make the area vary; we can make the “dot product”
vary; and we can make the magnetic ﬁeld vary. Let’s look at these three situations one by
one.
15.1.1
Changing area
We already discussed exactly this situation when we looked at the rod sliding on rails in a
uniform magnetic ﬁeld:
L
x
R
v
B
+++
−−−
136


## Page 2

The changing ﬂux in this case is due to the continually changing area. We get an EMF
whose magnitude is E = BLv/c, and that (by Lenz’s law) drives a current which circulates
counterclockwise in the loop.
In principle, we could imagine using this as a power source. For example, we could replace
the resistor with a lightbulb and use this arrangement as a lamp. However, you’d have to
ﬁnd some way to continually slide the bar: the energy radiated by the lamp has to come
from somewhere! In this case, it would come from the poor schmuck who continually drags
the bar back and forth.
15.1.2
Changing “dot product”
Another way to generate an EMF is to make the “dot product” — i.e., the relative orientation
of our area and the magnetic ﬁeld — vary with time. Imagine we have a circular loop sitting
in a uniform magnetic ﬁeld:
B
n^
The magnetic ﬂux through the loop is given by
ΦB
=
πr2⃗B · ˆn
=
πr2B cos θ
where θ is the angle between the loop’s normal vector and the magnetic ﬁeld. Now, suppose
we make the loop rotate: say the angle varies with time, θ = ωt. The EMF that is generated
in this case is then given by
E = ωπr2B
c
sin ωt .
This kind of arrangement is in fact exactly how most power generators operate: An external
force (ﬂowing water, steam, gasoline powered engine) forces loops to spin in some magnetic
ﬁeld, generating electricity. Note that the EMF that is thereby generated is sinusoidal —
generators typically produce AC (alternating current) power.
137


## Page 3

15.1.3
Changing ﬁeld
Finally, in many situations we can make the magnetic ﬁeld itself vary. Suppose the integral
is very simple, so that it just boils down to ﬁeld times area. If the magnetic ﬁeld is a function
of time, then the ﬂux will be a function of time:
ΦB(t) = B(t)A .
We just need to take a derivative, divide by c, and we have an EMF.
This method of creating an EMF is one of the most important. In practice, it typically
comes about when our magnetic ﬁeld comes from some current that varies in time. This is
the case that we will focus on in the remainder of this lecture.
15.2
Inductance example
Consider the following arrangement: we place a loop of wire with radius r in the center of
a long solenoid. The solenoid has a wire that is wrapped N times around its total length l;
hence, the number of turns per unit length is N/l. A current Isol runs through this solenoid;
this current varies with time. What is the EMF Eloop that is induced in the wire loop?
I
I
sol
sol
loop
We begin with our deﬁning relation,
E = 1
c
dΦB
dt
.
(In what follows, I will often drop the minus sign. This is ﬁne provided we bear in mind that
we need to use Lenz’s law to tell us the direction in which any induced current will ﬂow.)
The magnetic ﬂux is given by the magnetic ﬁeld of the solenoid times the cross sectional
area of the loop:
ΦB
=
BsolAloop
=
4πNIsol
cl
πr2 .
138


## Page 4

(Recall that the current per unit length is nI if the input current is I and the number of
turns per unit length is n.) This means that the EMF induced in the little loop is
Eloop = 4π2r2N
c2l
dIsol
dt
.
In words, the EMF induced in the loop is totally set by the rate of change of current in the
solenoid, times a bunch of constants that depend on the geometry of our setup.
We will return to look at this example somewhat more systematically.
15.3
Self inductance
Suppose we take the loop out of the solenoid:
I
I
sol
sol
Is there any EMF induced in this case? Let’s think about this carefully: The magnetic ﬁeld
threading the solenoid is
B = 4πNIsol
cl
.
The magnetic ﬂux through each loop that constitutes the solenoid is
Φ1 loop
B
= 4π2R2NIsol
cl
where R is the solenoid’s radius. This means that the total ﬂux as far as any induction is
concerned must be Φtot
B = NΦ1 loop
B
— we get a contribution of Φ1 loop
B
from every loop that
constitutes the solenoid! In other words, we end up with
Φtot
B = 4π2R2N 2Isol
cl
.
Taking the time derivative, we ﬁnd the EMF that is induced when this current varies:
E = 4π2R2N 2
c2l
dIsol
dt
.
139


## Page 5

Again, we have a bunch of stuﬀthat just depends on the solenoid’s geometry (and constants)
times the rate of change of the current.
The math hopefully makes sense. What you should be asking yourself at this point is
“OK, ﬁne, I’ve got an EMF, but what IS it??” Lenz’s law helps us to understand what this
EMF is and does: Suppose the current is increasing, so that the magnetic ﬁeld is likewise
increasing. Lenz’s law tells us that the induced EMF will try to “ﬁght” this: the EMF that
is induced will tend to drive currents which oppose the change in magnetic ﬂux. For this
setup, this means that the EMF will oppose the increase — it will drive a current which
tries to prevent B from changing. If the current was decreasing, the EMF will oppose the
decrease. The punchline is that inductance opposes the change in the current. The EMF
that is induced in a situation like this is often called the “back EMF” since it acts “back”
on the circuit to try to hold the current steady.
From this situation, we deﬁne a quantity called the “self-inductance”, L:
E = LdI
dt .
Quantities which have a self-inductance and are used in circuits (as we’ll study next lecture)
are called “inductors”. For a solenoidal inductor, we can read oﬀthe value of L from the
preceding calculation:
Lsol = 4π2N 2R2
c2l
.
Bear in mind that this formula only holds for solenoids! The solenoid is, however, a very
important example of an inductor and crops up quite a lot.
15.3.1
Units
Since EMF has units of potential, and dI/dt is [charge]/[time]2, it is simple to deduce the
units of self-inductance. In cgs units, we have
[Potential]
[charge]/[time]2 →esu/cm
esu/sec2 →sec2
cm .
Inductance is measured in the rather odd unit of sec2/cm in cgs units.
In SI units, we have
[Potential]
[charge]/[time]2 →
Volts
Amp/sec .
We could reduce this further, but what is done instead is to give this combination a name:
1 Volt/(Amp sec−1) = 1 Henry. This unit is named after Joseph Henry, who discovered
self-inductance. There’s no question it’s a pretty goofy name for a unit, though.
15.4
Energy stored in an inductor
Suppose we have an inductor that is sitting on its own, and we somehow force a current to
ﬂow through it. As soon as the current level starts changing, a back EMF is induced that
opposes the ﬂow of the current. We can force the current to ﬂow by ﬁghting this back EMF;
140


## Page 6

but, it takes power to do so. To overcome the back EMF of the inductor, we must supply a
power to the inductor of
P = IE = LI dI
dt .
Suppose we increase the current ﬂowing through the inductor from I = 0 at t = 0 to I at
some later time t. How much work is done to do this? Since P = dW/dt, we just integrate:
W
=
Z t
0 P dt
=
Z t
0 LI dI
dt dt
=
Z I
0 LI dI
=
1
2LI2 .
Since we did this much work to get the current ﬂowing, this is the energy that is stored in
the inductor:
UL = 1
2LI2 .
15.4.1
Magnetic ﬁeld energy
How exactly is this energy stored in the inductor? The key thing that we changed is that we
created a magnetic ﬁeld where there was none previously. This energy must essentially be the
energy that is stored in the magnetic ﬁeld we have just created! (Since we previously talked
about energy stored in electric ﬁelds, and since electric and magnetic ﬁelds are essentially
the same thing from the viewpoint of special relativity, it shouldn’t be too much of a surprise
that we can discuss the energy of magnetic ﬁelds as well.)
It is easy to see that a magnetic ﬁeld has an energy density by looking at the spe-
ciﬁc example of the solenoidal inductor.
Suppose a current I is ﬂowing in the solenoid
discussed previously. The energy that is stored in it is UL =
1
2LI2. We also know that
L = 4π2N 2R2/(c2l). Let’s write this out and reorganize things:
UL
=
1
2LI2
=
2π2N 2R2
c2l
I2 .
The volume of the solenoid is just V = πR2l (it’s a cylinder of radius R and height l). The
magnetic ﬁeld of the solenoid is B = 4πNI/(cl). Knowing this, we can rewrite the above
formula as
UL
=
πR2l
8π
4πNI
cl
2
=
(Volume) B2
8π .
This means that the magnetic ﬁeld has an energy per unit volume of B2/8π — a result that
is VERY similar to the energy per unit volume of the electric ﬁeld!
141


## Page 7

This is one of the nice things about cgs units: it really brings out the symmetry between
the ﬁelds. If uX is the energy per unit volume of the X ﬁeld, then we have
uE
=
E2
8π
uB
=
B2
8π .
In SI units, it’s not quite so symmetric:
uE
=
ϵ0 E2
2
uB
=
B2
2µ0
.
15.4.2
Using energy to ﬁnd L
In many cases, the result that the energy density uB = B2/8π and the total energy U = 1
2LI2
can be used as a tool for computing the self inductance. This is sometimes easier than looking
at a time varying current, calculating the EMF induced, and reading out the inductance L.
Here’s a simple recipe that often works very nicely:
• Compute the magnetic ﬁeld.
• Integrate B2/8π over a volume.
• Divide by I2; multiply by 2.
What is left must be the inductance L.
You will have an opportunity to test drive this trick on a pset.
142


## Page 8

15.5
Mutual inductance and reciprocity
Let’s return to the ﬁrst example that we discussed: the loop inside the solenoid. Let us
label the solenoid with a “1” (i.e., it is “circuit element 1”), and the loop with a “2”. We
I
I
sol
sol
loop
found that the EMF induced in the loop was equal to some factor times the rate of change
of current in the solenoid. Using our new labeling system, we would say
E2 = M21
dI1
dt .
The coeﬃcient M21 is called the mutual inductance; in this case it is the mutual inductance
from element 1 to element 2. For this setup, it is something we already worked out:
M21 = 4π2r2N
c2l
where r is the radius of the small loop.
Suppose that we now reverse things: rather than putting our time varying current through
the solenoid, we put it through the small loop. By deﬁnition, the EMF induced in the solenoid
by this time changing current must be described by
E1 = M12
dI2
dt .
However, how do we calculate M12? It should be a total mess — the B ﬁeld from the loop is
highly non trivial, and the geometry of the solenoid through which we need to calculate the
ﬂux is very complicated. It seems like there is no hope to possibly calculate this!
It turns out there is an amazing theorem — the “reciprocity theorem” — that makes it
all easy. The reciprocity theorem tells us that
M12 = M21 .
Operationally, this means we can solve the “hard” problem — induced EMF in solenoid due
to changing currents in loop — by ﬁrst solving the “easy” problem — induced EMF in loop
due to changing currents in solenoid. This is fantastic news for solving nasty problems.
143


## Page 9

The proof of this result is a very nice application of the vector potential. Consider two
loops of wire,
Loop 1
Loop 2
Suppose that a current I runs through loop 1. What is the ﬂux of magnetic ﬁeld through
loop 2 due to the current in loop 1? By deﬁnition, this ﬂux will be
Φ21 =
Z
S2⃗
B1 · d⃗a2
where⃗B1 is the magnetic ﬁeld arising from loop 1, S2 is the surface spanned by loop 2, and
d⃗a2 is an area element on this surface. (You’ll see why I choose a lower case a for the area
element in just a moment.) Now, we rewrite this result in terms of the vector potential
arising from loop 1:
Φ21
=
Z
S2
⃗
∇×⃗A1

· d⃗a2
=
I
C2⃗
A1 · d⃗l2 .
On the last line, we’ve used Stokes’ theorem to reexpress the ﬂux as a line integral of the
vector potential. Finally, we use the fact that the vector potential from a current in loop 1
to some ﬁeld point is⃗
A1 = I
c
I
C1
d⃗l1
r .
With this, the ﬂux becomes
Φ21
=
I
c
I
C1
I
C2
d⃗l1 · d⃗l2
r21
where r21 is the distance from the length element d⃗l1 to the length element d⃗l2.
Now, what happens if I put the current I in loop 2 and ask what is the ﬂux that goes
through loop 1? Going through all of these steps again, we ﬁnd
Φ12
=
I
c
I
C2
I
C1
d⃗l2 · d⃗l1
r12
.
This is the exact same thing as Φ21! Since the ﬂuxes are the same, the derivative of the ﬂuxes
must be the same; it follows that the mutual inductance M12 = M21, and the reciprocity
theorem is proved.
144


## Page 10

15.6
Transformers
A very important practical application of mutual inductance is in the construction of trans-
formers: devices which step up (or step down) an AC voltage. The simplest transformer
consists of a pair of nested solenoids:
Primary: N1 turns
Secondary: N2 turns
The idea is that we drive a time varying current through the primary, making a time
varying magnetic ﬂux:
E1 = N1
c
dΦB
dt
where ΦB is the magnetic ﬂux from a single turn. Since the same ﬂux threads the second
solenoid, the induced EMF in the outer solenoid is
E2 = N2
c
dΦB
dt
.
Comparing, we have
E2 = E1
N2
N1
.
By changing the ratio of turns, we can make enormous voltages ... or, we can step voltages
down.
145
