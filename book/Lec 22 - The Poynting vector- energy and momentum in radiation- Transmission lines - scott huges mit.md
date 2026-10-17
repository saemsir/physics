# Lec 22 - The Poynting vector- energy and momentum in radiation- Transmission lines - scott huges mit

> Source: `Lec 22 - The Poynting vector- energy and momentum in radiation- Transmission lines - scott huges mit.pdf`  
> Pages: 9


## Page 1

Scott Hughes
6 May 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 22:
The Poynting vector: energy and momentum in radiation.
Transmission lines.
22.1
Electromagnetic energy
It is intuitively obvious that electromagnetic radiation carries energy — otherwise, the sun
would do a pretty lousy job keeping the earth warm. In this lecture, we will work out how
to describe the ﬂow of energy carried by electromagnetic waves.
To begin, consider some volume V . Let its surface be the area A. This volume contains
some mixture of electric and magnetic ﬁelds:
Volume V
Electric field E
Magnetic field B
Surface A
The electromagnetic energy density in this volume is given by
energy
volume = u = 1
8π
⃗
E ·⃗E +⃗B ·⃗B

.
We are interested in understanding how the total energy,
U =
Z
V u dV = 1
8π
Z
V dV
⃗
E ·⃗E +⃗B ·⃗B

changes as a function of time. So, we take its derivative:
∂U
∂t = ∂
∂t
1
8π
Z
V dV
⃗
E ·⃗E +⃗B ·⃗B

.
205


## Page 2

Since we have ﬁxed the integration region, we can take the ∂/∂t ender the integral:
∂U
∂t
=
1
8π
Z
V dV ∂
∂t
⃗
E ·⃗E +⃗B ·⃗B

=
1
4π
Z
V dV

⃗E · ∂⃗E
∂t +⃗B · ∂⃗B
∂t

.
Rearranging the source free Maxwell equations,
∂⃗E
∂t = c⃗∇×⃗B
∂⃗B
∂t = −c⃗∇×⃗E
we can get rid of the⃗E and⃗B time derivatives:
∂U
∂t = c
4π
Z
V dV
h⃗
E ·
⃗
∇×⃗B

−⃗B ·
⃗
∇×⃗E
i
.
22.2
The Poynting vector
The expression for ∂U/∂t given above is as far as we can go without invoking a vector
identity. With a little eﬀort, you should be able to prove that⃗
∇·
⃗
E ×⃗B

= −⃗E ·
⃗
∇×⃗B

+⃗B ·
⃗
∇×⃗E

.
Comparing with our expression for ∂U/∂t, we see that this expression simpliﬁes things:
∂U
∂t
=
−c
4π
Z
V dV⃗∇·
⃗
E ×⃗B

≡
−
Z
V dV⃗∇·⃗S .
On the second line we have deﬁned⃗
S = c
4π⃗E ×⃗B ;
we’ll discuss this vector in greater detail very soon.
Since we have a volume integral of a divergence, the obvious thing to do here is to apply
Gauss’s theorem. This changes the integral over V into an integral over the surface A:
∂U
∂t
=
−
Z
A d⃗a ·⃗S .
In other words, The rate of change of the electromagnetic energy in the volume
V is given by the ﬂux of⃗S through V ’s surface. Notice the minus sign; this is easily
explained. Recall that d⃗a points outward. If⃗S and d⃗a are parallel, energy is leaving the
system, so U decreases. And vice versa.⃗
S is called the Poynting1 vector. It points2 in the same direction as the electromagnetic
energy ﬂow. (This gives a somewhat more physical picture of the fact that⃗E ×⃗B tells us the
1It’s actually named after a person, John Henry Poynting. You’ve got to wonder if he was fated to work
this quantity out.
2This is usually when a lesser lecturer would make a terrible pun about the direction in which the ﬂow
of energy “Poynts”. I’ll spare you.
206


## Page 3

propagation direction for electromagnetic radiation.) As noted above, the ﬂux of⃗S through
some surface A gives the total power ﬂowing through A:
Power through A =
Z
A⃗S · d⃗a .
22.2.1
Dimensional analysis
The units of the Poynting vector are
Poynting
≡
velocity × electric ﬁeld × magnetic ﬁeld
≡
velocity × electric ﬁeld2
Electric ﬁeld squared gives us energy per unit volume, so
Poynting
≡
length
time × energy
length3
=
power
area .
This is just what we should have if the ﬂux of⃗S is to be the power through an area. In cgs
units,⃗S has the units of erg/(s-cm2).
It’s worth noting at this point that the magnitude of⃗S is a quantity known as the
intensity, I. A very intense source of radiation is something that emits lots of power into a
very small area.
22.3
Examples
22.3.1
Plane wave
Let’s look at a linearly polarized plane wave,⃗E = E0ˆx sin(kz −ωt),⃗B = E0ˆy sin(kz −ωt).
The Poynting vector associated with this wave is⃗
S = c
4π⃗E ×⃗B = c
4πE2
0 sin2(kz −ωt)ˆk .
It’s useful to compare this to the energy density in the wave:
u
=
1
8π
⃗
E ·⃗E +⃗B ·⃗B

=
1
4πE2
0 sin2(kz −ωt)
Comparing, we see that⃗
S = u⃗c
where⃗c = cˆk is the vectorial velocity of the radiation. This is very nicely in keeping with the
idea that⃗S tells us about the ﬂow of energy! (Note the similarity to the relation between
current density and the velocity of moving charges,⃗J = ρ⃗v.⃗S is a ﬂow of energy density in
the same way that⃗J is a ﬂow of charge density.)
For many kinds of radiation that we will wish to study, k and ω are so large that
sin2(kz −ωt) oscillates extremely quickly. (For example, the frequency of visible light —
207


## Page 4

mean wavelength roughly 500 nanometers — is about 6 × 1014 Hz.) It makes a lot more
sense to take the average of this quantity, which amounts to replacing the sin2 with 1/2:
⟨⃗S⟩= cˆk
8πE2
0 .
The intensity (magnitude of⃗S) is most typically discussed in terms of the averaged Poynting
vector:
I = |⟨⃗S⟩| = c
8πE2
0 .
22.3.2
Spherical wavefronts
If we solve the wave equation in spherical coordinates, one important solution is given by⃗
E
=
ω2p
c2 sin θsin(kr −ωt)
r
ˆθ⃗
B
=
ω2p
c2 sin θsin(kr −ωt)
r
ˆφ .
(This solution is actually only good for distances r ≫λ, where λ = 2π/k is the usual
wavelength. This is a subtlety far beyond the scope of 8.022! For now, just trust me.)
This radiation solution is what we ﬁnd for an oscillating dipole arranged so that the
dipole vector,⃗p, lies parallel to the z axis (p is the magnitude of⃗p).
Notice that the
radiation propagates out radially: although there is some angular dependence, the radiation
ﬂows out through spheres.
The Poynting vector we construct for this wave is⃗
S
=
c
4π⃗E ×⃗B
=
1
4πc3ω4p2 sin2 θsin2(kr −ωt)
r2
ˆr .
Averaging over time, we have
⟨⃗S⟩= ω4p2
8πc3r2 sin2 θˆr .
The Poynting vector (and hence the intensity) fall of with a 1/r2 law. This is extremely
important! Suppose we draw a sphere of radius R around this system, centered on the origin
(where the oscillating dipole is located). Let’s now compute the total rate of energy ﬂowing
through this sphere:
*∂U
∂t
+
=
Z
R d⃗a · ⟨⃗S⟩.
The area element on this sphere is d⃗a = R2 sin θ dθ dφ ˆr; the integral becomes
*∂U
∂t
+
=
Z 2π
0
dφ
Z π
0 dθ

R2 sin θˆr

·
 ω4p2
8πc3R2 sin2 θˆr
!
=
ω4p2
8πc3
Z 2π
0
dφ
Z π
0 sin3 θ dθ
=
ω4p2
4c3
Z π
0 sin3 θ dθ
=
ω4p2
3c3 .
208


## Page 5

This ﬁnal result is a special case of what is known as the Larmor formula. Notice that this
result is completely independent of the radius R! What happened is that the Poynting vector
or intensity drops oﬀlike 1/r2. However, the total area of a spherical surface grows with r2,
so the total rate of energy ﬂow is constant.
This, in essence, is telling us that electromagnetic waves conserve energy.
They are
spreading out over large areas, but the total energy they carry remains constant.
22.3.3
Capacitor
The Poynting vector applies in any situation in which both an electric and a magnetic ﬁeld
appear, not just with radiation. In this example, we will apply it to the charging up of
a capacitor. Consider a capacitor that currently has a charge separation of Q, and has a
current I ﬂowing onto it:
a
+Q
−Q
I
The electric ﬁeld between the plates is
E = 4πQ/A = 4Q/a2 ;
it points down. From the generalized Ampere’s law, we have
I⃗
B · d⃗s = 1
c
dΦE
dt
We take the contour integral around a ring of radius r; the ﬂux is computed through this
ring:
2πrB(r)
=
πr2
c
dE
dt
=
πr2
c
4
a2
dQ
dt
=
4πIr2
ca2
.
So the magnetic ﬁeld at radius r from the center of the capacitor is
B(r) = 2Ir
ca2 .
The direction is of course circulational, deﬁned by right hand rule with your thumb pointing
down. This means that at the front of the capacitor⃗B points to the left; at the back, it
points to the right; etc.
209


## Page 6

The cool thing is to now evaluate the Poynting vector: since⃗E and⃗B are orthogonal,
we clearly have
S(r) = c
4πEB = 2QI
πa4 .
What is the direction? At the front, we have (down)×(left). This points into the capacitor.
At the back, we have (down)×(right). This again points into the capacitor. In fact, we can
quickly show that at all points,⃗S points into the capacitor.
This makes perfect sense! It should point inwards since, as we well know, the amount of
energy in the capacitor increases as the plates charge up. The Poynting vector provides us
with a way of visualizing this.
You will explore this facet of the Poynting vector further on Pset 11.
22.4
Momentum carried by radiation
Since electromagnetic radiation carries energy, it won’t surprise you to learn that it carries
momentum as well. A simple way to see this is to make use of the relativistic mass-energy-
momentum formula you worked out in Pset 6:
E2 = |⃗p|2c2 + m2c4 .
If we plug in m = 0, we ﬁnd
E = |⃗p|c ;
|⃗p| = E/c .
Let’s think about using the relationship with what we’ve worked out so far. The Poynting
vector tells us about the rate at energy is delivered to a unit area, just as we learned in the
dimensional analysis discussion above. If we divide by c, then what we must have is the rate
at which momentum is delivered to a unit area:⃗
S
c =⃗E ×⃗B
4π
Dimensionally,⃗
S
c = momentum
time × area = force
area = pressure .
Radiation exerts pressure! Intensity divided by the speed of light tells us how much pressure
is exerted by some source of light.
22.5
Transmission lines
Suppose we want to send a signal from one device to another — our goal is to get electro-
magnetic energy from point A to point B. What’s the best way to do this? If we just use
wires, we’re going to have problems — the wires will act like antennas and we’ll lose a lot
of energy to radiation. Instead, we would like to set up some kind of structure that shields
the signal, so that no ﬁeld leaks outside. This setup is called a transmission line.
The simplest example of a transmission line is a coaxial cable: a pair of conducting tubes
nested in one another. Equal and opposite currents ﬂow on the inner and the outer tubes,
210


## Page 7

Inner radius:
Outer radius:
a
b
so that the net current “seen” outside the cylinder is zero. Note that this is not a simple DC
current — it is a highly oscillatory AC current. This means that there must be some charge
distribution as well. Equal and opposite charges “live” on the inner and outer tubes of the
coax.
Suppose that the inductance per unit length of this cable is L′, and that its capacitance
per unit length is C′. Consider a short length ∆x of this cable. This little segment has a
total inductance of L′∆x. If the current ﬂowing down the cable is I and has the rate of
change ∂I/∂t, then the voltage drop due to inductance over this short length is
∆V = V (x + ∆x) −V (x) = −(L′∆x)∂I
∂t .
Divide both sides by ∆x and take the limit:
∂V
∂x = −L′∂I
∂t .
Consider now the charge on this little segment: since it is at potential V (x), and its
capacitance is C′∆x, the amount of charge on this segment is
∆Q = (C′∆x)V (x) .
Divide and take the limit:
∂Q
∂x = C′V (x) .
Let’s take another derivative of this:
∂2Q
∂x2
=
C′∂V
∂x
=
−C′L′∂I
∂t
=
C′L′∂2Q
∂t2 .
211


## Page 8

In going from the ﬁrst to the second line, we used our previous result relating ∂V/∂x and
∂I/∂t; in going from the second to the third line, we used I = −∂Q/∂t (discharging capacitor
current).
Rearranging this, we see yet another wave equation!
∂2Q
∂t2 −
1
C′L′
∂2Q
∂x2 = 0 .
With a little bit of tweaking, you should be able to convince yourself that this equation holds
replacing Q with V and I as well. The speed of propagation of this wave is
v =
1
√
L′C′ .
Now, for the coaxial cable introduced above, you should be able to show very easily that
C′
=
1
2 ln(b/a)
L′
=
2 ln(b/a)
c2
.
(If you can’t work it out, go back to old psets! You worked out the capacitance in Pset 4
and the inductance in Pset 8; you just to divide out the length l to put things on a “per unit
length” basis.) This means that
v =
1
√
L′C′ = c .
The wave propagates down the transmission line at the speed of light! Not surprising, at
least in retrospect.
One other very important quantity determines the characteristic of a transmission line: its
impedance. Following our intuition from our study of AC circuits, we deﬁne the impedance
as the ratio of the voltage to the current:
Z = V
I =
V
∆Q/∆t .
As we already discussed, for a small segment of the cable ∆Q = (C′∆x)V , so
∆Q
∆t = C′V ∆x
∆t =
C′V
√
L′C′ = V
s
C′
L′
where we have used the fact that ∆x/∆t is just the speed of propagation down the line.
Putting everything together, we ﬁnd
Z =
s
L′
C′ .
For the coaxial cable, this yields
Z = 2 ln(b/a)
c
.
212


## Page 9

Using the conversion factor 1 Ohm = 1.1 × 10−12 sec/cm, this means
Z = 60 Ohms ln(b/a) .
Many coaxial cables are actually ﬁlled with a dielectric material (which we have not dis-
cussed in detail); this has the eﬀect of increasing the capacitance, which reduces the line’s
characteristic impedance. 50 Ohms is a value that is commonly encountered (e.g., in cable
TV systems).
One of the most important consequences of the impedance of a transmission line is in
determining how it must be terminated. Roughly speaking, a terminated cable has the form
The resistor might actually be some electronic device, like a television or a computer; then
again, it might just be a resistor. The point is that the signal which is ﬂowing down the
cable is then fed into this device or resistor.
If the resistance of this “load” precisely matches the impedance of the cable, then we
have matched the impedances. Because V/I does not change in going from the cable to the
resistor, it is as though the cable were of inﬁnite length! There is no way for the signal to
“know” whether it is in the resistor or in the cable.
Suppose the resistance were ∞Ohms — an open circuit.
Then, the currents would
essentially bounce oﬀthe “resistor” and head back where they came from. The signal would
just reverse course — you’d get a horrible reﬂection back up the line. Suppose the resistance
were 0 Ohms — a short circuit. Then, the currents would just ﬂow from the inner tube
to the outer tube, and vice versa — the signal would reverse course and switch sign on its
amplitude!
In general, if the impedance of the cable doesn’t match the impedance of the load, you
get reﬂections of this sort. This is one reason why cheap cable TV equipment can give you
a horrible picture — there are these extra signals bouncing around, which eventually arrive
at the TV late, and possible with a 180◦phase shift. This causes ghost images to appear,
and generally confuses your equipment.
213
