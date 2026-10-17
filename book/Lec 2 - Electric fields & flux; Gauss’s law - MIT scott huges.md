# Lec 2 - Electric fields & flux; Gauss’s law - MIT scott huges

> Source: `Lec 2 - Electric fields & flux; Gauss’s law - MIT scott huges.pdf`  
> Pages: 12


## Page 1

Scott Hughes
3 February 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 2:
Electric fields & flux; Gauss’s law
2.1
The electric ﬁeld
Last time, we learned that Coulomb’s law plus the principle of superposition allowed us to
write down fairly simple formulas for the force that a “swarm” of N charges exerts on a test
charge Q:⃗
F =
N
X
i=1
Q qi ˆri
r2
i
.
We found another simple formula for the force that a blob of charged material with charge
density ρ exerts on a test charge:⃗
F =
Z Q ρ dV ˆri
r2
i
.
And, of course, similar formulas exist if the charge is smeared out over a surface with surface
density σ, or over a line with line density λ.
In all of these cases, the force ends up proportional to the test charge Q. We might as
well factor it out. Doing so, we deﬁne the electric ﬁeld:⃗
E
≡⃗
F
Q
=
N
X
i=1
qi ˆri
r2
i
(N Point charges)
=
Z ρ dV ˆri
r2
i
(Charge continuum) .
Given an electric ﬁeld, we can ﬁgure out how much force will be exerted on some point
charge q in the obvious way:⃗F = q⃗E.
In cgs units, the electric ﬁeld is measured in units of dynes/esu, or esu/cm2, or stat-
volts/cm — all of these choices are equivalent. (We’ll learn about statvolts in about a week.)
In SI units, ﬁrst of all, we must multiply all of the above formulae by 1/4πϵ0. The units of
electric ﬁeld are then given in Newtons/Coulomb, or Coulomb/meter2, or Volts/meter.
Let’s look at a couple of examples.
2.1.1
Example: Electric ﬁeld at center of charged ring
Take a ring of radius R with uniform charge per unit length λ = Q/2πR. What is the
electric ﬁeld right at its center? Well, if we don’t think about it too carefully, we want to do
something like this:⃗
E =
Z λ ˆr
r2 ds ,
11


## Page 2

where the integral will be take around the ring; ds will be a path length element on the ring,
r is the radius of the ring, and ˆr is a unit vector pointing from each length element on the
ring to the ring’s center ...
But wait a minute! You should quickly notice that for each contribution due to a little
length element on the ring, there is an equal contribution from the ring’s opposite side
pointing in the opposite direction. Each contribution to the⃗E ﬁeld at the center of the ring
is precisely canceled by its opposite contribution:
So the ﬁeld at the center of the ring is zero.
2.1.2
Example: Electric ﬁeld on ring’s axis
Suppose we move along the ring’s axis to some coordinate z above the disk’s center. The
ﬁeld does not cancel in this case, at least not entirely: Considering the contribution of pieces
of the ring, we see that there is a component in the radial direction, and a component along
z. The radial component cancels by the same symmetry argument as we used above. The z
component, however, deﬁnitely does not cancel:
Radius R
Height above ring z
cancels in radial direction, does not
cancel in z direction.
Vectorial contribution to field
θ
So, let’s calculate: the contribution coming from a little segment of the ring is
d⃗E
=
dQ
r2 cos θ ˆz
12


## Page 3

=
λ ds
R2 + z2 cos θ ˆz
=
λ z ds
(R2 + z2)3/2 ˆz .
The length ds represents the length of a little segment of the ring.
Integrating this up
is trivial: we go around the circumference, so the only “action” as far as the integral is
concerned is that we replace ds with 2πR. We end up with⃗
E
=
2πR λ z
(R2 + z2)3/2 ˆz
=
Q z
(R2 + z2)3/2 ˆz .
2.1.3
Example: Electric ﬁeld on disk’s axis
Using that result, it is now simple to work out a more complicated⃗E ﬁeld, that above a
disk. Suppose we have a charge Q smeared out uniformly over a disk of radius R, so that
the charge per unit area σ = Q/πR2. What is⃗E a distance z above the disk?
A simple way to do this is to consider the disk to be made out of an inﬁnite number of
inﬁnitesimally thin rings:
A single ring of radius r and thickness dr carries a total charge dQ = σ 2πr dr. The con-
tribution of that ring to the disk’s electric ﬁeld can be easily ﬁgured using our ring electric
ﬁeld result, replacing R with r and Q with dQ:
d⃗E = σzˆz
2πr dr
(z2 + r2)3/2 .
To get the total ﬁeld, we integrate this from r = 0 to r = R:⃗
E
=
Z R
0 σzˆz
2πr dr
(z2 + r2)3/2
=
2πσˆz
Ã z
√
z2 −
z
√
R2 + z2
!
.
13


## Page 4

Before moving on, it’s useful to consider two limits of this formula. First, consider z large
and positive: this formula can be rewritten⃗
E
=
2πσˆz

1 −
1
q
1 + (R/z)2


≃
2πσˆz
"
1 −
Ã
1 −1
2
R2
z2
!#
=
πR2σˆz
z2
= Q
z2 ˆz .
On the second line we have used z ≫R to expand the square root via the binomial expansion.
The ﬁnal result tells us that, at large z the disk has the same⃗E ﬁeld as a point charge —
which should not be a surprise!
Next consider z very small and not necessarily positive: putting
√
z2 = |z|, we have⃗
E
=
2πσˆz
Ã z
|z| −
z
√
R2 + z2
!
≃
2πσˆz z
|z| .
The function z/|z| = +1 above the disk, and −1 below the disk. Thus, our electric ﬁeld has
constant magnitude, E = 2πσ, and points away from the disk: up on the top side, down on
the bottom. Remember this result — we will see it again soon!
2.2
Electric ﬁeld lines
A useful concept to illustrate the electric ﬁeld is the notion of ﬁeld lines. These are ﬁctitious
lines we sketch which point in the direction of the electric ﬁeld, and whose density gives us
(at least roughly) an idea of how strong the ﬁeld is. Here is a sketch of the electric ﬁeld lines
around a pair of point charges:
+
−
The ﬁeld lines are bunched up near the charges (where the ﬁeld is strongest), and spread
out farther away. They point in towards the minus charge, and away from the plus charge.
Field lines can never cross. If they did, what would the ﬁeld direction be at the crossing
point? It wouldn’t be deﬁned! Sometimes you have situation where it seems like ﬁeld lines
are crossing; it usually turns out the magnitude goes to zero when that happens.
14


## Page 5

2.3
Flux
The notion of ﬂux is an important one in physics. It refers to the ﬂow of some vectorial
quantity through an area. The simplest example to picture is the ﬂow of ﬂuid. Imagine that
ﬂuid is ﬂowing with velocity⃗v = vˆx. Now imagine that we dip a square wire loop of cross
section area A into this ﬂuid. We describe this loop with a vector⃗A = Aˆn, where ˆn is the
normal to the plane of the loop:
Loop, area A
^
Unit normal n
The velocity ﬂux Φv is deﬁned as the overlap between the velocity vector⃗v and the loop
area⃗A:
Φv =⃗v ·⃗A .
For a uniform, plane loop, and constant, uniform velocity⃗v, we have Φv = vA cos θ, where
θ is the angle between ˆn and the velocity vector:
Φ = 
Φ = 
Φ = 
0
v A
v A cos
θ
θ
For this example, the rate of ﬂuid ﬂow through this loop is proportional to this ﬂux, Φv.
What if things aren’t nice and uniform like this? Then, we break the cross sectional area
of the loop up into little squares d⃗A; we assign each square its own normal ˆn. The ﬂux then
becomes an integral:
Φv =
Z⃗
v · d⃗A .
The integral is taken over the entire surface through which we wish to compute the ﬂux.
15


## Page 6

2.4
Electric ﬂux and Gauss’s law (intuitive picture)
The electric ﬂux ΦE (which I’ll usually just write Φ) is just like the velocity ﬂux discussed
above, using the electric ﬁeld⃗E rather than the ﬂuid velocity⃗v:
Φ =
Z
Surface⃗E · d⃗A .
Electric ﬂux has a very nice interpretation in terms of ﬁeld lines.
To motivate this
interpretation, imagine that we have a uniform electric ﬁeld. Let’s calculate the ﬂux through
a square with cross sectional area A:
Uniform electric field
θ
Φ = (⃗E) · (Aˆn) = EA cos θ .
No surprise — it looks just like the velocity ﬂux we discussed above. The cool thing is how
we can interpret this: the electric ﬂux Φ is proportional to the number of ﬁeld lines that pass
through the loop!1 In this case, we can see that when θ = 0 we have the maximum possible
number of ﬁeld lines passing through the loop. The number of lines that can ﬁt decreases as
we tilt the loop until, when θ = π/2, no lines go through.
This interpretation holds perfectly well if we make our surface more complicated: if we
make the surface wiggly,
Edge of wiggly
surface
Uniform electric field
1A reasonable objection to raise at this point is that ﬁeld lines are really ﬁctitious — is the notion that
the number that passes through the loop at all meaningful? The answer is yes, provided that we remember
it is just the proportionality that means anything. We can’t actually calculate the number of ﬁeld lines
passing through the loop without deﬁning some convention for what the density of ﬁeld lines means. Clearly,
though, we can see when the number that ﬂow through is maximum — θ = 0 — and minimum — θ = π/2.
Those statements are independent of any convention deﬁning the ﬁeld lines.
16


## Page 7

the total electric ﬂux found by integrating over this surface still has this interpretation that
it is the number of ﬁeld lines passing through the surface.
A particular interesting and important case is when the surface is closed:
Uniform electric field
Closed surface S
What is the ﬂux that we ﬁnd integrating over the total surface? With our intuitive inter-
pretation, the answer is obvious:
Φ = 0 .
Why?
Just as many ﬁeld lines enter the surface as leave it!
Mathematically, you can
see where this comes from by noting that the unit normal ˆn for each area element d⃗A is
continually pointing in diﬀerent directions as we move over the closed surface. On the left
side of S, it mostly points to the left; on the right, mostly to the right. Summing over all
elements we end up with a net cancellation.
What if we have a closed surface that only has ﬁeld lines entering or leaving? As an
example, imagine that we enclose a point charge q within a spherical surface of radius r:
r
q
The electric ﬂux through this surface is
Φ =
I⃗
E · d⃗A = qˆr
r2 · 4πr2ˆr = 4πq .
(The symbol
H is used for integrals over closed surfaces, or around a closed path, etc.) The
integral was simple to do: since the surface of the sphere is at radius r, the⃗E ﬁeld is constant
there; and, the normal vector is just the radial unit vector ˆr.
17


## Page 8

What if we the surface is not spherical? It turns out we get exactly the same answer!
I’ll derive this carefully in the next section. An intuitive explanation is to use the Gaussian
amoeba. We take an arbitrarily shaped closed surface S containing a charge. We then carve a
sphere out of it, breaking the region up into the “nucleus” and “protoplasm” of our amoeba:
=
+
q
q
q
Flux through S
Flux through
Flux through
S
S
1
2
Notice, in this picture, the orientation of the normals to the various surfaces. The original
surface S has its normals pointing outward, as usual. Normals to the bounding surface of the
“nucleus” S1 also point outward. The bounding surface S2 is a bit wierd: the surface that
abuts the “nucleus” has inward normals; the surface on the outer edge has normal pointing
outward as normal. The inward normal on the inner surface ensures that when we combine
surfaces S1 and S2, the inner bits cancel and only the original surface S is left over.
Whereas the ﬂux through S is hard to compute, the ﬂuxes through S1 and S2 are easy:
Φ1
=
I
S1⃗
E · d⃗A = 4πq
Φ2
=
I
S2⃗
E · d⃗A = 0 .
The ﬁrst result holds because the surface S1 is a sphere, and we can use the ﬂux through a
sphere result we already worked out. The second result holds because the number of ﬁeld
lines entering the surface S2 on the inner edge is exactly equal to the number that leave S2
on the outer edge. The total ﬂux through the surface S is therefore 4πq:
Φ =
I
S⃗E · d⃗A = 4πq .
Just like for a sphere.
What if there’s more than one charge inside S?
We just invoke superposition, and
compute the ﬂux from each individual charge; then we add the result. It’s pretty obvious
what we get:
Φ =
I
S⃗E · d⃗A = 4π
N
X
i=1
qi .
We have just worked out Gauss’s Law: The electric ﬂux Φ through a closed surface S
is equal to the total charge contained inside S. Mathematically, we say
Φ =
I
S⃗E · d⃗A = 4πq(Contained within S) .
18


## Page 9

This is in CGS units; in SI units, the factor 4π becomes 1/ϵ0.
2.5
Gauss’s law: More careful proof
Let’s revisit the Gaussian amoeba and show the ﬂux is 4πq independent of the surface’s
shape a little more carefully. Consider a cone of solid angle dΩthat goes out from the charge
through both the spherical “nucleus” and out to the “real” surface:
θ
r
R
n^
The cone intersects the sphere at radius r; the surface of intersection is a circle whose area
is da = r2 dΩ, oriented parallel to ˆr. The electric ﬂux through this patch is
dΦsphere = qˆr
r2 · r2 dΩˆr = q dΩ.
The cone intersects the outer surface at a radius R. The surface of intersection is a very
small ellipse whose area is R2 dΩ/ cos θ, oriented parallel to ˆn, which is inclined at an angle
θ with respect to ˆr. The electric ﬂux through this patch is
dΦS
=
qˆr
R2 · R2 dΩˆn
cos θ
=
q dΩˆn · ˆr
cos θ
=
q dΩ.
The ﬂuxes through each diﬀerential patch are equal; integrating over the total solid angle
(4π steradians) subtended by each surface, we ﬁnd the same ﬂux: ΦS = Φsphere = 4πq.
The generalization to multiple charges is then simple; Gauss’s law follows.
2.6
Using Gauss’s law
As I hope you’ll come to appreciate, Gauss’s law is our friend: in situations with lots of
symmetry it makes calculating⃗E really easy. The caveat is that it is only useful for this
19


## Page 10

purpose when there’s enough symmetry. Gauss’s law is always true, but it is not always
useful in this way.
The simplest example is the case of spherical symmetry.
2.6.1
Example: Spherical symmetry
Suppose we’ve got some perfectly spherical distribution of charge, with density ρ(r). (Note
that this density is a function of radius.) Enclose this distribution with a spherical surface
S of radius r. Gauss’s law tells us
I
S⃗E · d⃗A = 4πq(inside S) .
Since the ﬁeld is spherically symmetric,⃗E must point in the radial direction:⃗E ∝ˆr. Further,
it can only depend on r, which means that it is constant over any spherical surface. The
integral is thus easy to evaluate:
I
S⃗E · d⃗A = 4πr2E(r) .
The amount of charge contained inside S is given by integrating the charge density ρ(r) over
the volume V contained by S:
q =
Z
V ρ(r) dV .
So,⃗
E(r) =
R
V ρ(r) dV
r2
ˆr = q(r)
r2 ˆr .
Let’s specialize this further: put
ρ(r)
=
ρ
r ≤a
=
0
r > a .
(ρ is a constant.) Then,
q(r)
=
Z
V ρ(r) dV
=
Z r
0 4πρ r2 dr
=
4
3πr3ρ
r ≤a
=
4
3πa3ρ
r > a .
The electric ﬁeld is⃗
E(r)
=
4
3πρ rˆr
r ≤a
=
4πρa3/3
r2
ˆr
r > a .
The electric ﬁeld grows linearly with r inside the sphere, but falls oﬀas 1/r2 outside the
sphere. In fact, the external ﬁeld is exactly that of a point charge q = 4πρa3/3.
20


## Page 11

2.6.2
Example: Spherical symmetry 2
Suppose we’ve got a spherical shell of radius a, and a total charge q is distributed over the
shell, so that the charge per unit area on the shell is σ = q/4πa2. What is the electric ﬁeld
in this case?
a
Consider two Gaussian surfaces, one at r < a, one at r > a. For r < a, we have
4πr2E(r) = 4πq(r < a) = 0
→E(r) = 0
r < a .
There is no electric ﬁeld anywhere inside the shell! On the outside, we have
4πr2E(r) = 4πq(r > a) = 4πq
→E(r) = q
r2
r > a .
Outside, it looks just like a point charge sitting at the origin! The exterior of spherical charge
distributions always look just like point charges at the origin.
Notice that, as we go from just barely inside the shell to just barely outside the shell, the
electric ﬁeld jumps suddenly:
∆E = q
a2 −0 = 4πa2σ
a2
= 4πσ .
This discontinuous jump ∆E = 4πσ as we “cross” a sheet of charge per unit area σ is a
general feature of such charge distributions. We see it in another example:
21


## Page 12

2.6.3
Example: Inﬁnite sheet
Suppose we have a sheet of charge, lying in the (x, y) plane, and stretching out all the way
to inﬁnity. What is the electric ﬁeld a distance z away from this sheet?
One way to do this would be to use the calculation of the disk we did earlier on, and
take the limit R →∞. Here, we’ll use Gauss’s law: we make a “Gaussian pillbox” around
the sheet like so:
Disk has cross section
area A
z
z
E(z)
E(z)
Now, we think about the symmetry of the problem to ﬁgure out what Gauss’s law tells us.
The electric ﬁeld cannot depend on our horizontal position — the sheet is the same in all
directions, so all horizontal positions are identical. The ﬁeld must also point either out (if
it is positive charged) or in (negative). Finally, there can be no ﬂux through the sides of
the pillbox — the ﬁeld can only point straight out by the planar symmetry. (If it did not,
imagine rotating the plane — the ﬁeld would change direction. That contradicts the notion
that it is the same everywhere.) Gauss’s law reduces to
Φ = 2AE(z) .
The total charge contained inside the pillbox is σA, so we ﬁnd
E(z) = 2πσ .
Notice three things here: ﬁrst, this is the same ﬁeld we found for the disk when z was very
small. When we get extremely close to something like a disk, the inﬁnite sheet calculation is
approximately the electric ﬁeld — essentially, you get so close that you can’t “see” the edges
of the disk, and it acts as though it were inﬁnite. Second, this electric ﬁeld is independent
of distance —⃗E is uniform all through space. Third, we see once again that, when we cross
a sheet of uniform charge density, the change in the electric ﬁeld is 4πσ. In this case, it is
2πσ pointing down below, and 2πσ pointing up above.
22
