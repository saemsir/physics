# Lec 12 - Forces and Fields in Special Relativity- scott huges mit

> Source: `Lec 12 - Forces and Fields in Special Relativity- scott huges mit.pdf`  
> Pages: 9


## Page 1

Scott Hughes
17 March 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 12:
Forces and Fields in Special Relativity
12.1
Transformation of the electric ﬁeld
It is very easy to see how the electric ﬁeld transforms by considering a special case. Examine
a capacitor in its rest frame. Orient the capacitor such that its plates are parallel to the x−y
plane. We take the capacitor to have charge density σ on the lower plate, −σ on the upper
plate. We take the plates to be square, with each side having length L. The total amount
of charge on the plates is thus Q = σL2; the electric ﬁeld between the plates is⃗E = 4πσ ˆz:
L
The ﬁeld inside the capacitor is represented by the ﬁeld lines sketched here.
Consider now this capacitor “boosted” to a velocity v in the x direction. Charge is a
“Lorentz invariant”: all observers agree that the total charge on the plates is Q. Because
of the Lorentz contraction, the plate’s dimension along the direction of motion is seen to be
L/γ.
v
γ
L/
The charge density is thus augmented: σ′ = Q/(L × L/γ) = γQ/L2 = γσ. The electric ﬁeld
is therefore augmented as well:⃗E′ = 4πγσ ˆz. Notice that the ﬁeld lines are denser in this
picture: keep in mind that density of ﬁeld lines tells us how strong the ﬁeld is.
110


## Page 2

How about if the capacitor is oriented diﬀerently? Let’s rotate it so that the plates lie in
the y −z plane. The electric ﬁeld in the rest frame is thus⃗E = 4πσ ˆx. When this capacitor
is boosted in the x direction, the plates appear closer together, but the charge density does
not change: σ′ = σ with this orientation:⃗E′ =⃗E = 4πσ.
v
L
Notice that the density of ﬁeld lines are not changed in this picture, reﬂecting the fact that
the ﬁeld is not changed by the boost.
Even though we have only looked at the electric ﬁelds for a rather special circumstance,
the rule we deduce from this is in fact quite general: Components of the electric ﬁeld
perpendicular to the velocity are augmented by the Lorentz transformation;
components that are parallel to the velocity are unaﬀected. Mathematically,
E′
⊥
=
γE⊥
E′
||
=
E|| .
12.2
Transformation of energy and momentum
Our next goal will be to understand how forces transform between diﬀerent frames of refer-
ence. To do this, we ﬁrst must understand how to describe energy and momentum in special
relativity.
Consider an object whose rest mass — the mass that we would measure when this object
is at rest with respect to us — is m. If this object moves with velocity⃗u, what is its energy
and its momentum? In the “old-fashioned” mechanics you came to know and love in 8.012,
we said that a moving body has a kinetic energy
Ekin = 1
2m|⃗u|2
111


## Page 3

and a momentum⃗
p = m⃗u .
These deﬁnitions form the foundations of kinematics — using them and the notions of
conservation of momentum and conservation of energy, an enormous amount of mechanics
follow.
To develop a generalization of kinematics for special relativity, we insist that some notion
of “conservation of energy” and “conservation of energy” must be preserved — some kind of
notion of energy and momentum must be the same before and after two objects collide (for
example), even if those objects are moving at near light speed relative to one another. We
unfortunately will not be able to go into the “hows” of the way that this works in this course;
interested former 8.012 students can ﬁnd good discussion in Chapter 13 of Kleppner and
Kolenkow’s textbook; students who take 8.033 next year will study this by the bucketload.
I will instead just quote the ﬁnal result: “conservation of energy” and “conservation of
momentum” work in special relativity by requiring that the energy and momentum of a
mass observed to move with velocity⃗u is given by⃗
p
=
γum⃗u
E
=
γumc2
where γu = 1/
q
1 −u2/c2. Before moving on, it is worth looking at the small u expansion
of these quantities. We expand γu as
γu ≃1 + 1
2
u2
c2
u ≪c .
Using this, we ﬁnd⃗
p
≃
Ã
1 + 1
2
u2
c2
!
m⃗u
≃
m⃗u
E
≃
Ã
1 + 1
2
u2
c2
!
mc2
≃
mc2 + 1
2mu2 .
In the momentum formula, we could have included another term whose magnitude scales
proportional to u3; for small u, this term is negligible and can usually be ignored. The result
is nothing more than the “usual” momentum we all learned to love and cherish in 8.012.
The energy formula is particularly interesting: it tells us that the energy of a body with
mass m is just the “usual” kinetic energy, mu2/2, plus a “rest energy” mc2. This is probably
the most well-known physics equation on Earth, the energy associated with mass itself.
For our purposes, the most important result will be how these generalizations of energy
and momentum Lorentz transform. Suppose in frame 1 — the “unprimed” frame — a body
is seen to move with velocity⃗u. Its energy E and momentum⃗p will then be given by the
formulas above.
Consider now frame 2. Frame 2 claims that frame 1 is moving with velocity⃗v = vˆx.
What are the energy and angular momentum of the body as seen in frame 2 — the “primed”
112


## Page 4

frame? The Lorentz transformation we need is given by
E′
=
γv(E −βvcpx)
p′
x
=
γv(px −βvE/c)
p′
y
=
py
p′
z
=
pz
where βv = v/c, and γv = 1/
q
1 −v2/c2.
12.3
Transformation of forces
We are now ready to work out how force transforms between reference frames. Let us ﬁrst
work out a few quantities in the “rest frame” of our body. Note that the name “rest frame”
is somewhat misleading here — if there’s a force acting on it, it must be accelerating, so it
isn’t going to be at rest for very long! Our “rest frame” will be the frame in which the body
is initially at rest — p = 0 at t = 0, and then moves slowly enough that the old-fashioned,
slow u description of the body’s motion is accurate.
Suppose the force acts in the x direction. In this “rest frame”, the force on the body is
Fx
=
dpx
dt .
For what follows, we will also need to know about changes in the body’s position and in its
energy. The change in its position is given by
∆x
=
1
2
µFx
m
¶
∆t2
since Fx/m is the acceleration of the body. The change in its energy is given by
∆E
=
(Fx∆t)2
2m
.
You should be able to show very easily that this is just 1
2mu2 [bear in mind that u = a∆t =
(Fx/m)∆t].
Now consider the way things look in the “lab frame”. People in the lab frame see the
“rest frame” moving with velocity vˆx. They will deﬁne the force F ′
x as
F ′
x
=
dp′
x
dt′ .
To work this quantity out in terms of Fx we use the Lorentz transformation: we need ∆p′
x
and ∆t′,
∆p′
x
=
γv (∆px −βv∆E/c)
=
γv
h
∆px −βv(Fx∆t)2/(2mc)
i
∆t′
=
γv (∆t −βv∆x/c)
=
γv
h
∆t −βvFx∆t2/(2mc)
i
=
γv∆t [1 −βvFx∆t/(2mc)]
113


## Page 5

Now, we divide and take a limit:
F ′
x
=
lim
∆t′→0
∆p′
x
∆t′
=
lim
∆t→0
γv [∆px −βv(Fx∆t)2/(2mc)]
γv∆t [1 −βvFx∆t/(2mc)]
=
lim
∆t→0
γv∆px
γv∆t
=
Fx .
Components of force parallel to the frames’ relative motion are the same in both
reference frames!
Suppose the force was in a perpendicular direction. The analysis goes through largely
the same:
F ′
y
=
lim
∆t′→0
∆p′
y
∆t′
=
lim
∆t→0
∆py
γv∆t [1 −βvFx∆t/(2mc)]
=
lim
∆t→0
∆py
γv∆t
=
Fy
γv
.
Components of force perpendicular to the frames’ relative motion are related by
a factor of 1/γ: The force in the “lab” frame is smaller by 1/γ than the force in
the “rest” frame.
114


## Page 6

12.4
The force exerted by a current upon a moving charge
Warning: the going gets a little rough in this section.
12.4.1
Lab frame
In the lab frame, we have a wire that is electrically neutral, but that carries a current. The
wire contains positive charges with density per unit length λ+ = λ0. This is the rest frame
of those charges, so this means λREST
+
= λ0.
: positive charge
: negative charge
Figure 1: The moving negative charges generate a current moving to the left. This in turn
leads to a magnetic ﬁeld that pushes the charge Q away from the wire.
The wire also contains negative charges; these charges are of course moving with some
velocity⃗u. Since the wire is neutral overall, the density of these negative charges is λ−= −λ0.
This is not the density of the electrons in THEIR OWN rest frame!!!! Suppose that the charge
density of the electrons in their own rest frame is λREST
−
. By the Lorentz contraction, we
must have
λ−= γuλREST
−
where γu = 1/
q
1 −u2/c2. Doing the math, this tells us that
λREST
−
= −λ0
γu
.
We’ll need this result shortly.
A charge Q outside of the wire is moving to the right. What forces act on the charge?
Since the wire is neutral, there can be no electric force. However, there is a current with
magnitude I = λ0u ﬂowing in the wire. This generates a magnetic ﬁeld,
B = 2I
rc = 2λ0u
rc
and so there is a force of magnitude
F = qvB/c = 2qλ0uv
rc2
.
By doing the right hand rule game, we quickly see that this force repels the charge from the
wire.
115


## Page 7

12.4.2
Charge’s rest frame
By deﬁnition, the charge sits still in this frame. Since it’s not moving, there cannot be a
magnetic force that acts on it. But, for there to be a consistent description of the system
in the two reference frames there has to be some kind of force. What can it be? The only
possibility is that there is an electric force.
“Where the hell does that come from???”
you ask.
Let’s ﬁnd out by analyzing the
charges in the wire in this frame:
: positive charge
: negative charge
Figure 2: Currents in the wire are irrelevant since the charge does not move in this frame.
However, the diﬀerent length contractions experienced by the positive and the negative
charges leads to the wire having a net positive charge as seen in this frame, leading, again,
to a force repelling the charge from the wire.
Positive charges: the positive charges are moving in this frame with velocity −⃗v. Their
density as seen in this frame is thus given by
λ′
+ = γvλREST
+
= γvλ0 ,
where γv = 1/
q
1 −v2/c2.
Negative charges: the negative charges are moving in this frame with a velocity given by
adding the velocity −⃗u to⃗v in the correct, relativistic fashion: their velocity is
u′ =
u −v
1 −uv/c2
and so their density is given by
λ′
−= γu′λREST
−
= −γu′
γu
λ0 .
The Lorentz factor γu′ is a bit of a mess: we need 1/
q
1 −(u′)2/c2.
Let’s look at this
methodically. First, to simplify the notation a bit, deﬁne
βv
=
v/c
βu
=
u/c
βu′
=
u′/c .
116


## Page 8

Next, look at 1 −(u′/c)2 = 1 −β2
u′:
1 −β2
u′
=
1 −
Ã βu −βv
1 −βuβv
!2
=
1 −β2
u + β2
v −2βuβv
(1 −βuβv)2
=
1 −2βuβv + β2
uβ2
v
(1 −βuβv)2
−β2
u + β2
v −2βuβv
(1 −βuβv)2
=
1 −β2
u −β2
v + β2
uβ2
v
(1 −βuβv)2
=
(1 −β2
u)(1 −β2
v)
(1 −βuβv)2
=
1
γ2
uγ2
v(1 −βuβv)2 .
This means that
γu′ = γuγv(1 −βuβv) .
We now ﬁnally have enough information to calculate the density of negative charges:
λ′
−
=
−γu′
γu
λ0
=
−γv(1 −βuβv)λ0 .
The net, total charge density of the wire in this frame is given by adding the contributions
of the negative and the positive charges:
λ′
net
=
λ′
+ + λ′
−
=
γvλ0 −γv(1 −βuβv)λ0
=
γvβuβvλ0 .
=
γv
uvλ0
c2
.
The wire has a net positive line charge density in this reference frame!!!
This means it
generates an electric ﬁeld
E′
=
2λ′
net
r
=
2γvuvλ0
rc2
which in turn means that there is a force
F ′ = 2γvqλ0uv
rc2
.
repelling it from the wire.
Note that there is also a magnetic ﬁeld in this frame — there are currents associated
with both the positive and the negative charges in the wire. However, since the charge Q is
at rest, only the electric ﬁeld is relevant to the force that it experiences.
117


## Page 9

12.4.3
Comparison of the forces in the two frames
In the “lab frame”, we see the charge moving with speed v and deduce that it will feel a
magnetic force
F = 2uvλ0
rc2
.
In the “charge frame”, the charge is at rest, so it cannot feel any magnetic force. However,
we just showed that in this frame the wire is not electrically neutral, and so the charge
experiences an electric force of
F ′ = γv
2uvλ0
rc2
.
Are these results consistent? Yes!! Remember that rule for transforming forces: the force
that is experienced in the “lab frame” is related to that in the moving frame by a factor of
1/γv. In other words, we expect to ﬁnd
F = 1
γv
F ′
— exactly what we do in fact ﬁnd.
You may object that one force is electric and the other is magnetic — aren’t we comparing
apples and oranges here? For many years, people thought this way: electric forces were one
phenomenon, magnetic forces were another. There was no connection between the two. As
thought experiments like this show, however, this distinction is a false one. The electric
force acting on a charge in that charge’s rest frame is exactly what we need to explain the
magnetic force in a frame in which that charge is moving.
Physics is consistent: even though we give diﬀerent detailed explanations ascribing what
mechanism produces the forces in the two reference frames, we agree exactly as to what this
force should be. This is the essence of special relativity! It also tells us that electric forces and
magnetic forces are really the same thing. “Electricity” and “magnetism” are not separate
phenomena: they are diﬀerent speciﬁc manifestations of a single critter, “electromagnetism”.
12.5
Summary
The discussion of the past two lectures is probably the most diﬃcult that we will face all
semester. Let’s recap the major points:
• Moving clocks run slow. Time dilation means that a clock which is moving very
quickly relative to you will tick more slowly than a clock that is at rest with respect
to you.
• Moving rulers are shortened. The Lorentz contraction means that you will measure
a car shooting past you at very high speed to be shorter than an identical car that is
at rest with respect to you.
– But only along the direction of motion!!! There is no Lorentz contraction
in a direction orthogonal to the relative motion.
• What looks like a pure magnetic ﬁeld in one frame looks like a mixture
of magnetic and electric ﬁelds in another frame. This guarantees that there is
some kind of force acting on our charge even when we go into its rest frame.
118
