# Lec 16 - Undriven RLC circuits; phasor representation - scott huges mit

> Source: `Lec 16 - Undriven RLC circuits; phasor representation - scott huges mit.pdf`  
> Pages: 10


## Page 1

Scott Hughes
12 April 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 16:
RL Circuits.
Undriven RLC circuits; phasor representation.
16.1
RL circuits
Now that we know all about inductance, it’s time to start thinking about how to use it in
circuits. A simple circuit that illustrates the major concepts of inductive circuits is this:
V
L
R
S2
S1
Suppose that at t = 0, we close the switch S1, leaving S2 open. How does the current evolve
in the circuit after this?
Let’s ﬁrst think about this physically. Lenz’s law tells us that the magnetic ﬂux through
the inductor does not “want” to change. Since this ﬂux is initially zero, the inductor will
impede any current that tries to ﬂow it — the current will initially try to remain at zero.
As time passes, current will gradually leak through, and the magnetic ﬂux will build up.
Eventually, it should saturate at I = V/R — at this point the most current possible is
ﬂowing through the circuit.
16.1.1
To Kirchhoﬀor not to Kirchhoﬀ
We’d now like to analyze this circuit quantitively as well.
In all other circumstances in
which we’ve examined a circuit, we’ve used Kirchhoﬀ’s laws for this; for a a simple single-
loop circuit, the relevant rule is Kirchhoﬀ’s second law, “The sum of the EMFs and the
voltage drops around a closed loops is zero”.
This rule is essentially a restatement of the old electrostatics rule that
H⃗E ·d⃗s = 0. This
rule DOES NOT HOLD when we have a time changing magnetic ﬁeld! In other
words, inductors completely invalidate — at least formally — the foundation of Kirchhoﬀ’s
second law.
146


## Page 2

So what do we do? Let’s reconsider: in place of
H⃗E · d⃗s = 0, we have Faraday’s law:
I⃗
E · d⃗s = −1
c
dΦB
dt
= Eind = LdI
dt .
The closed loop integral of⃗E gives us the induced EMF. I personally ﬁnd it best to think of
the inductor as an EMF source; it acts in the circuit eﬀectively like a battery would. Even
though Kirchhoﬀ’s laws no longer stand, formally, on a very solid foundation, we can extend
the formalism by thinking of inductors in the circuit as a source of EMF. The equations
then carry over just ﬁne; indeed, they carry over so well that almost all textbooks tell you
to just apply Kirchhoﬀ’s laws to circuits containing inductors without even mentioning this
subtlety. It’s always worth bearing in mind that what you are really using is Faraday’s law.
I will try to refer to the loop rule as Faraday’s law; it’s such a habit to call it Kirchhoﬀ’s
law, though, that I will surely slip from time to time.
The tricky thing in these kinds of problems is getting the signs right. In all of these cases,
Lenz’s law should guide you: the induced EMF will act in such a way as to oppose changes
in the inductor’s magnetic ﬂux. If a circuit initially has no current ﬂowing through it, the
inductor will oppose the build-up of current; if it initially does have current ﬂowing, the
inductor will try to keep that current ﬂowing. Keep this intuition in mind and you should
have no problem choosing the correct sign for the inductor’s EMF.
(Very detailed discussion of inductors and the failure of Kirchhoﬀ’s laws can be found in
Walter Lewin’s OCW 8.02 lectures from 2002; see Lectures 15 and 20 in particular.)
16.1.2
Back to our regularly scheduled program
OK, let’s calculate. The EMF due to the battery is +V ; the EMF induced in the inductor
is −LdI/dt. Why the minus sign? It’s going to ﬁght the growth in current, and so must be
opposite to the battery. Finally, there’s a voltage drop −IR at the resistor:
V −IR −LdI
dt = 0 .
Rearrange:
dI
dt
=
V −IR
L
=
R
L
µV
R −I
¶
.
Now divide; we end up with something that is of the form du/u:
dI
I −V/R = −R dt
L
so it is easy to integrate up, using the boundary conditions I = 0 at t = 0, I = I(t) at some
general time t:
ln
"I(t) −V/R
−V/R
#
= −Rt
L
or
I(t) = V
R
³
1 −e−Rt/L´
.
147


## Page 3

As we guessed on physical grounds, the current builds up, with a “growth timescale” L/R.
The timescale L/R plays a role in LR circuits similiar to that played by the timescale RC
in circuits with capacitors.
Suppose we let this circuit sit in this state for a very long time, so that the current
saturates at its equilibrium value, I = V/R. What happens if we now simultaneously open
S1 and close S2? Physically, our expectation is that Lenz’s law will try to hold the current
ﬂow constant — the inductor says “I don’t want the ﬂux through me to change!” However,
we know that the resistor dissipates energy, so the current must bleed away — we should
see some kind of exponential decay.
Time to calculate. Going around the circuit, we have
−LdI
dt −IR = 0 .
The ﬁrst term is the EMF due to the inductor, −LdI/dt. Why the minus sign? By Lenz’s
law, the inductor always ﬁghts change. If the current “wants” to be reduced, the sign of
the inductor’s EMF needs to ﬁght that. The second term is the usual voltage drop across a
resistor. Rearranging leads to the easily integrated equation
dI
I = −R dt
L
,
which in turn leads to the exponential solution
I(t) = I(t = 0)e−Rt/L .
(Note that we have redeﬁned the meaning of t = 0 — this is now the time at which we open
S1 and close S2.)
When thinking about any circuit with inductance, the key thing you should keep in mind
is that inductors cause currents to have a kind of “inertia”. If there is no current ﬂowing, the
inductor will force the current to build up gradually; if there is current ﬂowing, the inductor
will force it to change gradually. If current is already ﬂowing and there is a sudden break in
the circuit, the inductor will do whatever it takes to keep the current ﬂowing. A consequence
of this is that when we open switches or break circuits very suddenly, we may see a large
spark! That spark is because of Lenz’s law — inductors in the circuit refuse to let the ﬂux
through them change. If that means that they must force the current to ﬂow through the
air, creating a huge, ﬁery spark — so be it.
16.1.3
Unit check
Before moving on, let’s do the traditional sanity check on our units: the ratio L/R should
have the dimension of time for any of the above results to make sense. In cgs, the units of
L are sec2/cm; the units of R are sec/cm. So L/R is indeed a time measured in seconds.
In SI, the unit of L is the Henry, which is Volt-sec/Amp; the unit of R is the Ohm, which
is Volt/Amp. So L/R is again a time measured in seconds. Three cheers for dimensional
analysis.
16.2
LC circuits
Exponential decay (or saturation) is dull. We’re now going to look at a circuit conﬁgura-
tion that does something new. Consider what happens when we connect an inductor to a
capacitor:
148


## Page 4

L
C
Suppose that the capacitor is charged up to a charge separation Q0. We close the switch at
t = 0. How does the circuit behave after this?
As usual, our governing analysis of the system comes from Kirchhoﬀ/Faraday: going
around the circuit, we have
Q
C −LdI
dt = 0
where Q is the charge on the capacitor, and I is the current ﬂowing through the inductor.
To get anywhere with this, we of course need to relate the current ﬂowing to the charge on
the capacitor. Since the current comes from charge ﬂowing oﬀthe capacitor, we have
I = −dQ
dt .
We thus ﬁnally end up with the diﬀerential equation
d2Q
dt2 + 1
LC Q = 0 .
Diﬀerential equations of this form are best solved via an age old technique: guessing. In
particular, guided by our experience with other systems that have a similar form, we guess
that the solution has the form
Q(t) = A cos ω0t + B sin ω0t .
We plug this solution back into our diﬀerential equation; the key thing we need is
d2Q
dt2
=
−ω2
0A cos ω0t −ω2
0B sin ω0t
=
−ω2
0Q .
149


## Page 5

Our assumed solution works ﬁne provided we set the angular frequency
ω0 =
1
√
LC .
(You should be able to verify immediately that this has the correct units.) The constants A
and B are free to be adjusted to match our initial conditions — the value of the charge on
the capacitor Q at t = 0, and the current ﬂowing in the circuit at t = 0:
Q(0)
=
Q0
=
A cos(0) + B sin(0)
→A
=
Q0 .
I(0)
=
−
ÃdQ
dt
!
t=0
= 0
=
−ω0A sin(0) + ω0B cos(0)
→B
=
0 .
We now have the full solution to this problem: the charge on the capacitor, as a function of
time, is
Q(t) = Q0 cos ω0t .
Equivalently, the current ﬂowing in the circuit, I(t) = −dQ/dt, is
I(t)
=
ω0Q0 sin ω0t
=
Q0
√
LC sin ω0t .
This sinusoidal behavior is the generic feature of LC circuits. Notice that the charge has
maximum magnitude when the current is zero, and vice versa — the current and the charge
are “90◦out of phase” with each other.
A nice way to make sense of the current and charge behavior is by looking at the energetics
of the circuit elements. The energy stored in the capacitor, as a function of time, is
UC(t)
=
Q(t)2
2C
=
Q2
0
2C cos2 ω0t .
The energy stored in the inductor, as a function of time, is
UL(t)
=
1
2LI(t)2
=
1
2
1
LC LQ2
0 sin2 ω0t
=
Q2
0
2C sin2 ω0t .
150


## Page 6

The energy in the inductor and the energy in the capacitor each oscillate. Note that their
sum is constant, and is exactly equal to the total energy that was initially stored in the
capacitor:
Utot
=
UC(t) + UL(t) = Q2
0
2C
³
cos2 ω0t + sin2 ω0t
´
=
Q2
0
2C .
Conservation of energy works! In this case, there’s an even cooler interpretation. The energy
in the capacitor is stored as electric ﬁelds; that in the inductor is stored as magnetic ﬁelds.
What we are seeing here is that the system’s total energy is just sloshing back and forth,
from electric to magnetic to electric to ... This circuit is just an electromagnetic swing set!
16.3
RLC circuits
The circuit we just discussed is an interesting one ... but it’s also somewhat ﬁctional, since
we are idealizing it as having no resistance. Since all circuits have some resistance1, the RLC
circuit sketched here is far more relevant to real world applications than the LC circuit:
C
L
R
How would we expect this circuit to behave? Our intuition on the energetics of LC circuits
is helpful here: qualitatively, we should expect the same “sloshing” of energy between the
inductor and capacitor. However, we now expect that some energy will be dissipated through
each cycle because of the circuit’s resistance. Our solution for the charge and the current in
the circuit should look like a decaying oscillation of some kind.
To make progress, we need to do some calculating. We again assume that the capacitor
initially has some charge Q0 on it, and that we close the switch at t = 0. Faraday/Kirchhoﬀ
then tells us how to set up the equations for this circuit:
Q
C −IR −LdI
dt = 0
1Unless they are superconducting, but that opens a whole new barrel of worms ...
151


## Page 7

which reduces to
d2Q
dt2 + R
L
dQ
dt + 1
LC Q = 0 .
The usual way to solve these equations is the tried and true friend of the physicist,
inspired guessing: we assume that the solution takes the form
Q(t) = e−t/τ (A cos ωt + B sin ωt)
— very similar to the form we found for the LC circuit.
The major new feature is the
exponentially decaying prefactor. We could then plug this assumed form of Q(t) into the
diﬀerential equation and then grind out a lot2 of algebra. After the smoke clears, the algebra
will tell you that, for this solution to work, τ and ω must take on certain values.
The
constants A and B will be left as adjustable parameters to be used for matching initial
conditions.
Feel free to pursue this route on your own!
We will instead use this moment as an
opportunity to introduce a diﬀerent way of thinking about this problem: we will use complex
exponentials. For the remainder of this lecture, I will assume that you are familiar with the
supplementary notes on complex numbers I put together (available under “Handouts” on
the 8.022 webpage).
The key idea is to take the solution Q(t) to be the real part of a complex function ˜Q(t):
Q(t) = Re
h ˜Q(t)
i
.
Then, as long as the resistance, capacitance, and inductance are themselves real numbers,
the complex charge ˜Q is also a solution to the diﬀerential equation:
d2 ˜Q
dt2 + R
L
d ˜Q
dt + 1
LC
˜Q = 0 .
Our assumption is that
˜Q = Aeiφ0eiαt .
As we will see shortly, A and φ0 (the “amplitude” and the “phase”) are the constants that
we adjust to match initial conditions. We will now work out what α is. Bear in mind that
α may itself be a complex number!!!
To proceed, we need to know the derivatives of ˜Q. This is where the magic of using com-
plex exponentials for solving diﬀerential equations comes in: This technique turns diﬀerential
equations into algebraic ones. In particular, we have
d ˜Q
dt
=
iα ˜Q
d2 ˜Q
dt2
=
−α2 ˜Q .
Plugging this back into the governing diﬀerential equation, we get
˜Q
µ
−α2 + iαR
L + 1
LC
¶
= 0
2A LOT.
152


## Page 8

which means that α must satisfy
α2 −iαR
L −1
LC = 0 .
This is just a quadratic equation, whose solution is
α = i R
2L ±
s
1
LC −R2
4L2 .
We thus have two solutions for ˜Q:
˜Q+
=
Aeiφ0e−Rt/(2L)e+it√
1/(LC)−R2/(4L2)
˜Q−
=
Aeiφ0e−Rt/(2L)e−it√
1/(LC)−R2/(4L2) .
The distinction between these two solutions is physically meaningless since they have the
same real part! We might as well just keep one (the + solution, say) and be done with it.
Taking the real part, our ﬁnal solution becomes
Q(t) = Ae−Rt/(2L) cos (ωt + φ0)
where
ω =
s
1
LC −R2
4L2 .
Although the use of complex numbers may seem kind of counterintuitive here, it makes
solving this problem almost trivial. Rather than needing to ﬁght through trig functions and
their derivatives, you just need to solve one quadratic equation.
Complex numbers make for simple analysis.
16.3.1
The “weak damping” limit
An important limit of the above circuit is that of weak damping.
This holds when the
resistance is “small”, in a well-deﬁned way.
To see what constitutes weak damping, we
compute the current from our charge solution:
I(t)
=
−dQ
dt
=
Ae−Rt/(2L)
·
ω sin (ωt + φ0) + R
2L cos (ωt + φ0)
¸
.
The current consists of the sum of two diﬀerent sinusoidal functions. The amplitude of this
ﬁrst term is proportional to the frequency ω; the amplitude of the second is proportional to
the damping rate R/(2L).
Weak damping means that the frequency is much larger than the damping rate:
ω ≫R
2L .
If this is the case, then the second term in the current may be ignored, to high accuracy,
relative to the ﬁrst term:
I(t) ≃Ae−Rt/(2L)ω sin (ωt + φ0) .
153


## Page 9

We can actually make one further useful simpliﬁcation in this limit: if ω ≫R/2L, then you
should be able to convince yourself quite easily that
ω
≡
s
1
LC −R2
4L2
≃
s
1
LC
=
ω0 .
In other words, when we have weak damping, the oscillation frequency is — to high accuracy
— the same frequency as we would have found if the resistor were not present!
In the weak damping limit, it is now simple to match the constants A and φ0 to our
initial conditions:
Q(t = 0)
=
Q0
=
A cos(φ0)
I(t = 0)
=
0
=
Aω0 sin(φ0) .
The solution to these equations is
A = Q0
φ0 = 0 .
Thus, our “full” solution, in the weak damping limit, for this circuit is
Q(t)
=
Q0e−Rt/(2L) cos ω0t
I(t)
=
ω0Q0e−Rt/(2L) sin ω0t
ω0
=
s
1
LC .
A similar calculation can be done without assuming weak damping, but the details are much
messier.
16.3.2
The quality factor
In the weak damping limit, the energy content of the circuit behaves in a very nice way. The
energy of the capacitor is given by
UC(t)
=
Q(t)2
2C
=
Q2
0
2C e−Rt/L cos2 ω0t .
The energy of the inductor is given by
UL(t)
=
1
2LI(t)2
=
1
2ω2
0LQ2
0e−Rt/L sin2 ω0t
=
Q2
0
2C e−Rt/L sin2 ω0t .
154


## Page 10

(In going from the second to the third line, I’ve used ω2
0 = 1/LC.) The sum of these energies
is
Utot(t)
=
UC(t) + UL(t)
=
Q2
0
2C e−Rt/L ³
cos2 ω0t + sin2 ω0t
´
=
Q2
0
2C e−Rt/L .
Since Q2
0/2C is the initial energy stored in the system, this means that the total energy
content just exponentially damps away. (If we are not in the weak damping limit, a similar
result holds, though the details are not quite as nice.)
Scientists and engineers like to be able to quantify how “good” an RLC circuit is, and so
we invented a quantity called the circuit’s quality Q (not to be confused with its charge). A
circuit with high quality is one that oscillates many times before it loses a signiﬁcant amount
of energy. To make this somewhat vague notion precise, the following deﬁnition is typically
adopted: “The quality factor Q is the number of radians through which a damped system
oscillates by the time that its energy content has fallen by a factor of 1/e.”
This may sound a little odd, but it deconstructs into a very simple mathematical state-
ment. First, how much time does it take for the energy to fall by a factor of 1/e? By the
above discussion, this is easy:
T(energy to fall by 1/e) = L/R .
Plug this time into the energy stuﬀdiscussed above, and you see that the energy is at 1/e
of its initial level.
How many radians does the system oscillate through in this time? We just multiply the
time T by the system’s angular frequency ω ≃ω0! The quality factor of an RLC circuit is
Q
=
ωL
R
≃
ω0L
R
.
As we will see when we begin exploring AC circuits, there is another way to understand
the quality factor of circuits, related to how a circuit behaves “on resonance” (and very close
to resonance). We will deﬁne the quality factor in what seems to be a completely diﬀerent
way, and will end up with exactly the same result! This is not an accident of course, but is
deeply connected to how energy is stored and dissipated in circuits.
The concepts we hit in this lecture — exponential decay of an oscillation; quality factor
— and that we’ll hit in the next few lectures (e.g., resonance) pop up in an enormous
number of contexts. For example, the quality factor of a distorted black hole — the number
of radians worth of gravitational waves produced by the oscillations of its distorted event
horizon emitted as it settles down to an equilibrium state — is given approximately by
QBH ≃2
µ
1 −c
G
S
M 2
¶−9/20
(where G is the gravitational constant, c is the speed of light, S is the magnitude of the
black hole’s spin angular momentum, and M is its mass). There are many other examples
of quality factors that pop up repeatedly in science and engineering; you will see many of
these notions again!
155
