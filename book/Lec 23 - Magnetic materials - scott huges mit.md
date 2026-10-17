# Lec 23 - Magnetic materials - scott huges mit

> Source: `Lec 23 - Magnetic materials - scott huges mit.pdf`  
> Pages: 6


## Page 1

Scott Hughes
10 May 2005
Massachusetts Institute of Technology
Department of Physics
8.022 Spring 2005
Lecture 23:
Magnetic materials
23.1
Magnetic ﬁelds and stuﬀ
At this stage of 8.022, we have essentially covered all of the material that is typically taught
in this course. Congratulations — you now have a solid grounding in all the major concepts
of electricity and magnetism!
There remains one major, important subject which we have not discussed in depth: the
interaction of magnetic ﬁelds and materials. At this point, we don’t even have a really good
understanding of a bar magnet works — an unsatisfying state of aﬀairs, given that this is
the way in which we normally encounter magnetism in the real world!
One reason we have avoided covering this subject is that it is not really possible to discuss
it properly within getting into a detailed discussion of the quantum mechanical description
of matter. The way in which matter responds to magnetic ﬁelds is totally determined by the
quantum mechanical nature of their molecular structure, particularly their electrons.
Nonetheless, we can make signiﬁcant headway in understanding the interaction of mag-
netic ﬁelds and materials by combining what we have learned so far with a somewhat ap-
proximate, qualitative description of how materials respond to magnetic ﬁelds. The main
concepts we will need are summarized in the following two subsections:
23.1.1
Electron orbitals
The electrons in a molecule exist in orbits. Very roughly, we can picture an orbit as a simple
loop of current:
A loop of current like this of course tends to generate its own magnetic ﬁeld.
In most
materials, there are an enormous number of orbits like this, randomly oriented so that they
produce no net ﬁeld. Suppose an external magnetic ﬁeld is applied to some substance that
contains many orbitals like this. The net tendency can be understood in terms of Lenz’s
law: the orbits “rearrange” themselves in order to oppose the change in magnetic ﬂux. This
tendency for Lenz’s law to work on the microscopic scale ends up opposing the magnetic ﬁeld
from the material.
23.1.2
Intrinsic magnetic moment of the electron
One other quantum mechanical property of electrons plays an extremely important role in
this discussion: electrons have a built-in, intrinsic magnetic moment. Roughly speaking,
214


## Page 2

this means that each electron all on its own acts as a source of magnetic ﬁeld, producing a
dipole-type ﬁeld very similar to that of current loop.
Because this ﬁeld is associated with the electron itself, it does not exhibit the Lenz’s law
type behavior of the ﬁeld that we see from the orbits. Instead, the most important behavior
in this context is the fact that a magnetic moment⃗m placed in an external ﬁeld⃗B feels a
torque:⃗
N =⃗m ×⃗B .
In this case, the action of this torque tends to line up the electrons’ magnetic moments with
the external ﬁeld. In this case, you ﬁnd that the magnetic ﬁeld is augmented within the
material.
23.1.3
Which wins?
To summarize the above discussion, the quantum mechanical nature of electrons in molecules
leads to two behaviors:
• Lenz’s law on the scale of electron orbitals opposes magnetic ﬁelds from entering a
material.
• Magnetic torque acting on the individual electrons augments magnetic ﬁelds in a ma-
terial.
These two behaviors are in complete opposition to one another! However, both occur, and
both are important. A natural question to ask is: Which of these two behaviors is more
important?
The answer to this question varies from material to material, depending upon its detailed
electronic orbital structure. The ﬁrst property — Lenz’s law on the orbital scale — plays
some role in all materials.
In many cases, this is the end of the story.
Such materials
are called diamagnetic. A diamagnetic material is one whose magnetization (to be deﬁned
precisely in a moment) opposes an external magnetic ﬁeld. Even though almost all materials
are diamagnetic, the eﬀect is so puny that it is typically very diﬃcult to see. A consequence
of this is that a diagmagnetic substance will be expelled from a magnetic ﬁeld.
For some materials, the second property — alignment of electron magnetic moments
— wins out. Such materials typically have several electron orbits that contain unpaired
electrons; the orbit thus has a net magnetic moment. (In most diamagnetic materials, the
orbits are ﬁlled with paired electrons, so that the orbit has no net moment1.) Such materials
are called paramagnetic. A paramagnetic material has a magnetization that augments an
external ﬁeld. Paramagnetic substances are pulled into a magnetic ﬁeld. In the vast majority
of cases, paramagnetic eﬀects are also so puny that they can barely be seen2.
One particular class of materials acts essentially as paramagnetic materials do. However,
they respond so strongly that they truly belong in a class of their own.
These are the
ferromagnetic materials.
1Bear in mind that this is a highly qualitative discussion!
2There are some interesting exceptions.
Oxygen, O2, turns out to be paramagnetic.
However, the
random motion of gaseous oxygen wipes out any observable eﬀect. If we cool it to a liquid state, though,
the paramagnetism is easily seen.
215


## Page 3

23.2
Some deﬁnitions
A couple of deﬁnitions are needed to describe what we are going to discuss. Foremost is the
magnetization⃗M: the magnetic dipole moment per unit volume of a material. Notice that
magnetization has the same dimensions as magnetic ﬁeld:⃗
M
=
magnetic moment
volume
=
current × area/velocity
length3
=
current/velocity
length
.
A material with constant magnetization⃗M and volume V acts just like a magnetic dipole
with⃗m =⃗M V .
The second important deﬁnition is a bit of a wierd one: it is a new kind of magnetic
ﬁeld denoted⃗H.
This⃗H is deﬁned in terms of the “normal” magnetic ﬁeld⃗B and the
magnetization⃗M via⃗
B =⃗H + 4π⃗M .
In other words, when there is no magnetization, the “normal” magnetic ﬁeld⃗B is just this
new ﬁeld⃗H. This means that⃗H is nothing more than the bit of the magnetic ﬁeld that
arises from “normal” electric currents, as opposed to those that are “bound” in matter.
23.2.1
More details on⃗H
We can do some more stuﬀwith⃗H, though this is really beyond the scope of what we need
for our discussion. If we take the curl of⃗H, we get⃗
∇×⃗H = 4π
c⃗Jfree
where Jfree is the density of free electrical current. The curl of the magnetization deﬁnes
bound currents:⃗
∇×⃗M =⃗Jbound/c .
Putting these together, we have⃗
∇×⃗B
=⃗
∇×⃗H + 4π⃗∇×⃗M
=
4π
c⃗Jfree + 4π
c⃗Jbound
=
4π
c⃗J .
In other words, the total current density is given by adding the free current density (the
current due to moving charges that we can imagine controlling) and the bound current density
(the current that is “bound up” in electron orbits, and is really a part of the material).
216


## Page 4

23.3
Magnetic susceptibility
A wide variety of materials exhibit linear magnetization, meaning that the magnetization⃗M
depends linearly on the ﬁeld⃗H:⃗
M = χm⃗H .
The quantity χm is the magnetic susceptibility. From this, we have⃗
B =⃗H (1 + 4πχm) .
If χm < 0, the magnetic ﬁeld is decreased by the material. This corresponds to diamag-
netism. If χm > 0, the magnetic ﬁeld is increased by the material. This corresponds to
paramagnetism.
23.4
Ferromagnetism
Roughly speaking, ferromagnetism is paramagnetism on steroids. Its key feature is that it
is nonlinear: the⃗M and⃗H do not have a simple linear relation between one another. This
leads to some surprising results. In particular, it means that once the “external” ﬁeld⃗H
is turned oﬀ, the magnetization⃗M remains! This of course is how permanent magnets are
made.
The reasons for this nonlinear behavior are surprisingly complicated, and are diﬃcult to
explain correctly in a simple manner. (It is ironic that permanent magnets, probably the
most familiar manifestation of magnetism, turn out to be so diﬃcult to explain!) It isn’t so
hard to describe the most important facets of ferromagnetism qualitatively; the hard part is
explaining why those qualitative behaviors emerge. That, sadly, is far beyond the scope of
8.022.
23.4.1
Ferromagnetic domains
Since ferromagnetism is conceptually a lot like paramagnetism, we expect that it will be
explainable in terms of the alignment of many atomic scale magnetic moments.
This is
indeed the case. However, with ferromagnetism there is an important modiﬁcation: one
ﬁnds that the moments of many atoms or molecules tend to be aligned in small regions.
In “normal” paramagnetic materials, the moments are randomly arranged until an external
ﬁeld comes along and aligns them.
If you were to look at the magnetic moment layout of a typical ferromagnetic materials,
you would ﬁnd something like this:
217


## Page 5

Enough atomic scale moments are aligned that deﬁnite regions or domains of magnetization
exist. Each domain is fairly small, and each is randomly oriented with respect to its neighbor;
the material as a whole has no net magnetization. This is why a random piece of iron (a
representative ferromagnetic material) is usually not magnetized.
If this material is placed into a strong enough external magnetic ﬁeld, the domains are
re-aligned so that they all point in the same direction:
Once the external magnetic ﬁeld is removed, it turns out to be energetically favorable for
these domains to remain pointing in this direction. The domains are ﬁxed with this magne-
tization. This is how permanent magnets are made.
23.4.2
Hysteresis
The nonlinear relationship between⃗H and⃗B means that the magnetic ﬁeld⃗B in a ferro-
magnetic material has a rather complicated dependence on the “external” applied ﬁeld⃗H.
As⃗H is varied between a minimum and a maximum, one ﬁnds that⃗B in the material traces
out an interesting shape called a hysteresis curve:
218


## Page 6

Notice that when H = 0, B̸ = 0 — reﬂecting the fact that the material has been given a
permanent magnetization. You may wonder looking at this plot which of the two possible
values it will take — the positive B or the negative one? The answer depends on the history
of the magnetization. If H was large and positive most recently, B will go to the positive
value when H is set to zero. If H was large and negative, B will go to the negative value.
It turns out (though it’s a bit beyond the scope of this course to show this) that it takes
work to “go around” the hysteresis curve. As we go from +H to −H, we have to ﬂip lots
of magnetic domains around — it takes energy to do that! The amount of work that is
done in going from +H →−H →+H is proportional to the area of the hysteresis curve.
One consequence of this is that solenoids with an iron core can be very lossy elements in
AC circuits. An AC circuit is continually changing the direction of ﬂow of the current, and
hence of the⃗H ﬁeld. If a portion of the circuit contains a ferromagnet, some of the power
put into the circuit will be lost by continually changing the orientation of the ferromagnet’s
domains.
23.4.3
Curie temperature
No discussion of ferromagnetism is complete without mentioning the Curie temperature. The
Curie temperature, TC, is a temperature above which a material very suddenly ceases to act
like a ferromagnetic. If the temperature is above TC, the random motion of the magnetic
moments is so strong that they can never become aligned. Just a tiny bit below, though,
and they can align! It’s somewhat amazing how strong the transition is at this temperature.
For iron, TC = 770◦Celsius.
219
