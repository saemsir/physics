# Lec 20 - Wave equation & electromagnetic radiation - scott huges mit

> Source: `Lec 20 - Wave equation & electromagnetic radiation - scott huges mit.pdf`  
> Pages: 9


## Page 1

Scott Hughes
28 April 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 20:
Wave equation & electromagnetic radiation
20.1
Revisiting Maxwell’s equations
In our last lecture, we ﬁnally ended up with Maxwell’s equations, the four equations which
encapsulate everything we know about electricity and magnetism. These equations are:
Gauss’s law:⃗
∇·⃗E = 4πρ
Magnetic law:⃗
∇·⃗B = 0
Faraday’s law:⃗
∇×⃗E = −1
c
∂⃗B
∂t
Generalized Ampere’s law:⃗
∇×⃗B = 4π
c⃗J + 1
c
∂⃗E
∂t .
In this lecture, we will focus on the source free versions of these equations: we set ρ = 0 and⃗
J = 0. We then have⃗
∇·⃗E
=
0⃗
∇·⃗B
=
0⃗
∇×⃗E
=
−1
c
∂⃗B
∂t⃗
∇×⃗B
=
1
c
∂⃗E
∂t .
The source free Maxwell’s equations show us that⃗E and⃗B are coupled: variations in⃗E act
as a source for⃗B, which in turn acts as a source for⃗E, which in turn acts as a source for⃗B,
which ... The goal of this lecture is to fully understand this coupled behavior.
To do so, we will ﬁnd it easiest to ﬁrst uncouple these equations. We do this by taking
the curl of each equation. Let’s begin by looking at⃗
∇×
³⃗
∇×⃗E
´
=⃗∇×

−1
c
∂⃗B
∂t

.
The curl of the left-hand side of this equation is⃗
∇×⃗∇×⃗E =⃗∇
³⃗
∇· E
´
−∇2⃗E = −∇2⃗E .
(We used this curl identity back in Lecture 13; it is simple to prove, albeit not exactly
something you’d want to do at a party.) The simpliﬁcation follows because we have restricted
ourselves to the source free equations — we have⃗∇·⃗E = 0. Now, look at the curl of the
right-hand side:⃗
∇×

−1
c
∂⃗B
∂t

= −1
c
∂
∂t
³⃗
∇×⃗B
´
= −1
c2
∂2⃗E
∂t2 .
186


## Page 2

Putting the left and right sides together, we end up with
∂2⃗E
∂t2 −c2∇2⃗E = 0 .
Repeating this procedure for the other equation, we end up with something that is essentially
identical, but for the magnetic ﬁeld:
∂2⃗B
∂t2 −c2∇2⃗B = 0 .
As we shall now discuss, these equations are particularly special and important.
20.2
The wave equation
Let us focus on the equation for⃗E; everything we do will obviously pertain to the⃗B equation
as well. Furthermore, we will simplify things initially by imagining that⃗E only depends on
x and t. The equation we derived for⃗E then reduces to
∂2⃗E
∂t2 −c2∂2⃗E
∂x2 = 0 .
20.2.1
General considerations
At this point, it is worth taking a brief detour to talk about equations of this form more
generally. This equation for the electric ﬁeld is a special case of
∂2f
∂t2 −v2∂2f
∂x2 = 0 .
This equation is satisﬁed by ANY function whatsoever1 provided that the argument of the
function is written in the following special way:
f = f(x ± vt) .
This is easy to prove. Let u = x ± vt, so that f = f(u). Then, using the chain rule,
∂f
∂x = ∂u
∂x
∂f
∂u = ∂f
∂u ;
it follows quite obviously that
∂2f
∂x2 = ∂2f
∂u2 .
The time derivatives are not quite so trivial:
∂f
∂t = ∂u
∂t
∂f
∂u = ±v∂f
∂u ,
1To the mathematical purists, we must insist that the function f be smooth enough that it has well-
behaved derivatives. At the 8.022 level, this is a detail we can largely ignore.
187


## Page 3

so
∂2f
∂t2 = v2∂2f
∂u2 .
Plugging in, we see
∂2f
∂t2 −v2∂2f
∂x2 = v2∂2f
∂u2 −v2∂2f
∂u2 = 0 .
Having shown that any function of the form f(x ± vt) satisﬁes this equation, we now
need to examine what this solution means. Let’s consider f(x −vt) ﬁrst; and, let’s say that
v = 1. (Don’t worry about units just yet.) Suppose that at t = 0, the function f has the
following shape:
f
x
t = 0
x = 5
The peak of this function occurs when the argument of f is 5 — in other words, for t = 0,
the peak occurs at x = 5.
188


## Page 4

What does this function look at t = 1?
Clearly it will have the exact same shape.
However, that shape will be shifted over on the x-axis by one unit! For example, the peak of
f still occurs when the argument of f is 5. This means we must have x −vt = 5, which for
t = 1 means the peak occurs at x = 6. All other points in the shape are similarly shifted:
f
x
t = 1
x = 6
As time passes, this shape just slides to the right, in the direction of increasing x. In other
words, f(x −vt) representes a wave traveling in the POSITIVE x direction with speed v.
What is the other solution? Applying this logic to f(x + vt), we see that this represents
a wave moving in the opposite direction, towards smaller x. For example, at t = 1, the
x + vt = 5 means x = 4 — the peak of the curve shifts to x = 4 after 1 time unit:
f
x
t = 1
x = 4
f(x + vt) representes a wave traveling in the NEGATIVE x direction with speed v.
189


## Page 5

OK, what we’ve got so far is that equations of the form
∂2f
∂t2 −v2∂2f
∂x2 = 0
generically have solutions of the form f = f(x ± vt), where f(u) is essentially arbitrary.
These solutions represent waves travelling at speed v; the solution with x −vt represents
a wave travelling in the positive x direction; the solution with x + vt represents a wave
travelling in the negative x direction.
20.2.2
Maxwell and the wave equation
You can probably see where we’re going with this now! The equation for⃗E that we derived
earlier,
∂2⃗E
∂t2 −c2∂2⃗E
∂x2 = 0
is itself a wave equation. It represents a wave travelling along the x axis with speed c —
the speed of light! This kind of analysis is what made people realize that light is itself an
electromagnetic wave.
This would have been far more interesting if we had worked in SI units throughout
— getting the speed of light at the end of the day in cgs units is one of those “Well, duh”
moments, since c appears throughout those equations already. In SI units, the wave equation
that we end up with is
∂2⃗E
∂t2 −
1
ϵ0µ0
∂2⃗E
∂x2 = 0
indicating that electromagnetic waves travel with speed
v =
1
√µ0ϵ0
.
Plug in some numbers:
ϵ0
=
8.85418 × 10−12 Coulomb2 Newton−1 meter−2
µ0
=
4π × 10−7 Newton sec2 Coulomb−2
so,
ϵ0µ0 = 1.11265 × 10−17 s2 m−2
−→
1
√ϵ0µ0
= 2.998 × 108 m/s = 2.998 × 1010 cm/s .
This again is of course the speed of light.
The fact that light is connected to electric and magnetic ﬁelds was ﬁrst recognized from
this kind of calculation. Maxwell ﬁrst showed that the four equations describing electric and
magnetic ﬁelds could be rearranged to form a wave equation, with a speed of propagation
as given above.
190


## Page 6

At the time, ϵ0 and µ0 were empirical quantities that were determined through careful
measurements of static electric and magnetic ﬁelds — in SI units, ϵ0 shows up in the capac-
itance formula, and µ0 shows up in the inductance formula . It was quite a shock to ﬁnd
that these quantities determined the behavior of highly dynamical ﬁelds as well, and even
more of a shock to realize that the speed 1/√ϵ0µ0 was the speed of light! At the time, ϵ0, µ0,
and c were uncertain enough that the correspondance between 1/√ϵ0µ0 was not perfectly
deﬁnitive. However, it was close enough that Maxwell wrote in 18642
This velocity is so nearly that of light that it seems we have strong reason to conclude that
light itself (including radiant heat and other radiations) is an electromagnetic disturbance
in the form of waves propagated through the electromagnetic ﬁeld according to
electromagnetic laws.
It is largely for this reason that this whole set of equations is named for Maxwell.
20.3
Plane waves
A particularly important and useful form of wave for our study are the class known as plane
waves. The most general form of these waves is⃗
E
=⃗
E0 sin(⃗k ·⃗r −ωt)
=⃗
E0 sin(kxx + kyy + kzz −ωt) ,⃗
B
=⃗
B0 sin(⃗k ·⃗r −ωt)
=⃗
B0 sin(kxx + kyy + kzz −ωt) .
The quantities⃗E0 and⃗B0 are the amplitudes of the electric and magnetic ﬁelds. Note that
these amplitudes are vectors; we will determine some important properties for these vectors
soon.
The vector⃗k = kxˆx + kyˆy + kzˆz is the “wavevector”; its magnitude k =
q
k2
x + k2
y + k2
z
is the “wavenumber”. The unit vector ˆk =⃗k/k is the wave’s propagation direction. The
number ω is the angular frequency of the wave.
Earlier, we showed that electromagnetic waves are given by functions of the form f(x−ct).
Generalizing to three dimensions, we would write this as f(⃗r−cˆkt) — the position⃗r changes
with velocity cˆk. With this in mind, we can quickly show that the wavenumber k and ω are
related to one another:⃗
k ·⃗r −ωt =⃗k ·
µ⃗
r −ω
k
ˆkt
¶
.
Combining this with the requirement that the dependence on⃗r and t must be of the form
f(⃗r −cˆkt) tells us that k and ω are related by the speed of light:
ω = ck .
2See R. Baierlein, Newton to Einstein (Cambridge, 1992).
191


## Page 7

20.3.1
More on⃗k and ω
For the moment, let’s simplify our wave vector so that it is oriented along the x-axis: we
put⃗k = kˆx. Our plane wave solution is then⃗
E
=⃗
E0 sin(kx −ωt)⃗
B
=⃗
B0 sin(kx −ωt) .
Let’s look at the spatial variation of this wave at t = 0: clearly, we just have⃗
E
=⃗
E0 sin(kx)⃗
B
=⃗
B0 sin(kx) .
These functions pass through zero at x = 0, x = 2π/k, x = 4π/k, etc. 2π/k is clearly a
special lengthscale: it is called the wavelength, λ. It tells us about the lengthscale over which
the wave repeats its pattern.
Now, think about the time variations at a particular location, say x = 0:⃗
E
=
−⃗E0 sin(ωt)⃗
B
=
−⃗B0 sin(ωt) .
These functions pass through zero at t = 0, t = 2π/ω, t = 4π/ω, etc. 2π/ω is the period
of the wave, T. This of course the usual relationship between the period of an oscillation
and its angular frequency. The inverse period is the wave’s frequency (as opposed to angular
frequency), usually written ν or f:
ν = f = ω/2π = 1/T .
20.3.2
Summary of wavenumber and frequency relations
Putting all of this together we end up with several relations between wavenumber, wave-
length, frequency, angular frequency, and the speed of light. First, we have
ω = ck .
Plugging in ω = 2πν and k = 2π/λ, we ﬁnd
νλ = c .
20.4
Final constraints
Let’s assess what we have so far: the source free Maxwell equations,⃗
∇·⃗E
=
0⃗
∇·⃗B
=
0⃗
∇×⃗E
=
−1
c
∂⃗B
∂t⃗
∇×⃗B
=
1
c
∂⃗E
∂t ,
192


## Page 8

can be manipulated in such a way as to show that⃗E and⃗B each obey the wave equation,
∂2⃗E
∂t2 −c2∇2⃗E
=
0
∂2⃗B
∂t2 −c2∇2⃗B
=
0 .
We’re not done yet! In addition to satisfying the wave equation, we must also verify
that our functions⃗E and⃗B satisfy the other Maxwell equations — I can write down lots of
functions that satisfy the wave equations, but that are not valid electromagnetic ﬁelds for
ρ = 0 and⃗J = 0.
First,⃗E and⃗B must satisfy⃗∇·⃗E = 0 and⃗∇·⃗B = 0. Let’s plug our plane wave solutions
into this:⃗
∇·⃗E
=⃗
∇·
h⃗
E0 sin(kxx + kyy + kzz −ωt)
i
=
(kxE0,x + kyE0,y + kzE0,z) cos(kxx + kyy + kzz −ωt)
=
³⃗
k ·⃗E0
´
cos(kxx + kyy + kzz −ωt) .
Likewise,⃗
∇·⃗B =
³⃗
k ·⃗B0
´
cos(kxx + kyy + kzz −ωt) .
The only way for this to hold for all x and t is if⃗
k ·⃗E0
=
0⃗
k ·⃗B0
=
0 .
In other words, the divergence equations require that
Radiation’s electric and magnetic ﬁelds are orthogonal to the propagation
direction.
Let’s next look at one of the curl equations:⃗
∇×⃗B = 1
c
∂⃗E
∂t .
This equation tells us that⃗E and⃗B are perpendicular to one another. On the right-hand
side, we have ∂⃗E/∂t. This points in the same direction as⃗E — the time derivative does not
change the vector’s direction. On the left, we have⃗∇×⃗B. This is perpendicular to⃗B —
the curl of any vector is orthogonal to that vector.
So, the ﬁrst thing the curl equations tell us is that
Radiation’s electric and magnetic ﬁelds are orthogonal to each other.
Now, let’s actually compute the derivatives. The right-hand side is easiest, so let’s do it ﬁrst:
1
c
∂⃗E
∂t
=
−ω
c⃗E0 cos(⃗k ·⃗r −ωt)
=
−k⃗E0 cos(⃗k ·⃗r −ωt) .
193


## Page 9

Now, the left-hand side:⃗
∇×⃗B
=⃗
∇×
h⃗
B0 sin
³⃗
k ·⃗r −ωt
´i
=⃗
∇×
h⃗
B0 sin (kxx + kyy + kzz −ωt)
i
.
This looks like it might be a mess. However, back on Pset 3 we proved a very useful identity:⃗
∇× (⃗Ff) = f⃗∇×⃗F +⃗∇f ×⃗F .
Put⃗F ≡⃗B0, f = sin
³⃗
k ·⃗r −ωt
´
. Then, we have⃗∇×⃗F = 0 —⃗B0 is constant! Only the
other term contributes; plugging in for⃗F and f, what we are left with is⃗
∇×⃗B
=⃗
∇[sin (kxx + kyy + kzz −ωt)] ×⃗B0
=
[(kxˆx + kyˆy + kzˆz) cos (kxx + kyy + kzz −ωt)] ×⃗B0
=
³⃗
k ×⃗B0
´
cos
³⃗
k ·⃗r −ωt
´
.
After slogging through all of this, we ﬁnally obtain⃗
∇×⃗B
=
1
c
∂⃗E
∂t
−→
³⃗
k ×⃗B0
´
cos
³⃗
k ·⃗r −ωt
´
=
−k⃗E0 cos(⃗k ·⃗r −ωt) ,
or⃗
E0 = −ˆk ×⃗B0 .
There are two interesting things we can do with this. First, let’s take the magnitude of both
sides:
|⃗E0|
=
| −ˆk ×⃗B0|
=
|ˆk||⃗B0|
since ˆk is orthogonal to⃗B0
=
|⃗B0|
since |ˆk| = 1.
In cgs units, the radiation’s electric and magnetic ﬁelds have the same
magnitude.
Second, one can show from this equation that⃗E0 ×⃗B0 = |⃗E0|2ˆk:⃗
E0 ×⃗B0
=
−(ˆk ×⃗B0) ×⃗B0
=⃗
B0 × (ˆk ×⃗B0)
=
ˆk
³⃗
B0 ·⃗B0
´
−⃗B0
³ˆk ·⃗B0
´
=
ˆk|⃗E0|2 .
To go from the 1st line to the 2nd line, I used⃗a×⃗b = −⃗b×⃗a; to go to the 3rd line I used the
vector identity⃗a×(⃗b×⃗c) =⃗b(⃗a·⃗c)−⃗c(⃗a·⃗b). I won’t prove this identity explicitly; it’s simple
(albeit fairly tedious) to prove this in Cartesian coordinates. Finally, to go to the last line I
used the results we just proved about the magnitude of the⃗B ﬁeld and its orthogonality to
ˆk. The punchline is that⃗
E0 ×⃗B0 is parallel to the propagation direction ˆk.
As we shall soon see,⃗E ×⃗B has a separate, very important physical meaning: Up to a
constant,⃗E ×⃗B tells us about the ﬂow of energy that is carried by the radiation. This
makes it very clear that⃗E ×⃗B must be parallel to ˆk!
194
