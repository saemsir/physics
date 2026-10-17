# Lec 19 - Displacement current. Maxwell’s equations. Scott huges mit

> Source: `Lec 19 - Displacement current. Maxwell’s equations. Scott huges mit.pdf`  
> Pages: 9


## Page 1

Scott Hughes
26 April 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 19:
Displacement current. Maxwell’s equations.
19.1
Inconsistent equations
Over the course of this semester, we have derived 4 relationships between the electric and
magnetic ﬁelds on the one hand, and charge and current density on the other. They are:
Gauss’s law:⃗
∇·⃗E = 4πρ
Magnetic law:⃗
∇·⃗B = 0
Faraday’s law:⃗
∇×⃗E = −1
c
∂⃗B
∂t
Ampere’s law:⃗
∇×⃗B = 4π⃗J
c
As written, these equations are slightly inconsistent. We can see this inconsistency very
easily — we just take the divergence of both sides of Ampere’s law. Look at the left hand
side ﬁrst:
Left hand side:⃗
∇·
³⃗
∇×⃗B
´
= 0 .
This follows from the rule that the divergence of the curl is always zero (as you proved on
pset 3). Now look at the right hand side:
Right hand side:⃗
∇·

4π⃗J
c

= −4π
c
∂ρ
∂t .
Here, I’ve used the continuity equation,⃗∇·⃗J = −∂ρ/∂t.
Ampere’s law is inconsistent with the continuity equation except when ∂ρ/∂t = 0!!! A
charge density that is constant in time is actually a fairly common circumstance in many
applications, so it’s not too surprising that we can go pretty far with this “incomplete”
version of Ampere’s law. But, as a matter of principle — and, as we shall soon see, of
practice as well — it’s just not right. We need to ﬁx it somehow.
19.2
Fixing the inconsistency
We can ﬁx up this annoying little inconsistency by inspired guesswork. When we take the
divergence of Ampere’s left hand side, we get zero — no uncertainty about this whatsoever,
it’s just ZERO. We should be able to add a function to the right hand side such that the
divergence of the right side is forced to be zero as well.
Let’s suppose that our “generalized Ampere’s law” takes the form⃗
∇×⃗B = 4π⃗J
c
+⃗F .
177


## Page 2

Our goal now is to ﬁgure out what⃗F must be. Taking the divergence of both sides, we ﬁnd
0
=
4π⃗∇·⃗J
c
+⃗∇·⃗F
−→⃗∇·
³
c⃗F
´
=
4π∂ρ
∂t .
Our mystery function has the property that when we take its divergence (and multiply by
c), we get the rate of change of charge density.
This looks a lot like Gauss’s law! If we take the time derivative of Gauss’s law, we have
∂
∂t⃗∇·⃗E
=
4π∂ρ
∂t
−→4π∂ρ
∂t
=⃗
∇·

∂⃗E
∂t


On the last line, I’ve use the fact that it is OK to exchange the order of partial derivatives:
∂
∂t⃗∇
=
ˆx ∂
∂t
∂
∂x + ˆy ∂
∂t
∂
∂y + ˆz ∂
∂t
∂
∂z
=
ˆx ∂
∂x
∂
∂t + ˆy ∂
∂y
∂
∂t + ˆz ∂
∂z
∂
∂t
=⃗
∇∂
∂t .
(This actually works in any coordinate system; Cartesian coordinates are good enough to
demonstrate the point.)
Substituting in for 4π ∂ρ/∂t, we have⃗
∇·
³
c⃗F
´
=⃗∇·

∂⃗E
∂t


which tells us⃗
F = 1
c
∂⃗E
∂t .
Ampere’s law becomes⃗
∇×⃗B = 4π⃗J
c
+ 1
c
∂⃗E
∂t .
Substituting this in with our other equations yields the Maxwell equations:
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
∇×⃗B = 4π⃗J
c
+ 1
c
∂⃗E
∂t .
178


## Page 3

It was James Clerk Maxwell who ﬁrst ﬁxed this inconsistency and argued that the ∂⃗E/∂t
term must be present in Ampere’s law. Interestingly, he did not argue this on the basis of
continuity, but rather purely on the grounds of symmetry. We’ll return to this point later.
You should also be aware of the form of these equations in SI units1 — all those cs and
4πs are replaced with various combinations of µ0s and ϵ0s:
Gauss’s law:⃗
∇·⃗E = ρ
ϵ0
Magnetic law:⃗
∇·⃗B = 0
Faraday’s law:⃗
∇×⃗E = −∂⃗B
∂t
Generalized Ampere’s law:⃗
∇×⃗B = µ0⃗J + µ0ϵ0
∂⃗E
∂t .
These four equations completely summarize 8.022.
Every phenomenon in electricity and
magnetism can be derived from these equations.
Many of our most important tools for
various analyses come from the integral version of these equations, which we will discuss
shortly.
19.3
The displacement current
What does this new term mean? It turns out that it actually has a very nice, physical
interpretation. We can begin to understand this using the old trick of dimensional analysis:
electric ﬁeld has the units of (charge)/(length)2. The rate of change of electric ﬁeld has units
of (charge)/[(time)(length)2]. This is the same thing as (current)/(length)2, which is current
density. The generalized Ampere’s law is thus often written⃗
∇×⃗B = 4π
c
³⃗
J +⃗Jd
´
where⃗
Jd = 1
4π
∂⃗E
∂t
is known as the displacement current, or, more correctly, the displacement current density.
The displacement current is not a “real” current, in the sense that it does not describe
charges ﬂowing through some region. However, it acts just like a real current. Whenever we
have a changing⃗E ﬁeld, we can treat its eﬀects as due to the displacement current density
arising from that ﬁeld’s variations.
1Note that there’s a serious typo in Purcell’s listing of these equations in SI units, Eq. (15’) of Chapter 9.
179


## Page 4

In particular, the displacement current helps to ﬁx up a few subtleties in circuits that
might have bothered you. (I know for a fact that some students have wondered about these
issues, and have asked some very good questions!) Consider a current ﬂowing down a wire
and charging up a capacitor:
+
+
+
+
+
−
−
−
−
−
The old integral formulation of Ampere’s law (which can be derived from the diﬀerential
form) tells us
I
C⃗B · d⃗s
=
4π
c Iencl
Iencl
=
Z
S⃗J · d⃗a .
In words, the line integral of the magnetic ﬁeld around a closed contour C equals 4π/c times
the current enclosed by that contour. The current enclosed by that contour is given by
integrating the ﬂux of the current density through a surface S which is bounded by C.
We’ve normally used this law in the following way: we make a little “Amperian loop”
around one of our wires. The contour C is this loop; the surface S is the disk for which S is
the border:
+
+
+
+
+
−
−
−
−
−
Contour C
Surface
(hashed region)
S
The current Iencl is then just the current I ﬂowing into the capacitor. Nice, simple, logical.
180


## Page 5

We now make this complicated. To go between the diﬀerential form of Ampere’s law and
this integral form of it, we use Stoke’s theorem. A key fact of using this theorem is that the
surface S can be ANY surface that has C as its boundary. In particular, we can choose this
surface, S′:
+
+
+
+
+
−
−
−
−
−
Contour C
Surface S’
The amount of current ﬂowing through this surface is ZERO: no charge ﬂows between the
plates! However, there is a ﬂux of displacement current between the plates. When we turn
our “generalized Ampere’s law” into an integral form, we get
I
C⃗B · d⃗s
=
4π
c (Iencl + Id, encl)
where
Id, encl
=
Z
S⃗Jd · d⃗a
=
1
4π
Z
S
∂⃗E
∂t · d⃗a
=
1
4π
∂
∂t
Z
S⃗E · d⃗a
=
1
4π
∂ΦE
∂t
.
The displacement current ﬂowing through a surface S (as opposed to the displacement
current density) is simply related to the rate of change of electric ﬂux through that surface.
It is simple to show that, for the goofy surface S′ drawn above, this rate of change of
electric ﬂux is exactly what we need to ﬁx up Ampere’s law. First, note that the electric
ﬁeld between the plates points in the same direction as the current; call that direction ˆx.
At any given instant, the electric ﬁeld between the plates (approximating it to be perfectly
181


## Page 6

uniform) is given by⃗
E = 4πQ
A ˆx
where A is the area of the plates. The electric ﬂux between the plates is
ΦE = 4πQ
— not too surprising, given Gauss’s law! The rate of change of this ﬂux is
∂ΦE
∂t
= 4π∂Q
∂t = 4πI .
(Since we are charging up this capacitor, I = dQ/dt = ∂Q/∂t. Partial derivatives and total
derivatives are the same since the charge only depends on time.) The displacement current
“ﬂowing” between the plates is thus
Id, encl = 1
4π
∂ΦE
∂t
= I .
This tells us that
Z
S⃗J · d⃗a =
Z
S′⃗Jd · d⃗a = I .
No matter which surface we use, we ﬁnd
I
C⃗B · d⃗s = 4πI
c
.
That’s good!
Before moving on, note that the displacement current ﬁxes up a somewhat bizarre aspect
of circuits with capacitors that I know had some people a tad confused. When we analyze a
circuit like this,
R
s
C
Vb
we claim that the same current I(t) ﬂows through all the circuit elements. However, we
know that this cannot be totally true — there is no way for “real” current to make it across
182


## Page 7

the plates of the capacitor. However, displacement current certainly makes it across! The
displacement current plays the role of continuing2 the “real” current through the gap in the
capacitor. As such, it plays a very important role in ensuring that our use of Kirchhoﬀ’s
laws is valid.
19.3.1
Integral form of Maxwell’s equations
To wrap this section up, let’s write down the four Maxwell equations in integral form. These
are easily derived by plugging the diﬀerential forms into integrals and invoking various vector
theorems; hopefully, such manipulations are close to second nature for you now.
Gauss’s law:
ΦE(S) =
I
S⃗E · d⃗a = 4πQencl .
In words: The electric ﬂux through a closed surface S equals 4π times the charge
enclosed by S.
Magnetic Gauss’s law:
ΦB(S) =
I
S⃗B · d⃗a = 0 .
In words: The magnetic ﬂux through a closed surface S equals 0.
We’ve never
actually derived this, but it follows quite naturally from our earlier discussion of Gauss’s law
(no magnetic point charges!) and the rule⃗∇·⃗B = 0.
Faraday’s law:
E =
I
C⃗E · d⃗s = −1
c
∂ΦB
∂t
= −1
c
∂
∂t
Z
S⃗B · d⃗a .
In words: The EMF induced around a closed contour C equals −1/c times the rate
of change of the magnetic ﬂux through the surface S bounded by C.
Generalized Ampere’s law:
I
C⃗B · d⃗s = 4π
c (I + Id)
where
I =
Z
S⃗J · d⃗a
Id =
Z
S⃗Jd · d⃗a = 1
4π
∂ΦE(S)
∂t
.
In words: The line integral of the magnetic ﬁeld around a closed contour C equals
4π/c times the sum of the total current — real plus displacement — passing
through that contour.
2Indeed, in many older textbooks, the phrase “continuation current” is found instead of displacement
current, reﬂecting the fact it continues the real current.
183


## Page 8

19.4
Example: Using the displacement current
The beautiful thing about the displacement current is that we can now treat it just like a
regular current. Consider this example: suppose we have an RC circuit, and we charge up
the capacitor:
R
s
C
Vb
As the capacitor charges up, a displacement current ﬂows between the plates. As a conse-
quence, a magnetic ﬁeld is induced between the plates, in addition to the electric ﬁeld that
is building up. We’ll now calculate this magnetic ﬁeld.
The key thing we need is the electric ﬁeld between the plates as a function of time. To
keep things simple, let’s assume the plates are circular, with radius a, and we’ll assume that
they are close enough that we can ignore edge eﬀects. Then, the electric ﬁeld between the
plates as a function of time is
E(t) = 4πQ(t)
πa2
.
The displacement current density is
Jd(t)
=
1
4π
∂E
∂t =
1
πa2
∂Q
∂t
=
I(t)
πa2 .
Note that this is spatially constant, though it varies with time.
This circuit is something we beat to death long ago, so we can just quote the results for
the current we found then:
I(t) = Vb
R e−t/RC .
We’re now ready to compute magnetic ﬁelds inside the plates. Since no “real” current
ﬂows there, our generalized Ampere’s law reduces to
I
C⃗B · d⃗s = 4π
c
Z
S⃗Jd · d⃗a .
184


## Page 9

Let’s pick as our contour C a circular path of radius r < a; the simplest surface S is then
the disk of radius r. Then,
I
C⃗B · d⃗s = 2πrB(r) .
For the right hand side, we need
4π
c
Z
S⃗Jd · d⃗a = 4πI(t)r2
ca2
.
The magnetic ﬁeld is thus
B(r) = 2rI(t)
ca2
= 2rVb
cRa2e−t/RC .
Direction is of course given by right-hand rule: point your right thumb parallel to⃗Jd and
your ﬁngers curl in the same sense⃗B.
19.5
Source-free Maxwell’s equations
As we shall see shortly, an extremely important limit of Maxwell’s equations is found when
there are no sources: ρ = 0,⃗J = 0. The equations become⃗
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
These equations are almost perfectly symmetric! Indeed, when Maxwell ﬁrst introduced the
new term in the “generalized Ampere’s law”, this was his major motivation: he felt that
there must be an underlying symmetry between electric and magnetic ﬁelds. It is a mark of
his remarkable insight that this feeling was entirely correct.
Even more signiﬁcantly, these equations point to an extremely interesting and important
coupling between the magnetic and electric ﬁelds. If we imagine we have a time varying
electric ﬁeld, this shows that it will “source” some kind of magnetic ﬁeld. That magnetic
ﬁeld will be time varying, and so it will source an electric ﬁeld. That electric ﬁeld will then
source a magnetic ﬁeld, which will source an electric ﬁeld, which will ...
You get the point. We end up with an inﬁnite chain of electric to magnetic to electric to
... This is radiation. It will be our next major topic.
185
