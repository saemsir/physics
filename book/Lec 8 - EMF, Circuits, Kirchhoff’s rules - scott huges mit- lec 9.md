# Lec 8 - EMF, Circuits, Kirchhoff’s rules - scott huges mit- lec 9

> Source: `Lec 8 - EMF, Circuits, Kirchhoff’s rules - scott huges mit- lec 9.pdf`  
> Pages: 8


## Page 1

Scott Hughes
3 March 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 8:
EMF, Circuits, Kirchhoff’s rules
8.1
EMF: Electromotive force
The workings of our technological civilization are largely based on the idea that we use
electric currents as a means to get devices to do work for us. In this lecture, we will begin
to understand at a fundamental level how this works.
In order for a current to ﬂow, we must create a potential diﬀerence over some conductive
material; and, we must have continuous source of charges that can ﬂow through our conduc-
tor. Such a source, with a “built-in” potential diﬀerence is called a source of “electromotive
force” (a rather misleading name, since it isn’t a force). This is usually abbreviated EMF,
and is often denoted E.
The simplest example of an EMF source is a battery. A battery is a device that maintains
a separation of charges between two terminals. Current can ﬂow inside the battery from
one terminal to another via an electrochemical reaction. One example, used in many car
batteries, is based on the electrochemistry of lead. Two terminals, one of lead oxide, another
of porous lead, are immersed in sulphuric acid.
E
−
+
H+
PbO2
Pb
When immersed in the acid, it is energetically favorable for the porous lead terminal to
provide free electrons, producing lead sulfate and free hydrogen ions in the solution:
Pb + HSO−
4 →PbSO4 + H+ + 2e−
At the lead oxide electrode, a reaction which absorbs free electrons and free hydrogen ions
is energetically favorable:
PbO2 + 3H+ + HSO−
4 + 2e−→PbSO4 + 2H2O
If it is possible for both electrons and H+ ions to travel from one terminal to the other, then
the net chemical reaction
Pb + PbO2 + 2H2SO4 →2PbSO4 + 2H2O
72


## Page 2

can proceed.
When the terminals of the battery shown above are not connected, there is no way for
electrons to get from one terminal to another. An electric ﬁeld inside the battery builds
up, pointing from the + terminal to the −terminal. This ﬁeld opposes the motion of H+
ions — they cannot cross to the + terminal, and the reaction stops. When the terminals
are connected by a conductor, on the other hand, electrons freely ﬂow to the + terminal.
The electric ﬁeld is reduced, the H+ ions can now easily move across, and the reaction runs
happily.
The EMF of the battery is just the potential of the + terminal with respect to the −
terminal:
E = −
Z + term
−term⃗E · d⃗s .
This EMF is then the potential diﬀerence that is available to drive currents in an electrical
circuit.
8.2
Circuits and Kirchhoﬀ’s second rule
Suppose we take a battery that provides EMF V and connect its terminals with conducting
material of resistance R:
V
R
(The symbol on the left is used for a battery in a circuit; the long bar denotes the + terminal,
the short bar denotes −. The symbol on the right describes a “resistor”, some conducting
material with known resistance R.) How much current ﬂows in this circuit? From Ohm’s
law, we must have
V = IR →I = V/R .
Another way to view this is to say that when a current I ﬂows through a resistance R, there
is a “voltage drop” ∆V = −IR. This motivates what is known as “Kirchhoﬀ’s second1 rule”
for circuits: Around any closed loop, the sum of the EMFs and the potential drops
across circuit elements must equal zero. This rule was ﬁrst deduced by the German
scientist G. Kirchhoﬀin the mid 1800s; really, it is just a restatement of the rule
H⃗E ·d⃗s = 0.
1We’ll get to Kirchhoﬀ’s ﬁrst rule soon enough.
73


## Page 3

Suppose we have multiple resistors in our circuit:
V
R
R
R
1
2
3
The battery still supplies an EMF V to the circuit. Now, it must be shared among all three
resistors. To ﬁgure out how much voltage drop occurs across each resistor, notice that the
current must be the same through all of the circuit elements — if it were not the same,
charge would pile up somewhere in the circuit. The voltage drop across the jth resistor is
∆Vj = −IRj; for the whole circuit, Kirchhoﬀ’s second rule tells us
V
+
X
j
∆Vj = 0
V
−
I(R1 + R2 + R3) = 0
→I
=
V
R1 + R2 + R3
.
This is equivalent to a circuit containing a single resistor, with Req = R1 + R2 + R3. This
logic obviously generalizes: if we have N resistors hooked up in series like this, the equivalent
resistance of the circuit is given by
Req =
N
X
i=1
Ri .
74


## Page 4

8.3
Circuits and Kirchhoﬀ’s ﬁrst rule
In the previous example, the resistors were connected in series. Another important network
topology comes from connecting the resistors in parallel:
V
R1
R2
I
I
I
1
2
The battery in this circuit supplies a total current I to all circuit elements. This current
divides up into pieces I1 and I2. Kirchhoﬀ#2 tells us that the sum of the EMFs and the
voltage drops around any closed loop must be zero. A circuit network like that shown here
contains three loops to which we can apply this rule: the left loop, the right loop, and the
loop that goes around the perimeter of the circuit. The left loop tells us
V = I1R1 →I1 = V
R1
;
the perimeter loop tells us
V = I2R2 →I2 = V
R2
.
(The right loop tells us I1R1 = I2R2, which we already knew.)
To make further progress, we need to introduce Kirchhoﬀ’s ﬁrst rule: The sum of the
currents entering any junction must equal the sum of the currents coming out
of the junction. This is a kind of “well, duh” rule: if it were not true, charge would pile
up like mad in the circuit, which we know can’t happen in the steady state. In the case of
this circuit, it tells us that I = I1 + I2, so
I = V
µ 1
R1
+ 1
R2
¶
.
The resistors in parallel act like a single resistor with equivalent resistance Req given by
1
Req
= 1
R1
+ 1
R2
.
More generally, if you have N resistors in parallel, their equivalent resistance is
1
Req
=
N
X
i=1
1
Ri
.
75


## Page 5

In series, multiple resistors add, increasing the net resistance — there is only one path for
the current to follow, and you are making that path “harder” by increasing its resistance.
In parallel, multiple resistors add reciprocals, decreasing the net resistance. Rather than
making the path “harder” for the current to follow, you are opening up new paths for it.
In many (though not all) cases, one can use the parallel and series rules to reduce a
circuit to an “equivalent circuit” that is much simpler: every time you encounter resistors in
series, replace them with an equivalent resistor equal to their sum; every time you encounter
resistors in parallel, replace them with equivalent resistor whose reciprocal resistance equals
the sum of their reciprocal resistance. In some cases, combinations of resistances that look
absolutely horrible can be reduced to a single equivalent resistor; see, for example, Figure
4.16 of Purcell.
8.4
Power dissipation in circuits
As current ﬂows in the circuit, it moves through a potential diﬀerence. Work must be done
for this current to keep ﬂowing. If the source of EMF drives charge dq through the potential
diﬀerence V , the amount of work that is done is dW = V dq. If this is done in time dt, the
rate at which work is done — i.e., the power that is exerted — is given by
P = dW
dt = V dq
dt = V I .
For a circuit element that obeys Ohm’s law, this tells us that
P = (IR) I = I2R .
This is also the power that is dissipated in a resistor. If you touch a circuit element and it
feels hot, this is because it is dissipating energy at the rate I 2R.
Units: in cgs, I is in esu/sec, and V is in esu/cm. This unit of potential is equivalent
to erg/esu — recall the potential diﬀerence is work or energy per unit charge. I V thus has
units erg/sec. In SI, I is in amps, or Coulomb/sec; V is in Volts, or Joules/Coulomb. I V
thus has units Joules/sec, or Watts.
76


## Page 6

8.5
Multiple voltage source networks
How do we handle the following circuit?
R
R
V
V1
2
1
R
2
3
I
I
1
2
The multiple sources of EMF in this circuit network make this problem somewhat more
complicated than those seen so far. In particular, we cannot simply reduce the resistors into
those that are in series in the circuit and those that are in parallel — the extra battery
makes it hard to even deﬁne a meaningful notion of “in series” or “in parallel” in this case.
Kirchhoﬀ’s rules save us, provided we establish procedures for how to use them:
1. Regard the circuit as collection of independent closed current loops. “Independent”
means that the loops may overlap, but each loop has at least one portion that does not
overlap with other loops. In the example show above, there are two independent loops:
the left loop and the right loop are independent (though they share one common leg);
the left loop and the whole perimeter are independent; the right loop and the perimeter
are independent. Once you’ve picked two, the third can be regarded as a subset of them.
2. Label the currents in the loops, I1, I2, etc, until each loop has some circulating cur-
rent assigned to it. Pick the direction arbitrarily; if you guess “wrong”, but do the
subsequent calculation correctly, the current will just come out with a minus sign.
3. Apply Kirchhoﬀ’s #2 to each loop: traverse the loop in the direction of the current
that you established. Every time you cross a resistor, you get a voltage drop −IR; the
I to be used here is the total current passing through the resistor.
Every time you cross an EMF source, it contributes +V if you cross it in the “right”
direction (from the −terminal to the +). It contributes −V if you cross it in the
“wrong” direction (+ →−).
4. Apply Kirchhoﬀ’s #1 at each junction.
Following these rules, we end up with a set of linear equations which can be reduced
to ﬁnd all unknown currents in the circuit (albeit sometimes requiring a hideous amount of
77


## Page 7

algebra). Let’s look at the circuit above as an example: Traversing the left loop, Kirchhoﬀ
#2 tells us
V1 −I1R1 −(I1 −I2)R2 = 0 .
For the right loop, we ﬁnd
−V2 −I2R3 −(I2 −I1)R2 = 0 .
Kirchhoﬀ’s #1 is automatically satisﬁed, since we have I1 + I2 both entering and leaving
each junction. Rearranging these equations yields
V1
=
I1R1 + (I1 −I2)R2
V2
=
−I2R3 −(I2 −I1)R2 .
With a little eﬀort, we can reduce these equations to ﬁnd
I1
=
V1R3 + (V1 −V2)R2
R1R2 + R1R3 + R2R3
,
I2
=
(V1 −V2)R2 −V2R1
R1R2 + R1R3 + R2R3
.
Although it is somewhat beyond the scope of this course, it is worth noting that the equations
we get with Kirchhoﬀ’s laws can be rewritten as a matrix equation. For the example discussed
here, we would ﬁnd
· V1
V2
¸
=
· R1 + R2
−R2
R2
−R2 −R3
¸
·
· I1
I2
¸
.
We can use matrix algebra to solve for the currents I1 and I2 in terms of V1 and V2; the
answer will of course be identical to that given above.
More generally, if there are n independent loops in the circuit, Kirchhoﬀ’s laws provide
n equations that can be written in the form
˜V = R · ˜I ,
where
˜V =


V1
V2...
Vn

,
˜I =


I1
I2...
In

,
and where R is an n × n matrix whose elements all have the units of resistance. This may
sound hideous ... but, the solution is now relatively simple: we “simply” invert the matrix,
and ﬁnd the n currents from the equation
˜I = R−1 · ˜V .
This is the only practical way to solve for the currents in circuits that have lots of loops.
Doing the inversion isn’t even all that bad, thanks to computerized math tools. For very
large matrices (n > 100 or so), very fast matrix inverters exist for numerically speciﬁed
matrices.
78


## Page 8

8.6
EMF and batteries revisisted: Internal resistance
One ﬁnal issue of practice is often of great importance when working with batteries. When
a battery is delivering current to a circuit, there is necessarily a ﬂow of current within the
battery itself. In the example discussed at the start of this lecture, this current comes from
the motion of H+ ions from the Pb to the PbO2.
Because this reaction proceeds chemically, these reactions will dissipate energy; the bat-
tery gets hot, and energy which could have gone into the circuit is lost. This is described
mathematically by giving the battery an internal resistance r. For the purpose of any cal-
culation, the internal resistance is taken into account by simply putting a small resistor r in
series with the battery. This is usually drawn something like this:
V
r
An important consequence of internal resistance is that a battery has a maximum current
it can deliver: Imax = V/r. Roughly speaking, its chemical reactions cannot proceed fast
enough to deliver more than this current. When this happens, a power I 2
maxr is dissipated in
the battery, which gets hot in a hurry. A good way to prove to yourself the reality of internal
resistance is to carry a nine-volt battery in a pocket full of keys and change. The pieces of
metal short out the battery’s terminals, it gets hot, you scream in pain and hop around like
a lunatic2.
2Yes, I speak from personal experience.
79
