# Lec 17 - AC Circuits; Impedance.- scott huges- mit

> Source: `Lec 17 - AC Circuits; Impedance.- scott huges- mit.pdf`  
> Pages: 12


## Page 1

Scott Hughes
14 April 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 17:
AC Circuits; Impedance.
17.1
AC circuits: Intro
As mentioned in Lecture 15, we use induction to generate the vast majority of electrical
power in the world. Typically, we do this with some variation on the “vary the dot product”
mechanism:
B
n^
The loops of wire are rotated by some external source of work — a diesel engine, a waterfall,
nuclear produced steam, etc. The magnetic ﬁeld largely acts as a mechanism to transform
that external work into electrical power. Doing so, we end up with a driving EMF that is
sinusoidal:
ΦB = BA cos ωt
−→E = ωBA
c
sin ωt .
At least in part for this reason, the electricity that we get “from the wall” oscillates sinu-
soidally. To insure some degree of uniformity, standard choices for the oscillation frequency
have been agreed upon. To demonstrate that humans are illogical beings who will shoot
themselves in the foot at any opportunity, two such standards are commonly used:
ω
=
2π × 60 Hz
ω
=
2π × 50 Hz .
60 Hz is used in North America, much of South America, South Korea, and western Japan; 50
Hz is used in Europe, most of Africa (except, for example, Liberia), the rest of South America,
156


## Page 2

and most of Asia (including eastern Japan). See http://kropla.com/electric2.htm for a
summary.
The main reason for going through this is to motivate how essential it is to understand
how alternating current (AC) circuits work. Having spent as much time as we have studying
direct current (DC) circuits, generalizing to AC is not too diﬃcult — particularly if we are
smart enough to recognize that our life is made a LOT easier by working with complex
valued quantities.
Our goal in this lecture will be to understand how to ﬁnd the current which ﬂows in the
following circuit:
C
L
R
The symbol on the left is a source of AC EMF. This device supplies an EMF to the rest of
the circuit which we will take to be
E(t) = E0 cos ωt .
In much of our analysis, we will ﬁnd it very useful to take this be the real part of a complex
EMF ˜E(t):
E(t) = Re
h ˜E(t)
i
where
˜E(t) = E0eiωt .
(Note that E0 is a purely real number.)
We will analyze this circuit by just generalizing the operating principles that we used for
DC circuits. In particular,
1. The sum of the voltage drops in the loop must equal the driving EMF. This is true for
both the real form of the voltage
E(t) = VR(t) + VC(t) + VL(t)
and the complex form:
˜E(t) = ˜VR(t) + ˜VC(t) + ˜VL(t) .
157


## Page 3

You may ask “What is the voltage drop across an inductor — doesn’t an inductor act
as a source of EMF?” Indeed, you would be correct for asking this. To keep things
uniform, what we do is move the EMF from the left-hand side to the right-hand side,
introducing a minus sign. Hence, VL(t) = −Eind = LdI/dt. There’s nothing deep here
— it’s just a trick we introduce in order to treat all circuit elements in a uniform way.
2. The same current must pass through every circuit element. Likewise true both for real
and for complex:
I(t) = IR(t) = IC(t) = IL(t)
˜I(t) = ˜IR(t) = ˜IC(t) = ˜IL(t) .
To understand this “driven RLC” circuit, we will ﬁrst analyze the response of each of its
circuit elements one by one.
17.1.1
AC + resistor
Resistors obey Ohm’s law. Period. End of story. If we hook our driving AC EMF source
across a resistor R, we have
E(t) = VR(t) = I(t)R .
At the risk of totally beating this to death, if we plot our driving EMF and the current in
the circuit together, the plot generally looks like this:
2
4
6
8
10
12
-4
-2
2
4
(The solid line is the driving EMF, the dotted line is the current.) The key thing to take
away is the following rule:
In a resistor, the current and the voltage are IN PHASE with each other.
In other words, the peak voltage occurs at the same time as the peak current, the minimum
voltage coincides with the minimum current, etc.
158


## Page 4

The same information represented by phasors in the complex plane is
Re(I)
Re(V)
Im(V)
Im(I)
ω
ωt
t
“In phase” means that both phasors are at the same angle (though their magnitudes, or
lengths, may be diﬀerent).
17.1.2
AC + capacitor
The situation is not quite so straightforward if we hook our AC EMF source across a capac-
itor. The governing equation in this case is
E(t) = VC(t) = Q(t)
C
.
Plugging in E(t) = E0 cos ωt, solving for Q(t) and taking the derivative, we have
I(t)
=
−ωCE0 sin ωt
=
ωCE0 cos(ωt + π/2) .
Let’s plot the voltage and the current together:
2
4
6
8
10
12
-4
-2
2
4
Notice that maxima in the current occur before maxima in the voltage (likewise for minima):
159


## Page 5

Current LEADS voltage by 90◦. Equivalently, voltage LAGS current by 90◦.
The relation between the current and the voltage in the capacitor has a particularly nice
form when expressed using complex numbers. The voltage is given by
VC(t) = E0 cos(ωt) = Re
h˜VC(t)
i
where
˜VC(t) = E0eiωt .
The current is given by
I(t) = ωCE0 cos(ωt + π/2) = Re
h˜I(t)
i
where
˜I(t)
=
ωCE0ei(ωt+π/2)
=
iωCE0eiωt .
(On the last line I have used the fact that eiπ/2 = i.)
Putting all of this together, we can write the relation between the voltage and the current
in the capacitor in a form that is just Ohm’s law:
˜VC(t) = ˜I(t)ZC
where
ZC =
1
iωC
is the impedance of the capacitor. Viewed as phasors in the complex plane, the current and
the voltage look as follows:
Re(I)
Re(V)
Im(V)
Im(I)
ωt
ωt + π/2
Notice that the current is rotated 90◦ahead of the voltage, in keeping with the “current
leads voltage, voltage lags current” rule.
160


## Page 6

17.1.3
AC + inductor
Now, let’s hook our AC EMF across an inductor. Our governing equation is clearly going to
be
E(t) = VL(t) = LdI
dt .
Plugging in E(t) = E0 cos ωt, we ﬁnd
dI
dt = E0
L cos ωt .
Integrating up, we ﬁnd
I(t)
=
E0
ωL sin ωt
=
E0
ωL cos (ωt −π/2) .
Let’s plot the voltage and the current together:
2
4
6
8
10
12
-4
-2
2
4
In this case, maxima in the current occur after maxima in the voltage (likewise for minima):
Current LAGS voltage by 90◦. Equivalently, voltage LEADS current by 90◦.
The relation between the inductor’s current and voltage again has a particularly nice form
when expressed with complex numbers. The voltage is
VL(t) = E0 cos(ωt) = Re
h˜VL(t)
i
where
˜VL(t) = E0eiωt .
The current is given by
I(t) = E0
ωL cos(ωt −π/2) = Re
h˜I(t)
i
161


## Page 7

where
˜I(t)
=
E0
ωLei(ωt−π/2)
=
E0
iωLeiωt .
(On the last line I have used the fact that e−iπ/2 = 1/i.)
Putting all of this together, we can write the relation between the voltage and the current
in the inductor in a form that is just Ohm’s law:
˜VL(t) = ˜I(t)ZL
where
ZL = iωL
is the impedance of the inductor.
Viewed as phasors in the complex plane, the current and the voltage are
Re(I)
Re(V)
Im(V)
Im(I)
ωt
ωt − π/2
Notice that the current is 90◦behind in the voltage, in keeping with the notion that current
lags voltage in inductors.
162


## Page 8

17.2
Putting it together: Driven series RLC, take 1
We’re now ﬁnally ready to analyze this circuit:
C
L
R
Doing so is actually quite easy as long as we work in the complex domain! We just use the
rules we established earlier,
˜E(t) = ˜VR(t) + ˜VL(t) + ˜VC(t)
˜I(t) = ˜IR(t) = ˜IL(t) = ˜IC(t)
to which we now add our new version of Ohm’s law:
˜VX(t) = ˜IX(t)ZX
where X stands for the resistor, the capacitor, or the inductor.
Our ﬁrst equation becomes
E0eiωt
=
˜I(t)
·
R + iωL +
1
iωC
¸
=
˜I(t)
·
R + i
µ
ωL −1
ωC
¶¸
=
˜I(t)Ztot
where Ztot is the total impedance of the circuit:
Ztot = R + iωL −
i
ωC = R + i
µ
ωL −1
ωC
¶
.
Notice that the total impedance is dominated by the inductor at high frequency, and by the
capacitor at low frequency. We will see this again very soon.
Using the above result, the complex current in the circuit is given by
˜I(t) =
E0eiωt
R + i [ωL −1/(ωC)] .
To keep our notation simple, we will write this as
˜I(t) = I0eiωte−iφ .
163


## Page 9

In other words, we are just factoring out the eiωt piece, and putting
I0e−iφ =
E0
R + i [ωL −1/(ωC)] .
Don’t get excited about the minus sign in front of the iφ. All this means is that we deﬁne
φ as the angle by which the current will LAG the voltage. This is convention, not anything
deep. If φ turns out to be negative, then it means that the current actually leads the voltage.
Our job now will be to ﬁgure out the “current amplitude” I0 and the current phase angle
φ. To make progress on this, we note that any complex number can be written in the form
z = re−iφ
where r =
√
zz∗. Let’s look at the magnitude of the current ﬁrst:
|˜I| = I0
=
q
˜I ˜I∗
=
E0
v
u
u
t
Ã
1
R + i [ωL −1/(ωC)]
! Ã
1
R −i [ωL −1/(ωC)]
!
=
E0
q
R2 + [ωL −1/(ωC)]2 .
This is pretty cool. The amount of current that ﬂows through this circuit varies — quite
strongly! — as a function of the AC frequency ω. Notice that the maximum current ampli-
tude occurs when ω = ω0 = 1/
√
LC: at this frequency, the L and the C terms cancel each
other out, leaving just the resistance term.
Now we need to ﬁgure out that phase term. To set things up, note that from the rule
z = re−iφ = r (cos φ −i sin φ)
we can extract
tan φ = −Im [z]
Re [z] .
Now, we want to do something like this for our complex current. Let us massage this relation
a bit:
I0e−iφ
=
E0
R + i [ωL −1/(ωC)]
=
E0
R + i [ωL −1/(ωC)]
ÃR −i [ωL −1/(ωC)]
R −i [ωL −1/(ωC)]
!
=
E0
R2 + [ωL −1/(ωC)]2 (R −i [ωL −1/(ωC)]) .
164


## Page 10

Taking the ratio of the imaginary part to the real part, we have
tan φ
=
ωL −1/(ωC)
R
=
ωL
R −
1
ωCR .
Typically, φ ends up having a shape as a function of ω that looks something like this:
500
1000
1500
2000
-1.5
-1
-0.5
0.5
1
1.5
Figure 1: φ vs ω for R = 1 Ohm, L = 0.01 Henry, C = 10−4 Farad.
Notice that, for low frequency, the phase angle limits to −π/2: the current LEADS the volt-
age by ∼90◦at low frequency. This is exactly the behavior we saw when we considered our
EMF attached to just the capacitor! This has a very nice interpretation: at low frequencies,
the capacitor dominates the overall impedance of the circuit — exactly what we expected
on intuitive grounds from the form of Ztot. Likewise, at high frequencies, the phase angle
limits to +π/2: the current LAGS voltage by ∼90◦— exactly the behavior we see for EMF
attached to the inductor; and, exactly what Ztot would suggest.
165


## Page 11

17.3
Putting it together: Driven series RLC, take 2
The phasor picture allows us to put together another way of getting the above result that
is perhaps a little more intuitive. The basic idea is to treat the phasors as vectors in the
complex plane. Then, we just add them all head to tail:
Re(V)
Im(V)
V
V
V
R
L
C
~
~
~
This diagram shows the voltage drop across the resistor, ˜VR, along with the drop across
the inductor (90◦ahead) and across the capacitor (90◦behind). This drawing simpliﬁes by
combining the voltage drops across the inductor and the capacitor:
Re(V)
Im(V)
V
V
R
L
~
~
+ V~
C
E~
φ
We can now work out a lot of things using simple geometry and trigonometry! For example,
the rule that the total voltage drop in the circuit must equal the driving EMF tells us that
˜VR + ˜VL + ˜VC = ˜E .
The driving EMF ˜E is the “resultant” vector we obtain by summing the other three phasors;
φ is the angle between ˜E and ˜VR (since ˜VR is in phase with the current in the circuit).
With the Pythagorean theorem, we get the current’s magnitude very easily:
E2
0
=
V 2
R + (VL −VC)2
166


## Page 12

=
I2
0
"
R2 +
µ
ωL −1
ωC
¶2#
−→I0
=
E0
q
R2 + [ωL −1/(ωC)]2 .
Likewise, we can get the phase angle φ with simple trigonometry:
tan φ
=
VL −VC
VR
=
ωL
R −
1
ωCR .
Exactly what we had before!
17.4
Summary
AC circuits are surprisingly easy to analyze, provided you follow some simple rules:
1. Do all of your calculations using complex voltages and currents. Replace cos(ωt) with
eiωt; replace sin(ωt) with cos(ωt −π/2) = ei(ωt−π/2).
2. Relate the voltage drops and currents across any circuit element using our “generalized
Ohm’s law”:
˜VX = ˜IXZX .
The quantity ZX is the impedance of a circuit element X. Impedence is just resistance
on steroids: it works exactly like resistance in a DC circuit, but is complex, frequency
dependent, and works in AC circuits. The impedance formulas you need to know are
ZR
=
R
ZC
=
1/(iωC)
ZL
=
iωL .
3. Analyze your circuit using impedance and complex voltages and currents just like you
would analyze a DC circuit containing only resistors. Be careful to get all magnitudes
and phases correct — the math is likely to be a little more hairy than a simple DC
circuit. A good phasor diagram can help organize things.
4. Take the real parts of all relevant quantities at the end of the day.
And that’s it.
167
