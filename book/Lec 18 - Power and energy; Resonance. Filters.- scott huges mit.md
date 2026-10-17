# Lec 18 - Power and energy; Resonance. Filters.- scott huges mit

> Source: `Lec 18 - Power and energy; Resonance. Filters.- scott huges mit.pdf`  
> Pages: 9


## Page 1

Scott Hughes
21 April 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 18:
AC Circuits.
Power and energy; Resonance. Filters.
18.1
AC circuits: Recap and summary
Last time, we looked at AC circuits and found that they are quite simple to analyze provided
we follows some simple rules:
1. Work with complex valued voltages and currents. Our driving AC EMF is usually some-
thing like E(t) = E0 cos ωt; replace this with ˜E(t) = E0eiωt (so that E(t) = Re[ ˜E0(t)]).
2. The voltage drop across any circuit element obeys a generalized, complex version of
Ohm’s law:
˜VX = ˜IXZX
where ZX is the impedance of circuit element X. Impedance works just like resistance,
but is complex and frequency dependent:
ZR
=
R
ZC
=
1/(iωC)
ZL
=
iωL .
3. Analyze the circuit as though it were a simple DC circuit containing only resistors as
circuit elements. You may ﬁnd phasor diagrams helpful for making sure that you get
the magnitudes and phases correct.
4. Take the real part at the end of the day.
168


## Page 2

18.2
Power delivered to an AC circuit
Let’s look again at our prototypical driven RLC circuit:
C
L
R
Assume that the EMF supplied is E(t) = E0 cos ωt. In the complex representation, this
becomes ˜E(t) = E0eiωt.
We can now solve for the complex current in this circuit:
˜E
=
˜VR + ˜VL + ˜VC
=
˜I
·
R + iωL +
1
iωC
¸
−→˜I
=
˜E
R + i[ωL −1/(ωC)] .
We now substitute ˜E(t) = E0eiωt, ˜I(t) = I0e−iφeiωt. Then, we ﬁnd
I0
=
E0
q
R2 + [ωL −1/(ωC)]2
≡
E0/|Ztot(ω)|
where |Ztot(ω)| is the magnitude of the total impedance. The phase is deﬁned by
tan φ
=
−Im[˜I]
Re[˜I]
=
ωL
R −
1
ωCR .
The real current ﬂowing in this circuit is thus given by
I(t) = I0 cos(ωt −φ)
169


## Page 3

where
I0
=
E0
|Ztot(ω)|
tan φ
=
ωL
R −
1
ωCR .
How much power is delivered to this circuit? From the deﬁnition of EMF as work per
unit charge, and from the deﬁnition of current as charge per unit time, we know that the
power delivered to this circuit must be
P(t) = I(t)E(t) .
Let’s plug in the results we have for I(t) and E(t):
P(t)
=
E2
0
|Ztot(ω)| cos ωt cos(ωt −φ)
=
E2
0
|Ztot(ω)| [cos ωt cos ωt cos φ + cos ωt sin ωt sin φ] .
On the second line, I have used a trig identity, cos(a −b) = cos a cos b + sin a sin b, to expand
the second cosine.
This result for P(t) is exact.
It tells us that the power delivered to the circuit is a
quantity that oscillates. In many circumstances, the frequency of this oscillation is far too
rapid for us to be able to track the detailed oscillations. For example, electricity out of the
wall oscillates 60 times per second — way faster than anything we can keep track of without
special equipment.
In this circumstance, when the oscillations are much faster than the phenomena that
we are interested in, it makes a lot more sense to average. The “average” of any oscillating
function is given by integrating that function over its period, and then dividing by the period.
For example, the average power delivered to the circuit is given by
⟨P⟩
=
1
T
Z T
0 P(t) dt
=
ω
2π
Z 2π/ω
0
P(t) dt .
(On the last line, I’m using the fact that the period of a function whose angular frequency
is ω is 2π/ω.)
The average power that the EMF delivers to the circuit is thus given by
⟨P⟩=
E2
0
|Ztot(ω)|
ω
2π
"Z 2π/ω
0
(cos ωt cos ωt cos φ) dt +
Z 2π/ω
0
(cos ωt sin ωt sin φ) dt
#
.
The integrals we need are
ω
2π
Z 2π/ω
0
(cos ωt cos ωt cos φ) dt
=
1
2 cos φ
ω
2π
Z 2π/ω
0
(cos ωt sin ωt cos φ) dt
=
0 .
170


## Page 4

The average power delivered to the circuit is thus
⟨P(ω)⟩= 1
2
E2
0 cos φ
|Ztot(ω)| .
(I’ve written the power as a function of ω to emphasize its dependence on the driving
frequency.) This average power is the one that is used to describe most common household
items. For example, when we talk about a 100 Watt lightbulb, we mean that the average
power delivered to the bulb is 100 Watts.
This power is often written in terms of the “root mean squared”, or RMS, voltage. The
RMS is often used when we talk about oscillating quantities whose average values are zero:
we average the square of the quantity. For example, the RMS EMF is given by
E2
rms
=
ω
2π
Z 2π/ω
0
E(t)2 dt
=
E2
0
2
−→Erms
=
E0
√
2 .
For purely sinusoidal AC EMF and current, the RMS value is just the amplitude divided by
√
2. Typically, when AC voltages are discussed, it is the RMS value that is indicated. For
example, the wall voltage throughout North America is typically 120 Volts. This is the RMS
value of the voltage from the wall; the amplitude of the voltage is
√
2 × 120 = 170 Volts.
Note that, since I0 = E0/|Ztot|, we also have Irms = Erms/|Ztot|.
The average power delivered by the AC EMF can thus be written
⟨P(ω)⟩= E2
rms cos φ
|Ztot(ω)| .
This is the form in which we most commonly see the AC power related to AC voltage (or
currents).
With a little bit of eﬀort, we can show that
cos φ =
R
q
R2 + [ωL −1/(ωC)]2 =
R
|Ztot(ω)| .
Using this, the average power can be rewritten as follows:
⟨P(ω)⟩
=
E2
rmsR
|Ztot(ω)|2
=
Irms(ω)2 R .
The average power delivered has a really simple form when expressed in terms of the RMS
current — it looks just like the DC power dissipation formula! (Be a little careful, though:
don’t forget that the current in this case, Irms, is a function of ω.)
171


## Page 5

18.3
Resonance
The average power that is delivered to the circuit is a function of frequency. Using the
formula
⟨P(ω)⟩
=
E2
rmsR
|Ztot(ω)|2
we see that the frequency dependence enters through 1/|Ztot|2. This has the following ap-
pearance as a function of ω:
10
20
30
40
50
0.05
0.1
0.15
0.2
(The parameters R = 5 Ohms, L = 1 Henry, C = 2 × 10−3 Farads were used for this plot.)
Clearly, there is some frequency at which the amount of power delivered is a maximum —
at this frequency, the circuit is in resonance with the driving EMF. Our goal now will be to
calculate this frequency: we look for maxima of
1
|Ztot(ω)|2 =
1
R2 + [ωL −1/(ωC)]2 .
We could do the usual procedure of looking for frequencies at which the derivative of this
with respect to ω goes to zero; however, the answer is actually obvious by inspection! The
maximum occurs when the ωL and 1/ωC terms cancel each other out. This happens when
ω = ωres =
1
√
LC .
Notice that the resonant frequency is ω0, the oscillation frequency of the pure LC circuit!
At this frequency, |Ztot| = R, and so
⟨P(ωres)⟩= ⟨Pmax⟩= E2
rms
R
.
Also at this frequency, we must have φ = 0 — the current in the circuit is exactly in phase
with the driving EMF. The voltage drops due to the capacitor and the inductor precisely
cancel each other out — it is as though only the resistor matters in the circuit.
When one talks about a resonant system, one would like to quantify how “good” the
resonance is. A “good” resonance is one in which the power versus ω curve is very narrow
— the power delivered has a very sharp peak. A convenenient way to quantify this is to look
172


## Page 6

for the two frequencies, ωhigh and ωlow, at which the power delivered has fallen to 1/2 of the
peak value:
⟨P(ωhigh)⟩= ⟨P(ωlow)⟩= 1
2⟨Pmax⟩.
This tells us that
1
2R
=
R
|Ztot(ωhigh/low)|2
=
R
R2 + [ωhigh/lowL −1/(ωhigh/lowC)]2 .
This in turn tells us that
ωhigh/lowL −
1
ωhigh/lowC = R .
This equation can be rearranged to form a quadratic equation; solving it yields the two
frequencies ωhigh and ωlow.
The “width” of the peak ∆ω is then deﬁned as ∆ω = ωhigh −ωlow. The ratio of this
width to the resonant frequency is then deﬁned as the quality factor of the driven system:
Q ≡ωres
∆ω .
On an upcoming problem set, you will show that limit,
∆ω = R
L .
Combining this with the fact that ωres = ω0 (the oscillation frequency of the LC circuit) and
we have
Q = ω0L
R
.
This is exactly the same quality factor that we determined for the un-driven RLC circuit!
This is not an accident. In the undriven system, the quality factor tells us about how quickly
the system loses energy. In the driven system, it tells us about the power delivered to the
system on resonance compared to slightly oﬀresonance. Although it is beyond the scope of
this course to prove this, these two concepts are intimately related to one another.
173


## Page 7

18.4
Filters
The frequency dependent response of an RLC circuit means that they can act as ﬁlters —
diﬀerent frequencies are preferentially “let through” diﬀerent parts of the circuit. To see this
principle in action, consider the following simple LR circuit with an AC driving EMF:
L
R
Working in the complex representation, we know that
˜E = ˜VR + ˜VL .
We also know there is a single current passing through both the resistor and the inductor:
˜E = ˜I (R + iωL)
˜I =
˜E
R + iωL .
What then is the magnitude of the voltage drop across the resistor? Multiplying by R
and taking the magnitudes, we ﬁnd
VR = |˜IR| = E
R
√
R2 + ω2L2 .
In this circuit, the resistor acts like a low pass ﬁlter: the voltage at low frequencies is
essentially the same magnitude as the “input” voltage. However, at high frequencies, the
voltage is very suppressed. Plotting VR versus ω, we ﬁnd something like this:
200
400
600
800
1000
0.2
0.4
0.6
0.8
1
174


## Page 8

How about the magnitude of the voltage drop across the inductor? In this case, we have
VL = |˜IZL| = E
ωL
√
R2 + ω2L2 .
The inductor acts like a high pass ﬁlter: high frequency parts of the signal get through, but
the stuﬀat low frequencies is highly suppressed: Plotting VL versus ω gives us
200
400
600
800
1000
0.4
0.5
0.6
0.7
0.8
0.9
How about if we have a circuit like this:
C
R
This again gives us ﬁltering behavior. The complex current in the circuit is given by
˜I
=
˜E
R + 1/(iωC)
=
iωC ˜E
1 + iωRC .
The voltage across the resistor is
VR = |˜IR| = E
ωCR
√
1 + ω2R2C2 .
This acts like a high pass ﬁlter: VR = 0 at ω = 0, but asymptotically approaches E as we go
to high frequency.
175


## Page 9

The voltage across the capacitor is
VC = |˜IZC| = E
1
√
1 + ω2R2C2 .
This acts as a low pass ﬁlter.
The rule that capacitors act as low pass devices and inductors as high pass devices follows
quite simply from the form of their impedance: A capacitor has a large impedance at low
frequency,
ZC = 1/(iωC)
and so shows a large voltage drop at low frequency.
Likewise, an inductor has a large
impedance at high frequency,
ZL = iωL
and hence shows a large voltage drop at high frequency.
176
