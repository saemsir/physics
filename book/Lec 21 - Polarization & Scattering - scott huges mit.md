# Lec 21 - Polarization & Scattering - scott huges mit

> Source: `Lec 21 - Polarization & Scattering - scott huges mit.pdf`  
> Pages: 10


## Page 1

Scott Hughes
3 May 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 21:
Polarization & Scattering
21.1
Summary: radiation so far
In the last few lectures, we examined solutions of the source free Maxwell equations:⃗
∇·⃗E = 0⃗
∇×⃗E = −1
c
∂⃗B
∂t⃗
∇·⃗B = 0⃗
∇×⃗B = 1
c
∂⃗E
∂t .
With a little massaging, we discovered that these equations can be rewritten as wave equa-
tions for⃗E and⃗B:
∂2⃗E
∂t2 −c2∇2⃗E = 0
∂2⃗B
∂t2 −c2∇2⃗B = 0 .
A particularly instructive solution to the wave equations are the plane wave forms:⃗
E(⃗r, t) =⃗E0 sin(⃗k ·⃗r −ωt)⃗
B(⃗r, t) =⃗B0 sin(⃗k ·⃗r −ωt) .
This solution represents an electromagnetic wave propagating in the ˆk =⃗k/k direction
(where k =
q⃗
k ·⃗k =
q
k2
x + k2
y + k2
z).
By considering how the wave behaves at some ﬁxed time, we learned that k is simply
related to the wavelength λ:
k = 2π/λ .
The requirement that this solution satisfy the wave equation tells us that
ω = ck .
From the deﬁnition ω = 2πν (angular frequency is 2π radians times “regular” frequency),
we then obtain
λν = c .
Finally, requiring that the plane wave solution satisfy all of Maxwell’s equations leads to
some important constraints on the vector amplitudes⃗E0 and⃗B0. These constraints are:
195


## Page 2

• The amplitudes are orthogonal to the propagation direction: ˆk ·⃗E0 = 0, ˆk ·⃗B0 = 0.
• The amplitudes are orthogonal to each otherL⃗E0 ·⃗B0 = 0.
• The amplitudes have the same magnitude: |⃗E0| = |⃗B0|.
• The propagation direction is parallel to⃗E ×⃗B.
These are important and rather constraining conditions. Nonetheless, they leave us with a
great deal of freedom in the amplitudes. This freedom is described in terms of the radiation’s
polarization state.
21.2
Linear polarization
Since plane waves propagate in a straight line, we might as well just deﬁne their propagation
direction as something simple and be done with it. In what follows, we will take ˆk = ˆz, so
our wave is of the form⃗
E =⃗E0 sin(kz −ωt)⃗
B =⃗B0 sin(kz −ωt) .
Suppose that the wave is arranged (somehow) so that the electric ﬁeld is aligned with the x
axis:⃗E0 = E0ˆx. Then, our requirement that⃗E ×⃗B be parallel to ˆk tells us that⃗B0 = E0ˆy.
(We’re also using |⃗E0| = |⃗B0|.)
This conﬁguration is known as a linearly polarized wave, as the electric (and magnetic)
ﬁelds at all points align parallel to a line. Such an electromagnetic wave is quite simple to
produce: we just need to take a conductor and arrange things so that it has an oscillating
charge distribution. Here’s an example:
+
+
+
−
−
−
+
+
+
−
−
−
t = 0
ω
t = 
t = 
π/2
ω
ω
π
196


## Page 3

The top part of this ﬁgure shows an antenna: a long conductor in which we drive a very
rapidly oscillating current, so that the conductor has a charge distribution. As we move to
the right, time increases.
At any given instant, one end is likely to have a net positive charge, the other end a net
negative charge; the whole thing is neutral overall. This setup creates an electric ﬁeld which
oscillates in phase with the current’s oscillation; this is sketched by the sinusoid below the
antenna.
The antenna we have described here is more properly a generating or broadcast antenna.
What if we want to measure the electromagnetic wave that this antenna is broadcasting?
Quite simple: we just need to setup a second antenna that will “catch” the oscillating
electromagnetic ﬁeld of the broadcaster.
If we put a second antenna down near it, the
oscillating electric ﬁeld will shake charges in this receiving antenna:
+
+
+
−
−
−
The oscillating charges themselves produce a current, which we can measure and (possibly)
extract information from. This is how a radio works!
197


## Page 4

When the generated electromagnetic wave is linearly polarized, it is (hopefully) intuitive
obvious that the receiving antenna should be oriented parallel to the polarization vector.
Suppose we get it wrong by 90◦:
+
+
+
−
−
−
For this orientation, the receiving antenna measures doodly squat: there’s not enough “room”
for a signiﬁcant charge oscillation to occur.
21.3
Polaroids
Certain substances act like antennas for radiation in the visual band — light that we can
see. They typically consist of organic molecules that are fairly extended in one direction.
These molecules can carry a current along that direction; but, no current can ﬂow in the
direction orthogonal to the molecule’s orientation.
A polaroid is a sheet of plastic embedded with molecules of this type all lined up along
some axis. Suppose linearly polarized light impinges on these molecules. Suppose further
that the light is polarized such that⃗E is aligned with its organic molecules. Then, the light
shakes charges in the polaroid; it generates a current, which generates heat in the plastic
sheet. The light is absorbed — nothing gets through.
Suppose instead that light is linearly polarized in a direction perpendicular to the sheet’s
organic molecules. This light will not be able to shake the charges in the sheet — they
are not free to move in that direction. Rather than being absorbed, the light passes right
through the sheet.
The direction that allows light through is, by convention, the “preferred” direction of the
polaroid. The punchline of this discussion is that
Polaroids are transparent to light with polarization parallel to their preferred
direction. They are opaque to light with polarization perpendicular to their
preferred direction.
198


## Page 5

21.3.1
Changing the polarization direction
What if the light is polarized in a direction somewhere between parallel and perpendicular
to the polaroid’s preferred orientation? For concreteness, suppose the light’s electric ﬁeld is
oriented along the x axis:⃗
Eincoming = E0ˆx cos(kz −ωt) .
Suppose the polaroid’s orientation ˆp is at some angle θ between the x and y axes:
ˆp = ˆx cos θ + ˆy sin θ .
Since the polaroid has a component of its orientation parallel to the light’s electric ﬁeld, the
light will partially be able to go through the polaroid. The amount of electric ﬁeld coming
out of the polaroid will be given by the overlap between the incoming electric ﬁeld and the
polaroid’s orientation:
|⃗Eoutgoing| =⃗Eincoming · ˆp = E0 cos θ cos(kz −ωt) .
This outgoing light must be parallel to the polaroid’s orientation — the polaroid deﬁnes the
new polarization direction. Thus, the full solution for the outgoing light’s⃗E ﬁeld is⃗
Eoutgoing =
³⃗
Eincoming · ˆp
´
ˆp .
A polaroid reduces the amplitude of linearly polarization light by cos θ, where θ
is the angle between the polaroid’s orientation and the light’s electric ﬁeld. It
rotates the orientation of that ﬁeld by θ.
21.3.2
Random light
In many situations, light is not linearly polarized — the light generated by a bulb, or coming
from the surface of the sun, or from a ﬁre, is best described as a superposition of many plane
waves, each with their own polarization1:⃗
Erandom =
huge
X
j=1
E0 (cos θjˆx + sin θjˆy) cos(kz −ωt) .
We can make this light linearly polarized by passing in through a polaroid. For concreteness,
imagine the polaroid is aligned along the x axis, so ˆp = ˆx. The light that comes out of the
polaroid is no longer randomly oriented:⃗
Eoutgoing = E0ˆx cos(kz −ωt)
huge
X
j=1
cos θj .
Polaroids can thus be used to produce linearly polarized light. As we’ll discuss in the next
lecture, one ends up reducing the intensity (brightness) when this is done; but, the light that
comes out has⃗E ﬁelds all lined up in the same way.
1The waves will also in general have an independent phase oﬀset, so that their behavior with respect to
time and space should be written as cos(kz −ωt + ϕj). This complication, though often important, does
not play a role in this discussion. An example where it does matter, quite a bit, is the laser. Lasers produce
light in which all of these “oﬀset phases” line up. This means that the light is coherent: the electric and
magnetic ﬁelds are spatially and temporally in phase with each other.
199


## Page 6

21.3.3
3 polaroids let more light through than 2
From this discussion, we can now easily understand how 3 polaroids let more light through
than 2. Consider 2 ﬁrst: we have one polaroid aligned with the x axis (ˆp1 = ˆx), and then a
second aligned with the y axis (ˆp2 = ˆy).
Source of
unpolarized
light
x
y
z
p1
p2
After passing through p1, the light will be polarized along the x axis. It hits p2, which is
aligned with ˆy. Since ˆx and ˆy are orthogonal, nothing gets through.
We now place a third polaroid p3 between p1 and p2. We set p3 to an orientation halfway
between p1 and p2: ˆp3 = cos θˆx + sin θˆy, with θ = π/4.
Source of
unpolarized
light
x
y
z
p1
p2
p3
After passing through p1, the light will be polarized along the x axis. It then hits p3. The
electric ﬁelds are reduced by a factor of cos π/4 = 1/
√
2, and the ﬁeld is then aligned with
ˆp3. It then hits p2. The electric ﬁelds are again reduced by a factor of cos π/4 = 1/
√
2. The
ﬁelds are reduced (by quite a bit!) but they are not eliminated.
200


## Page 7

21.4
Scattering
Many materials scatter light: we send light into a medium, and the light is scattered into
new directions. This is an extremely rich subject — very dense tomes have been written
about the properties and physics of light scattering! Here, we’ll content ourselves with a few
mostly qualitative observations based on what we’ve learned so far.
First, consider unpolarized light passing through some medium. The source of unpo-
larized light could be, for example, the sun; the medium could be the earth’s atmosphere.
x
y
z
sun
atmosphere
earth
The (unpolarized) sunlight is initially propagating in the z direction. We look up, in the x
direction. What can we say about the light that we see when we look up?
First, we know that, since the light is initially propagating in the z direction, it can
have no polarization along that axis. Second, since we then “measure” (with our eyes) light
that is propagating along the x direction, it can have no polarization along that axis. Our
conclusion is that the light that comes down to us from the sky should be linearly
polarized along ˆy.
In truth, this isn’t quite the case. Among other things, the light that we actually measure
tends to scatter multiple times. This gives the polarization vectors additional chances to
change direction, so we are likely to end up with a mixture rather than a perfectly linear
state. But, this argument does suggest a general tendency: the light that scatters out of the
sky will tend to have a preferred polarization axis.
Suppose the light from the sun were somehow made to be linearly polarized. Then, the
scattered light will be most intense in the direction orthogonal to the polarization direction.
If we put a giant polaroid in front of the sun, we could make the sky vary from dark to
bright by rotating the polaroid! It would be bright when the polarization axis is orthogonal
to “up”; it would be dark when the axis is parallel to “up”.
201


## Page 8

x
y
z
sun
atmosphere
earth
Figure 1: Dark above my head.
x
y
z
sun
atmosphere
earth
Figure 2: Bright above my head.
Something that has been missing so far is some discussion as to the likelihood that light
will be scattered. The scattering process works roughly as follows: Light impinges on a
molecule. Its electric ﬁeld shakes that molecule’s charges charges at the input frequency ω.
The molecule then re-radiates this input light (often changing its direction, subject to the
polarization constraints discussed above).
The electric ﬁeld of the scattered light is determined by the acceleration of the charges
in the scattering molecule — as we discussed back when we looked at special relativity,
radiation comes from accelerating charges. This means that
Escattered ∝∂2d
∂t2 ∝ω2
202


## Page 9

where d is the dipole moment of the shaken molecule. This moment will look something like
cos ωt, which is how we get the ω2 proportionality for the scattered electric ﬁeld.
As we will discuss in much greater detail in our next lecture, the intensity or brightness
of electromagnetic radiation is determined by the electric ﬁeld squared:
I ∝E2
scattered ∝ω4 ∝λ−4 .
The higher the radiation’s frequency — or the smaller its wavelength — the higher the
probability that it will be scattered.
Red light has a wavelength of about 700 nanometers. Blue light has a wavelength of
about 350 nanometers. This means that blue light is scattered about (700/350)4 = 16 times
more eﬀectively than red light!
This is why the sky is blue during the day: when we look away from the sun, the light
we see is light that has scattered out of the initial propagation direction. The input light
from the sun includes all wavelengths, but only the short wavelength stuﬀhas a very high
probability of scattering.
This is also why the sunset is red. At sunset, you are looking right at the sun — along the
initial propagation direction — and you are looking through a large thickness of atmosphere.
Most of the short wavelength stuﬀis already scattered out; only the long wavelength stuﬀ
remains.
21.5
Circular polarization
There is another polarization state that is encountered a lot in nature. Consider a wave that
has the following form:⃗
E = E0ˆx sin(kz −ωt) + E0ˆy cos(kz −ωt)⃗
B = E0ˆy sin(kz −ωt) −E0ˆx cos(kz −ωt) .
You should be able to show pretty easily that this satisﬁes all of our requirements for a plane
wave. But what exactly is going on with this screwy form???
We can get some intuition for considering what this wave looks like at a ﬁxed position.
Suppose we focus on z = 0, so⃗
E = −E0ˆx sin(ωt) + E0ˆy cos(ωt)⃗
B = −E0ˆy sin(ωt) −E0ˆx cos(ωt) .
The electric and magnetic ﬁelds rotate at the frequency ω! This is a state called circular
polarization: the tip of the electric (and magnetic) ﬁeld vector traces out a circle.
203


## Page 10

Circular polarization can often be particularly important because nature likes to produce
it. Recall how we made linearly polarized radiation: we shook a charge conﬁguration back
and forth, with the charges oscillating along a simple line. It shouldn’t surprise you to know
that circular polarization is produced by a rotating charge conﬁguration:
+
−
+
−
+
−
+
−
+
−
t = 0
ω
t = 
ω
π/4
ωt = π/2
ωt = 3π/4
ωt = π
This rotating charge distribution would produce a circularly polarized wave that propagates
out of the page.
The general polarization state is more usually somewhere between linear and circular
polarization.
Not surprisingly, this is called elliptical polarization.
It is produced from
rotating charge conﬁgurations that are viewed at some oblique angle. For example, if we
looked at the conﬁguration sketched above along its edge, we would get linearly polarized
light. If we looked at it face on, we would get circular polarization. Elliptical polarization is
what we get in the general case; it is intermediate to circular and linear polarization.
Finally, it’s worth knowing that a linearly polarized state can be thought as a superposi-
tion of two circularly polarized states, but with their vectors propagating in opposite senses.
Mathematically, this is so obvious that it may seem stupid. Let⃗Elin denote a linearly polar-
ized state; let⃗ECW denote a state in which (at ﬁxed location) the electric ﬁeld is clockwise
circular polarized; and let⃗ECCW denote a state in which the electric ﬁeld is counterclockwise
circular polarized:⃗
ECW = −E0ˆx sin(kz −ωt) + E0ˆy cos(kz −ωt)⃗
ECCW = E0ˆx sin(kz −ωt) + E0ˆy cos(kz −ωt)⃗
Elin =⃗ECW +⃗ECCW = 2E0ˆy cos(kz −ωt) .
This is so obvious you may wonder: why even bother belaboring the point? Well, the
reason is that certain media interact with circularly polarized light in very interesting ways!
For example, many organic molecules have a “chirality”, meaning that they twist in a par-
ticular way. This turns out to mean that they interact with clockwise circular polarization
diﬀerently than they interact with counterclockwise circular polarization!
If we were to shoot linearly polarized light into a medium containing such molecules, it
would interact with the clockwise component of the linear wave diﬀerently than it would
interact with the counterclockwise component. In other words, the medium would separate
the linear polarization into its two circular components. We might expect any number of
funky things to happen in this case.
204
