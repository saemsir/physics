# Lec 11 - Spacetime- Introduction to Special Relativity - scott huges mit

> Source: `Lec 11 - Spacetime- Introduction to Special Relativity - scott huges mit.pdf`  
> Pages: 9


## Page 1

Scott Hughes
15 March 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 11:
Spacetime: Introduction to Special Relativity
Preamble: The vast majority of material presented in this course consists of subjects that
are challenging, but that I am convinced every 8.022 student can — and should! — learn
well. Special relativity is the only exception to this rule. The material that we will begin
covering today (and that we will conclude on Thursday) is, in my experience, by far the
most confusing subject that we cover all term. Further, it is not strictly necessary to learn
this material inside and out in order to understand and excel in 8.022.
You may wonder, given this, why we are bothering to study it at all. The reason is that
special relativity “explains” the magnetic ﬁeld: what we ﬁnd at the end of all of this is that
magnetic forces are nothing but electric forces viewed in another frame of reference. Magnetic
ﬁelds are just electric ﬁelds “in drag”, so to speak.
Conceptually, this is an extremely
important point: even if you do not fully grasp the details of where many of the formulas we
are about to derive come from, I ﬁrmly believe every 8.022 student should understand what
magnetic forces “look like” in diﬀerent frames of reference.
The punchline of this preamble is that you should not be too worried if 8.022’s discussion
of special relativity makes your brain hurt. Those of you who take more physics courses
will encounter these concepts several more times; if you don’t quite get it now, you will
have plenty of chances to get it later1. Try to get the ﬂavor of what is happening now, and
practice manipulating these formulas, even if it is not 100% clear what is going on.
11.1
Principles of special relativity
Special relativity depends upon two postulates:
1. The laws of physics are the same in all frames of reference.
2. The speed of light is the same in all frames of reference.
These postulates beg the question — what is a frame of reference? A frame of reference
(more properly an inertial frame of reference) is any set of coordinates that can be used to
describe a non-accelerating observer. In the following discussion we will compare measure-
ments in two frames of reference: a station, and a train that is moving through this station
in the x direction with constant speed v.
11.2
Time dilation
These postulates have consequences that are rather amazing. In particular, it means that
inertial observers in diﬀerent frames of reference measure diﬀerent intervals of time between
1I studied special relativity in 4 separate courses as an undergrad; I honestly can’t say I really knew what
I was doing until about halfway through the third time. Even then, the fourth study was useful to me.
101


## Page 2

events, and diﬀerent spatial separations between events. As we’ll see in a moment, clocks
that appear to be moving run slow; rulers that appear to be moving are shrunk.
Consider a pulse of light emitted from a bulb in the center of a train. The train is moving
at speed v in the x direction with respect to a station. The pulse of light is directed toward
a photosensor on the ﬂoor of the train, directly under the bulb. Two events are of interest
to observers on the train and in the station: the emission of light from the bulb, and the
reception of this light by the photodetector.
v
h
h’
Our ﬁrst question is: How much time passes between the emission of this pulse and its
reception on the ﬂoor?
The amount of time that is measured to pass is diﬀerent for observers on the train (at
rest with respect to the bulb and the photosensor) than it is for observers in the station
(who see the bulb and the photosensor in motion). Let’s look at things in the train frame
ﬁrst: the amount of time between emission and reception is just the vertical distance h the
light pulse travels divided by the speed of light c:
∆ttrain = h
c
How do things look to observers in the station, watching the train go by? They agree
that the pulse of light moves vertically through a distance h. However, they claim it also
moves through horizontal distance because the train is moving with speed v. If the elapsed
time between emission and reception as seen in the station frame is ∆tstation, then the pulse
moves through a total distance h′ =
q
h2 + (v∆tstation)2. Since the speed of light is the same
in all frames of reference, the time interval ∆tstation = h′/c:
∆tstation = 1
c
q
h2 + (v∆tstation)2
Substitute h = c∆ttrain:
(∆tstation)2 = (∆ttrain)2 + v2
c2 (∆tstation)2
∆tstation
=
∆ttrain
q
1 −v2/c2
≡
γ∆ttrain
102


## Page 3

where we have deﬁned γ = 1/
q
1 −v2/c2; note that γ ≥1. This relation tells us that the
moving clock runs slow: the time interval measured by observers who see the clock moving
(those in the station) is larger than the time interval measured by observers who are at rest
with respect to it.
11.3
Length contraction
Let’s move our light source to the back of the train. We ﬂash it in the forward direction,
where it reﬂects oﬀa mirror at the front of the train. The light then returns to the light
source, where we measure it. This is a way to measure the length of the railway car.
v
mirror
The two events of interest in this case are the emission of light by the bulb, and its reception
after it bounces back to us.
Let’s examine what’s going on in the train’s reference frame ﬁrst. If the elapsed time
between emission of the light and reception is ∆ttrain, we would infer that the length of the
train is
∆xtrain = c∆ttrain/2
How do things look in the station frame? We break down the light travel into two pieces:
emission to the mirror, then mirror back to reception. Let’s say it takes a time ∆tstation, 1 for
the ﬁrst piece — emission to the mirror. An interval ∆tstation, 2 passes following reﬂection
to travel back to reception. If the length of the train as measured in the station is ∆xstation,
then the travel times in each bounce is given by
∆tstation,1
=
(∆xstation + v∆tstation,1)/c
∆tstation,2
=
(∆xstation −v∆tstation,2)/c
The time from emission to mirror is longer since the mirror is moving in the same direction
as the light — the light has to chase the mirror on the ﬁrst piece of the round trip, which
takes extra time. On the second piece, the back of the train is rushing towards the light, so
it takes less time.
We rearrange these expressions to isolate the travel times:
∆tstation,1
=
∆xstation
c −v
∆tstation,2
=
∆xstation
c + v
103


## Page 4

Then, we add them together to get the total travel time:
∆tstation
≡
∆tstation,1 + ∆tstation,2
=
2∆xstation/c
1 −v2/c2
=
2γ2∆xstation/c
From our discussion of time dilation, we also know that ∆tstation = γ∆ttrain = 2γ∆xtrain/c.
Combining this with our result for ∆tstation, we get
γ∆xtrain = γ2∆xstation
or
∆xstation = ∆xtrain/γ
Since γ ≥1, this tells us that moving objects are contracted: the train’s length according to
observers that see it moving is less than the length measured in the “rest frame”.
11.3.1
No contraction for perpendicular directions
What about the dimensions of the train that are perpendicular to the train’s motion? With-
out getting too technical, a simple thought experiment can convince us that the perpendicular
directions cannot be aﬀected by the motion.
Imagine a train moving towards the mouth of a tunnel. Suppose that the tunnel is 4
meters tall in its rest frame, and that the train is 3.5 meters tall in its rest fram. Suppose the
train is moving at 90% of the speed of light. What would happen if the Lorentz contraction
shrunk the vertical size of the train?
In the rest frame of the tunnel, the train would appear very short: its height would be
Lorentz contracted to htrain, contracted = 3.5 meters/γ = 1.53 meters. It ﬁts into the tunnel
with no problem.
However, it is equally valid to say that the train is at rest and the tunnel is moving
toward it at 0.9c. Observers in the rest frame of the tunnel claim that the tunnel is shrunk
to a height htunnel, contracted = 4.0 meters/γ = 1.74 meters — far smaller than the train itself!!!
In one frame, the train ﬁts; in the other, it gets smashed. This is not consistent physics!
Lorentz contraction of the perpendicular directions does not happen since it does not follow
the rules that physics be the same in all reference frames.
11.3.2
Example: Cosmic ray muons
Muons are elementary particles that act, for all practical purposes, like heavy electrons.
They are commonly created on earth when high energy protons (cosmic rays) slam into the
upper reaches of the earth’s atmosphere, several tens of kilometers about the surface. Muons
decay into an electron and a neutrino in about 2 × 10−6 seconds. This suggests a mystery:
how can a particle that is produced 20 kilometers about the earth possibly reach the ground
if it decays in 2 microseconds? Even if the particle were moving at nearly the speed of light,
it could only move about 600 meters before decaying.
104


## Page 5

Special relativity saves the day. Suppose the muon is moving at 99.99% of the speed of
light. As seen on the surface of the earth, time dilation stretches out its lifetime to
∆tmuon = 2 × 10−6 sec
√
1 −0.99992 = 1.4 × 10−4 sec
With this lifetime, the muon can travel a distance
∆xmuon = 0.9999 × c × 1.4 × 10−4 sec = 42 kilometers
before decaying. The muon can easily make it from high up in the atmosphere to the ground.
It’s also interesting to think about this from the muon’s perspective. In this frame, the
muon is at rest, and the earth’s atmosphere is rushing past it at 99.99% of the speed of light.
This means that the atmosphere is length contracted by a factor of 1/γ = 1/71. From the
muon’s perspective, the atmosphere is so thin that it can easily reach the ground.
The two perspectives shown here encapsulate what the slogan “The laws of physics are
the same in all frames of reference” really means. On the earth’s surface, we say that the
lifetime of the muon is time dilated until it lives long enough to reach the earth’s surface.
In the muon’s rest frame, its lifetime is only 2 microseconds, so there’s no way it could
make it through tens of kilometers of atmosphere. However, in this frame, the atmosphere
is length contracted until the muon can easily penetrate it in 2 microseconds.
The two
observers interpret the details of what is going on very diﬀerently. But both agree on the
most important aspect of the phenomena: the muon reaches the ground.
11.4
Lorentz transformation
Length and time dilation are speciﬁc manifestations of a general consequence of special
relativity: what we consider to be “time” and “space” in one reference frame is mixture
of the notions of “time” and “space” as measured in another reference frame. The general
relation between time and space coordinates in diﬀerence frames of reference is described by
the Lorentz transformation.
The Lorentz transformation is a linear relation between the coordinates of the “rest
frame” (for example, the train station) and the “moving frame” (for example, on the train).
Let us denote the coordinates of the rest frame as (t, x, y, z); the coordinates of the moving
frame are (t′, x′, y′, z′). The moving frame moves with speed v in the x direction, as seen in
the rest frame.
The general form of the transformation that relates the two coordinates is
x′
=
Ax + Bt
t′
=
Cx + Dt
y′
=
y
z′
=
z
The y and z coordinates are the same in both frames since the relative motion is in the x
direction. Note that the transformation is linear — there are no terms that go proportional
to t2, for example. This is necessary to ensure that the reference frames are inertial — if
there were nonlinear terms, the frames would appear to be accelerating with respect to one
another rather than moving at a relative velocity.
105


## Page 6

Our goal now is to calculate A, B, C, and D. We ﬁrst require that the two coordinate
systems must match at the origin: the coordinate x′ = 0 must match x = vt:
x′
=
Ax + Bt
=
Avt + Bt
=
0
The ﬁrst line is the general Lorentz tranformation relating x′ to x and t. On the second line,
we plug in x = vt. Setting x′ = 0 and solving, we ﬁnd.
→B = −Av .
Matching at the origin also requires that x = 0 must match x′ = −vt′:
x′
=
A(x −vt)
(General transform for x′)
=
−Avt
(x = 0)
=
−vt′
(x′ = −vt′)
=
−v(Cx + Dt)
(General transform for t′)
=
−vDt
(x = 0)
Comparing the second and ﬁfth lines, we have
A = D
OK, so far we’ve determined two of the four constants, and so we can rewrite the Lorentz
transformation as
x′
=
A(x −vt)
t′
=
Cx + At
To determine the remaining two constants, we think about the properties of light pulses as
described by the two coordinate systems.
First, consider a light pulse that is sent out in the x direction. We shoot this pulse out
at t = 0. The location of the pulse in the unprimed coordinate system is x = ct. This pulse
will also move out parallel to the x′ coordinate system since the relative motion of the two
systems is in this direction.
Since the speed of light is the same in all reference frames, its position in the primed
coordinate system is given by x′ = ct′:
x′
=
ct′
A(x −vt)
=
c(Cx + At)
Act −Avt
=
c2Ct + cAt
−Av
=
c2C
→C
=
−Av/c2
The Lorentz transformation now becomes
x′
=
A(x −vt)
t′
=
A(t −vx/c2)
106


## Page 7

To ﬁnally determine A, we shoot a light pulse out along the y axis.
In the unprimed
coordinate system, the location of the pulse is given by y = ct, x = 0. What is its location in
the primed system? The motion of the frame itself will cause it to move in the x′ direction.
The total distance that the pulse moves is ct′. We therefore must have (x′)2 +(y′)2 = c2(t′)2:
(x′)2 + (y′)2
=
c2(t′)2
A2(x −vt)2 + y2
=
c2A2(t −vx/c2)2
A2(−vt)2 + c2t2
=
c2A2t2
(x = 0, y = ct)
A2
=
1
1 −v2/c2 = γ2
We thus have ﬁnally ﬁxed the Lorentz transformation’s form:
x′
=
γ(x −vt)
t′
=
γ(t −vx/c2)
This can be written more symmetrically by deﬁnining β = v/c and multiplying the t trans-
formation by c:
x′
=
γ[x −β(ct)]
ct′
=
γ[ct −βx]
The inverse of this transformation is quite simple. Observers at rest on the train see the
station moving in the −x direction with speed v. This means that the Lorentz transformation
is inverted by just reversing the direction of v — i.e., we replace v with −v:
x
=
γ(x′ + vt′)
t
=
γ(t′ + vx′/c2)
or
x
=
γ[x′ + β(ct′)]
ct
=
γ[ct′ + βx′]
107


## Page 8

11.5
Transformation of velocity
An important result that follows from this is a formula for addition of velocity. Suppose I
am in the moving train, walking from one end to the other with a speed dx′/dt′ = u′
x:
v
u’x
With what speed ux does someone in the station frame see me move? In old fashioned
mechanics, we would just add my speed to the speed of the moving train, and so we’d have
ux = u′
x + v. To do it correctly in special relativity, we use the Lorentz transformation:
ux
=
dx
dt
=
γ(dx′ + vdt′)
γ(dt′ + vdx′/c2)
=
(dx′/dt′) + v
1 + (v/c2)(dx′/dt′)
=
u′
x + v
1 + (vu′
x/c2)
This formula shows how it is impossible for anything to move faster than the speed of light.
Suppose the train is moving at v = 0.95c. Suppose further that my walking speed within the
train is u′
x = 0.95c. In old fashioned mechanics, we would predict that my walking speed as
seen from the ground would be 1.9c — almost twice the speed of light. In special relativity,
we ﬁnd
ux
=
0.95c + 0.95c
1 + 0.95 × 0.95
=
1.9c
1.9025
=
0.9987c
Close to, but still less than, the speed of light.
Suppose that I walk perpendicular to the train’s motion: I walk with
u′
y = dy′
dt′
What is this as seen from the ground? Again, we use the Lorentz transformation:
uy
=
dy
dt
108


## Page 9

=
dy′
γ(dt′ + vdx′/c2)
=
dy′/dt′
γ[1 + (v/c2)(dx′/dt′)]
=
u′
y
γ[1 + (vu′
x/c2)]
Likewise,
uz =
u′
z
γ[1 + (vu′
x/c2)]
We will use these formulas in the next lecture to explore how things transform from the
“viewpoint” of moving charges and currents.
109
