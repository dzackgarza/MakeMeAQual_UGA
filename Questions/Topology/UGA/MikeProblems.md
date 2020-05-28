# General Topology

## 1 (Spring '06). 
Suppose $(X, d)$ is a metric space. State criteria for continuity of a function $f : X \to X$ in terms of:

i. open sets;

ii. $\eps$'s and $\delta$'s; and

iii. convergent sequences.

Then prove that (iii) implies (i).

## 2 (Spring '12). 
Let $X$ be a topological space.

i. State what it means for $X$ to be compact.

ii. Let $X = \theset{0} \cup \theset{{1\over n} \mid n \in \ZZ^+ }$. Is $X$ compact?

iii. Let $X = (0, 1]$. Is $X$ compact?

## 3 (Spring '09). 
Let $(X, d)$ be a compact metric space, and let $f : X \to X$ be an isometry: 
$$\forall~ x, y \in X, \qquad d(f (x), f (y)) = d(x, y).$$
Prove that $f$ is a bijection.

## 4 (Spring '05). 
Suppose $(X, d)$ is a compact metric space and $U$ is an open covering of $X$. 

Prove that there is a number $\delta > 0$ such that for every $x \in X$, the ball of radius $\delta$ centered at $x$ is contained in some element of $U$.

## 5 (Fall '11). 
Let $X$ be a topological space, and $B \subset A \subset X$. 
Equip $A$ with the subspace topology, and write $\cl_X (B)$ or $\cl_A (B)$ for the closure of $B$ as a subset of, respectively, $X$ or $A$. 

Determine, with proof, the general relationship between $\cl_X (B) \cap A$ and $\cl_A (B)$ 

> I.e., are they always equal? Is one always contained in the other but not conversely? Neither?

## 6 (Fall '05). 
Prove that the unit interval $I$ is compact. Be sure to explicitly state any properties of $\RR$ that you use.

## 7 (Fall '06). 
A topological space is **sequentially compact** if every infinite sequence in $X$ has a convergent subsequence. 

Prove that every compact metric space is sequentially compact.

## 8 (Fall '10). 
Show that for any two topological spaces $X$ and $Y$ , $X \cross Y$ is compact if and only if both $X$ and $Y$ are compact.

## 9 (Spring '13). 
Recall that a topological space is said to be **connected** if there
does not exist a pair $U, V$ of disjoint nonempty subsets whose union is $X$.

i.  Prove that $X$ is connected if and only if the only subsets of $X$ that are both open and closed are $X$ and the empty set.

ii. Suppose that $X$ is connected and let $f : X \to \RR$ be a continuous map. 
    If $a$ and $b$ are two points of $X$ and $r$ is a point of $\RR$ lying between $f (a)$ and $f (b)$ show that there exists a point $c$ of $X$ such that $f (c) = r$.

## 10 (Fall '05). 
Let 
$$
X = \theset{(0, y) \mid - 1 \leq y \leq 1} \cup \theset{\qty{x, s = \sin\qty{1 \over x}} \mid 0 < x \leq 1}
.$$

Prove that $X$ is connected but not path connected.

## 11 (Fall '18). 
Let
\begin{align*}
X=\left\{(x, y) \in \mathbb{R}^{2} | x>0, y \geq 0, \text { and } \frac{y}{x} \text { is rational }\right\}
\end{align*}
and equip $X$ with the subspace topology induced by the usual topology on $\RR^2$.

Prove or disprove that $X$ is connected.

## 12 (Spring '06). 
Write $Y$ for the interval $[0, \infty)$, equipped with the usual topology. 

Find, with proof, all subspaces $Z$ of $Y$ which are retracts of $Y$.

## 13 (Fall '06).
a. Prove that if the space $X$ is connected and locally path connected then $X$ is path connected.

b. Is the converse true? Prove or give a counterexample.

## 14 (Fall '07). 
Let $\theset{X_\alpha \mid \alpha \in A}$ be a family of connected subspaces of a space $X$ such that there is a point $p \in X$ which is in each of the $X_\alpha$.

Show that the union of the $X_\alpha$ is connected.

## 15 (Fall '04). 
Let $X$ be a topological space.

a.  Prove that $X$ is connected if and only if there is no continuous
    nonconstant map to the discrete two-point space $\theset{0, 1}$.

b.  Suppose in addition that $X$ is compact and $Y$ is a connected Hausdorff space. 
    Suppose further that there is a continuous map $f : X \to Y$ such that 
    every preimage $f\inv (y)$ for $y \in Y$, is a connected subset of $X$. 

    Show that $X$ is connected.

c.  Give an example showing that the conclusion of (b) may be false if
    $X$ is not compact.

## 16 (Spring '10). 
If $X$ is a topological space and $S \subset X$, define in terms of
open subsets of $X$ what it means for $S$ **not** to be connected. 

Show that if $S$ is not connected there are nonempty subsets $A, B \subset X$ 
such that 
$$
A \cup B = S \qtext{and} A \cap \bar B = \bar A \cap B = \emptyset
$$ 

> Here $\bar A$ and $\bar B$ denote closure with respect to the topology on the ambient space $X$.

## 17 (Spring '11). 
A topological space is **totally disconnected** if its only connected subsets are one-point sets. 

Is it true that if $X$ has the discrete topology, it is totally disconnected? 

Is the converse true? Justify your answers.

## 18 (Fall '07). 
Prove that if $(X, d)$ is a compact metric space, $f : X \to X$ is a
continuous map, and $C$ is a constant with $0 < C < 1$ such that 
$$
d(f (x), f (y)) \leq C \cdot d(x, y) \quad \forall x, y
,$$ 
then $f$ has a fixed point.

## 19 (Spring '15). 
Prove that the product of two connected topological spaces is connected.

## 20 (Fall '14). 
a. Define what it means for a topological space to be:

    i. **Connected**

    ii. **Locally connected**

b. Give, with proof, an example of a space that is connected but not locally connected.

## 21 (Fall '14). 
Let $X$ and $Y$ be topological spaces and let $f : X \to Y$ be a function. 

Suppose that $X = A \cup B$ where $A$ and $B$ are closed subsets, and that
the restrictions $f \mid_A$ and $f \mid_B$ are continuous (where $A$ and $B$ have the subspace topology). 

Prove that $f$ is continuous.

## 22 (Fall '18). 
Let $X$ be a compact space and let $f : X \times R \to R$ be a continuous function such that $f (x, 0) > 0$ for all $x \in X$. 

Prove that there is $\eps > 0$ such  that $f (x, t) > 0$ whenever $\abs t < \eps$. 

Moreover give an example showing that this conclusion may not hold if $X$ is not assumed compact.

## 23 (Spring '15). 
Define a family $\mct$ of subsets of $\RR$ by saying that $A \in T$ is $\iff A = \emptyset$ or $\RR \setminus A$ is a finite set. 

Prove that $\mct$ is a topology on $\RR$, and that $\RR$ is compact with respect to this topology.

## 24 (Spring '16). 
In each part of this problem $X$ is a compact topological space.

Give a proof or a counterexample for each statement.

a. If $\theset{F_n }_{n=1}^\infty$ is a sequence of nonempty *closed* subsets of $X$ such that $F_{n+1} \subset F_{n}$ for all $n$ then $$\intersect^\infty_{n=1} F_n\neq \emptyset.$$

b. If $\theset{O_n}_{n=1}^\infty$ is a sequence of nonempty *open* subsets of $X$ such that $O_{n+1} \subset O_n$ for all $n$ then $$\intersect_{n=1}^\infty O_{n}\neq \emptyset.$$


## 25 (Fall '16). 
Let $\mcs, \mct$ be topologies on a set $X$.
Show that $\mcs \cap \mct$ is a topology on $X$. 

Give an example to show that $\mcs \cup \mct$ need not be a topology.

## 26 (Fall '17). 
Let $f : X \to Y$ be a continuous function between topological spaces. 

Let $A$ be a subset of $X$ and let $f (A)$ be its image in $Y$ . 

One of the following statements is true and one is false. 
Decide which is which, prove the true statement, and provide a counterexample to the false statement:

1. If $A$ is closed then $f (A)$ is closed.

2. If $A$ is compact then $f (A)$ is compact.

## 27 (Fall '17). 
A metric space is said to be **totally bounded** if for every $\eps > 0$ there exists a finite cover of $X$ by open balls of radius $\eps$.

a. Show: a metric space $X$ is totally bounded iff every sequence in $X$ has a Cauchy subsequence.

b. Exhibit a complete metric space $X$ and a closed subset $A$ of $X$ that is bounded but not totally bounded. 

> You are not required to prove that your example has the stated properties.

## 28 (Spring '19). 
Is every complete bounded metric space compact? 

If so, give a proof; if not, give a counterexample.

## 29 (Fall '14). 
Is every product (finite or infinite) of Hausdorff spaces Hausdorff?

If yes, prove it. If no, give a counterexample.

## 30 (Spring '18). 
Suppose that $X$ is a Hausdorff topological space and that $A \subset X$. 

Prove that if $A$ is compact in the subspace topology then $A$ is closed as a subset of X.

## 31 (Spring '09). 
a. Show that a continuous bijection from a compact space to a Hausdorff space is a homeomorphism.

b. Give an example that shows that the "Hausdorff" hypothesis in part (a) is necessary.

## 32 (Fall '14). 
Let $X$ be a topological space and let
$$
\Delta = \theset{(x, y) \in X \times X \mid x = y}
.$$

Show that $X$ is a Hausdorff space if and only if $\Delta$ is closed in $X \times X$.

## 33 (Fall '06). 
If $f$ is a function from $X$ to $Y$ , consider the graph 
$$
G = \theset{(x, y) \in X \times Y \mid f (x) = y}
.$$

a. Prove that if $f$ is continuous and $Y$ is Hausdorff, then $G$ is a closed subset of $X \times Y$.

b. Prove that if $G$ is closed and $Y$ is compact, then $f$ is continuous.

## 34 (Fall '04). 
Let X be a noncompact locally compact Hausdorff space, with topology $\mct$. 
Let $\tilde X = X \cup \theset{\infty}$ ($X$ with one point adjoined), and consider the family $\mcb$ of subsets of $\tilde X$ defined by
$$
\mcb = T \cup \theset{S \cup \theset{\infty}\mid S \subset X,~~ X \backslash S \text{ is compact}}
.$$

a. Prove that $\mcb$ is a topology on $\tilde X$, that the resulting space is compact, and that $X$ is dense in $\tilde X$.

b. Prove that if $Y \supset X$ is a compact space such that $X$ is dense in $Y$ and $Y \backslash X$ is a singleton, 
  then Y is homeomorphic to $\tilde X$. 

  > The space $\tilde X$ is called the **one-point compactification** of $X$.

c. Find familiar spaces that are homeomorphic to the one point compactifications of 

    i. $X = (0, 1)$ and 
    
    ii. $X = \RR^2$.

## 35 (Fall '16). 
Prove that a metric space $X$ is **normal**, i.e. if $A, B \subset X$ are closed and disjoint then there exist open sets $A \subset U \subset X, ~B \subset V \subset X$ such that
$U \cap V = \emptyset$.

## 36 (Spring '06). 
Prove that every compact, Hausdorff topological space is normal.

## 37 (Spring '09). 
Show that a connected, normal topological space with more than a single point is uncountable.

## 38 (Spring '08). 
Give an example of a quotient map in which the domain is Hausdorff, but the quotient is not.

## 39 (Fall '04). 
Let $X$ be a compact Hausdorff space and suppose $R \subset X \times X$ is a closed equivalence relation. 

Show that the quotient space $X/R$ is Hausdorff.

## 40 (Spring '18). 
Let $U \subset \RR^n$ be an open set which is bounded in the standard Euclidean metric. 

Prove that the quotient space $\RR^n / U$ is not Hausdorff.

## 41 (Fall '09). 
Let $A$ be a closed subset of a normal topological space $X$.

Show that both $A$ and the quotient $X/A$ are normal.

## 42 (Spring '10). 
Define an equivalence relation $\sim$ on $\RR$ by $x \sim y$ if and only if $x - y \in Q$. 
Let $X$ be the set of equivalence classes, endowed with the quotient topology induced by the canonical projection $\pi : \RR \to X$.

Describe, with proof, all open subsets of $X$ with respect to this topology.

## 43 (Fall '12). 
Let $A$ denote a subset of points of $S^2$ that looks exactly like the capital letter A. 
Let $Q$ be the quotient of $S^2$ given by identifying all points of $A$ to a single point. 

Show that $Q$ is homeomorphic to a familiar topological space and identify that space.

## 44 (Spring '15). 
a. Prove that a topological space that has a countable base for its topology also contains a countable dense subset.

b. Prove that the converse to (a) holds if the space is a metric space.

## 45 (Spring '11). 
Recall that a topological space is **regular** if for every point $p \in X$ and for every closed subset $F \subset X$ not containing $p$, there exist disjoint open sets $U, V \subset X$ with $p \in U$ and $F \subset V$. 

Let $X$ be a regular space that has a countable basis for its topology, and let $U$ be an open subset of $X$.

a. Show that $U$ is a countable union of closed subsets of $X$.

b. Show that there is a continuous function $f : X \to [0,1]$ such that $f (x) > 0$ for $x \in U$ and $f (x) = 0$ for $x \in U$.

# The Fundamental Group

## 1 (Spring '15). 
Let $S^1$ denote the unit circle in $C$, $X$ be any topological space, $x_0 \in X$, and $$\gamma_0, \gamma_1 : S^1 \to X$$ be two continuous maps such that $\gamma_0 (1) = \gamma_1 (1) = x_0$.

Prove that $\gamma_0$ is homotopic to $\gamma_1$ if and only if the elements represented by $\gamma_0$ and $\gamma_1$ in $\pi_1 (X, x_0 )$ are conjugate.

## 2 (Spring '09/Spring '07/Fall '07/Fall '06).
a. State van Kampen's theorem.

b. Calculate the fundamental group of the space obtained by taking two copies of the torus $T = S^1 \times S^1$ and gluing them along a circle $S^1 \times {p}$ where $p$ is a point in $S^1$.

c. Calculate the fundamental group of the Klein bottle.

d. Calculate the fundamental group of the one-point union of $S^1 \times S^1$ and $S^1$.

e. Calculate the fundamental group of the one-point union of $S^1 \times S^1$ and $\RP^2$.

> **Note: multiple appearances!!**

## 3 (Fall '18). 
Prove the following portion of van Kampen's theorem. 
If $X = A\cup B$ and $A$, $B$, and $A \cap B$ are nonempty and path connected with $\pt \in A \cap B$, then there is a surjection 
$$
\pi_1 (A, \pt) \ast \pi_1 (B, \pt) \to \pi_1 (X, \pt)
.$$

## 4 (Spring '15). 
Let $X$ denote the quotient space formed from the sphere $S^2$ by identifying two distinct points. 

Compute the fundamental group and the homology groups of $X$.

## 5 (Spring '06). 
Start with the unit disk $\DD^2$ and identify points on the boundary if their angles, thought of in polar coordinates, differ a multiple of $\pi/2$. 

Let $X$ be the resulting space. Use van Kampen's theorem to compute $\pi_1 (X, \ast)$.

## 6 (Spring '08). 
Let $L$ be the union of the $z$-axis and the unit circle in the $xy\dash$plane. 
Compute $\pi_1 (\RR^3 \backslash L, \ast)$.

## 7 (Fall '16). 
Let $A$ be the union of the unit sphere in $\RR^3$ and the interval $\theset {(t, 0, 0) : -1 \leq t \leq 1} \subset \RR^3$. 

Compute $\pi_1 (A)$ and give an explicit description of the universal cover of $X$.

## 8 (Spring '13). 
a. Let $S_1$ and $S_2$ be disjoint surfaces. 
    Give the definition of their connected sum $S^1 \#S^2$.

b. Compute the fundamental group of the connected sum of the projective plane and the two-torus.

## 9 (Fall '15). 
Compute the fundamental group, using any technique you like, of $\RP^2 \#\RP^2 \#\RP^2$.

## 10 (Fall '11) 
Let 
$$
V = \DD^2 \times S^1 = \theset{ (z, e^{it}) \suchthat \norm z \leq 1,~~ 0 \leq t < 2\pi}
$$ 
be the "solid torus" with boundary given by the torus $T = S^1 \times S^1$ . 

For $n \in Z$ define 
\begin{align*}
\phi_n : T &\to T \\
(e^{is} , e^{it} ) &\mapsto (e^{is} , e^{i(ns+t)})
.\end{align*}

Find the fundamental group of the identification space
$$
V_n = {V\disjoint V \over \sim n}
$$
where the equivalence relation $\sim_n$ identifies a point $x$ on the boundary $T$ of the first copy of $V$ with the point $\phi_n (x)$ on the boundary of the second copy of $V$.

## 11 (Fall '16). 
Let $S_k$ be the space obtained by removing $k$ disjoint open disks from the sphere $S^2$. 
Form $X_k$ by gluing $k$ Möbius bands onto $S_k$ , one for each circle boundary component of $S_k$ (by identifying the boundary circle of a Möbius band homeomorphically with a given boundary component circle). 

Use van Kampen's theorem to calculate $\pi_1 (X_k)$ for each $k > 0$ and identify $X_k$ in terms of the classification of surfaces.


## 12 (Spring '13).
i.  Let $A$ be a subspace of a topological space $X$. 
    Define what it means for $A$ to be a **deformation retract** of $X$.

ii. Consider $X_1$ the "planar figure eight" and $$X_2 = S^1 \cup ({0} \times [-1, 1])$$ (the "theta space"). 
    Show that $X_1$ and $X_2$ have isomorphic fundamental groups.

iii. Prove that the fundamental group of $X_2$ is a free group on two generators.

# Covering spaces

## 1 (Spring 11/Spring '14). 
a.  Give the definition of a **covering space** $\hat{X}$
    (and **covering map** $p : \hat{X} \to X$) for a topological space $X$.

b.  State the homotopy lifting property of covering spaces. 
    Use it to show that a covering map $p : \hat{X} \to X$ induces an injection 
    $$
    p^\ast : \pi_1 (\hat{X}, \hat{x}) \to \pi_1 (X, p(\hat{x}))
    $$ 
    on fundamental groups.

c.  Let $p : \hat{X} \to X$ be a covering map with $Y$ and $X$ path-connected. 
    Suppose that the induced map $p^\ast$ on $\pi_1$ is an isomorphism. 
    Prove that $p$ is a homeomorphism.

## 2 (Fall '06/Fall '09/Fall '15). 
a. Give the definitions of **covering space** and **deck transformation** (or covering transformation).

b. Describe the universal cover of the Klein bottle and its group of deck transformations.

c. Explicitly give a collection of deck transformations on $$\theset{(x, y) \mid -1 \leq x \leq 1, -\infty < y < \infty}$$ such that the quotient is a Möbius band.

d. Find the universal cover of $\RP^2 \times S^1$ and explicitly describe its group of deck transformations.

## 3 (Spring '06/Spring '07/Spring '12). 
a.  What is the definition of a **regular** (or Galois) covering space?

b.  State, without proof, a criterion in terms of the fundamental group for a covering map $p : \tilde X \to X$ to be regular.

c.  Let $\Theta$ be the topological space formed as the union of a circle and its diameter (so this space looks exactly like the letter $\Theta$). 
    Give an example of a covering space of $\Theta$ that is not regular.

## 4 (Spring '08). 
Let $S$ be the closed orientable surface of genus 2 and let $C$ be the commutator subgroup of $\pi_1 (S, \ast)$. Let $\tilde S$ be the cover corresponding to $C$. 
Is the covering map $\tilde S \to S$ regular? 

> The term "normal" is sometimes used as a synonym for regular in this context.

What is the group of deck transformations?

Give an example of a nontrivial element of $\pi_1 (S, \ast)$ which lifts to a trivial deck transformation.

## 5 (Fall '04). 
Describe the 3-fold connected covering spaces of $S^1 \lor S^1$.

## 6 (Spring '17). 
Find all three-fold covers of the wedge of two copies of $\RP^2$ .
Justify your answer.

## 7 (Fall '17). 
Describe, as explicitly as you can, two different (non-homeomorphic) connected two-sheeted covering spaces of $\RP^2 \lor \RP^3$, and prove that they are not homeomorphic.

## 8 (Spring '19). 
Is there a covering map from
$$
X_3 = \theset{x^2 + y^2 = 1} \cup \theset{(x - 2)^2 + y^2 = 1} \cup \theset{(x + 2)^2 + y^2 = 1} \subset \RR^2
$$ 
to the wedge of two $S^1$'s? 
If there is, give an example; if not, give a proof.

## 9 (Spring '05). 

a.  Suppose $Y$ is an $n$-fold connected covering space of the torus $S^1 \times S^1$. 
    Up to homeomorphism, what is $Y$? Justify your answer.

b.  Let $X$ be the topological space obtained by deleting a disk from a torus.
    Suppose $Y$ is a 3-fold covering space of $X$. 
    
    What surfaces could $Y$ be?
    Justify your answer, but you need not exhibit the covering maps explicitly.

## 10 (Spring '07). 

Let $S$ be a connected surface, and let $U$ be a connected open subset of $S$. 
Let $p : \tilde S \to  S$ be the universal cover of $S$. 
Show that $p\inv (U )$ is connected if and only if the homeomorphism $i_\ast : \pi_1 (U ) \to \pi_1 (S)$ induced by the inclusion $i : U \to S$ is onto.

## 11 (Fall '10). 
Suppose that X has universal cover $p : \tilde X \to X$ and let $A \subset X$ be a subspace with $p(\tilde a) = a \in A$. 
Show that there is a group isomorphism 
$$
\ker(\pi_1 (A, a) \to \pi_1 (X, a)) \cong \pi_1 (p\inv A, \bar a)
.$$

## 12 (Fall '14). 
Prove that every continuous map $f : \RP^2 \to S^1$ is homotopic to a constant. 

> Hint: think about covering spaces.

## 13 (Spring '16). 
Prove that the free group on two generators contains a subgroup isomorphic to the free group on five generators by constructing an appropriate covering space of $S^1 \lor S^1$.

## 14 (Fall '12). 
Use covering space theory to show that $\ZZ_2 \ast \ZZ$  (that is, the free product of $\ZZ_2$ and $\ZZ$)  has two subgroups of index 2 which are not isomorphic to each other.

## 15 (Spring '17). 
a.  Show that any finite index subgroup of a finitely generated free group is free. 
    State clearly any facts you use about the fundamental groups of graphs.

b.  Prove that if $N$ is a nontrivial normal subgroup of infinite index in a finitely generated free group $F$ , then $N$ is not finitely generated.

## 16 (Spring '19). 
Let $p : X \to Y$ be a covering space, where $X$ is compact, path-connected, and locally path-connected. 

Prove that for each $x \in X$ the set $p\inv (\theset{p(x)})$ is finite, and has cardinality equal to the index of $p_* (\pi_1 (X, x))$ in $\pi_1 (Y, p(x))$.

# Homology and Degree Theory

## 1 (Spring '09). 
Compute the homology of the one-point union of $S^1 \times S^1$ and $S^1$.

## 2 (Fall '06). 

a.  State the **Mayer-Vietoris theorem**.

b.  Use it to compute the homology of the space $X$ obtained by gluing two solid tori along their boundary as follows. 
    Let $\DD^2$ be the unit disk and let $S^1$ be the unit circle in the complex plane $\CC$. 
    Let $A = S^1 \times \DD^2$ and $B = \DD^2 \times S^1$. 
    
    Then $X$ is the quotient space of the disjoint union $A \disjoint B$ obtained by identifying $(z, w) \in A$ with $(zw^3 , w) \in B$ for all $(z, w) \in S^1 \times S^1$.

## 3 (Fall '12). 
Let $A$ and $B$ be circles bounding disjoint disks in the plane $z = 0$ in $\RR^3$. 
Let $X$ be the subset of the upper half-space of $\RR^3$ that is the union of the plane $z = 0$ and a (topological) cylinder that intersects the plane in $\partial C = A \cup B$.

Compute $H_* (X)$ using the Mayer--Vietoris sequence.

## 4 (Fall '14). 
Compute the integral homology groups of the space $X = Y \cup Z$ which is the union of the sphere 
$$
Y = \theset{x^2 + y^2 + z^2 = 1}
$$ 
and the ellipsoid 
$$
Z =  \theset{x^2 + y^2 + {z^2 \over 4} = 1}
.$$

## 5 (Spring '08). 
Let $X$ consist of two copies of the solid torus $\DD^2 \times S^1$, glued together by the identity map along the boundary torus $S^1 \times S^1$.
Compute the homology groups of $X$.

## 6 (Spring '17). 
Use the circle along which the connected sum is performed and the Mayer-Vietoris long exact sequence to compute the homology of $\RP^2 \# \RP^2$.

## 7 (Fall '15). 
Express a Klein bottle as the union of two annuli. 

Use the Mayer Vietoris sequence and this decomposition to compute its homology.

## 8 (Spring '09). 
Let $X$ be the topological space obtained by identifying three distinct points on $S^2$. 
Calculate $H_* (X; Z)$.

## 9 (Fall '05). 
Compute $H_0$ and $H_1$ of the complete graph $K_5$ formed by taking five points and joining each pair with an edge.

## 10 (Fall '18). 
Compute the homology of the subset $X \subset \RR^3$ formed as the union of the unit sphere, the $z\dash$axis, and the $xy\dash$plane.

## 11 (Spring '05/Fall '13). 
Let $X$ be the topological space formed by filling in two circles $S^1 \times \theset{p_1 }$ and $S^1 \times \theset{p_2 }$ in the torus $S^1 \times S^1$ with disks.

Calculate the fundamental group and the homology groups of $X$.

## 12 (Spring '19). 
a.  Consider the quotient space 
    $$
    T^2 = \RR^2 / \sim \qtext{where} (x, y) \sim (x + m, y + n) \text{ for } m, n \in \ZZ
    ,$$ 
    and let $A$ be any $2 \times 2$ matrix whose entries are integers such that $\det A = 1$. 
    
    Prove that the action of $A$ on $\RR^2$ descends via the quotient $\RR^2 \to T^2$ to induce a homeomorphism $T^2 \to T^2$.

b.  Using this homeomorphism of $T^2$, we define a new quotient space 
    $$
    T_A^3 \definedas {T^2\cross \RR \over \sim} \qtext{where} ((x, y), t) \sim (A(x, y), t + 1)
    $$
    Compute $H_1 (T_A^3 )$ if $A=\left(\begin{array}{ll} 1 & 1 \\ 0 & 1 \end{array}\right).$

## 13 (Spring '12). 
Give a self-contained proof that the zeroth homology $H_0 (X)$ is isomorphic to $\ZZ$ for every path-connected space $X$.

## 14 (Fall '18). 
It is a fact that if $X$ is a single point then $H_1 (X) = \theset{0}$. 

One of the following is the correct justification of this fact in terms of the singular chain complex. 

Which one is correct and why is it correct?

a. $C_1 (X) = \theset{0}$.

b. $C_1 (X) \neq \theset{0}$ but $\ker \partial_1 = 0$ with $\partial_1 : C_1 (X) \to C_0 (X)$.

c. $\ker \partial_1 \neq 0$ but $\ker \partial_1 = \im\partial_2$ with $\partial_2 : C_2 (X) \to C_1 (X)$.

## 15 (Fall '10). 
Compute the homology groups of $S^2 \times S^2$.

## 16 (Fall '16). 
Let $\Sigma$ be a closed orientable surface of genus $g$.
Compute $H_i(S^1 \times \Sigma; Z)$ for $i = 0, 1, 2, 3$.

## 17 (Spring '07). 
Prove that if $A$ is a retract of the topological space $X$, then for all nonnegative integers $n$ there is a group $G_n$ such that $H_{n} (X) \cong H_{n} (A) \oplus G_n$.

> Here $H_{n}$ denotes the $n$th singular homology group with integer coefficients.

## 18 (Spring '13). 
Does there exist a map of degree 2013 from $S^2 \to S^2$.

## 19 (Fall '18). 
For each $n \in \ZZ$ give an example of a map $f_n : S^2 \to S^2$. 

For which $n$ must any such map have a fixed point?

## 20 (Spring '09).
a.  What is the degree of the antipodal map on the $n$-sphere? 
    (No justification required)

b.  Define a CW complex homeomorphic to the real projective $n\dash$space $\RP^n$.

c.  Let $\pi : \RP^n \to X$ be a covering map. Show that if $n$ is even, $\pi$ is a homeomorphism.

## 21 (Fall '17). 
Let $A \subset X$. 
Prove that the relative homology group $H_0 (X, A)$ is trivial if and only if $A$ intersects every path component of $X$.

## 22 (Fall '18). 
Let $\DD$ be a closed disk embedded in the torus $T = S^1 \times S^1$ and let $X$ be the result of removing the interior of $\DD$ from $T$ . 
Let $B$ be the boundary of $X$, i.e. the circle boundary of the original closed disk $\DD$. 

Compute $H_i (T, B)$ for all $i$.

## 23 (Fall '11). 
For any $n \geq 1$ let $S^n = \theset{(x_0 , \cdots , x_n )\mid \sum x_i^2 =1}$ denote the $n$ dimensional unit sphere and let $$E = \theset{(x_0 , . . . , x_n )\mid x_n = 0}$$ denote the "equator".

Find, for all $k$, the relative homology $H_k (S^n , E)$.

## 24 (Spring '12/Spring '15). 
Suppose that $U$ and $V$ are open subsets of a space $X$, with $X = U \cup V$. 
Find, with proof, a general formula relating the Euler characteristics of $X, U, V$, and $U \cap V$. 

> You may assume that the homologies of $U, V, U \cap V, X$ are finite-dimensional so that their Euler characteristics are well defined.

# Cell Complexes and "Attaching Map" Spaces

## 1 (Fall '07). 
Describe a cell complex structure on the torus $T = S^1 \times S^1$ and use
this to compute the homology groups of $T$. 

> To justify your answer you will need to consider the attaching maps in detail.

## 2 (Fall '04). 
Let $X$ be the space formed by identifying the boundary of a
Möbius band with a meridian of the torus $T^2$. 

Compute $\pi_1 (X)$ and $H_* (X)$.

## 3 (Spring '06). 
Compute the homology of the space $X$ obtained by attaching a Möbius band to $\RP^2$ via a homeomorphism of its boundary circle to the standard $\RP^1$ in $\RP^2$.

## 4 (Spring '14). 
Let $X$ be a space obtained by attaching two 2-cells to the torus $S^1 \times S^1$, one along a simple closed curve $\theset{x} \times S^1$ and the other along $\theset{y} \times S^1$ for two points $x \neq y$ in $S^1$ .

a. Draw an embedding of $X$ in $\RR^3$ and calculate its fundamental group.

b. Calculate the homology groups of $X$.

## 5 (Fall '07). 
Let $X$ be the space obtained as the quotient of a disjoint union of a 2-sphere $S^2$ and a torus $T = S^1 \times S^1$ by identifying the equator in $S^2$ with a circle $S^1 \times \theset{p}$ in $T$. 

Compute the homology groups of $X$.

## 6 (Spring '06). 
Let $X = S^2 / \theset{p_1 = \cdots = p_k }$ be the topological space obtained from the 2-sphere by identifying $k$ distinct points on it ($k \geq 2$).

Find:

a. The fundamental group of $X$.

b. The Euler characteristic of $X$.

c. The homology groups of $X$.

## 7 (Fall '16). 
Let $X$ be the topological space obtained as the quotient of the sphere $S^2 = \theset{\vector x \in \RR^3 \suchthat \norm{\vector x} = 1}$ under the equivalence relation $\vector x \sim -\vector x$ for $\vector x$ in the equatorial circle, i.e. for $\vector x = (x_1, x_2, 0)$. 

Calculate $H_* (X; \ZZ)$ from a CW complex description of $X$.

## 8 (Fall '17).
Compute, by any means available, the fundamental group and all the homology groups of the space obtained by gluing one copy $A$ of $S^2$ to another copy $B$ of $S^2$ via a two-sheeted covering space map from the equator of $A$ onto the equator of $B$.

## 9 (Spring '14). 
Use cellular homology to calculate the homology groups of $S^n \times S^m$.

## 10 (Fall '09/Fall '12). 
Denote the points of $S^1 \times I$ by $(z, t)$ where $z$ is a unit complex number and $0 \leq t \leq 1$. 
Let $X$ denote the quotient of $S^1 \times I$ given by identifying $(z, 1)$ and $(z_2 , 0)$ for all $z \in S^1$. 

Give a cell structure, with attaching maps, for $X$, and use it to compute $\pi_1 (X, \ast)$ and $H_1 (X)$.

## 11 (Spring '15). 
Let $X = S_1 \cup S_2 \subset \RR^3$ be the union of two spheres of radius 2, one about $(1, 0, 0)$ and the other about $(-1, 0, 0)$, i.e. 
\begin{align*}
S_1 &= \theset{(x, y,z) \mid (x-1)^2 + y^2 +z^2 = 4} \\
S_2 &= \theset{(x, y, z) \mid (x + 1)^2 + y^2 + z^2 = 4}
.\end{align*}

a. Give a description of $X$ as a CW complex.

b. Write out the cellular chain complex of $X$.

c. Calculate $H_* (X; Z)$.

## 12 (Spring '06). 
Let $M$ and $N$ be finite CW complexes.

a. Describe a cellular structure of $M \times N$ in terms of the cellular structures of $M$ and $N$.

b. Show that the Euler characteristic of $M \times N$ is the product of the Euler characteristics of $M$ and $N$.

## 13 (Spring '07). 
Suppose the space $X$ is obtained by attaching a 2-cell to the torus $S^1 \times S^1$.

In other words, $X$ is the quotient space of the disjoint union of the closed disc $\DD^2$ and the torus $S^1 \times S^1$ by the identification $x \sim f(x)$ where $S^1$ is the boundary of the unit disc and $f : S^1 \to S^1 \times S^1$ is a continuous map.

What are the possible homology groups of $X$? 
Justify your answer.

## 14 (Spring '15). 
Let $X$ be the topological space constructed by attaching a closed 2-disk $\DD^2$ to the circle $S^1$ by a continuous map $\partial\DD^2 \to S^1$ of degree $d > 0$ on the boundary circle.

a.  Show that every continuous map $X \to X$ has a fixed point.

b.  Explain how to obtain all the connected covering spaces of $X$.

## 15 (Spring '11). 
Let $X$ be a topological space obtained by attaching a 2-cell to $\RP^2$ via some map $f: S^1 \to \RP^2$ . 

What are the possibilities for the homology $H_* (X; Z)$?

## 16 (Spring '12). 
For any integer $n \geq 2$ let $X_n$ denote the space formed by attaching a 2-cell to the circle $S^1$ via the attaching map 
\begin{align*}
a_n: S^1 &\to S^1 \\
e^{i\theta} &\mapsto e^{in\theta}
.\end{align*}

a.  Compute the fundamental group and the homology of $X_n$.

b.  Exactly one of the $X_n$ (for $n \geq 2$) is homeomorphic to a surface. 
    Identify, with proof, both this value of $n$ and the surface that $X_n$ is homeomorphic to (including a description of the homeomorphism).

## 17 (Spring '09). 
Let $X$ be a CW complex and let $\pi : Y \to X$ be a covering space.

a. Show that $Y$ is compact iff $X$ is compact and $\pi$ has finite degree.

b.  Assume that $\pi$ has finite degree $d$. 
    Show show that $\chi (Y ) = d \chi (X)$.

c.  Let $\pi :\RP^N \to X$ be a covering map. 
    Show that if $N$ is even, $\pi$ is a homeomorphism.

## 18 (Spring '18). 
For topological spaces $X, Y$ the **mapping cone** $C(f )$ of a map $f : X \to Y$ is defined to be the quotient space 
\begin{align*}
(X \times [0, 1])\disjoint Y / \sim &\qtext{where}  \\ 
(x, 0) &\sim (x', 0) \qtext{for all} x, x' \in X \text{ and } \\ 
(x, 1) &\sim f (x) \qtext{for all } x \in X
.\end{align*}


Let $\phi_k : S^n \to S^n$ be a degree $k$ map for some integer $k$. 

Find $H_i(C(\phi_k ))$ for all $i$.

## 19 (Fall '18). 
Prove that a finite CW complex must be Hausdorff.

# Surfaces

## 1 (Fall '05). 
State the classification theorem for surfaces (compact, without boundary, but not necessarily orientable). 
For each surface in the classification, indicate the structure of the first homology group and the value of the Euler characteristic. 

Also, explain briefly how the 2-holed torus and the connected sum $\RP^2 \# \RP^2$ fit into the classification.

## 2 (Spring '16). 
Give a list without repetitions of all compact surfaces (orientable or non-orientable and with or without boundary) that have Euler characteristic negative one. 

Explain why there are no repetitions on your list.

## 3 (Spring '07). 
Describe the topological classification of all compact connected surfaces $M$ without boundary having Euler characteristic $\chi(M )\geq -2$. 

No proof is required.

## 4 (Spring '09). 
How many surfaces are there, up to homeomorphism, which are: 

- Connected, 
- Compact, 
- Possibly with boundary, 
- Possibly nonorientable, and 
- With Euler characteristic -3? 

Describe one representative from each class.

## 5 (Fall '13). 
Prove that the Euler characteristic of a compact surface with boundary which has $k$ boundary components is less than or equal to $2 - k$.

## 6 (Spring '13). 
What surface is represented by the $6\dash$gon with edges identified according to the symbol $xyzxy\inv z\inv$ ?

## 7 (Spring '15). 
Let $X$ be the topological space obtained as the quotient space of a regular $2n\dash$gon ($n \geq 2$) in $\RR^2$ by identifying opposite edges via translations in the plane. 

First show that X is a compact, orientable surface without boundary, and then identify its genus as a function of $n$.

## 8 (Fall '10).
a.  Show that any compact connected surface with nonempty boundary is homotopy equivalent to a wedge of circles 

    > Hint: you may assume that any compact connected surface without boundary is given by identifying edges of a polygon in pairs.

b.  For each surface appearing in the classification of compact surfaces with nonempty boundary, say how many circles are needed in the wedge from part (a). 

    > Hint: you should be able to do this even if you have not done part (a).

## 9 (Fall '04). 
Let $M_g^2$ be the compact oriented surface of genus $g$. 

Show that there exists a continuous map $f : M_g^2 \to S^2$ which is not homotopic to a constant map.

## 10 (Spring '11) 
Show that $\RP^2 \lor S^1$ is *not* homotopy equivalent to a compact surface (possibly with boundary).

## 11 (Fall '14). 
Identify (with proof, but of course you can appeal to the classification of surfaces) all of the compact surfaces without boundary that have a cell decomposition having exactly one 0-cell and exactly two 1-cells (with no restriction on the number of cells of dimension larger than 1).

## 12 (Fall '11). 
For any natural number $g$ let $\Sigma_g$ denote the (compact, orientable) surface of genus $g$. 

Determine, with proof, all valued of $g$ with the property that there exists a covering space $\pi : \Sigma_5 \to \Sigma_g$ . 

> Hint: How does the Euler characteristic behave for covering spaces?

## 13 (Spring '14). 
Find *all* surfaces, orientable and non-orientable, which can be covered by a closed surface (i.e. compact with empty boundary) of genus 2. 
Prove that your answer is correct.

## 14 (Spring '18).
a. Write down (without proof) a presentation for $\pi_1 (\Sigma_2 , p)$ where $\Sigma_2$ is a closed, connected, orientable genus 2 surface and $p$ is any point on $\Sigma_2$ .

b.  Show that $\pi_1 (\Sigma_2 , p)$ is not abelian by showing that it surjects onto a free group of rank 2.

c.  Show that there is no covering space map from $\Sigma_2$ to $S^1 \times S^1$ . 
    You may use the fact that $\pi_1 (S^1 \times S^1 ) \cong \ZZ^2$ together with the result in part (b) above.

## 15 (Fall '16). 
Give an example, with explanation, of a closed curve in a surfaces which is not nullhomotopic but is nullhomologous.

## 16 (Fall '17). 
Let $M$ be a compact orientable surface of genus $2$ without boundary. 

Give an example of a pair of loops $$\gamma_0 , \gamma_1 : S^1 \to M$$ with $\gamma_0 (1) = \gamma_1 (1)$ such that there is a continuous map $\Gamma: [0, 1] \times S^1 \to M$ such that 
$$
\Gamma(0, t) = \gamma_0 (t), \quad \Gamma(1, t) = \gamma_1 (t) \qtext{for all} t \in S^1
,$$ 
but such that there is no such map $\Gamma$ with the additional property that $\Gamma_s (1) = \gamma_0 (1)$ for all $s \in [0, 1]$.

(You are not required to prove that your example satisfies the stated property.)

## 17 (Fall '18). 
Let $C$ be cylinder. 
Let $I$ and $J$ be disjoint closed intervals contained in $\partial C$. 

What is the Euler characteristic of the surface $S$ obtained by identifying $I$ and $J$? 

Can all surface with nonempty boundary and with this Euler characteristic be obtained from this construction?

## 18 (Spring '19). 
Let $\Sigma$ be a compact connected surface and let  $p_1, \cdots , p_k \in \Sigma$.

Prove that $H_2 \qty{\Sigma \setminus \union_{i=1}^k {p_i} } = 0$.

# Fixed points

## 1 (Fall '14). 
Prove that, for every continuous map $f : B^2 \to B^2$, there is a point $x$ such that $f (x) = x$. 

> This is the $n = 2$ case of the Brouwer fixed point theorem; your proof shouldn't appeal to either of the Brouwer or the Lefschetz fixed point theorems.

## 2 (Spring '18). 
Prove or disprove: 

Every continuous map from $S^2$ to $S^2$ has a fixed point.

## 3 (Spring '11)
a. State the **Lefschetz Fixed Point Theorem** for a finite simplicial complex $X$.

b. Use degree theory to prove this theorem in case $X = S^n$.

## 4 (Spring '12).
a. Prove that for every continuous map $f : S^2 \to S^2$ there is some $x$ such that either $f (x) = x$ or $f (x) = -x$. 

> Hint: Where $A : S^2 \to S^2$ is the antipodal map, you are being asked to prove that either $f$ or $A \circ f$ has a fixed point.

b. Exhibit a continuous map $f : S^3 \to S^3$ such that for every $x \in S^3$, $f (x)$ is equal to neither $x$ nor $-x$.

> Hint: It might help to first think about how you could do this for a map from $S^1$ to $S^1$.

## 5 (Spring '14). 
Show that a map $S^n \to S^n$ has a fixed point unless its degree is equal to the degree of the antipodal map $a : x \to -x$.

## 6 (Spring '08). 
Give an example of a homotopy class of maps of $S^1 \lor  S^1$ each member of which must have a fixed point, and also an example of a map of $S^1 \lor S^1$ which doesn't have a fixed point.

## 7 (Spring '17). 
Prove or disprove: 

Every map from $\RP^2 \lor \RP^2$ to itself has a fixed point.

## 8 (Fall '09). 
Find all homotopy classes of maps from $S^1 \times \DD^2$ to itself such that every element of the homotopy class has a fixed point.

## 9 (Spring '10). 
Let $X$ and $Y$ be finite connected simplicial complexes and let $f : X \to Y$ and $g : Y \to X$ be basepoint-preserving maps. 

Show that no matter how you homotope $f \lor g : X \lor Y \to X \lor Y$, there will always be a fixed point.

## 10 (Fall '12) 
Let $f = \id_{\RP^2} \lor \ast$ and $g = \ast \lor id_{S^1}$ be two maps of $\RP^2 \lor S^1$ to itself where $\ast$ denotes the constant map of a space to its basepoint.

Show that one map is homotopic to a map with no fixed points, while the other is not.

## 11 (Spring '09). 
View the torus $T$ as the quotient space $\RR^2 /\ZZ^2$. 

Let $A$ be a $2 \times 2$ matrix with $\ZZ$ coefficients.

a. Show that the linear map $A : \RR^2 \to \RR^2$ descends to a continuous map $\mca : T \to T$.

b. Show that, with respect to a suitable basis for $H_1 (T ; \ZZ)$, the matrix $A$ represents the map induced on $H_1$ by $\mca$.

c. Find a necessary and sufficient condition on $A$ for $\mca$ to be homotopic to the identity.

d. Find a necessary and sufficient condition on $A$ for $\mca$ to be homotopic to a map with no fixed points.

## 12 (Spring '19). 
a. Use the Lefschetz fixed point theorem to show that any degree-one map $f : S^2 \to S^2$ has at least one fixed point.

b. Give an example of a map $f : \RR^2 \to \RR^2$ having no fixed points.

c. Give an example of a degree-one map $f : S^2 \to S^2$ having exactly one fixed point.

## 13 (Fall '10). 
For which compact connected surfaces $\Sigma$ (with or without boundary) does there exist a continuous map $f : \Sigma \to \Sigma$ that is homotopic to the identity and has no fixed point? 

Explain your answer fully.

## 14 (Spring '16). 
Use the Brouwer fixed point theorem to show that an $n \times n$ matrix with nonnegative entries has a real eigenvalue.

# Miscellaneous algebraic topology

## 1 (Fall '14). 
Prove that $\RR^2$ is not homeomorphic to $\RR^n$ for $n > 2$.

## 2 (Spring '12). 
Prove that any finite tree is contractible, where a **tree** is a connected graph that contains no closed edge paths.

## 3 (Spring '13). 
Show that any continuous map $f : \RP^2 \to S^1 \times S^1$ is necessarily null-homotopic.

## 4 (Fall '11). 
Prove that, for $n \geq 2$, every continuous map $f: \RP^n \to S^1$ is null-homotopic.

## 5 (Spring '06). 
Let $S^2 \to \RP^2$ be the universal covering map. 

Is this map null-homotopic? 
Give a proof of your answer.

## 6 (Spring '17). 
Suppose that a map $f : S^3 \times S^3 \to \RP^3$ is not surjective. 

Prove that $f$ is homotopic to a constant function.

## 7 (Fall '06). 
Prove that there does not exist a continuous map $f : S^2 \to S^2$ from the unit sphere in $\RR^3$ to itself such that $f (\vector x) \perp \vector x$ 
(as vectors in $\RR^3$ for all $\vector x \in S^2$).

## 8 (Spring '08). 
Let $f$ be the map of $S^1 \times [0, 1]$ to itself defined by
$$
f (e^{i\theta} , s) = (e^{i(\theta+2\pi s)} , s)
,$$ 
so that $f$ restricts to the identity on the two boundary circles of $S^1 \times [0, 1]$. 

Show that $f$ is homotopic to the identity by a homotopy $f_t$ that is stationary on one of the boundary circles, but not by any homotopy that is stationary on both boundary circles. 

> Hint: Consider what $f$ does to the path $s \mapsto (e^{i\theta_0} , s)$ for fixed $e^{i\theta_0} \in S^1$.

## 9 (Spring '17). 
Show that $S^1 \times S^1$ is not the union of two disks (where there is no assumption that the disks intersect along their boundaries).

## 10 (Spring '14). 
Suppose that $X \subset Y$ and $X$ is a deformation retract of $Y$. 

Show that if $X$ is a path connected space, then $Y$ is path connected.

## 11 (Spring '05). 
Do one of the following:

a. Give (with justification) a contractible subset $X \subset \RR^2$ which is not a retract of $\RR^2$ .

b. Give (with justification) two topological spaces that have the same homology groups but that are not homotopy equivalent.

## 12 (Spring '16). 
Recall that the **suspension** of a topological space, denoted $SX$, is the quotient space formed from $X \times [-1, 1]$ by identifying $(x, 1)$ with $(y, 1)$ for all $x, y \in X$, and also identifying $(x, -1)$ with $(y, -1)$ for all $x, y \in X$.

a. Show that $SX$ is the union of two contractible subspaces.

b. Prove that if $X$ is path-connected then $\pi_1 (SX) = \theset{0}$.

c. For all $n \geq 1$, prove that $H_{n} (X) \cong H_{n+1} (SX)$.
