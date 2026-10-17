# Lec 9 - Charging and discharging of Capacitor- mit - scot huges

> Source: `Lec 9 - Charging and discharging of Capacitor- mit - scot huges.pdf`  
> Pages: 9


## Page 1

Scott Hughes
8 March 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 9:
Variable currents; Th´evenin equivalence
9.1
Variable currents 1: Discharging a capacitor
Up til now, everything we have done has assumed that things are in steady state: all ﬁelds
are constant; charges are either nailed in place or else are ﬂowing uniformly. In reality, such
a situation tends to be the exception rather than the rule. We now start to think about
things that vary in time.
Suppose we have a capacitor C charged up until the potential diﬀerence between its
plates is V0; the charge separation is Q0 = CV0. We put this capacitor into a circuit with a
resistor R and a switch s:
R
s
C
What happens when the switch is closed?
Before thinking about this with equations, let’s think about what happens here physically.
The instant that the switch is closed, there is a potential diﬀerence of V0 across the resistor.
This drives a current to ﬂow. Now, this current can only come from the charge separation
on the plates of the capacitor: the excess charges on one plate ﬂow oﬀand neutralize the
deﬁcit of charges on the other plate. The ﬂow of current thus serves to reduce the amount
of charge on the capacitor; by Q = CV , this must reduce the voltage across the capacitor.
The potential diﬀerence which drives currents thus becomes smaller, and so the current ﬂow
should reduce. We expect to see a ﬂow of current that starts out big and gradually drops
oﬀ.
To substantiate this, turn to Kirchhoﬀ’s laws: at any moment, the capacitor supplies an
EMF V = Q/C. As the current ﬂows, there is a voltage drop −IR across the resistor:
Q
C −IR = 0 .
80


## Page 2

This is true, but not very helpful — we need to connect the charge on the capacitor Q to
the ﬂow of current I. Thinking about it a second, we see that we must have
I = −dQ
dt .
Why the minus sign? The capacitor is losing charge; more accurately, the charge separation
is being reduced. In this situation, a large, positive current reﬂects a large reduction in the
capacitor’s charge separation.
Putting this into Kirchhoﬀ, we end up with a ﬁrst order diﬀerential equation:
Q
C + RdQ
dt = 0 .
To solve it, rearrange this in a slightly funny way:
dQ
Q = −dt
RC .
Then integrate both sides. We use the integral to enforce the boundary conditions: initially
(t = 0), the charge separation is Q0. At some later time t, it is a value Q(t). Our goal is to
ﬁnd this Q(t):
Z Q=Q(t)
Q=Q0
dQ
Q = −
Z t
t=0
dt
RC
→ln
"Q(t)
Q0
#
= −t
RC .
Taking the exponential of both sides gives the solution:
Q(t) = Q0e−t/RC .
The charge decays exponentially. After every time interval of RC, the charge has fallen by
a factor of 1/e relative to its value at the start of the interval.
Sanity check: does RC make sense as a time? Let’s check its units:
• CGS: R × C has units (sec/cm) × (cm) = seconds.
• SI: R×C is (ohms)×(farads) = (volts/amps)×(coulombs/volts) = coulombs/amps =
seconds.
So it does make sense.
Let’s look at the current I(t):
I(t) = −dQ
dt = −Q0
d
dte−t/RC = Q0
RC e−t/RC .
Just like the charge, the current decays exponentially. In particular, it starts out at some
big value, and then falls away — just as our physical intuition told us it would.
81


## Page 3

9.2
Variable currents 2: Charging a capacitor
Let’s consider a diﬀerent kind of circuit. The capacitor begins, at t = 0, with no charge;
but, the circuit now contains a battery:
R
s
C
Vb
Now, what happens when the switch is closed?
Let’s again think about this physically before doing the math. When the switch is ﬁrst
closed, the EMF of the battery can very easily drive a current, so we expect the current to
jump up, and charge to begin accumulating on the capacitor. As this charge accumulates,
an⃗E ﬁeld will build up in a direction that opposes the ﬂow of current! Thus, we expect that,
as time goes on, the ﬂow of current will decrease. Eventually it will stop, when there is just
enough charge on the capacitor to totally oppose the battery.
Let’s check this. For Kirchhoﬀ, we have an EMF Vb from the battery, and two voltage
drops: −Q/C from the capacitor, and −IR across the resistor:
Vb −Q
C −IR = 0 .
We again need to relate the current I and the capacitor’s charge Q. Thinking about it for a
second, we must have
I = +dQ
dt .
Why a plus sign?
In this case we are adding charge to the capacitor (more accurately,
increasing the charge separation). Large current means a large increase in the charge sepa-
ration. When doing a problem involving a circuit like this, it is important to stop and think
carefully about how the capacitor’s charge relates to the charge ﬂowing onto it or oﬀof it.
We end up with the following diﬀerential equation:
Vb −Q
C −RdQ
dt = 0 .
Rearrange:
dQ
dt = −Q −CVb
RC
82


## Page 4

or
dQ
Q −CVb
= −dt
RC .
Integrate: we require Q(t = 0) = 0, so we ﬁnd
ln
"CVb −Q(t)
CVb
#
= −t
RC .
Exponentiating both sides and solving for Q(t), we ﬁnd
Q(t) = CVb
³
1 −e−t/RC´
.
This charge starts oﬀat zero, builds up quickly at ﬁrst, then starts building up more and
more slowly. It asymptotically levels oﬀat Q = CVb as t →∞. Let’s look at the current:
I(t)
=
CVb
d
dt
³
1 −e−t/RC´
=
Vb
R e−t/RC .
As we intuitively guessed, the current starts large, but drops oﬀas time passes and the
capacitor’s electric ﬁeld impedes it.
Notice that the voltage across the capacitor
VC(t) = Q(t)
C
= Vb
³
1 −e−t/RC´
and the voltage across the resistor
VR(t) = I(t)R = Vbe−t/RC
sum to give a constant,
VC(t) + VR(t) = Vb
³
1 −e−t/RC´
+ Vbe−t/RC = Vb ,
the EMF of the battery. If you think about Kirchhoﬀ’s rules for a moment, this should make
a lot of sense!
9.3
Charging and discharging revisited
Suppose you’re taking a test and you don’t want to slog through setting up a bunch of
integrals and running the risk of botching the details because of a silly mistake. Provided
you understand physically what is going on in the above discussions, you can write down
the rules for charge on a capacitor without doing any math. You only need to know three
things:
1. The time variation has to look like e−t/RC.
2. You need the initial (t = 0) charge on the capacitor, and
3. You need the ﬁnal (t →∞) charge on the capacitor.
83


## Page 5

Then, you just need to ﬁgure out to hook everything together so that you get a formula
that obeys the correct boundary conditions. For example, if a problem involves discharging
a capacitor, you know that you start out with some initial value Q0, and that it must fall
towards zero as time passes. The only formula that obeys these conditions and has the
correct time variation is
Q(t) = Q0e−t/RC ,
just what we derived carefully before. If it involves charging up a capacitor, you want a
formula that has Q = 0 at t = 0, and that levels oﬀat CVb as t →∞. Using 1 −e−t/RC as
our “time variation” piece of the solution gets the t = 0 behavior right; multiplying by CVb
ensures that we level oﬀat the right value at large t. We end up with
Q(t) = CVb
³
1 −e−t/RC´
.
Again, just what we derived carefully before.
If you can remember these physical reasons why the charge behaves as it does, you can
save yourself some pain later on.
9.4
Th´evenin equivalence
The RC circuits we’ve looked at so far are quite simple — there’s only one resistor, and it’s
hooked up to the capacitor and/or battery in series. How do we handle a more complicated
circuit? Consider the following:
C
Vb
R
R
2
1
How does the charge on the capacitor evolve with time?
This problem can be tackled quite simply by using Kirchhoﬀ’s laws: we have multiple
loops, so we go around them and write down equations balancing the voltage drops and
EMFs; we make sure the currents balance at the junctions; math happens; we ﬁnd Q(t). As
an exercise, this is straightforward, but slightly tedious.
84


## Page 6

There is in fact a very cute way to approach this, based on a theorem proved by L´eon
Charles Th´evenin1:
Th´evenin’s Theorem: Any combination of batteries and resistances with two
terminals can be replaced by a single voltage source VOC and a single series
resistor RT.
For our problem, this means that we can redraw the circuit as
VOC
RT
s
C
The answer is now obvious! We just steal results from before, and write down
Q(t) = CVOC
³
1 −e−t/RT C´
.
We just need to know how to work out VOC and RT.
1I tried to ﬁnd biographical information about this guy and totally failed. Fortunately, an anonymous
Spring ’04 8.022 student was more persistant than me, and found a web bio:
http://www.eleceng.adelaide.edu.au/famous.html#thevenin
He was a French telegraph engineer, and hence very well versed in practical aspects of electrical circuits.
Interestingly, “his” theorem was actually ﬁrst derived by Hermann Von Helmholtz.
85


## Page 7

To do this, we take the capacitor out of the circuit and consider what remains as a pair
of terminals:
Vb
R
R
2
1
If we short circuit these terminals with a wire, a current ISC — the “short circuit” current
— will ﬂow. On the other hand, if we leave it open, there will be a potential diﬀerence —
the “open circuit” voltage, VOC — between the terminals (equivalent to the potential drop
over the resistor R2).
Let’s calculate these quantities. Shorting the terminals out is equivalent to putting a 0
Ohm resistor in parallel with R2. The current that ﬂows is what you would get if R2 were
not even present:
ISC = Vb
R1
.
On the other hand, if we leave the terminals open, the current that ﬂows through the circuit
is I = Vb/(R1 + R2). The open circuit voltage is thus given by
VOC = VR2 = IR2 =
VbR2
R1 + R2
.
The Th´evenin equivalent resistance is deﬁned as the ratio of these quantities:
RT ≡VOC
ISC
.
For this particular circuit, it takes the value
RT
=
VbR2
R1 + R2
× R1
Vb
=
R1R2
R1 + R2
.
The solution for the charge on the capacitor is thus ﬁnally given by
Q(t) = CVb
µ
R2
R1 + R2
¶
[1 −exp(−t(R1 + R2)/CR1R2)] .
86


## Page 8

9.5
Th´evenin in general
Th´evenin’s theorem is much more general than this simple example. In general, it means
that you can be given any grungy mess of resistors and batteries and reduce it to a single
battery with EMF VOC and a single resistor RT: anything like this
Huge mess of
resistors and
batteries
can be reduced to this
VOC
RT
If you know what the big mess inside the “black box” is made out of, then you can ﬁgure
out VOC and RT as we did for the example above.
In some situations, you don’t know. For example, you might have a piece of lab equipment
that you need to use for some experiment, and you need to know how to treat it in a circuit.
In that case, you measure VOC; you short out the terminals and measure ISC; and then you
know RT = VOC/ISC.
Th´evenin’s theorem works only when all the elements inside the box obey Ohm’s law.
This means that the relationship between current and voltage for every element is linear.
This in turn means that the relationship between current and voltage for any combination
of circuit elements in the box must be linear. (Why? Add a bunch of lines together: you get
a line!) The procedure for determining the Th´evenin equivalence of a circuit simply assumes
that you have some linear relationship between the voltage and current at the terminals.
VOC tells us where this relationship crosses the voltage axis; ISC tells us where it crosses the
current axis. RT is the slope. (Negative slope, really, since the line rises in the “wrong”
direction; same diﬀerence.)
87


## Page 9

V
I
OC
V
ISC
Slope = RT
88
