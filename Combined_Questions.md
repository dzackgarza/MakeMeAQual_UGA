---
title: Combined Qual Questions
---

# Algebra (140 Questions)

**Question 1**

Let $G$ be a finite group with $n$ distinct conjugacy classes.
Let $g_1 \cdots g_n$ be representatives of the conjugacy classes of $G$.

Prove that if $g_i g_j = g_j g_i$ for all $i, j$ then $G$ is abelian.


**Question 2**

Let $G$ be a group of order 105 and let $P, Q, R$ be Sylow 3, 5, 7 subgroups respectively.

(a) Prove that at least one of $Q$ and $R$ is normal in $G$.

(b) Prove that $G$ has a cyclic subgroup of order 35.

(c) Prove that both $Q$ and $R$ are normal in $G$.

(d) Prove that if $P$ is normal in $G$ then $G$ is cyclic.


**Question 3**

Let $R$ be a ring with the property that for every $a \in R, a^2 = a$.

(a) Prove that $R$ has characteristic 2.

(b) Prove that $R$ is commutative.


**Question 4**

Let $F$ be a finite field with $q$ elements.

Let $n$ be a positive integer relatively prime to $q$ and let $\omega$ be a primitive $n$th root of unity in an extension field of $F$.

Let $E = F [\omega]$ and let $k = [E : F]$.

(a) Prove that $n$ divides $q^{k}-1$.

(b) Let $m$ be the order of $q$ in $\ZZ/n\ZZ$.
Prove that $m$ divides $k$.

(c) Prove that $m = k$.


**Question 5**

Let $R$ be a ring and $M$ an $R\dash$module.

> Recall that the set of torsion elements in M is defined by
$$
\Tor(m) = \{m \in M \suchthat \exists r \in R, ~r \neq 0, ~rm = 0\}
.$$

(a) Prove that if $R$ is an integral domain, then $\Tor(M )$ is a submodule of $M$ .

(b) Give an example where $\Tor(M )$ is not a submodule of $M$.

(c) If $R$ has zero-divisors, prove that every non-zero $R\dash$module has non-zero torsion elements.


**Question 6**

Let $R$ be a commutative ring with multiplicative identity. Assume Zorn's Lemma.

(a) Show that
$$
N = \{r \in R \mid r^n = 0 \text{ for some } n > 0\}
$$
is an ideal which is contained in any prime ideal.

(b) Let $r$ be an element of $R$ not in $N$.
Let $S$ be the collection of all proper ideals of $R$ not containing any positive power of $r$. Use Zorn's Lemma to prove that
there is a prime ideal in $S$.

(c) Suppose that $R$ has exactly one prime ideal $P$ . Prove that every element $r$ of $R$ is either nilpotent or a unit.


**Question 7**

Let $\zeta_n$ denote a primitive $n$th root of 1 $\in \QQ$.
You may assume the roots of the minimal polynomial $p_n(x)$ of $\zeta_n$ are exactly the primitive $n$th roots of 1.

Show that the field extension $\QQ(\zeta_n )$ over $\QQ$ is Galois and prove its Galois group is $(\ZZ/n\ZZ)\units$.

How many subfields are there of $\QQ(\zeta_{20} )$?


**Question 8**

Let $\{e_1, \cdots, e_n \}$ be a basis of a real vector space $V$ and let
$$
\Lambda \definedas \theset{ \sum r_i e_i \mid ri \in \ZZ}
$$

Let $\cdot$ be a non-degenerate ($v \cdot w = 0$ for all $w \in V \iff v = 0$) symmetric bilinear form on V such that the Gram matrix $M = (e_i \cdot e_j )$ has integer entries.

Define the dual of $\Lambda$ to be

$$
\Lambda \dual \definedas \{v \in V \suchthat v \cdot x \in \ZZ \text{ for all } x \in \Lambda
\}
.$$

(a) Show that $\Lambda \subset \Lambda \dual$.

(b) Prove that $\det M \neq 0$ and that the rows of $M\inv$ span $\Lambda\dual$.

(c) Prove that $\det M = |\Lambda\dual /\Lambda|$.


**Question 9**

Let $A$ be a square matrix over the complex numbers.
Suppose that $A$ is nonsingular
and that $A^{2019}$ is diagonalizable over $\CC$.

Show that $A$ is also diagonalizable over $\CC$.


**Question 10**

Let $F = \FF_p$ , where $p$ is a prime number.

(a) Show that if $\pi(x) \in F[x]$ is irreducible of degree $d$, then $\pi(x)$ divides $x^{p^d} - x$.


(b) Show that if $\pi(x) \in F[x]$ is an irreducible polynomial that divides $x^{p^n} - x$,
then $\deg \pi(x)$ divides $n$.


**Question 11**

How many isomorphism classes are there of groups of order 45?

Describe a representative from each class.


**Question 12**

For a finite group $G$, let $c(G)$ denote the number of conjugacy classes of $G$.

(a) Prove that if two elements of $G$ are chosen uniformly at random,then the probability they commute is precisely
$$
\frac{c(G)}{\abs G}
.$$

(b) State the class equation for a finite group.

(c) Using the class equation (or otherwise) show that the probability in part (a) is at most $$
\frac 1 2 + \frac 1 {2[G : Z(G)]}
.$$

> Here, as usual, $Z(G)$ denotes the center of $G$.


**Question 13**

Let $R$ be an integral domain. Recall that if $M$ is an $R\dash$module, the *rank* of $M$ is
defined to be the maximum number of $R\dash$linearly independent elements of $M$ .

(a) Prove that for any $R\dash$module $M$, the rank of $\tor(M )$ is 0.

(b) Prove that the rank of $M$ is equal to the rank of of $M/\tor(M )$.

(c) Suppose that M is a non-principal ideal of $R$.

(d) Prove that $M$ is torsion-free of rank 1 but not free.


**Question 14**

Let $R$ be a commutative ring with 1.

> Recall that $x \in R$ is nilpotent iff $xn = 0$ for
some positive integer $n$.

(a) Show that every proper ideal of $R$ is contained within a maximal ideal.

(b) Let $J(R)$ denote the intersection of all maximal ideals of $R$.

    Show that $x \in J(R) \iff 1 + rx$ is a unit for all $r \in R$.

(c) Suppose now that $R$ is finite. Show that in this case $J(R)$ consists precisely
of the nilpotent elements in R.


**Question 15**

Let $p$ be a prime number.
Let $A$ be a $p \times p$ matrix over a field $F$ with 1 in all
entries except 0 on the main diagonal.

Determine the Jordan canonical form (JCF) of $A$

(a) When $F = \QQ$,

(b) When $F = \FF_p$.

> Hint: In both cases, all eigenvalues lie in the ground field. In each case find a
matrix $P$ such that $P\inv AP$ is in JCF.


**Question 16**

Let $\zeta = e^{2\pi i/8}$.

(a) What is the degree of $\QQ(\zeta)/\QQ$?

(b) How many quadratic subfields of $\QQ(\zeta)$ are there?

(c) What is the degree of $\QQ(\zeta, \sqrt[4] 2)$ over $\QQ$?


**Question 17**

Let $G$ be a finite group whose order is divisible by a prime number $p$.
Let $P$ be a normal $p\dash$subgroup of $G$
(so $\abs P = p^c$ for some $c$).

(a) Show that $P$ is contained in every Sylow $p\dash$subgroup of $G$.

(b) Let $M$ be a maximal proper subgroup of $G$. Show that either $P \subseteq M$ or $|G/M | = p^b$ for some $b \leq c$.


**Question 18**

(a) Suppose the group $G$ acts on the set $X$ . Show that the stabilizers of elements in the same orbit are conjugate.

(b) Let $G$ be a finite group and let $H$ be a proper subgroup. Show that the union of the conjugates of $H$ is strictly smaller than $G$, i.e.
$$
\union_{g\in G} gHg\inv \subsetneq G
$$

(c) Suppose $G$ is a finite group acting transitively on a set $S$ with at least 2 elements. Show that there is an element of $G$ with no fixed points in $S$.


**Question 19**

Let $F \subset K \subset L$ be finite degree field extensions.
For each of the following assertions, give a proof or a counterexample.

(a) If $L/F$ is Galois, then so is $K/F$.

(b) If $L/F$ is Galois, then so is $L/K$.

(c) If $K/F$ and $L/K$ are both Galois, then so is $L/F$.


**Question 20**

Let $V$ be a finite dimensional vector space over a field (the field is not necessarily algebraically closed).

Let $\phi : V \to V$ be a linear transformation. Prove that there exists a decomposition of $V$ as $V = U \oplus W$ , where $U$ and $W$ are $\phi\dash$invariant subspaces of $V$ , $\restrictionof{\phi}{U}$ is nilpotent, and $\restrictionof{\phi}{W}$ is nonsingular.


**Question 21**

Let $A$ be an $n \times n$ matrix.

(a) Suppose that $v$ is a column vector such that the set $\{v, Av, . . . , A^{n-1} v\}$ is linearly independent. Show that any matrix $B$ that commutes with $A$ is a polynomial in $A$.

(b) Show that there exists a column vector $v$ such that the set $\{v, Av, . . . , A^{n-1} v\}$ is linearly independent $\iff$ the characteristic polynomial of A equals the minimal polynomial of A.


**Question 22**

Let $R$ be a commutative ring, and let $M$ be an $R\dash$module. 
An $R\dash$submodule $N$ of $M$ is maximal if there is no $R\dash$module $P$ with $N \subsetneq P \subsetneq M$.

(a) Show that an $R\dash$submodule $N$ of $M$ is maximal $\iff M /N$ is a simple $R\dash$module: i.e., $M /N$ is nonzero and has no proper, nonzero $R\dash$submodules.

(b) Let $M$ be a $\ZZ\dash$module. Show that a $\ZZ\dash$submodule $N$ of $M$ is maximal $\iff \#M /N$ is a prime number.

(c) Let $M$ be the $\ZZ\dash$module of all roots of unity in $\CC$ under multiplication.
Show that there is no maximal $\ZZ\dash$submodule of $M$.


**Question 23**

Let $R$ be a commutative ring.

(a) Let $r \in R$. Show that the map
\begin{align*}
r\bullet : R &\to R \\
x &\mapsto r x
.\end{align*}
is an $R\dash$module endomorphism of $R$.

(b) We say that $r$ is a **zero-divisor** if r$\bullet$ is not injective.
Show that if $r$ is a zero-divisor and $r \neq 0$, then the kernel and image of $R$ each consist of zero-divisors.

(c) Let $n \geq 2$ be an integer. Show: if $R$ has exactly $n$ zero-divisors, then $\#R \leq n^2$ .

(d) Show that up to isomorphism there are exactly two commutative rings $R$ with precisely 2 zero-divisors.

> You may use without proof the following fact: every ring of order 4 is isomorphic to exactly one of the
following:
$$
\frac{ \ZZ }{ 4\ZZ}, \quad
\frac{ \frac{  \ZZ }{ 2\ZZ} [t]}{(t^2 + t + 1)}, \quad
\frac{ \frac{ \ZZ }{ 2\ZZ} [t]}{ (t^2 - t)}, \quad
\frac{ \frac{ \ZZ}{2\ZZ}[t]}{(t^2 )}
.$$


**Question 24**

(a) Use the Class Equation (equivalently, the conjugation action of a group on itself) to prove that any $p\dash$group (a group whose order is a positive power of a prime integer $p$) has a nontrivial center.

(b) Prove that any group of order $p^2$ (where $p$ is prime) is abelian.

(c) Prove that any group of order $5^2 \cdot 7^2$ is abelian.

(d) Write down exactly one representative in each isomorphism class of groups of order $5^2 \cdot 7^2$.


**Question 25**

Let $f(x) = x^4 - 4x^2 + 2 \in \QQ[x]$.

(a) Find the splitting field $K$ of $f$, and compute $[K: \QQ]$.

(b) Find the Galois group $G$ of $f$, both as an explicit group of automorphisms, and as a familiar abstract group to which it is isomorphic.

(c) Exhibit explicitly the correspondence between subgroups of $G$ and intermediate fields between $\QQ$ and $k$.


**Question 26**

Let $K$ be a Galois extension of $\QQ$ with Galois group $G$, and let $E_1 , E_2$ be intermediate fields of $K$ which are the splitting fields of irreducible $f_i (x) \in \QQ[x]$. 

Let $E = E_1 E_2 \subset K$. 

Let $H_i = \Gal(K/E_i)$ and $H = \Gal(K/E)$.

(a) Show that $H = H_1 \cap H_2$.

(b) Show that $H_1 H_2$ is a subgroup of $G$.

(c) Show that 
$$
\Gal(K/(E_1 \cap E_2 )) = H_1 H_2
.$$


**Question 27**

Let

$$
A=\left[\begin{array}{lll}{0} & {1} & {-2} \\ {1} & {1} & {-3} \\ {1} & {2} & {-4}\end{array}\right] \in M_{3}(\mathbb{C})
$$

(a) Find the Jordan canonical form J of A.

(b) Find an invertible matrix $P$ such that $P\inv AP = J$. 

> You should not need to compute $P\inv$.


**Question 28**

Let 
$$
M=\left(\begin{array}{ll}{a} & {b} \\ {c} & {d}\end{array}\right)
\quad \text{and} \quad 
N=\left(\begin{array}{cc}{x} & {u} \\ {-y} & {-v}\end{array}\right)
$$

over a commutative ring $R$, where $b$ and $x$ are units of $R$. 
Prove that
$$
M N=\left(\begin{array}{ll}{0} & {0} \\ {0} & {*}\end{array}\right)
\implies MN = 0
.$$


**Question 29**

Let
$$
M = \{(w, x, y, z) \in \ZZ^4 \suchthat w + x + y + z \in 2\ZZ\}
,$$

and

$$
N = \{(w, x, y, z) \in \ZZ^4 \suchthat 4\divides (w - x),~ 4\divides (x - y),~ 4\divides ( y - z)\}
.$$

(a) Show that $N$ is a $\ZZ\dash$submodule of $M$ .

(b) Find vectors $u_1 , u_2 , u_3 , u_4 \in \ZZ^4$ and integers $d_1 , d_2 , d_3 , d_4$ such that
$$
\{u_1 , u_2 , u_3 , u_4 \}
$$
is a free basis for $M$, and
$$
\{d_1 u_1,~ d_2 u_2,~ d_3 u_3,~ d_4 u_4 \}
$$
is a free basis for $N$ .

(c) Use the previous part to describe $M/N$ as a direct sum of cyclic $\ZZ\dash$modules.


**Question 30**

Let $R$ be a PID and $M$ be an $R\dash$module. Let $p$ be a prime element of $R$. The module $M$ is called *$\generators{p}\dash$primary* if for every $m \in M$ there exists $k > 0$ such that $p^k m = 0$.

(a) Suppose M is $\generators{p}\dash$primary. Show that if $m \in M$ and $t \in R, ~t \not\in \generators{p}$, then there exists $a \in R$ such that
$atm = m$.

(b) A submodule $S$ of $M$ is said to be *pure* if $S \cap r M = rS$ for all $r \in R$. Show that if $M$ is $\generators{p}\dash$primary, then $S$ is pure if and only if $S \cap p^k M = p^k S$ for all $k \geq 0$.


**Question 31**

Let $R = C[0, 1]$ be the ring of continuous real-valued functions on the interval $[0, 1]$. Let I be an ideal of $R$.

(a) Show that if $f \in I, a \in [0, 1]$ are such that $f (a) \neq 0$, then there exists $g \in I$ such that $g(x) \geq 0$ for all $x \in [0, 1]$, and $g(x) > 0$ for all $x$ in some open neighborhood of $a$.

(b) If $I \neq R$, show that the set $Z(I) = \{x \in [0, 1] \suchthat f(x) = 0 \text{ for all } f \in I\}$ is nonempty.

(c) Show that if $I$ is maximal, then there exists $x_0 \in [0, 1]$ such that $I = \{ f \in R \suchthat f (x_0 ) = 0\}$.


**Question 32**

Suppose the group $G$ acts on the set $A$. 
Assume this action is faithful (recall that this means that the kernel of the homomorphism from $G$ to $\sym(A)$ which gives the action is trivial) and transitive (for all $a, b$ in $A$, there exists $g$ in $G$ such that $g \cdot a = b$.)

(a) For $a \in A$, let $G_a$ denote the stabilizer of $a$ in $G$. 
Prove that for any $a \in A$, 
$$
\intersect_{\sigma\in G} \sigma G_a \sigma\inv = \theset{1}
.$$

(b) Suppose that $G$ is abelian. Prove that $|G| = |A|$. Deduce that every abelian transitive subgroup of $S_n$ has order $n$.


**Question 33**

(a) Classify the abelian groups of order 36.

For the rest of the problem, assume that $G$ is a non-abelian group of order 36. 

> You may assume that the only subgroup of order 12 in $S_4$ is $A_4$ and that $A_4$ has no subgroup of order 6.

(b) Prove that if the 2-Sylow subgroup of $G$ is normal, $G$ has a normal subgroup $N$ such that $G/N$ is isomorphic to $A_4$.

(c) Show that if $G$ has a normal subgroup $N$ such that $G/N$ is isomorphic to $A_4$ and a subgroup $H$ isomorphic to $A_4$ it must be the direct product of $N$ and $H$.

(d) Show that the dihedral group of order 36 is a non-abelian group of order 36 whose Sylow-2 subgroup is not normal.


**Question 34**

Let $F$ be a field. Let $f(x)$ be an irreducible polynomial in $F[x]$ of degree $n$ and let $g(x)$
be any polynomial in $F[x]$. Let $p(x)$ be an irreducible factor (of degree $m$) of the polynomial $f(g(x))$.

Prove that $n$ divides $m$. Use this to prove that if $r$ is an integer which is not a perfect square, and $n$ is a positive integer then every irreducible factor of $x^{2n} - r$ over $\QQ[x]$ has even degree.


**Question 35**

(a) Let $f (x)$ be an irreducible polynomial of degree 4 in $\QQ[x]$ whose splitting field $K$ over $\QQ$ has Galois group $G = S_4$. 

    Let $\theta$ be a root of $f(x)$. Prove that $\QQ[\theta]$ is an extension of $\QQ$ of degree 4 and that there are no intermediate fields between $\QQ$ and $\QQ[\theta]$.

(b) Prove that if $K$ is a Galois extension of $\QQ$ of degree 4, then there is an intermediate subfield between $K$ and $\QQ$.


**Question 36**

A ring R is called *simple* if its only two-sided ideals are $0$ and $R$.

(a) Suppose $R$ is a commutative ring with 1. Prove $R$ is simple if and only if $R$ is a field.

(b) Let $k$ be a field. Show the ring $M_n (k)$, $n \times n$ matrices with entries in $k$, is a simple ring.


**Question 37**

For a ring $R$, let $U(R)$ denote the multiplicative group of units in $R$. Recall that in an integral domain $R$, $r \in R$ is called *irreducible* if $r$ is not a unit in R, and the only divisors of $r$ have the form $ru$ with $u$ a unit in $R$. 

We call a non-zero, non-unit $r \in R$ *prime* in $R$ if $r \divides ab \implies r \divides a$ or $r \divides b$. 
Consider the ring $R = \{a + b \sqrt{-5}\suchthat a, b \in Z\}$.

(a) Prove $R$ is an integral domain.

(b) Show $U(R) = \{\pm1\}$.

(c) Show $3, 2 + \sqrt{-5}$, and $2 - \sqrt{-5}$ are irreducible in $R$.

(d) Show 3 is not prime in $R$.

(e) Conclude $R$ is not a PID.


**Question 38**

Let $F$ be a field and let $V$ and $W$ be vector spaces over $F$ . 

Make $V$ and $W$ into $F[x]\dash$modules via linear operators $T$ on $V$ and $S$ on $W$ by defining $X \cdot v = T (v)$ for all $v \in V$ and $X \cdot w = S(w)$ for all w $\in$ W . 

Denote the resulting $F[x]\dash$modules by $V_T$ and $W_S$ respectively.

(a) Show that an $F[x]\dash$module homomorphism from $V_T$ to $W_S$ consists of an $F\dash$linear transformation $R : V \to W$ such that $RT = SR$.


**Question 39**

Classify the groups of order $182 = 2 \cdot 7 \cdot 13$.


**Question 40**

Let $G$ be a finite group of order $p^nm$ where $p$ is a prime and
$m$ is not divisible by $p$. Prove that if $H$ is a subgroup of $G$
of order $p^k$ for some $k<n$, then the normalizer of $H$ in $G$
properly contains $H$.


**Question 41**

Let $H$ be a subgroup of $S_n$ of index $n$. Prove:

1.  There is an isomorphism $f: S_n \to S_n$ such that $f(H)$ is the
    subgroup of $S_n$ stabilizing $n$. In particular, $H$ is
    isomorphic to $S_{n-1}$.

2.  The only subgroups of $S_n$ containing $H$ are $S_n$ and $H$.


**Question 42**


-   Prove that a group of order $351=3^3\cdot 13$ cannot be simple.

-   Prove that a group of order $33$ must be cyclic.


**Question 43**


1.  Let $G$ be a group, and $Z(G)$ the center of $G$. Prove that if
    $G/Z(G)$ is cyclic, then $G$ is abelian.

2.  Prove that a group of order $p^n$, where $p$ is a prime and
    $n \geq 1$, has non-trivial center.

3.  Prove that a group of order $p^2$ must be abelian.


**Question 44**

Let $G$ be a finite group.

1.  Prove that if $H < G$ is a proper subgroup, then $G$ is not the
    union of conjugates of $H$.

2.  Suppose that $G$ acts transitively on a set $X$ with $|X| > 1$.
    Prove that there exists an element of $G$ with no fixed points
    in $X$.


**Question 45**

Classify all groups of order $15$ and of order $30$.


**Question 46**

Count the number of $p$-Sylow subgroups of $S_p$.


**Question 47**


1.  Let $G$ be a group of order $n$. Suppose that for every divisor
    $d$ of $n$, $G$ contains at most one subgroup of order $d$. Show
    that $G$ is clyclic.

2.  Let $F$ be a field. Show that every finite subgroup of the group
    of units $F^\times$ is cyclic.


**Question 48**

Let $K$ and $L$ be finite fields. Show that $K$ is contained in $L$
if and only if $\# K = p^r$ and $\# L = p^s$ for the same prime $p$,
and $r \leq s$.


**Question 49**

Let $K$ and $L$ be finite fields with $K \subseteq L$. Prove that
$L$ is Galois over $K$ and that $\mathrm{Gal}(L/K)$ is cyclic.


**Question 50**

Fix a field $F$, a separable polynomial $f\in F[x]$ of degree
$n \geq 3$, and a splitting field $L$ for $f$. Prove that if
$[L:F] = n!$ then:

1.  $f$ is irreducible.

2.  For each root $r$ of $f$, $r$ is the unique root of $f$ in
    $F(r)$.

3.  For every root $r$ of $f$, there are no proper intermediate
    fields $F \subset L \subset F(r)$.


**Question 51**

1.  Show that $\sqrt{2+\sqrt{2}}$ is a root of
    $p(x) = x^2 - 4x^2 + 2 \in \mathbb{Q}[x]$.

2.  Prove that $\mathbb{Q}(\sqrt{2 + \sqrt{2}})$ is a Galois
    extension of $\mathbb{Q}$ and find its Galois group. (Hint: note
    that $\sqrt{2 - \sqrt{2}}$ is another root of $p(x)$).

3.  Let $f(x) = x^3 - 5$. Determine the splitting field $K$ of
    $f(x)$ over $\mathbb{Q}$ and the Galois group of $f(x)$. Give an
    example of a proper sub-extension
    $\mathbb{Q} \subset L \subset K$, such that $L/\mathbb{Q}$ is
    Galois.


**Question 52**

An integral domain $R$ is said to be an *Euclidean domain* if there
is a function $N: R \to \{n\in\mathbb{Z} \mid n\geq 0\}$ such that
$N(0)=0$ and for each $a,b\in R$ with $b\neq 0$, there exist
elements $q,r\in R$ with 
\begin{align*}
  a = qb + r, \quad \text{and} \quad r = 0 \, \text{ or } \, N(r) < N(b).
\end{align*} 

Prove:

1.  The ring $F[[x]]$ of power series over a field $F$ is an
    Euclidean domain.

2.  Every Euclidean domain is a PID.


**Question 53**

Let $F$ be a field, and let $R$ be the subring of $F[X]$ of
polynomials with $X$ coefficient equal to $0$. Prove that $R$ is not
a UFD.


**Question 54**

$R$ is a commutative ring with 1. Prove that if $I$ is a maximal
ideal in $R$, then $R/I$ is a field. Prove that if $R$ is a PID,
then every nonzero prime ideal in $R$ is maximal. Conclude that if
$R$ is a PID and $p\in R$ is prime, then $R/(p)$ is a field.


**Question 55**

Prove that any square matrix is conjugate to its transpose matrix.
(You may prove it over $\mathbb{C}$).


**Question 56**

Determine the number of conjugacy classes of $16 \times 16$ matrices
with entries in $\mathbb{Q}$ and minimal polynomial
$(x^2+1)^2(x^3+2)^2$.


**Question 57**

Let $V$ be a vector space over a field $F$. The evaluation map
$e\colon V \to (V^\vee)^\vee$ is defined by
$e(v)(f) \colonequals f(v)$ for $v\in V$ and $f\in V^\vee$.

1.  Prove that $e$ is an injection.

2.  Prove that $e$ is an isomorphism if and only if $V$ is finite
    dimensional.


**Question 58**

Let $R$ be a principal ideal domain that is not a field, and write
$F$ for its field of fractions. Prove that $F$ is not a finitely
generated $R$-module.


**Question 59**

Carefully state Zorn's lemma and use it to prove that every vector
space has a basis.


**Question 60**

Show that no finite group is the union of conjugates of a proper subgroup.


**Question 61**

Classify all groups of order 18 up to isomorphism.


**Question 62**

Let $\alpha,\beta$ denote the unique positive
real $5^{\text{th}}$ root of 7 and $4^{\text{th}}$ root of 5,
respectively. Determine the degree of $\mathbb Q(\alpha,\beta)$ over $\mathbb Q$.


**Question 63**

Show that the field extension $\mathbb Q\subseteq\mathbb Q\left(
\sqrt{2+\sqrt2}\right)$ is Galois and determine its Galois group.


**Question 64**

Let $M$ be a square matrix over a field $K$. Use a suitable canonical
form to show that $M$ is similar to its transpose $M^T$.


**Question 65**

Let $G$ be a finite group and $\pi_0$, $\pi_1$ be two irreducible representations of $G$. Prove or disprove the following assertion:
$\pi_0$ and $\pi_1$ are equivalent if and only if $\det\pi_0(g)=\det\pi_1(g)$
for all $g\in G$.


**Question 66**

Let $R$ be a Noetherian ring. Prove that $R[x]$ and $R[[x]]$ are both
Noetherian. (The first part of the question is asking you to prove the
Hilbert Basis Theorem, not to use it!)


**Question 67**

Classify (with proof) all fields with finitely many elements.


**Question 68**

Suppose $A$ is a commutative ring and $M$ is a finitely presented module.
Given any surjection $\phi:A^n\rightarrow M$ from a finite free
$A$-module, show that $\ker\phi$ is finitely generated.


**Question 69**

Classify all groups of order 57.


**Question 70**

Show that a finite simple group cannot have a 2-dimensional irreducible
representation over $\mathbb C$. 

> Hint: the determinant might prove useful.


**Question 71**

Let $G$ be a finite simple group. Assume that every proper subgroup
of $G$ is abelian. Prove that then $G$ is cyclic of prime order.


**Question 72**

Let $a\in\mathbb N$, $a>0$. Compute the Galois group of the splitting field
of the polynomial $x^5-5a^4x+a$ over $\mathbb Q$.


**Question 73**

Recall that an inner automorphism of a group is an automorphism given by conjugation by an element of the group. An outer automorphism is an automorphism that is not inner.

- Prove that $S_5$ has a subgroup of order 20.
- Use the subgroup from (a) to construct a degree 6 permutation representation of $S_5$ (i.e., an embedding $S_5 \hookrightarrow S_6$ as a transitive permutation group on 6 letters).
- Conclude that $S_6$ has an outer automorphism.


**Question 74**

Let $A$ be a commutative ring and $M$ a finitely generated $A$-module.
Define
\begin{align*}
  \Ann(M) = \{a \in A: am = 0 \text{ for all } m \in M\}
.\end{align*}
Show that for a prime ideal $\mathfrak p \subset A$, the following are equivalent:

- $\Ann(M) \not\subset \mathfrak p$

- The localization of $M$ at the prime ideal $\mathfrak p$ is $0$.

- $M \otimes_A k(\mathfrak p) = 0$, where $k(\mathfrak p) = A_{\mathfrak p}/\mathfrak p A_{\mathfrak p}$ is the residue field of $A$ at $\mathfrak p$.


**Question 75**

Let $A = \CC[x,y]/(y^2-(x-1)^3 - (x-1)^2)$.

- Show that $A$ is an integral domain and sketch the $\RR$-points of $\text{Spec} A$.
- Find the integral closure of $A$. Recall that for an integral domain $A$ with fraction field $K$, the integral closure of $A$ in $K$ is the set of all elements of $K$ integral over $A$.


**Question 76**

Let $R = k[x,y]$ where $k$ is a field, and let $I=(x,y)R$.

  - Show that
    \begin{align*}
    0 \to R \mapsvia{\phi} R \oplus R \mapsvia{\psi} R \to k \to 0
    \end{align*}
    where $\phi(a) = (-ya,xa)$, $\psi((a,b)) = xa+yb$ for $a,b \in R$, is a projective resolution of the $R$-module $k \simeq R/I$.

  - Show that $I$ is not a flat $R$-module by computing $\Tor_i^R(I,k)$


**Question 77**


- Find an irreducible polynomial of degree 5 over the
  field $\mathbb Z/2$ of two elements and use it to construct
  a field of order 32 as a quotient of the
  polynomial ring $\mathbb Z/2[x]$.
- Using the polynomial found in part (a), find a $5\times5$
  matrix $M$ over $\mathbb Z/2$ of order 31, so that $M^{31}=I$
  but $M\neq I$.


**Question 78**

Find the minimal polynomial of $\sqrt2+\sqrt3$ over $\mathbb Q$.
Justify your answer.


**Question 79**

\hfill
 - Let $R$ be a commutative ring with no nonzero nilpotent
   elements. Show that the only units in the polynomial ring
   $R[x]$ are the units of $R$, regarded as constant polynomials.
 - Find all units in the polynomial ring $\mathbb Z_4[x]$.


**Question 80**

Let $p$, $q$ be two distinct primes. Prove that there is at most one
non-abelian group of order $pq$ and describe the pairs $(p,q)$
such that there is no non-abelian group of order $pq$.


**Question 81**


- Let $L$ be a Galois extension of a field $K$ of degree 4.
  What is the minimum number of subfields there could
  be strictly between $K$ and $L$? What is the maximum
  number of such subfields? Give examples where these
  bounds are attained.
- How do these numbers change if we assume only that $L$
  is separable (but not necessarily Galois) over $K$?


**Question 82**

Let $R$ be a commutative algebra over $\mathbb C$. A derivation of $R$ is a
$\mathbb C$-linear map $D:R\rightarrow R$ such that (i) $D(1)=0$ and
(ii) $D(ab)=D(a)b+aD(b)$ for all $a,b\in R$.

- Describe all derivations of the polynomial ring $\mathbb C[x]$.

- Let $A$ be the subring (or $\mathbb C$-subalgebra) of
  $\mathrm{End}_{\mathbb C}(\mathbb C[x])$ generated by all derivations
  of $\mathbb C[x]$ and the left multiplications by $x$.
  Prove that $\mathbb C[x]$ is a simple left $A$-module.
  > Note that the inclusion $A\rightarrow\mathrm{End}_{\mathbb C}(\mathbb C[x])$
  defines a natural left $A$-module structure on $\mathbb C[x]$.


**Question 83**

Let $G$ be a non-abelian group of order $p^3$ with $p$ a prime.

- Determine the order of the center $Z$ of $G$.

- Determine the number of inequivalent complex
  1-dimensional representations of $G$.

- Compute the dimensions of all the inequivalent irreducible
  representations of $G$ and verify that the number of such
  representations equals the number of conjugacy classes of
  $G$.


**Question 84**


- Let $G$ be a group (not necessarily finite) that contains
  a subgroup of index $n$. Show that $G$ contains a
  \textit{normal} subgroup $N$ such that $n\leq[G:N]\leq n!$

- Use part (a) to show that there is no simple group
  of order 36.


**Question 85**

Let $p$ be a prime, let $\mathbb F_p$ be the $p$-element field,
and let $K=\mathbb F_p(t)$ be the field of rational functions in
$t$ with coefficients in $\mathbb F_p$. Consider the polynomial $f(x)=
x^p-t\in K[x]$.

- Show that $f$ does not have a root in $K$.

- Let $E$ be the splitting field of $f$ over $K$.
  Find the factorization of $f$ over $E$.

- Conclude that $f$ is irreducible over $K$.


**Question 86**

Recall that a ring $A$ is called \textit{graded} if it admits a direct
sum decomposition $A=\oplus_{n=0}^{\infty}A_n$ as abelian groups, with the
property that $A_iA_j\subseteq A_{i+j}$ for all $i,j\geq 0$.
Prove that a graded commutative ring $A=\oplus_{n=0}^{\infty} A_n$
is Noetherian if and only if $A_0$ is Noetherian and $A$ is finitely
generated as an algebra over $A_0$.


**Question 87**

Let $R$ be a ring with the property that $a^2=a$ for all $a\in R$.

- Compute the Jacobson radical of $R$.

- What is the characteristic of $R$?

- Prove that $R$ is commutative.

- Prove that if $R$ is finite, then $R$ is isomorphic
  (as a ring) to $(\mathbb Z/2\mathbb Z)^d$ for some $d$.


**Question 88**

Let $\overline{\mathbb F_p}$ denote the algebraic closure of $\mathbb F_p$. Show that
the Galois group $\Gal(\overline{\mathbb F_p}/\mathbb F_p)$
has no non-trivial finite subgroups.


**Question 89**

Let $C_p$ denote the cyclic group of order $p$.

- Show that $C_p$ has two irreducible representations over
  $\mathbb Q$ (up to isomorphism), one of dimension 1
  and one of dimension $p-1$.

- Let $G$ be a finite group, and let $\rho:G\rightarrow
  \GL_n(\mathbb Q)$ be a representation of $G$ over $\mathbb Q$.
  Let $\rho_{\mathbb C}:G\rightarrow\GL_n(\mathbb C)$ denote
  $\rho$ followed by the inclusion $\GL_n(\mathbb Q)\rightarrow
  \GL_n(\mathbb C)$. Thus $\rho_{\mathbb C}$ is a representation
  of $G$ over $\mathbb C$, called the \textit{complexification}
  of $\rho$. We say that an irreducible representation $\rho$
  of $G$ is \textit{absolutely irreducible} if its
  complexification remains irreducible over $\mathbb C$.\\
  Now suppose $G$ is abelian and that every representation
  of $G$ over $\mathbb Q$ is absolutely irreducible. Show that
  $G\cong(C_2)^k$ for some $k$ (i.e., is a product of
  cyclic groups of order 2).


**Question 90**

Let $G$ be a finite group and $\mathbb Z[G]$ the internal group algebra.
Let $\mathcal Z$ be the center of $\mathbb Z[G]$. For each conjugacy class
$C\subseteq G$, let $P_C=\sum_{g\in C}g$.

- Show that the elements $P_C$ form a $\mathbb Z$-basis for
  $\mathcal Z$. Hence $\mathcal Z\cong\mathbb Z^d$ as an
  abelian group, where $d$ is the number of
  conjugacy classes in $G$.

- Show that if a ring $R$ is isomorphic to $\mathbb Z^d$ as
  an abelian group, then every element in $R$ satisfies
  a monic integral polynomial.
  
  > **Hint:** Let $\{v_1,\dots,v_d\}$ be a basis of
    $R$ and for a fixed non-zero $r\in R$, write $rv_i=\sum_j
    a_{ij}v_j$. Use the Hamilton-Cayley theorem.

- Let $\pi:G\rightarrow\GL(V)$ be an irreducible representation
  of $G$ (over $\mathbb C$). Show that $\pi(P_C)$ acts on $V$
  as multiplication by the scalar
  
  \begin{align*}
  \frac{|C|\chi_{\pi}(C)}{\dim V},
  \end{align*}
  
  where $\chi_{\pi}(C)$ is the value of the character
  $\chi_{\pi}$ on any element of $C$.

- Conclude that $|C|\chi_{\pi}(C)/\dim V$ is an algebraic
  integer.


**Question 91**


- Suppose that $G$ is a finitely generated group. Let $n$
  be a positive integer. Prove that $G$ has only finitely
  many subgroups of index $n$

- Let $p$ be a prime number. If $G$ is any finitely-generated
  abelian group, let $t_p(G)$ denote the number of
  subgroups of $G$ of index $p$. Determine the possible
  values of $t_p(G)$ as $G$ varies over all
  finitely-generated abelian groups.


**Question 92**

Suppose that $G$ is a finite group of order 2013. Prove that $G$ has
a normal subgroup $N$ of index 3 and that $N$ is a cyclic group.
Furthermore, prove that the center of $G$ has order divisible by 11.
(You will need the factorization $2013=3\cdot11\cdot61$.)


**Question 93**

This question concerns an extension $K$ of $\mathbb Q$ such that
$[K:\mathbb Q]=8$. Assume that $K/\mathbb Q$ is Galois and let
$G=\Gal(K/\mathbb Q)$. Furthermore, assume that $G$ is non-abelian.

- Prove that $K$ has a unique subfield $F$ such that
  $F/\mathbb Q$ is Galois and $[F:\mathbb Q]=4$.

- Prove that $F$ has the form $F=\mathbb Q(\sqrt{d_1},\sqrt{d_2})$
  where $d_1,d_2$ are non-zero integers.

- Suppose that $G$ is the quaternionic group. Prove
  that $d_1$ and $d_2$ are positive integers.


**Question 94**

This question concerns the polynomial ring $R=\mathbb Z[x,y]$ and the ideal
$I=(5,x^2+2)$ in $R$.

- Prove that $I$ is a prime ideal of $R$ and that $R/I$ is
  a PID.

- Give an explicit example of a maximal ideal of $R$ which
  contains $I$. (Give a set of generators for such an ideal.)

- Show that there are infinitely many distinct maximal ideals
  in $R$ which contain $I$.


**Question 95**

Classify all groups of order 2012 up to isomorphism. 

> Hint: 503 is prime.


**Question 96**

For any positive integer $n$, let $G_n$ be the group generated by
$a$ and $b$ subject to the following three relations:
\begin{align*}
a^2=1, \quad b^2=1, \quad \text{and} \quad (ab)^n=1.
.\end{align*}

- Find the order of the group $G_n$


**Question 97**

Determine the Galois groups of the following polynomials over $\mathbb Q$.

- $f(x)=x^4+4x^2+1$

- $f(x)=x^4+4x^2-5$.


**Question 98**

Let $R$ be a (commutative) principal ideal domain, let $M$ and $N$ be
finitely generated free $R$-modules, and let $\varphi:M\rightarrow N$ be
an $R$-module homomorphism.

- Let $K$ be the kernel of $\varphi$. Prove that
  $K$ is a direct summand of $M$.

- Let $C$ be the image of $\varphi$. Show by example
  (specifying $R$, $M$, $N$, and $\varphi$) that $C$
  need not be a direct summand of $N$.


**Question 99**

In this problem, as you apply Sylow's Theorem, state precisely which portions
you are using.

- Prove that there is no simple group of order 30.

- Suppose that $G$ is a simple group of order 60. Determine
  the number of $p$-Sylow subgroups of $G$ for each prime
  $p$ dividing 60, then prove that $G$ is isomorphic to
  the alternating group $A_5$.

> Note: in the second part, you needn't show that $A_5$ is simple.
You need only show that if there is a simple group of order 60, then
it must be isomorphic to $A_5$.


**Question 100**

Describe the Galois group and the intermediate fields of the cyclotomic
extension $\mathbb Q(\zeta_{12})/\mathbb Q$.


**Question 101**

Let
\begin{align*}
R=\mathbb Z[x]/(x^2+x+1).
\end{align*}

- Answer the following questions with suitable justification.
    - Is $R$ a Noetherian ring?
    - Is $R$ an Artinian ring?

- Prove that $R$ is an integrally closed domain.


**Question 102**

Let $R$ be a commutative ring. Recall that an element $r$ of $R$ is
\textit{nilpotent} if $r^n=0$ for some positive integer $n$ and that
the \textit{nilradical} of $R$ is the set $N(R)$ of nilpotent
elements.

- Prove that
  \begin{align*}
  N(R)=\cap_{P\text{ prime}}P.
  .\end{align*}
  
  > Hint: given a non-nilpotent element $r$ of $R$, you may
    wish to construct a prime ideal that does not
    contain $r$ or its powers.

- Given a positive integer $m$, determine the nilradical
  of $\mathbb Z/(m)$.

- Determine the nilradical of $\mathbb C[x,y]/(y^2-x^3)$.

- Let $p(x,y)$ be a polynomial in $\mathbb C[x,y]$ such that
  for any complex number $a$, $p(a,a^{3/2})=0$. Prove that
  $p(x,y)$ is divisible by $y^2-x^3$.


**Question 103**

Given a finite group $G$, recall that its *regular representation*
is the representation on the complex group algebra $\mathbb C[G]$ induced by
left multiplication of $G$ on itself and its \textit{adjoint representation}
is the representation on the complex group algebra $\mathbb C[G]$ induced
by conjugation of $G$ on itself.

- Let $G=\GL_2(\mathbb F_2)$. Describe the number and dimensions of
  the irreducible representations of $G$. Then describe the
  decomposition of its regular representation as a direct
  sum of irreducible representations.

- Let $G$ be a group of order 12. Show that its adjoint
  representation is reducible; that is, there is
  an $H$-invariant subspace of $\mathbb C[H]$ besides 0 and
  $\mathbb C[H]$.


**Question 104**

Let $R$ be a commutative integral domain. Show that the following
are equivalent:

- $R$ is a field;

- $R$ is a semi-simple ring;

- Any $R$-module is projective.


**Question 105**

Let $p$ be a positive prime number, $\mathbb F_p$ the field with $p$ elements,
and let $G=\text{GL}_2(\mathbb F_p)$.

- Compute the order of $G$, $|G|$.

- Write down an explicit isomorphism from $\mathbb Z/p\mathbb Z$ to
  \begin{align*}
  U=\left\{
  \begin{pmatrix}
    1 & a\\
    0 & 1
  \end{pmatrix}
  \bigg|a\in\mathbb F_p\right\}.
  \end{align*}

- How many subgroups of order $p$ does $G$ have? 
  
  > Hint: compute $gug\inv$ for $g\in G$ and $u\in U$; use this to find the size of the normalizer of $U$ in $G$.


**Question 106**


- Give definitions of the following terms:
  (i) a finite length (left) module, (ii) a
  composition series for a module, and (iii) the length
  of a module,

- Let $l(M)$ denote the length of a module $M$. Prove that if
  \begin{align*}
  0\rightarrow M_1\rightarrow M_2\rightarrow\dots\rightarrow
  M_n\rightarrow 0
  .\end{align*}
  
  is an exact sequence of modules of finite length, then
  \begin{align*}
  \sum_{i=1}^n(-1)^kl(M_i)=0.
  .\end{align*}


**Question 107**

Let $\mathbb F$ be a field of characteristic $p$, and $G$ a group of
order $p^n$. Let $R=\mathbb F[G]$ be the group ring (group algebra)
of $G$ over $\mathbb F$, and let $u:=\sum_{x\in G}x$ (so $u$ is an element of
$R$).

- Prove that $u$ lies in the center of $R$.

- Verify that $Ru$ is a 2-sided ideal of $R$.

- Show there exists a positive integer $k$ such that $u^k=0$.
  Conclude that for such a $k$, $(Ru)^k=0$.

- Show that $R$ is **not** a semi-simple ring.
  
  > **Warning:** Please use the definition of a semi-simple
  ring: do **not** use the result that a finite length
  ring fails to be semisimple if and only if it has a non-zero
  nilpotent ideal.


**Question 108**

Let $f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_0\in\mathbb Z[x]$
(where $a_n\neq 0$) and let $R=\mathbb Z[x]/(f)$.
Prove that $R$ is a finitely generated module over $\mathbb Z$ if and only if
$a_n=\pm 1$.


**Question 109**

Consider the ring
\begin{align*}
S=C[0,1]=\{f:[0,1]\rightarrow\mathbb R:f\text{ is continuous}\}
.\end{align*}

with the usual operations of addition and multiplication of functions.

- What are the invertible elements of $S$?

- For $a\in[0,1]$, define $I_a=\{f\in S:f(a)=0\}$.
  Show that $I_a$ is a maximal ideal of $S$.

- Show that the elements of any proper ideal of $S$ have a
  common zero, i.e., if $I$ is a proper ideal of $S$, then
  there exists $a\in[0,1]$ such that $f(a)=0$ for all $f\in I$.
  Conclude that every maximal ideal of $S$ is of the form
  $I_a$ for some $a\in[0,1]$. 

  > **Hint**: As $[0,1]$ is compact, every open cover of $[0,1]$ contains a finite subcover.


**Question 110**

Let $F$ be a field of characteristic zero, and let $K$
be an *algebraic* extension of $F$ that possesses the following
property: every polynomial $f\in F[x]$ has a root in $K$.
Show that $K$ is algebraically closed.\\

> **Hint:** if $K(\theta)/K$ is algebraic, consider $F(\theta)/F$
  and its normal closure; primitive elements might be of help.


**Question 111**

Let $G$ be the unique non-abelian group of order 21.

- Describe all 1-dimensional complex representations of $G$.

- How many (non-isomorphic) irreducible complex representations
  does $G$ have and what are their dimensions?

- Determine the character table of $G$.


**Question 112**


- Classify all groups of order $2009=7^2\times 41$.

- Suppose that $G$ is a group of order 2009. How many intermediate groups are
  there—that is, how many groups H are there with $1\subsetneq H\subsetneq G$, where both
  inclusions are proper? (There may be several cases to consider.)


**Question 113**

Let $K$ be a field. A discrete valuation on $K$ is a function $\nu:
K\setminus\{0\}\rightarrow\mathbb Z$ such that

- $\nu(ab)=\nu(a)+\nu(b)$

- $\nu$ is surjective

- $\nu(a+b)\geq\text{min}\{(\nu(a),\nu(b)\}$ for
  $a,b\in K\setminus\{0\}$ with $a+b\neq 0$.

Let $R:=\{x\in K\setminus\{0\}:\nu(x)\geq0\}\cup\{0\}$. Then
$R$ is called the valuation ring of $\nu$.

Prove the following:

- $R$ is a subring of $K$ containing the 1 in $K$.

- for all $x\in K\setminus\{0\}$, either $x$ or
  $x\inv$ is in $R$.

- $x$ is a unit of $R$ if and only if $\nu(x)=0$.

- Let $p$ be a prime number, $K=\mathbb Q$,
  and $\nu_p:\mathbb Q\setminus\{0\}\rightarrow\mathbb Z$
  be the function defined by $\nu_p(\frac ab)=n$ where
  $\frac ab=p^n\frac cd$ and $p$ does not divide $c$ and $d$.
  Prove that the corresponding valuation ring $R$ is the ring
  of all rational numbers whose denominators are relatively
  prime to $p$.


**Question 114**

Let $F$ be a field of characteristic not equal to 2.

- Prove that any extension $K$ of $F$ of degree 2
  is of the form $F(\sqrt D)$ where $D\in F$
  is not a square in $F$ and, conversely, that each such
  extension has degree 2 over $F$.

- Let $D_1,D_2\in F$ neither of which is a square in $F$.
  Prove that $[F(\sqrt{D_1},\sqrt{D_2}):F]=4$ if
  $D_1D_2$ is not a square in $F$ and is of degree
  2 otherwise.


**Question 115**

Let $F$ be a field and $p(x)\in F[x]$ an irreducible polynomial.

- Prove that there exists a field extension $K$ of $F$
  in which $p(x)$ has a root.

- Determine the dimension of $K$ as a vector space over $F$
  and exhibit a vector space basis for $K$.

- If $\theta\in K$ denotes a root of $p(x)$, express
  $\theta\inv$ in terms of the basis found in part (b).

- Suppose $p(x)=x^3+9x+6$. Show $p(x)$ is irreducible over
  $\mathbb Q$. If $\theta$ is a root of $p(x)$, compute
  the inverse of $(1+\theta)$ in $\mathbb Q(\theta)$.


**Question 116**

Fix a ring $R$, an $R$-module $M$, and an $R$-module homomorphism
$f:M\rightarrow M$.

- If $M$ satisfies the descending chain condition on submodules,
  show that if $f$ is injective, then $f$ is surjective.
  
  > Hint: note that if $f$ is injective, so are
    $f\circ f$, $f\circ f\circ f$, etc.

- Give an example of a ring $R$, an $R$-module $M$,
  and an injective $R$-module homomorphism $f:M\rightarrow M$
  which is not surjective.

- If $M$ satisfies the ascending chain condition on submodules,
  show that if $f$ is surjective, then $f$ is injective.

- Give an exampe of a ring $R$, and $R$-module $M$, and
  a surjective $R$-module homomorphism $f:M\rightarrow M$
  which is not injective.


**Question 117**

Let $G$ be a finite group, $k$ an algebraically closed field, and $V$
an irreducible $k$-linear representation of $G$.

- Show that $\hom_{kG}(V,V)$ is a division algebra with $k$
  in its center.

- Show that $V$ is finite-dimensional over $k$, and conclude
  that $\hom_{kG}(V,V)$ is also finite dimensional.

- Show the inclusion $k\hookrightarrow\hom_{kG}(V,V)$ found
  in (a) is an isomorphism. (For $f\in\hom_{kG}(V,V)$, view
  $f$ as a linear transformation and consider $f-\alpha I$,
  where $\alpha$ is an eigenvalue of $f$).


**Question 118**

Let $f(x)$ be an irreducible polynomial of degree 5 over the field
$\mathbb Q$ of rational numbers with exactly 3 real roots.

- Show that $f(x)$ is not solvable by radicals.

- Let $E$ be the splitting field of $f$ over $\mathbb Q$.
  Construct a Galois extension $K$ of degree 2 over
  $\mathbb Q$ lying in $E$ such that \textit{no} field $F$
  strictly between $K$ and $E$ is Galois over $\mathbb Q$.


**Question 119**

Let $F$ be a finite field. Show for any positive integer $n$ that
there are irreducible polynomials of degree $n$ in $F[x]$.


**Question 120**

Show that the order of the group $\text{GL}_n(\mathbb F_q)$ of invertible
$n\times n$ matrices over the field $\mathbb F_q$ of $q$ elements is given by
$(q^n-1)(q^n-q)\dots(q^n-q^{n-1})$.


**Question 121**


- Let $R$ be a commutative principal ideal domain. Show that
  any $R$-module $M$ generated by two elements takes the form
  $R/(a)\oplus R/(b)$ for some $a,b\in R$. What more
  can you say about $a$ and $b$?

- Give a necessary and sufficient condition for two direct sums
  as in part (a) to be isomorphic as $R$-modules.


**Question 122**

Let $G$ be the subgroup of $\text{GL}_3(\mathbb C)$ generated by the three
matrices
\begin{align*}
A=
\begin{pmatrix}
  0 & 0 & 1\\
  0 & 1 & 0\\
  1 & 0 & 0
\end{pmatrix},
\quad B=
\begin{pmatrix}
  0 & 0 & 1\\
  1 & 0 & 0\\
  0 & 1 & 0
\end{pmatrix},
\quad C=
\begin{pmatrix}
  i & 0 & 0\\
  0 & 1 & 0\\
  0 & 0 & 1
\end{pmatrix}
\end{align*}

where $i^2=-1$. Here $\mathbb C$ denotes the complex field.

- Compute the order of $G$.

- Find a matrix in $G$ of largest possible order (as an element
  of $G$) and compute this order.

- Compute the number of elements in $G$ with this largest
  order.


**Question 123**


- Let $G$ be a group of (finite) order $n$. Show that any
  irreducible left module over the group algebra $\mathbb CG$
  has complex dimension at least $\sqrt n$.

- Give an example of a group $G$ of order $n\geq5$ and an
  irreducible left module over $\mathbb CG$ of complex dimension
  $\lfloor\sqrt n\rfloor$, the greatest integer to
  $\sqrt n$.


**Question 124**

Use the rational canonical form to show that any square matrix $M$ over
a field $k$ is similar to its transpose $M^t$, recalling that $p(M)=0$
for some $p\in k[t]$ if and only if $p(M^t)=0$.


**Question 125**

Let $K$ be a field of characteristic zero and $L$ a Galois extension
of $K$. Let $f$ be an irreducible polynomial in $K[x]$ of degree 7 and
suppose $f$ has no zeroes in $L$. Show that $f$ is irreducible
in $L[x]$.


**Question 126**

Let $K$ be a field of characteristic zero and $f\in K[x]$ an
irreducible polynomial of degree $n$. Let $L$ be a splitting field for
$f$. Let $G$ be the group of automorphisms of $L$ which act trivially
on $K$.

- Show that $G$ embeds in the symmetric group $S_n$.

- For each $n$, give an example of a field $K$ and polynomial
  $f$ such that $G=S_n$.

- What are the possible groups $G$ when $n=3$. Justify
  your answer.


**Question 127**

Show there are exactly two groups of order 21 up to isomorphism.


**Question 128**

Let $K$ be the field $\mathbb Q(z)$ of rational functions in a variable $z$
with coeffiecients in the rational field $\mathbb Q$.
Let $n$ be a positive integer. Consider the polynomial $x^n-z\in K[x]$.

- Show that the polynomial $x^n-z$ is irreducible over $K$.

- Describe the splitting field of $x^n-z$ over $K$.

- Determine the Galois group of the splitting field
  of $x^5-z$ over the field $K$.


**Question 129**


- Let $p<q<r$ be prime integers. Show that a group of order
  $pqr$ cannot be simple.

- Consider groups of orders $2^2\cdot 3\cdot p$ where $p$
  has the values 5, 7, and 11. For each of those values
  of $p$, either display a simple group of order
  $2^2\cdot 3\cdot p$, or show that there cannot
  be a simple group of that order.


**Question 130**

Let $K/F$ be a finite Galois extension and let $n=[K:F]$. There is a theorem
(often referred to as the "normal basis theorem") which states that there
exists an irreducible polynomial $f(x)\in F[x]$ whose
roots form a basis for $K$ as a vector space over $F$. You may assume
that theorem in this problem.

- Let $G=\Gal(K/F)$. The action of $G$ on $K$ makes $K$ into
  a finite-dimensional representation space for $G$ over $F$.
  Prove that $K$ is isomorphic to the regular representation
  for $G$ over $F$.

  > The regular representation is defined by letting $G$ act
  on the group algebra $F[G]$ by multiplication on
  the left.

- Suppose that the Galois group $G$ is cyclic and that $F$
  contains a primitive $n^{\text{th}}$ root of unity. Show that
  there exists an injective homomorphism $\chi:G\rightarrow
  F^{\times}$.

- Show that $K$ contains a non-zero element $a$ with the
  following property:
  \begin{align*}
  g(a)=\chi(g)\cdot a
  .\end{align*}
  
  for all $g\in G$.

- If $a$ has the property stated in (c), show that $K=F(a)$ and
  that $a^n\in F^{\times}$.


**Question 131**

Let $G$ be the group of matrices of the form
\begin{align*}
\begin{pmatrix}
  1 & a & b\\
  0 & 1 & c\\
  0 & 0 & 1
\end{pmatrix}
.\end{align*}

with entries in the finite field $\mathbb F_p$ of $p$ element, where
$p$ is a prime.

- Prove that $G$ is non-abelian.

- Suppose $p$ is odd. Prove that $g^p=I_3$ for all $g\in G$.

- Suppose that $p=2$. It is known that there are exactly
  two non-abelian groups of order 8, up to isomorphism:
  the dihedral group $D_8$ and the quaternionic group.
  Assuming this fact without proof, determine which
  of these groups $G$ is isomorphic to.


**Question 132**

There are five nonisomorphic groups of order 8. For
each of those groups $G$, find the smallest positive integer n such that there is an
injective homomorphism $\varphi: G\rightarrow S_n$.


**Question 133**

For any group $G$ we define $\Omega(G)$ to be the image of the group
homomorphism $\rho:G\rightarrow\Aut(G)$ where $\rho$ maps
$g\in G$ to the conjugation automorphism $x\mapsto gxg\inv$.
Starting with a group $G_0$, we define $G_1=\Omega(G_0)$ and
$G_{i+1}=\Omega(G_i)$ for all $i\geq 0$. If $G_0$ is of order
$p^e$ for a prime $p$ and integer $e\geq 2$, prove that $G_{e-1}$
is the trivial group.


**Question 134**

Let $\mathbb F_2$ be the field with two elements.

- What is the order of $\text{GL}_3(\mathbb F_2)$?

- Use the fact that $\text{GL}_3(\mathbb F_2)$ is a simple group
  (which you should not prove) to find the number
  of elements of order 7 in $\text{GL}_3(\mathbb F_2)$.


**Question 135**

Let $G$ be a finite abelian group. Let $f:\mathbb Z^m\rightarrow G$ be a
surjection of abelian groups. We may think of $f$ as a homomorphism
of $\mathbb Z$-modules. Let $K$ be the kernel of $f$.

- Prove that $K$ is isomorphic to $\mathbb Z^m$.

- We can therefore write the inclusion map
  $K\rightarrow\mathbb Z^m$ as $\mathbb Z^m\rightarrow\mathbb Z^m$
  and represent it by an $m\times m$ integer matrix
  $A$. Prove that $|\det A|=|G|$.


**Question 136**

Let $R=C([0,1])$ be the ring of all continuous real-valued functions
on the closed interval $[0,1]$, and for each $c\in[0,1]$, denote by
$M_c$ the set of all functions $f\in R$ such that $f(c)=0$.

- Prove that $g\in R$ is a unit if and only if $g(c)\neq0$
  for all $c\in[0,1]$.

- Prove that for each $c\in[0,1]$, $M_c$ is a maximal ideal of
  $R$.

- Prove that if $M$ is a maximal ideal of $T$, then
  $M=M_c$ for some $c\in[0,1]$. 

  > Hint: compactness of $[0,1]$ may be relevant.


**Question 137**

Let $R$ and $S$ be commutative rings, and $f:R\rightarrow S$
a ring homomorphism.

- Show that if $I$ is a prime ideal of $S$, then
  \begin{align*}
  f\inv(I)=\{r\in R:f(r)\in I\}
  \end{align*}
  
  is a prime ideal of $R$.

- Let $N$ be the set of nilpotent elements of $R$:
  \begin{align*}
  N=\{r\in R:r^m=0\text{ for some }m\geq 1\}.
  .\end{align*}
  
  $N$ is called the \textit{nilradical} of $R$. Prove that
  it is an ideal which is contained in every prime ideal.

- Part (a) lets us define a function
  \begin{align*}
  f^*:\{\text{prime ideals of }S\} &\rightarrow
  \{\text{prime ideals of }R\}.
  I &\mapsto f\inv(I).
  .\end{align*}
  
  Let $N$ be the nilradical of $R$. Show that if
  $S=R/N$ and $f:R\rightarrow R/N$ is the quotient map,
  then $f^*$ is a bijection


**Question 138**

Consider the polynomial $f(x)=x^{10}+x^5+1\in\mathbb Q[x]$ with
splitting field $K$ over $\mathbb Q$.

- Determine whether $f(x)$ is irreducible over $\mathbb Q$ and find
  $[K:\mathbb Q]$.

- Determine the structure of the Galois group
  $\Gal(K/\mathbb Q)$.


**Question 139**

For each prime number $p$ and each positive integer $n$, how many
elements $\alpha$ are there in $\mathbb F_{p^n}$ such that
$F_p(\alpha)=F_{p^6}$?


**Question 140**

Assume that $K$ is a cyclic group, $H$ is an arbitrary group, and $\varphi_1$
and $\varphi_2$ are homomorphisms from $K$ into $\Aut(H)$ such that
$\varphi_1(K)$ and $\varphi_2(K)$ are conjugate subgroups
of $\Aut(H)$.

Prove by constructing an explicit isomorphism that
$H\rtimes_{\varphi_1}K\cong H\rtimes_{\varphi_2} K$.

> Suppose $\sigma_{\varphi_1}(K)\sigma\inv=\varphi_2(K)$
so that for some $a\in\mathbb Z$ we have $\sigma\varphi_1(k)\sigma\inv
=\varphi_2(k)^a$ for all $k\in K$. Show that the map $\psi:H
\rtimes_{\varphi_1}K\rightarrow H\rtimes_{\varphi_2}K$
defined by $\psi((h,k))=(\sigma(h),k^a)$ is a homomorphism.
Show $\psi$ is bijective by construcing a 2-sided inverse.

# Real Analysis (85 Questions)

**Question 1**

Prove or disprove each of the following statements.

(a) If $f$ is of bounded variation on $[0,1]$, then it is continuous on $[0,1]$.

(b) If $f : [0, 1] → [0, 1]$ is a continuous function, then there exists $x_0 \in [0, 1]$ such that $f(x_0) = x_0$.

(c) Let $\{f_n\}$ be a sequence of uniformly continuous functions on an interval $I$. If $\{f_n\}$ converges uniformly to a function $f$ on $I$, then $f$ is also uniformly continuous on $I$.

(h) If $f$ is differentiable on a connected set $E \subset \mathbb{R}^n$, then for any $x, y \in E$, there exists $z \in E$ such that $f(x) - f(y) = \nabla f(z)(x - y)$.  


**Question 2**

Prove or disprove each of the following statements.

(d) If $\lim_{n\to\infty} |a_n+1/a_n|$ exists, then $\lim_{n\to \infty} |a_n|^{1/n}$ exists and the two limits are equal.

(e) If $\sum_{n=1}^\infty a_n x^n$ converges for all $x ∈ [0, 1]$, then $\lim_{x\to 1^-} \sum_{n=1}^\infty a_n x^n=\sum_{n=1}^\infty a_n$


**Question 3**

Prove or disprove each of the following statements.

(f) If $E \subset \mathbb{R}$ and 

    $\mu(E) = \inf\{\sum_{I_i \in S} |I_i| : S = \{I_i\}_{i=1}^n \text{ such that } E \subset \union_{i=1}^n I_i \text{ for some } n \in \mathbb{N}\}$

    then $\mu$ coincides with the outer measure of $E$.

(g) If $E$ is a Borel set and $f$ is a measurable function, then $f^{-1}(E)$ is also measurable.


**Question 4**

If $f$ is a finite real valued measurable function on a measurable set $E \subset \mathbb{R}$, show that the set $\{(x, f(x)) : x ∈ E\}$ is measurable.


**Question 5**

Let g : $[0, 1] × [0, 1] → [0, 1]$ be a continuous function and let $\{f_n\}$ be a sequence of functions such that 

$$f_n(x)=\begin{cases}{0,   0\leq x\leq 1/n},\\{\int_0^{x-\frac1n} g(t,f_n(t))dt, 1/n\leq x \leq 1.}\end{cases}$$

With the help of the Arzela-Ascoli theorem or otherwise, show that there exists a continuous function $f : [0, 1] → \mathbb{R}$ such that 

$f(x) = \int_0^x g(t, f(t))dt$

for all $x \in [0, 1]$. 

> Hint: first show that $|f_n(x_1) - f_n(x_2)| ≤ |x_1 - x_2|$.


**Question 6**

If $\limsup_{n\rightarrow \infty} a_n\leq l$, show that $\limsup_{n\rightarrow \infty}\sum_{i=1}^n{a_i/n}\leq l$.  


**Question 7**

If $f$ is a nonnegative measurable function on $\mathbb{R}$ and $p > 0$, show that
$$\int f^p ~dx = \int_0^{\infty} p t^{p-1} \abs{\{x : f(x) > t\}} ~dt$$ 
where $\abs{\{x : f(x) > t\}}$ is the Lebesgue measure of the set $\{x : f(x) > t\}$.


**Question 8**

If $f$ is a nonnegative measurable function on $[0, \pi]$ and $\int_0^\pi f(x)^3~dx < \infty$, show that
$$\lim_{\alpha\to\infty} \int_{ \{x \suchthat f(x) > \alpha \} } f(x)^2 ~dx=0.$$


**Question 9**

Prove or disprove each of the following statements.

(a) If $f : [0, 1] → \mathbb{R}$ is a measurable function, then given any $\varepsilon > 0$, there exists a compact set $K \subset [0, 1]$ such that $f$ is continuous on $K$ relative to $K$.

(c) If f is Borel measurable on $\mathbb{R} × \mathbb{R}$, then for any $x \in \mathbb{R}$, the function $g(y) = f(x, y)$ is also Borel measurable on $\mathbb{R}$.

(d) If $E \subset \mathbb{R}$, then $E$ is measurable if and only if given any $\varepsilon > 0$, there exist a closed set $F$ and an open set $G$ such that $F \subset E \subset G$ and the measure of $G-F$ is less than $\varepsilon$.


**Question 10**

Prove or disprove each of the following statements.

(b) If ${f_n}$ is a sequence of measurable functions that converges uniformly to $f$ on $\mathbb{R}$, then $\int{f}=\lim_{k\to \infty} \int f_k$

(e) If $\{f_k\}$ is a sequence of function in $L_p[0,\infty)$ that converges to a function $f ∈ L_p [0,∞)$, then $\{f_k\}$ has a subsequence that converges to $f$ almost everywhere.


**Question 11**

Prove or disprove each of the following statements.

(f) If $f$ is Riemann integrable on $[ε, 1]$ for all $0 < ε < 1$, then $f$ is Lebesgue integrable on $[0,1]$ if $f$ is nonnegative and the following limit exists $\lim_{\varepsilon\to 0^+} \int_\varepsilon^1 f dx$.

(g) If $f$ is integrable on $[0,1]$, then $\lim_{n\to\infty} \int_0^1 f(x)\sin(n\pi x)dx = 0$.

(h) If $f$ is continuous on $[0, 1]$, then it is of bounded variation on [0, 1]$.


**Question 12**

(a) Let $f : \mathbb{R} → \mathbb{R}$ be a differentiable function. 
    If $f'(-1) < 2$ and $f'(1) > 2$, show that there exists $x_0 \in (i1, 1)$ such that $f'(x_0) = 2$.

    > Hint: consider the function $f(x) - 2x$ and recall the proof of Rolle’s theorem.)

(b) Let $f : (-1, 1) → \mathbb{R}$ be a differentiable function on $(-1, 0) \union (0, 1)$ such that $\lim_{x\to 0} f'(x) = L$. 
    If $f$ is continuous on $(-1, 1)$, show that $f$ is indeed differentiable at $0$ and $f'(0) = L$.


**Question 13**

Let $C([0, 1])$ denote the space of all continuous real-valued functions on $[0, 1]$.
  
a. Prove that $C([0, 1])$ is complete under the uniform norm $\norm{f}_u := \displaystyle\sup_{x\in [0,1]} |f (x)|$.
b. Prove that $C([0, 1])$ is not complete under the $L^1\dash$norm $\norm{f}_1 = \displaystyle\int_0^1 |f (x)| ~dx$.


**Question 14**

Let $\mathcal B$ denote the set of all Borel subsets of $\RR$ and $\mu : \mathcal B → [0, \infty)$ denote a finite Borel measure on $\RR$.

a. Prove that if $\{F_k\}$ is a sequence of Borel sets for which $F_k \supseteq  F_{k+1}$ for all $k$, then
$$
\lim _{k \rightarrow \infty} \mu\left(F_{k}\right)=\mu\left(\bigcap_{k=1}^{\infty} F_{k}\right)
$$

b. Suppose $µ$ has the property that $µ(E) = 0$ for every $E \in \mathcal B$ with Lebesgue measure $m(E) = 0$.
  Prove that for every $ε > 0$ there exists $δ > 0$ so that if $E \in \mathcal B$ with $m(E) < δ$, then $µ(E) < ε$.


**Question 15**

Let $\{f_k\}$ be any sequence of functions in $L^2([0, 1])$ satisfying $\norm{f_k}_2 ≤ M$ for all $k ∈ \NN$.
  
Prove that if $f_k → f$ almost everywhere, then $f ∈ L^2([0, 1])$ with $\norm{f}_2 ≤ M$ and
$$
\lim _{k \rightarrow \infty} \int_{0}^{1} f_{k}(x) dx = \int_{0}^{1} f(x) d x
$$

> Hint: Try using Fatou’s Lemma to show that $\norm{f}_2 ≤ M$ and then try applying Egorov’s Theorem.


**Question 16**

Let $f$ be a non-negative function on $\RR^n$ and $\mathcal A = \{(x, t) ∈ \RR^n × \RR : 0 ≤ t ≤ f (x)\}$.

Prove the validity of the following two statements:

a. $f$ is a Lebesgue measurable function on $\RR^n \iff  \mathcal A$ is a Lebesgue measurable subset of $\RR^{n+1}$

b. If $f$ is a Lebesgue measurable function on $\RR^n$, then
$$
m(\mathcal{A})=\int_{\mathbb{R}^{n}} f(x) d x=\int_{0}^{\infty} m\left(\left\{x \in \mathbb{R}^{n}: f(x) \geq t\right\}\right) d t
$$


**Question 17**

a.  Show that $L^2([0, 1]) ⊆ L^1([0, 1])$ and argue that $L^2([0, 1])$ in fact 
    forms a dense subset of $L^1([0, 1])$.

b.  Let $Λ$ be a continuous linear functional on $L^1([0, 1])$.
  
    Prove the Riesz Representation Theorem for $L^1([0, 1])$ by following the steps below:


    i. Establish the existence of a function $g ∈ L^2([0, 1])$ which represents $Λ$ in the sense that
    $$
    Λ(f ) = f (x)g(x) dx \text{ for all } f ∈ L^2([0, 1]).
    $$

    > Hint: You may use, without proof, the Riesz Representation Theorem for $L^2([0, 1])$.

    ii. Argue that the $g$ obtained above must in fact belong to $L^∞([0, 1])$ and represent $Λ$ in the sense that
    $$
    \Lambda(f)=\int_{0}^{1} f(x) \overline{g(x)} d x \quad \text { for all } f \in L^{1}([0,1])
    $$
    with
    $$
    \|g\|_{L^{\infty}([0,1])}=\|\Lambda\|_{L^{1}([0,1])\dual}
    $$


**Question 18**

Let $\{a_n\}_{n=1}^\infty$ be a sequence of real numbers.

a. Prove that if $\displaystyle\lim_{n→∞} a_n = 0$, then $\displaystyle\lim_{n→∞} a_1 + \cdots + a_n = 0$.
$$
\lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
$$

b. Prove that if $\displaystyle\sum_{n=1}^{\infty} \frac{a_{n}}{n}$ converges, then 
$$
\lim _{n \rightarrow \infty} \frac{a_{1}+\cdots+a_{n}}{n}=0
$$


**Question 19**

Prove that
$$
\left|\frac{d^{n}}{d x^{n}} \frac{\sin x}{x}\right| \leq \frac{1}{n}
$$

for all $x \neq 0$ and positive integers $n$.

> Hint: Consider $\displaystyle\int_0^1 \cos(tx) dt$


**Question 20**

Let $(X, \mathcal B, µ)$ be a measure space with $µ(X) = 1$ and $\{B_n\}_{n=1}^\infty$ be a sequence of $\mathcal B$-measurable subsets of $X$, and
$$
B \definedas \theset{x\in X \suchthat x\in B_n \text{ for infinitely many } n}.
$$

a. Argue that $B$ is also a $\mathcal{B} \dash$measurable subset of $X$.

b. Prove that if $\sum_{n=1}^\infty \mu(B_n) < \infty$ then $\mu(B)= 0$.

c. Prove that if  $\sum_{n=1}^\infty \mu(B_n) = \infty$ **and** the sequence of set complements $\theset{B_n^c}_{n=1}^\infty$ satisfies
$$
\mu\left(\bigcap_{n=k}^{K} B_{n}^{c}\right)=\prod_{n=k}^{K}\left(1-\mu\left(B_{n}\right)\right)
$$
for all positive integers $k$ and $K$ with $k < K$, then $µ(B) = 1$.

> Hint: Use the fact that $1 - x ≤ e^{-x}$ for all $x$.


**Question 21**

Let $\{u_n\}_{n=1}^∞$ be an orthonormal sequence in a Hilbert space $\mathcal{H}$.

a. Prove that for every $x \in \mathcal H$ one has 
$$
\displaystyle\sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2} \leq\|x\|^{2}
$$

b. Prove that for any sequence $\{a_n\}_{n=1}^\infty \in \ell^2(\NN)$ there exists an element $x\in\mathcal H$ such that 
$$
a_n = \inner{x}{u_n} \text{ for all } n\in \NN
$$
and
$$
\norm{x}^2 = \sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2}
$$


**Question 22**

a. Show that if $f$ is continuous with compact support on $\RR$, then 
$$
\lim _{y \rightarrow 0} \int_{\mathbb{R}}|f(x-y)-f(x)| d x=0
$$

b. Let $f\in L^1(\RR)$ and for each $h > 0$ let 
$$
\mathcal{A}_{h} f(x):=\frac{1}{2 h} \int_{|y| \leq h} f(x-y) d y
$$

i. Prove that $\left\|\mathcal{A}_{h} f\right\|_{1} \leq\|f\|_{1}$ for all $h > 0$.

ii. Prove that $\mathcal{A}_h f → f$ in $L^1(\RR)$ as $h → 0^+$.


**Question 23**

Define
$$
E:=\left\{x \in \mathbb{R}:\left|x-\frac{p}{q}\right|<q^{-3} \text { for infinitely many } p, q \in \mathbb{N}\right\}.
$$

Prove that $m(E) = 0$.


**Question 24**

Let
$$
f_{n}(x):=\frac{x}{1+x^{n}}, \quad x \geq 0.
$$

a. Show that this sequence converges pointwise and find its limit. Is the convergence uniform on $[0, \infty)$?

b. Compute 
$$
\lim _{n \rightarrow \infty} \int_{0}^{\infty} f_{n}(x) d x
$$


**Question 25**

Let $f$ be a non-negative measurable function on $[0, 1]$. 

Show that
$$
\lim _{p \rightarrow \infty}\left(\int_{[0,1]} f(x)^{p} d x\right)^{\frac{1}{p}}=\|f\|_{\infty}.
$$


**Question 26**

Let $f\in L^2([0, 1])$ and suppose
$$
\int_{[0,1]} f(x) x^{n} d x=0 \text { for all integers } n \geq 0.
$$
Show that $f = 0$ almost everywhere.


**Question 27**

Suppose that

- $f_n, f \in L^1$,
- $f_n \to f$ almost everywhere, and
- $\int\left|f_{n}\right| \rightarrow \int|f|$.

Show that $\int f_{n} \rightarrow \int f$


**Question 28**

Let $f(x) = \frac 1 x$.
Show that $f$ is uniformly continuous on $(1, \infty)$ but not on $(0,\infty)$.


**Question 29**

Let $E\subset \RR$ be a Lebesgue measurable set.
Show that there is a Borel set $B \subset E$ such that $m(E\setminus B) = 0$.


**Question 30**

Suppose $f(x)$ and $xf(x)$ are integrable on $\RR$.
Define $F$ by
$$
F(t):=\int_{-\infty}^{\infty} f(x) \cos (x t) d x
$$
Show that 
$$
F'(t)=-\int_{-\infty}^{\infty} x f(x) \sin (x t) d x.
$$


**Question 31**

Let $f\in L^1([0, 1])$.
Prove that
$$
\lim_{n \to \infty} \int_{0}^{1} f(x) \abs{\sin n x} ~d x= \frac{2}{\pi} \int_{0}^{1} f(x) ~d x
$$

> Hint: Begin with the case that $f$ is the characteristic function of an interval.


**Question 32**

Let $f \geq 0$ be a measurable function on $\RR$.
Show that
$$
\int_{\mathbb{R}} f=\int_{0}^{\infty} m(\{x: f(x)>t\}) d t
$$


**Question 33**

Compute the following limit and justify your calculations:
$$
\lim_{n \rightarrow \infty} \int_{1}^{n} \frac{d x}{\left(1+\frac{x}{n}\right)^{n} \sqrt[n]{x}}
$$


**Question 34**

Let $K$ be the set of numbers in $[0, 1]$ whose decimal expansions do not use the digit $4$.

> We use the convention that when a decimal number ends with 4 but all other digits are
different from 4, we replace the digit $4$ with $399\cdots$. For example, $0.8754 = 0.8753999\cdots$.

Show that $K$ is a compact, nowhere dense set without isolated points, and find the
Lebesgue measure $m(K)$.


**Question 35**


a. Let $\mu$ be a measure on a measurable space $(X, \mathcal M)$ and $f$ a positive measurable function.

Define a measure $\lambda$ by
$$
\lambda(E):=\int_{E} f ~d \mu, \quad E \in \mathcal{M}
$$

Show that for $g$ any positive measurable function, 
$$
\int_{X} g ~d \lambda=\int_{X} f g ~d \mu
$$

b. Let $E \subset \RR$ be a measurable set such that 
$$
\int_{E} x^{2} ~d m=0.
$$
Show that $m(E) = 0$.


**Question 36**

Let
$$
f_{n}(x)=a e^{-n a x}-b e^{-n b x} \quad \text{ where } 0 < a < b.
$$

Show that 

a. $\sum_{n=1}^{\infty}\left|f_{n}\right| \text { is not in } L^{1}([0, \infty), m)$

  > Hint: $f_n(x)$ has a root $x_n$.

b. 
$$
\sum_{n=1}^{\infty} f_{n} \text { is in } L^{1}([0, \infty), m) 
\quad \text { and } \quad 
\int_{0}^{\infty} \sum_{n=1}^{\infty} f_{n}(x) ~d m=\ln \frac{b}{a}
$$


**Question 37**

Let $f(x, y)$ on $[-1, 1]^2$ be defined by 
$$
f(x, y) = \begin{cases}
\frac{x y}{\left(x^{2}+y^{2}\right)^{2}} & (x, y) \neq (0, 0) \\
0 & (x, y) = (0, 0)
\end{cases}
$$
Determine if $f$ is integrable.


**Question 38**

Let $f, g \in L^2(\RR)$. 
Prove that the formula
$$
h(x):=\int_{-\infty}^{\infty} f(t) g(x-t) d t
$$
defines a uniformly continuous function $h$ on $\RR$.


**Question 39**

Show that the space $C^1([a, b])$ is a Banach space when equipped with the norm
$$
\|f\|:=\sup _{x \in[a, b]}|f(x)|+\sup _{x \in[a, b]}\left|f^{\prime}(x)\right|.
$$


**Question 40**

Let 
$$
f(x) = s \sum_{n=0}^{\infty} \frac{x^{n}}{n !}.
$$

Describe the intervals on which $f$ does and does not converge uniformly.


**Question 41**

Let $f(x) = x^2$ and $E \subset [0, \infty) \definedas \RR^+$.

1. Show that
$$
m^*(E) = 0 \iff m^*(f(E)) = 0.
$$

2. Deduce that the map

\begin{align*}
\phi: \mathcal{L}(\RR^+) &\to \mathcal{L}(\RR^+) \\
E &\mapsto f(E)
\end{align*}
  is a bijection from the class of Lebesgue measurable sets of $[0, \infty)$ to itself.


**Question 42**

Let 
$$
S = \spanof_\CC\theset{\chi_{(a, b)} \suchthat a, b \in \RR},
$$
the complex linear span of characteristic functions of intervals of the form $(a, b)$.

Show that for every $f\in L^1(\RR)$, there exists a sequence of functions $\theset{f_n} \subset S$ such that 
$$
\lim _{n \rightarrow \infty}\left\|f_{n}-f\right\|_{1}=0
$$


**Question 43**

Let
$$
f_{n}(x)=n x(1-x)^{n}, \quad n \in \mathbb{N}.
$$

1. Show that $f_n \to 0$ pointwise but not uniformly on $[0, 1]$.
    
    > Hint: Consider the maximum of $f_n$.

2. 
$$
\lim _{n \rightarrow \infty} \int_{0}^{1} n(1-x)^{n} \sin x d x=0
$$


**Question 44**

Let $\phi$ be a compactly supported smooth function that vanishes outside of an interval $[-N, N]$ such that $\int_{\mathrm{R}} \phi(x) d x=1$.

For $f\in L^1(\RR)$, define
$$
K_{j}(x):=j \phi(j x), \quad \quad f \ast K_{j}(x):=\int_{\mathbb{R}} f(x-y) K_{j}(y) ~d y
$$
and prove the following:

1. Each $f\ast K_j$ is smooth and compactly supported.

2. 
$$
\lim _{j \rightarrow \infty}\left\|f * K_{j}-f\right\|_{1}=0
$$

> Hint:
$$
\lim _{y \rightarrow 0} \int_{\mathbb{R}}|f(x-y)-f(x)| d y=0
$$


**Question 45**

Let $X$ be a complete metric space and define a norm
$$
\|f\|:=\max \{|f(x)|: x \in X\}.
$$

Show that $(C^0(\RR), \norm{\wait} )$ (the space of continuous functions $f: X\to \RR$) is complete.


**Question 46**

For $n\in \NN$, define
$$
e_{n}=\left(1+\frac{1}{n}\right)^{n} 
\quad \text { and } \quad 
E_{n}=\left(1+\frac{1}{n}\right)^{n+1}
$$

Show that $e_n < E_n$, and prove Bernoulli's inequality:
$$
(1+x)^{n} \geq 1+n x \text { for }-1<x<\infty \text { and } n \in \mathbb{N}
$$

Use this to show the following:

1. The sequence $e_n$ is increasing.
2. The sequence $E_n$ is decreasing.
3. $2 < e_n < E_n < 4$.
4. $\lim _{n \rightarrow \infty} e_{n}=\lim _{n \rightarrow \infty} E_{n}$.


**Question 47**

Let $0 < \lambda < 1$ and construct a Cantor set $C_\lambda$ by successively removing middle intervals of length $\lambda$.

Prove that $m(C_\lambda) = 0$.


**Question 48**

Let $f$ be Lebesgue measurable on $\RR$ and $E \subset \RR$ be measurable such that
$$
0<A=\int_{E} f(x) d x<\infty.
$$

Show that for every $0 < t < 1$, there exists a measurable set $E_t \subset E$ such that
$$
\int_{E_{t}} f(x) d x=t A.
$$


**Question 49**

Let $E \subset \RR$ be measurable with $m(E) < \infty$. 
Define
$$
f(x)=m(E \cap(E+x)).
$$

Show that

1. $f\in L^1(\RR)$.
2. $f$ is uniformly continuous.
3. $\lim _{|x| \rightarrow \infty} f(x)=0$

> Hint: 
$$
\chi_{E \cap(E+x)}(y)=\chi_{E}(y) \chi_{E}(y-x)
$$


**Question 50**

Let $(X, \mathcal M, \mu)$ be a measure space. For $f\in L^1(\mu)$ and $\lambda > 0$, define
$$
\phi(\lambda)=\mu(\{x \in X | f(x)>\lambda\}) 
\quad \text { and } \quad 
\psi(\lambda)=\mu(\{x \in X | f(x)<-\lambda\})
$$

Show that $\phi, \psi$ are Borel measurable and
$$
\int_{X}|f| ~d \mu=\int_{0}^{\infty}[\phi(\lambda)+\psi(\lambda)] ~d \lambda
$$


**Question 51**

Without using the Riesz Representation Theorem, compute
$$
\sup \left\{\left|\int_{0}^{1} f(x) e^{x} d x\right| \suchthat f \in L^{2}([0,1], m),~~ \|f\|_{2} \leq 1\right\}
$$


**Question 52**

Define
$$
f(x) = \sum_{n=1}^{\infty} \frac{1}{n^{x}}.
$$ 

Show that $f$ converges to a differentiable function on $(1, \infty)$ and that
$$
f'(x)  =\sum_{n=1}^{\infty}\left(\frac{1}{n^{x}}\right)^{\prime}.
$$

> Hint:
$$
\left(\frac{1}{n^{x}}\right)^{\prime}=-\frac{1}{n^{x}} \ln n
$$


**Question 53**

Let $f, g: [a, b] \to \RR$ be measurable with
$$
\int_{a}^{b} f(x) ~d x=\int_{a}^{b} g(x) ~d x.
$$

Show that either

1. $f(x) = g(x)$ almost everywhere, or
2. There exists a measurable set $E \subset [a, b]$ such that
$$
\int_{E} f(x) ~d x>\int_{E} g(x) ~d x
$$


**Question 54**

Let $f\in L^1(\RR)$.
Show that
$$
\lim _{x \rightarrow 0} \int_{\mathbb{R}}|f(y-x)-f(y)| d y=0
$$


**Question 55**

Let $(X, \mathcal M, \mu)$ be a measure space and suppose $\theset{E_n} \subset \mathcal M$ satisfies
$$
\lim _{n \rightarrow \infty} \mu\left(X \backslash E_{n}\right)=0.
$$

Define
$$
G \definedas \theset{x\in X \suchthat x\in E_n \text{ for only finitely many  } n}.
$$

Show that $G \in \mathcal M$ and $\mu(G) = 0$.


**Question 56**

Let $\phi\in L^\infty(\RR)$. Show that the following limit exists and satisfies the equality
$$
\lim _{n \rightarrow \infty}\left(\int_{\mathbb{R}} \frac{|\phi(x)|^{n}}{1+x^{2}} d x\right)^{\frac{1}{n}} = \norm{\phi}_\infty.
$$


**Question 57**

Let $f, g \in L^2(\RR)$. Show that
$$
\lim _{n \rightarrow \infty} \int_{\mathbb{R}} f(x) g(x+n) d x=0
$$


**Question 58**

Let $(X, d)$ and $(Y, \rho)$ be metric spaces, $f: X\to Y$, and $x_0 \in X$.

Prove that the following statements are equivalent:

1. For every $\varepsilon > 0 \quad \exists \delta > 0$ such that $\rho( f(x), f(x_0)  ) < \varepsilon$ whenever $d(x, x_0) < \delta$.
2. The sequence $\theset{f(x_n)}_{n=1}^\infty \to f(x_0)$ for every sequence $\theset{x_n} \to x_0$ in $X$.


**Question 59**

Let $f: \RR \to \CC$ be continuous with period 1. Prove that
$$
\lim _{N \rightarrow \infty} \frac{1}{N} \sum_{n=1}^{N} f(n \alpha)=\int_{0}^{1} f(t) d t \quad \forall \alpha \in \RR\setminus\QQ.
$$

> Hint: show this first for the functions $f(t) = e^{2\pi i k t}$ for $k\in \ZZ$.


**Question 60**

Let $\mu$ be a finite Borel measure on $\RR$ and $E \subset \RR$ Borel. 
Prove that the following statements are equivalent:

1. $\forall \varepsilon > 0$ there exists $G$ open and $F$ closed such that 
$$
F \subseteq E \subseteq G \quad \text{and} \quad \mu(G\setminus F) < \varepsilon.
$$
2. There exists a $V \in G_\delta$ and $H \in F_\sigma$ such that 
$$
H \subseteq E \subseteq V \quad \text{and}\quad \mu(V\setminus H) = 0
$$


**Question 61**

Define
$$
f(x, y):=\left\{\begin{array}{ll}{\frac{x^{1 / 3}}{(1+x y)^{3 / 2}}} & {\text { if } 0 \leq x \leq y} \\ {0} & {\text { otherwise }}\end{array}\right.
$$

Carefully show that $f \in L^1(\RR^2)$.


**Question 62**

Let $\mathcal H$ be a Hilbert space.

1. Let $x\in \mathcal H$ and $\theset{u_n}_{n=1}^N$ be an orthonormal set.
  Prove that the best approximation to $x$ in $\mathcal H$ by an element in $\spanof_\CC\theset{u_n}$ is given by
  $$
  \hat x \definedas \sum_{n=1}^N \inner{x}{u_n}u_n.
  $$
2. Conclude that finite dimensional subspaces of $\mathcal H$ are always closed.


**Question 63**

Let $f \in L^1(\RR)$ and $g$ be a bounded measurable function on $\RR$.

1. Show that the convolution $f\ast g$ is well-defined, bounded, and uniformly continuous on $\RR$.
2. Prove that one further assumes that $g \in C^1(\RR)$ with bounded derivative, then $f\ast g \in C^1(\RR)$ and
$$
\frac{d}{d x}(f * g)=f *\left(\frac{d}{d x} g\right)
$$


**Question 64**

Define
$$
f(x)=c_{0}+c_{1} x^{1}+c_{2} x^{2}+\ldots+c_{n} x^{n} \text { with } n \text { even and } c_{n}>0.
$$

Show that there is a number $x_m$ such that $f(x_m) \leq f(x)$ for all $x\in \RR$.


**Question 65**

Let $f: \RR \to \RR$ be Lebesgue measurable.

1. Show that there is a sequence of simple functions $s_n(x)$ such that $s_n(x) \to f(x)$ for all $x\in \RR$.
2. Show that there is a Borel measurable function $g$ such that $g = f$ almost everywhere.


**Question 66**

Compute the following limit:
$$
\lim _{n \rightarrow \infty} \int_{1}^{n} \frac{n e^{-x}}{1+n x^{2}} ~\sin \left(\frac x n\right) ~d x
$$


**Question 67**

Let $f: [1, \infty) \to \RR$ such that $f(1) = 1$ and
$$
f^{\prime}(x)= \frac{1} {x^{2}+f(x)^{2}}
$$

Show that the following limit exists and satisfies the equality
$$
\lim _{x \rightarrow \infty} f(x) \leq 1 + \frac \pi 4
$$


**Question 68**

Let $f, g \in L^1(\RR)$ be Borel measurable.

1. Show that 
  - The function $$F(x, y) \definedas f(x-y) g(y)$$ is Borel measurable on $\RR^2$, and
  - For almost every $y\in \RR$, $$F_y(x) \definedas f(x-y)g(y)$$ is integrable with respect to $y$.
2. Show that $f\ast g \in L^1(\RR)$ and
$$
\|f * g\|_{1} \leq\|f\|_{1}\|g\|_{1}
$$


**Question 69**

Let $f: [0, 1] \to \RR$ be continuous.
Show that
$$
\sup \left\{\|f g\|_{1} \suchthat g \in L^{1}[0,1],~~ \|g\|_{1} \leq 1\right\}=\|f\|_{\infty}
$$


**Question 70**

1. Give an example of a continuous $f\in L^1(\RR)$ such that $f(x) \not\to 0$ as$\abs x \to \infty$.

2. Show that if $f$ is *uniformly* continuous, then
$$
\lim_{\abs x \to \infty} f(x) = 0.
$$


**Question 71**

Let $\theset{a_n}$ be a sequence of real numbers such that
$$
\theset{b_n} \in \ell^2(\NN) \implies \sum a_n b_n < \infty.
$$
Show that $\sum a_n^2 < \infty$.

> Note: Assume $a_n, b_n$ are all non-negative.


**Question 72**

Let $f: \RR \to \RR$ and suppose
$$
\forall x\in \RR,\quad f(x) \geq \limsup _{y \rightarrow x} f(y)
$$
Prove that $f$ is Borel measurable.


**Question 73**

Let $(X, \mathcal M, \mu)$ be a measure space and suppose $f$ is a measurable function on $X$.
Show that
$$
\lim _{n \rightarrow \infty} \int_{X} f^{n} ~d \mu =
\begin{cases}
\infty & or \\
\mu(f\inv(1)),
\end{cases}
$$
and characterize the collection of functions of each type.


**Question 74**

Let $f, g \in L^1([0, 1])$ and for all $x\in [0, 1]$ define
$$
F(x):=\int_{0}^{x} f(y) d y \quad \text { and } \quad G(x):=\int_{0}^{x} g(y) d y.
$$

Prove that
$$
\int_{0}^{1} F(x) g(x) d x=F(1) G(1)-\int_{0}^{1} f(x) G(x) d x
$$


**Question 75**

Let $\theset{f_n}$ be a sequence of continuous functions such that $\sum f_n$ converges uniformly.

Prove that $\sum f_n$ is also continuous.


**Question 76**

Let $I$ be an index set and $\alpha: I \to (0, \infty)$.

1.  Show that
    $$
    \sum_{i \in I} a(i):=\sup _{\substack{ J \subset I \\ J \text { finite }}} \sum_{i \in J} a(i)<\infty \implies I \text{ is countable.}
    $$

2.  Suppose $I = \QQ$ and $\sum_{q \in \mathbb{Q}} a(q)<\infty$.
    Define
    $$
    f(x):=\sum_{\substack{q \in \mathbb{Q}\\ q \leq x}} a(q).
    $$
    Show that $f$ is continuous at $x \iff x\not\in \QQ$.


**Question 77**

Let $f\in L^1(\RR)$. Show that
$$
\forall\varepsilon > 0 ~~\exists \delta > 0 \text{ such that } m(E) < \delta \implies \int_{E}|f(x)| d x<\varepsilon
$$


**Question 78**

Let $g\in L^\infty([0, 1])$
Prove that
$$
\int_{[0,1]} f(x) g(x) d x=0 \quad\text{for all continuous } f:[0, 1] \to \RR \implies g(x) = 0 \text{ almost everywhere. }
$$


**Question 79**

1. Let $f \in C_c^0(\RR^n)$, and show
$$
\lim _{t \rightarrow 0} \int_{\mathbb{R}^{n}}|f(x+t)-f(x)| d x=0.
$$

2. Extend the above result to $f\in L^1(\RR^n)$ and show that
$$
f\in L^1(\RR^n),~ g\in L^\infty(\RR^n) \implies f \ast g \text{ is bounded and uniformly continuous. }
$$


**Question 80**

Let $1 \leq p,q \leq \infty$ be conjugate exponents, and show that
$$
f \in L^p(\RR^n) \implies \|f\|_{p}=\sup _{\|g\|_{q}=1}\left|\int f(x) g(x) d x\right|
$$


**Question 81**

Describe the process that extends a measure on an algebra
$\mathcal{A}$ of subsets of $X$, to a complete measure defined on a
$\sigma$-algebra $\mathcal{B}$ containing $\mathcal{A}$. State the
corresponding definitions and results (without proofs).


**Question 82**

State and prove Fatou's Lemma on a general measurable space.


**Question 83**

1.  State the Dominated Convergence Theorem for Lebesgue integrals.

2.  Let $\{f_n\}$ be a sequence of measurable functions on a
    Lebesgue measurable set $E$ which converges *in measure* to a
    function $f$ on $E$. Suppose that for every $n$, $|f_n| \leq g$
    with $g$ integrable on $E$. Using the above theorem show that
    \begin{align*}
        \int_E |f_n-f| \longrightarrow 0 \, .
    \end{align*}


**Question 84**

Let $f\in L^1([0,1])$. Show that

1.  The limit $\lim_{p\to 0^+} \| f \|_p$ exists.

2.  If $m \{x : f(x) = 0\} > 0$, then the above limit is zero.


**Question 85**

Let $f$ be a continuous function on $[0,1]$. Show that the following
statements are equivalent.

1.  $f$ is absolutely continuous.

2.  For any $\epsilon > 0$ there exists $\delta > 0$ such that
    $m(f(E)) < \epsilon$ for any set $E\subseteq [0,1]$ with
    $m(E) < \delta$.

3.  $m(f(E)) = 0$ for any set $E \subseteq [0,1]$ with $m(E)=0$.

# Complex Analysis (125 Questions)

**Question 1**

Find the number of zeroes, counting multiplicities, of the polynomial 

$f(z) = 2z^5 - 6z^2 - z + 1 = 0$

in the annulus $1 ≤ |z| ≤ 2$.


**Question 2**

Find an analytic isomorphism from the open region between $|z| = 1$ and $|z -\frac 1 2| =\frac 1 2$ to the upper half plane $\Im z > 0$. (You may leave your result as a composition of functions).


**Question 3**

Use Green theorem or otherwise to prove the Cauchy theorem.


**Question 4**

State and prove the divergence theorem on any rectangle in $\mathbb{R}^2$.


**Question 5**

Find an analytic isomorphism from the open region between $x = 1$ and $x = 3$ to the upper half unit disk $\{|z| < 1,\Im z > 0\}$. (You may leave your result as a composition of functions)


**Question 6**

Use Cauchy's theorem to prove the argument principle.


**Question 7**

Evaluate the following by the method of residues:
$\int_0^{\pi /2} \frac{1}{3+\sin^2x}dx$


**Question 8**

Evaluate the improper integral 

$\int_0^\infty \frac{x^2~dx}{(x^2+1)(x^2+4)}$


**Question 9**

(1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$
converges in $|z| < R$. Show that for $r <R$,
$$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
\sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

(2) Deduce Liouville's theorem from (1).


**Question 10**

Let $f$ be a continuous function in the region
$$D=\{z \suchthat  \abs{z}>R, 0\leq \arg z\leq \theta\}\quad\text{where}\quad
1\leq \theta \leq 2\pi.$$ If there exists $k$ such that
$\displaystyle{\lim_{z\to\infty} zf(z)=k}$ for $z$ in the region
$D$. 
Show that $$\lim_{R'\to\infty} \int_{L} f(z) dz=i\theta k,$$
where $L$ is the part of the circle $|z|=R'$ which lies in the
region $D$.


**Question 11**

Suppose that $f$ is an analytic function in the region $D$ which
contains the point $a$. Let
$$F(z)= z-a-qf(z),\quad \text{where}~ q \ \text{is a complex
parameter}.$$ 

(1) Let $K\subset D$ be a circle with the center at
point $a$ and also we assume that $f(z)\not =0$ for $z\in K$. Prove
that the function $F$ has one and only one zero $z=w$ on the closed
disc $\bar{K}$ whose boundary is the circle $K$ if $\displaystyle{
|q|<\min_{z\in K} \frac{|z-a|}{|f(z)|}.}$\

(2) Let $G(z)$ be an analytic function on the disk $\bar{K}$. Apply
the residue theorem to prove that
$\displaystyle{ \frac{G(w)}{F'(w)}=\frac{1}{2\pi
i}\int_K \frac{G(z)}{F(z)} dz,}$ where $w$ is the zero from (1).\

(3) If $z\in K$, prove that the function
$\displaystyle{\frac{1}{F(z)}}$ can be represented as a convergent
series with respect to $q$: $\displaystyle{
\frac{1}{F(z)}=\sum_{n=0}^{\infty} \frac{(qf(z))^n}{(z-a)^{n+1}}.}$


**Question 12**

Evaluate $$\displaystyle{ \int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \,
dx }.$$


**Question 13**

Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
that
$$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
\frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$


**Question 14**

Show that $\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n}
dx=\frac{\pi}{n\sin \frac{a\pi}{n}}$ using complex analysis, $0< a <
n$. Here $n$ is a positive integer.


**Question 15**

For $s>0$, the **gamma function** is defined by
$\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

1.  Show that the gamma function is analytic in the half-plane
    $\Re (s)>0$, and is still given there by the integral formula
    above.

2.  Apply the formula in the previous question to show that
    $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

> Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.


**Question 16**

Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra: If
$$P_n(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + a_nz^n\quad  (a_n \neq 0)$$
is a polynomial of degree n, then it has n zeros in $\mathbb C$.


**Question 17**

Suppose $f$ is entire and there exist $A, R >0$ and natural number
$N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show
that 

(i) $f$ is a polynomial and 

(ii) the degree of $f$ is at least $N$.


**Question 18**

Let $f: {\mathbb C} \rightarrow {\mathbb C}$ be an injective
analytic (also called *univalent*) function. Show that there exist
complex numbers $a \neq 0$ and $b$ such that $f(z) = az + b$.


**Question 19**

Let $g$ be analytic for $|z|\leq 1$ and $|g(z)| < 1$ for $|z| = 1$.

1.  Show that $g$ has a unique fixed point in $|z| < 1$.

2.  What happens if we replace $|g(z)| < 1$ with $|g(z)|\leq 1$ for
    $|z|=1$? Give an example if (a) is not true or give an proof
    if (a) is still true.

3.  What happens if we simply assume that $f$ is analytic for
    $|z| < 1$ and $|f(z)| < 1$ for $|z| < 1$? Suppose that $f(z)
    \not\equiv  z$. Can f have more than one fixed point in
    $|z| < 1$?

> Hint: The map $\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$ may be useful.


**Question 20**

Find a conformal map from $D = \{z :\  |z| < 1,\ |z - 1/2| > 1/2\}$
to the unit disk $\Delta=\{z: \ |z|<1\}$.


**Question 21**

Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded*
open set $\Omega$. Show without using Picard's theorems that $f(z)$ is a
constant.


**Question 22**

(1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$ converges
in $|z| < R$. Show that for $r <R$,
$$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta
= \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

(2) Deduce Liouville's theorem from (1).


**Question 23**

Let $f(z)$ be entire and assume that $f(z) \leq M |z|^2$ outside some
disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of
degree $\leq 2$.


**Question 24**

Let $a_n(z)$ be an analytic sequence in a domain $D$ such that
$\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$. Show that
$\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$.


**Question 25**

Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a
point $z_0$ inside $\Omega$. Show that if $f(z)$ is bounded in near
$z_0$, then $\displaystyle \int_\Delta f(z) dz = 0$ for all triangles
$\Delta$ in $\Omega$.


**Question 26**

Assume $f$ is continuous in the region:
$0< |z-a| \leq R, \; 0 \leq \arg(z-a) \leq \beta_0$
($0 < \beta_0 \leq 2 \pi$) and the limit
$\displaystyle \lim_{z \rightarrow a} (z-a) f(z) = A$ exists. Show that
$$\lim_{r \rightarrow 0} \int_{\gamma_r} f(z) dz  = i A \beta_0 \; , \; \;$$
where
$$\gamma_r : = \{ z \; | \; z = a + r e^{it}, \; 0 \leq  t \leq \beta_0 \}.$$


**Question 27**

Show that $f(z) = z^2$ is uniformly continuous in any open disk
$|z| < R$, where $R>0$ is fixed, but it is not uniformly continuous on
$\mathbb C$.


**Question 28**

(1) Show that the function $u=u(x,y)$ given by
$$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for
the Laplace equation
$$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$

(2) Show that there exist points $(x,y)\in D$ such that
$\displaystyle{\limsup_{n\to\infty} |u(x,y)|=\infty}$.


**Question 29**

(1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$
converges in $|z| < R$. Show that for $r <R$,
$$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
\sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

(2) Deduce Liouville's theorem from (1).


**Question 30**

Let $f$ be a continuous function in the region
$$D=\{z\ |  |z|>R, 0\leq \arg Z\leq \theta\}\quad\text{where}\quad
0\leq \theta \leq 2\pi.$$ If there exists $k$ such that
$\displaystyle{\lim_{z\to\infty} zf(z)=k}$ for $z$ in the region
$D$. Show that $$\lim_{R'\to\infty} \int_{L} f(z) dz=i\theta k,$$
where $L$ is the part of the circle $|z|=R'$ which lies in the
region $D$.


**Question 31**

Evaluate $\displaystyle{ \int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \,dx }$.


**Question 32**

Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
that
$$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
\frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$


**Question 33**

Show that $\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n}
dx=\frac{\pi}{n\sin \frac{a\pi}{n}}$ using complex analysis, $0< a <
n$. Here $n$ is a positive integer.


**Question 34**

For $s>0$, the **gamma function** is defined by
$\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

1.  Show that the gamma function is analytic in the half-plane
    $\Re (s)>0$, and is still given there by the integral formula
    above.

2.  Apply the formula in the previous question to show that
    $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

> Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.


**Question 35**

Suppose $f$ is entire and there exist $A, R >0$ and natural number
$N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show
that 

(i) $f$ is a polynomial and 

(ii) the degree of $f$ is at least $N$.


**Question 36**

Let $f: {\mathbb C} \rightarrow {\mathbb C}$ be an injective
analytic (also called univalent) function. Show that there exist
complex numbers $a \neq 0$ and $b$ such that $f(z) = az + b$.


**Question 37**

Let $g$ be analytic for $|z|\leq 1$ and $|g(z)| < 1$ for $|z| = 1$.

-   Show that $g$ has a unique fixed point in $|z| < 1$.

-   What happens if we replace $|g(z)| < 1$ with $|g(z)|\leq 1$ for
    $|z|=1$? Give an example if (a) is not true or give an proof
    if (a) is still true.

-   What happens if we simply assume that $f$ is analytic for
    $|z| < 1$ and $|f(z)| < 1$ for $|z| < 1$? Suppose that $f(z)
    \not\equiv  z$. Can f have more than one fixed point in
    $|z| < 1$?

> Hint: The map
$\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
> may be useful.


**Question 38**

Find a conformal map from $D = \{z :\  |z| < 1,\ |z - 1/2| > 1/2\}$
to the unit disk $\Delta=\{z: \ |z|<1\}$.


**Question 39**

Let $f(z)$ be entire and assume values of $f(z)$ lie outside a
*bounded* open set $\Omega$. Show without using Picard's theorems
that $f(z)$ is a constant.


**Question 40**

(1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$ converges
in $|z| < R$. Show that for $r <R$,
$$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta
= \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

(2) Deduce Liouville's theorem from (1).


**Question 41**

Let $f(z)$ be entire and assume that $f(z) \leq M |z|^2$ outside some
disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of
degree $\leq 2$.


**Question 42**

Let $a_n(z)$ be an analytic sequence in a domain $D$ such that
$\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$. Show that
$\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$.


**Question 43**

Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a
point $z_0$ inside $\Omega$. Show that if $f(z)$ is bounded in near
$z_0$, then $\displaystyle \int_\Delta f(z) dz = 0$ for all triangles
$\Delta$ in $\Omega$.


**Question 44**

Assume $f$ is continuous in the region:
$0< |z-a| \leq R, \; 0 \leq \arg(z-a) \leq \beta_0$
($0 < \beta_0 \leq 2 \pi$) and the limit
$\displaystyle \lim_{z \rightarrow a} (z-a) f(z) = A$ exists. Show that
$$\lim_{r \rightarrow 0} \int_{\gamma_r} f(z) dz  = i A \beta_0 \; , \; \;$$
where
$$\gamma_r : = \{ z \; | \; z = a + r e^{it}, \; 0 \leq  t \leq \beta_0 \}.$$


**Question 45**

Show that $f(z) = z^2$ is uniformly continuous in any open disk
$|z| < R$, where $R>0$ is fixed, but it is not uniformly continuous on
$\mathbb C$.

(1) Show that the function $u=u(x,y)$ given by
    $$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
    is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for
    the Laplace equation
    $$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
    u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$


**Question 46**

This question provides some insight into Cauchy's theorem. Solve the
problem without using Cauchy's theorem.

1.  Evaluate the integral $\displaystyle{\int_{\gamma} z^n dz}$ for
    all integers $n$. Here $\gamma$ is any circle centered at the
    origin with the positive (counterclockwise) orientation.

2.  Same question as (a), but with $\gamma$ any circle not
    containing the origin.

3.  Show that if $|a|<r<|b|$, then
    $\displaystyle{\int_{\gamma}\frac{dz}{(z-a)(z-b)} dz=\frac{2\pi i}{a-b}}$.
    Here $\gamma$ denotes the circle centered at the origin, of
    radius $r$, with the positive orientation.


**Question 47**

(1) Assume the infinite series
$\displaystyle  \sum_{n=0}^\infty c_n z^n$ converges in $|z| < R$
and let $f(z)$ be the limit. Show that for $r <R$,
$$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
\sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

(2) Deduce Liouville's theorem from (1). 

> Liouville's theorem: If $f(z)$ is entire and bounded, then $f$ is constant.


**Question 48**

Let $f$ be a continuous function in the region
$$D=\{z\ |  |z|>R, 0\leq \arg Z\leq \theta\}\quad\text{where}\quad
0\leq \theta \leq 2\pi.$$ 
If there exists $k$ such that
$\displaystyle{\lim_{z\to\infty} zf(z)=k}$ for $z$ in the region
$D$. 
Show that $$\lim_{R'\to\infty} \int_{L} f(z) dz=i\theta k,$$
where $L$ is the part of the circle $|z|=R'$ which lies in the
region $D$.


**Question 49**

Evaluate $\displaystyle{ \int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \,
dx }$.


**Question 50**

Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
that
$$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
\frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$


**Question 51**

Show that $\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n}
dx=\frac{\pi}{n\sin \frac{a\pi}{n}}$ using complex analysis, $0< a <
n$. Here $n$ is a positive integer.


**Question 52**

For $s>0$, the **gamma function** is defined by
$\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

-   Show that the gamma function is analytic in the half-plane
    $\Re (s)>0$, and is still given there by the integral formula
    above.

-   Apply the formula in the previous question to show that
    $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

> Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.


**Question 53**

Suppose $f$ is entire and there exist $A, R >0$ and natural number
$N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show
that 

(i) $f$ is a polynomial and 

(ii) the degree of $f$ is at least $N$.


**Question 54**

Let $f: {\mathbb C} \rightarrow {\mathbb C}$ be an injective
analytic (also called univalent) function. Show that there exist
complex numbers $a \neq 0$ and $b$ such that $f(z) = az + b$.


**Question 55**

Let $g$ be analytic for $|z|\leq 1$ and $|g(z)| < 1$ for $|z| = 1$.

 -   Show that $g$ has a unique fixed point in $|z| < 1$.

 -   What happens if we replace $|g(z)| < 1$ with $|g(z)|\leq 1$ for
     $|z|=1$? Give an example if (a) is not true or give an proof
     if (a) is still true.

 -   What happens if we simply assume that $f$ is analytic for
     $|z| < 1$ and $|f(z)| < 1$ for $|z| < 1$? Suppose that $f(z)
     \not\equiv  z$. Can f have more than one fixed point in
     $|z| < 1$?

 > Hint: The map
 $\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
 > may be useful.


**Question 56**

Find a conformal map from $D = \{z :\  |z| < 1,\ |z - 1/2| > 1/2\}$
to the unit disk $\Delta=\{z: \ |z|<1\}$.


**Question 57**

Let $a_n \neq 0$ and assume that $\displaystyle
\lim_{n \rightarrow \infty} \frac{|a_{n+1}|}{|a_n|} = L$. Show that
$\displaystyle
\lim_{n \rightarrow \infty}
\sqrt[n]{|a_n|} = L.
%p_n^{\frac{1}{n}} = L.$ In particular, this shows that when
applicable, the ratio test can be used to calculate the radius of
convergence of a power series.


**Question 58**

(a) Let $z, w$ be complex numbers, such that $\bar{z} w \neq 1$.
Prove that
$$\abs{\frac{w - z}{1 - \bar{w} z}} < 1 \; \; \; \mbox{if} \; |z| < 1 \; \mbox{and}\; |w| < 1,$$
and also that
$$\abs{\frac{w - z}{1 - \bar{w} z}} = 1 \; \; \; \mbox{if} \; |z| = 1 \; \mbox{or}\; |w| = 1.$$

(b) Prove that for fixed $w$ in the unit disk $\mathbb D$, the
mapping $$F: z \mapsto \frac{w - z}{1 - \bar{w} z}$$ satisfies the
following conditions:

(i) $F$ maps $\mathbb D$ to itself and is holomorphic. 

(ii) $F$ interchanges $0$ and $w$, namely, $F(0) = w$ and
$F(w) = 0$.

(iii) $|F(z)| = 1$ if $|z| = 1$.

(iv) $F: {\mathbb D} \mapsto {\mathbb D}$ is bijective. 

> Hint: Calculate $F \circ F$.


**Question 59**

Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show
that
$$2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n}
= n
\; .$$ 

> Hint: $1 - \cos 2 \theta = 2 \sin^2 \theta,\; \sin 2 \theta = 2 \sin \theta \cos \theta$.


**Question 60**

(a) Show that in polar coordinates, the Cauchy-Riemann
equations take the form

$$\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta}
\; \; \; \text{and} \; \; \;
\frac{\partial v}{\partial r} = - \frac{1}{r} \frac{\partial u}{\partial \theta}$$

(b) Use these equations to show that the logarithm function
defined by $$\log z = \log r + i \theta \; \;
\mbox{where} \; z = r e^{i \theta } \; \mbox{with} \; - \pi < \theta < \pi$$
is a holomorphic function in the region
$r>0, \; - \pi < \theta < \pi$. Also show that $\log z$ defined
above is not continuous in $r>0$.


**Question 61**

Assume $f$ is continuous in the region:
$x \geq x_0, \; 0 \leq y \leq b$ and the limit
$$\displaystyle \lim_{x \rightarrow + \infty} f(x + iy) = A$$ exists
uniformly with respect to $y$ (independent of $y$). 

Show that
$$\lim_{x \rightarrow + \infty} \int_{\gamma_x} f(z) dz  = iA b \; , \; \;$$
where $\gamma_x : = \{ z \; | \; z = x + it, \; 0 \leq  t \leq b\}.$


**Question 62**

(Cauchy's formula for "exterior" region) Let $\gamma$ be piecewise
smooth simple closed curve with interior $\Omega_1$ and exterior
$\Omega_2$. Assume $f'(z)$ exists in an open set containing $\gamma$
and $\Omega_2$ and $\lim_{z \rightarrow \infty } f(z) = A$. Show
that
$$\frac{1}{2 \pi i} \int_\gamma \frac{f(\xi)}{\xi - z} \, d \xi =
\begin{cases}
A,          &     \text{if\ $z \in \Omega_1$}, \\
-f (z) + A, &  \text{if\ $z \in \Omega_2$}
\end{cases}$$


**Question 63**

Let $f(z)$ be bounded and analytic in $\mathbb C$. Let $a \neq b$ be
any fixed complex numbers. Show that the following limit exists
$$\lim_{R \rightarrow \infty} \int_{|z|=R} \frac{f(z)}{(z-a)(z-b)} dz.$$
Use this to show that $f(z)$ must be a constant (Liouville's
theorem).


**Question 64**

Prove by *justifying all steps* that for all $\xi \in {\mathbb C}$
we have $\displaystyle
e^{- \pi \xi^2} = \int_{- \infty}^\infty e^{- \pi x^2} e^{2 \pi i x \xi} dx \; .$

> Hint: You may use that fact in Example 1 on p. 42 of the textbook
without proof, i.e., you may assume the above is true for real
values of $\xi$.


**Question 65**

Suppose that $f$ is holomorphic in an open set containing the closed
unit disc, except for a pole at $z_0$ on the unit circle. Let
$f(z) = \sum_{n = 1}^\infty c_n z^n$ denote the power series in
the open disc. Show that 

(1) $c_n \neq 0$ for all large enough $n$'s, and 

(2) $\displaystyle \lim_{n \rightarrow \infty} \frac{c_n}{c_{n+1}}= z_0$.


**Question 66**

Let $f(z)$ be a non-constant analytic function in $|z|>0$ such that
$f(z_n) = 0$ for infinite many points $z_n$ with
$\lim_{n \rightarrow \infty} z_n =0$. Show that $z=0$ is an
essential singularity for $f(z)$. (An example of such a function is
$f(z) = \sin (1/z)$.)


**Question 67**

Let $f$ be entire and suppose that
$\lim_{z \rightarrow \infty} f(z) = \infty$. Show that $f$ is a
polynomial.


**Question 68**

Expand the following functions into Laurent series in the indicated
regions:

(a)
$\displaystyle f(z) = \frac{z^2 - 1}{ (z+2)(z+3)}, \; \; 2 < |z| < 3$,
$3 < |z| < + \infty$.

(b)
$\displaystyle f(z) = \sin \frac{z}{1-z}, \; \; 0 < |z-1| < + \infty$


**Question 69**

Assume $f(z)$ is analytic in region $D$ and $\Gamma$ is a
rectifiable curve in $D$ with interior in $D$. Prove that if $f(z)$
is real for all $z \in \Gamma$, then $f(z)$ is a constant.


**Question 70**

Find the number of roots of $z^4 - 6z + 3 =0$ in $|z|<1$ and
$1 < |z| < 2$ respectively.


**Question 71**

Prove that $z^4 + 2 z^3 - 2z + 10 =0$ has exactly one root in each
open quadrant.


**Question 72**

(1) Let $f(z) \in H({\mathbb D})$, $\text{Re}(f(z)) >0$,
$f(0)= a>0$. Show that $$\abs{ \frac{f(z)-a}{f(z)+a}} \leq |z|, \; \; \;
|f'(0)| \leq 2a.$$

(2) Show that the above is still true if $\text{Re}(f(z)) >0$ is
replaced with $\text{Re}(f(z)) \geq 0$.


**Question 73**

Assume $f(z)$ is analytic in ${\mathbb D}$ and $f(0)=0$ and is not a
rotation (i.e. $f(z) \neq e^{i \theta} z$). Show that
$\displaystyle \sum_{n=1}^\infty f^{n}(z)$ converges uniformly to an
analytic function on compact subsets of ${\mathbb D}$, where
$f^{n+1}(z) = f(f^{n}(z))$.


**Question 74**

Let $f(z) = \sum_{n=0}^\infty c_n z^n$ be analytic and one-to-one in
$|z| < 1$. For $0<r<1$, let $D_r$ be the disk $|z|<r$. Show that the
area of $f(D_r)$ is finite and is given by
$$S = \pi \sum_{n=1}^\infty n |c_n|^2 r^{2n}.$$ (Note that in
general the area of $f(D_1)$ is infinite.)


**Question 75**

Let $f(z) = \sum_{n= -\infty}^\infty c_n z^n$ be analytic and
one-to-one in $r_0< |z| < R_0$. For $r_0<r<R<R_0$, let $D(r,R)$ be
the annulus $r<|z|<R$. Show that the area of $f(D(r,R))$ is finite
and is given by
$$S = \pi \sum_{n=- \infty}^\infty n |c_n|^2 (R^{2n} - r^{2n}).$$


**Question 76**

Let $a_n(z)$ be an analytic sequence in a domain $D$ such that
$\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$. Show that
$\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$.


**Question 77**

Let $f_n, f$ be analytic functions on the unit disk ${\mathbb D}$.
Show that the following are equivalent.

(i) $f_n(z)$ converges to $f(z)$ uniformly on compact subsets in
$\mathbb D$.

(ii) $\int_{|z|= r} |f_n(z) - f(z)| \, |dz|$ converges to $0$ if
$0< r<1$.


**Question 78**

Let $f$ and $g$ be non-zero analytic functions on a region $\Omega$.
Assume $|f(z)| = |g(z)|$ for all $z$ in $\Omega$. Show that
$f(z) = e^{i \theta} g(z)$ in $\Omega$ for some
$0 \leq \theta < 2 \pi$.


**Question 79**

Suppose $f$ is analytic in an open set containing the unit disc
$\mathbb D$ and $|f(z)| =1$ when $|z|$=1. Show that either
$f(z) = e^{i \theta}$ for some $\theta \in \mathbb R$ or there are
finite number of $z_k \in \mathbb D$, $k \leq n$ and
$\theta \in \mathbb R$ such that
$\displaystyle f(z) = e^{i\theta} \prod_{k=1}^n \frac{z-z_k}{1 - \bar{z}_k z } \, .$

> Also cf. Stein et al, 1.4.7, 3.8.17


**Question 80**

(1) Let $p(z)$ be a polynomial, $R>0$ any positive number, and
$m \geq 1$ an integer. Let
$$M_R = \sup \{ |z^{m} p(z) - 1|: |z| = R  \}.$$ Show that $M_R>1$.

(2) Let $m \geq 1$ be an integer and
$K = \{z \in {\mathbb C}: r \leq |z| \leq R \}$ where $r<R$.
Show (i) using (1) as well as, (ii) without using (1) that there
exists a positive number $\varepsilon_0>0$ such that for each
polynomial $p(z)$,
$$\sup \{|p(z) - z^{-m}|: z \in K  \} \geq \varepsilon_0 \, .$$


**Question 81**

Let $\displaystyle f(z) = \frac{1}{z} + \frac{1}{z^2 -1}$. Find all
the Laurent series of $f$ and describe the largest annuli in which
these series are valid.


**Question 82**

Suppose $f$ is entire and there exist $A, R >0$ and natural number
$N$ such that $|f(z)| \leq A |z|^N$ for $|z| \geq R$. Show that 

(i) $f$ is a polynomial and 

(ii) the degree of $f$ is at most $N$.


**Question 83**

(1) Explicitly write down an example of a non-zero analytic
function in $|z|<1$ which has infinitely zeros in $|z|<1$.

(2) Why does not the phenomenon in (1) contradict the uniqueness
theorem?


**Question 84**

(1) Assume $u$ is harmonic on open set $O$ and $z_n$ is a sequence
in $O$ such that $u(z_n) = 0$ and $\lim z_n \in O$. Prove or
disprove that $u$ is identically zero. What if $O$ is a region?

(2) Assume $u$ is harmonic on open set $O$ and $u(z) = 0$ on a
disc in $O$. Prove or disprove that $u$ is identically zero. What if
$O$ is a region?

(3) Formulate and prove a Schwarz reflection principle for
harmonic functions 

> cf. Theorem 5.6 on p.60 of Stein et al.

> Hint: Verify the mean value property for your new function obtained by
Schwarz reflection principle.


**Question 85**

Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that
for any $s<r$, there exists a constant $c>0$ such that
$$||f||_{(\infty, s)} \leq c ||f||_{(1, r)},$$ where
$\displaystyle |f||_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$
and $\displaystyle ||f||_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.

> Note: Exercise 3.8.20 on p.107 in Stein et al is a
straightforward consequence of this stronger result using the
integral form of the Cauchy-Schwarz inequality in real analysis.


**Question 86**

(1) Let $f$ be analytic in $\Omega: 0<|z-a|<r$ except at a
sequence of poles $a_n \in \Omega$ with
$\lim_{n \rightarrow \infty} a_n = a$. Show that for any
$w \in \mathbb C$, there exists a sequence $z_n \in \Omega$ such
that $\lim_{n \rightarrow \infty} f(z_n) = w$.

(2) Explain the similarity and difference between the above
assertion and the Weierstrass-Casorati theorem.


**Question 87**

Compute the following integrals.

\(i\) $\displaystyle \int_0^\infty \frac{1}{(1 + x^n)^2} \, dx$,
$n \geq 1$ (ii)
$\displaystyle \int_0^\infty \frac{\cos x}{(x^2 + a^2)^2} \, dx$,
$a \in \mathbb R$ (iii)
$\displaystyle \int_0^\pi \frac{1}{a + \sin \theta} \, d \theta$,
$a>1$

\(iv\) $\displaystyle \int_0^{\frac{\pi}{2}}
\frac{d \theta}{a+ \sin ^2 \theta},$ $a >0$. (v)
$\displaystyle \int_{|z|=2} \frac{1}{(z^{5} -1) (z-3)} \, dz$ (v)
$\displaystyle \int_{- \infty}^{\infty} \frac{\sin \pi a}{\cosh \pi x + \cos \pi a} e^{- i x \xi} \, d x$,
$0< a <1$, $\xi \in \mathbb R$ (vi)
$\displaystyle \int_{|z| = 1} \cot^2 z \, dz$.


**Question 88**

Compute the following integrals.

\(i\) $\displaystyle \int_0^\infty \frac{\sin x}{x} \, dx$ (ii)
$\displaystyle \int_0^\infty (\frac{\sin x}{x})^2 \, dx$ (iii)
$\displaystyle \int_0^\infty \frac{x^{a-1}}{(1 + x)^2} \, dx$,
$0< a < 2$

\(i\)
$\displaystyle \int_0^\infty \frac{\cos a x - \cos bx}{x^2} dx$,
$a, b >0$ (ii)
$\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$,
$0< a < n$

\(iii\) $\displaystyle \int_0^\infty \frac{\log x}{1 + x^n} \, dx$,
$n \geq 2$ (iv)
$\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2} dx$ (v)
$\displaystyle \int_0^{\pi} \log|1 - a \sin \theta| d \theta$,
$a \in \mathbb C$


**Question 89**

Let $0<r<1$. Show that polynomials
$P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in
$|z|<r$ for all sufficiently large $n$'s.


**Question 90**

Let $f$ be an analytic function on a region $\Omega$. Show that $f$
is a constant if there is a simple closed curve $\gamma$ in $\Omega$
such that its image $f(\gamma)$ is contained in the real axis.


**Question 91**

(1) Show that $\displaystyle \frac{\pi^2}{\sin^2 \pi z}$ and
$\displaystyle g(z) = \sum_{n = - \infty}^{ \infty} \frac{1}{(z-n)^2}$
have the same principal part at each integer point.

(2) Show that
$\displaystyle h(z) = \frac{\pi^2}{\sin^2 \pi z} - g(z)$ is bounded
on $\mathbb C$ and conclude that
$\displaystyle \frac{\pi^2}{\sin^2 \pi z} = \sum_{n = - \infty}^{ \infty} \frac{1}{(z-n)^2} \, .$


**Question 92**

Let $f(z)$ be an analytic function on
${\mathbb C} \backslash \{ z_0 \}$, where $z_0$ is a fixed point.
Assume that $f(z)$ is bijective from
${\mathbb C} \backslash \{ z_0 \}$ onto its image, and that $f(z)$
is bounded outside $D_r(z_0)$, where $r$ is some fixed positive
number. Show that there exist $a, b, c, d \in \mathbb C$ with
$ad-bc \neq 0$, $c \neq 0$ such that
$\displaystyle f(z) = \frac{az + b}{cz + d}$.


**Question 93**

Assume $f(z)$ is analytic in $\mathbb D: |z|<1$ and $f(0)=0$ and
is not a rotation (i.e. $f(z) \neq e^{i \theta} z$). Show that
$\displaystyle \sum_{n=1}^\infty f^{n}(z)$ converges uniformly to an
analytic function on compact subsets of ${\mathbb D}$, where
$f^{n+1}(z) = f(f^{n}(z))$.


**Question 94**

Let $f$ be a non-constant analytic function on $\mathbb D$ with
$f(\mathbb D) \subseteq \mathbb D$. Use $\psi_{a} (f(z))$ (where
$a=f(0)$, $\displaystyle \psi_a(z) = \frac{a - z}{1 - \bar{a}z}$) to
prove that $$\displaystyle
\frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq
\frac{|f(0)| + |z|}{1 - |f(0)||z|}.$$


**Question 95**

Find a conformal map

1.  from $\{ z: |z - 1/2| > 1/2, \text{Re}(z)>0 \}$ to $\mathbb H$

2.  from $\{ z: |z - 1/2| > 1/2, |z| <1  \}$ to $\mathbb D$

3.  from the intersection of the disk $|z + i| < \sqrt{2}$ with
    ${\mathbb H}$ to ${\mathbb D}$.

4.  from ${\mathbb D}  \backslash [a, 1)$ to
    ${\mathbb D} \backslash [0, 1)$ ($0<a<1)$. \[ Short solution
    possible using Blaschke factor\]

5.  from $\{ z: |z| < 1, \text{Re}(z) > 0 \} \backslash (0, 1/2]$ to
    $\mathbb H$.


**Question 96**

Let $C$ and $C'$ be two circles and let $z_1 \in C$, $z_2 \notin C$,
$z'_1 \in C'$, $z'_2 \notin C'$. Show that there is a unique
fractional linear transformation $f$ with $f(C) = C'$ and
$f(z_1) = z'_1$, $f(z_2) = z'_2$.


**Question 97**

Assume $f_n \in H(\Omega)$ is a sequence of holomorphic functions on
the region $\Omega$ that are uniformly bounded on compact subsets
and $f \in H(\Omega)$ is such that the set
$\displaystyle \{z \in \Omega: \lim_{n \rightarrow \infty} f_n(z) = f(z) \}$
has a limit point in $\Omega$. Show that $f_n$ converges to $f$
uniformly on compact subsets of $\Omega$.


**Question 98**

Let
$\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
with $|\alpha|<1$ and ${\mathbb D}=\{z:\ |z|<1\}$. Prove that

-   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}|^2 dx dy =1}$.

-   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}| dx dy =\frac{1-|\alpha|^2}{|\alpha|^2}
    \log \frac{1}{1-|\alpha|^2}}$.


**Question 99**

Prove that
$\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$ is a
conformal map from half disc $\{z=x+iy:\ |z|<1,\ y>0\}$ to upper
half plane ${\mathbb H}=\{z=x+iy:\ y>0\}$.


**Question 100**

Let $\Omega$ be a simply connected open set and let $\gamma$ be a
simple closed contour in $\Omega$ and enclosing a bounded region $U$
anticlockwise. Let $f: \ \Omega \to {\mathbb C}$ be a holomorphic
function and $|f(z)|\leq M$ for all $z\in \gamma$. Prove that
$|f(z)|\leq M$ for all $z\in U$.


**Question 101**

Compute the following integrals. 

(i)
$\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$,
$0< a < n$ 

(ii)
$\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$


**Question 102**

Let $0<r<1$. Show that polynomials
- Holomorphic Functions
$P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in
$|z|<r$ for all sufficiently large $n$'s.


**Question 103**

Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that
for any $s<r$, there exists a constant $c>0$ such that
$$\|f\|_{(\infty, s)} \leq c \|f\|_{(1, r)},$$ where
$\displaystyle \|f\|_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$
and $\displaystyle \|f\|_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.


**Question 104**

Let $\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
with $|\alpha|<1$ and ${\mathbb D}=\{z:\ |z|<1\}$. Prove that

-   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}|^2 dx dy =1}$.

-   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}| dx dy =\frac{1-|\alpha|^2}{|\alpha|^2}
    \log \frac{1}{1-|\alpha|^2}}$.


**Question 105**

Let $\Omega$ be a simply connected open set and let $\gamma$ be a simple
closed contour in $\Omega$ and enclosing a bounded region $U$
anticlockwise. Let $f: \ \Omega \to {\mathbb C}$ be a holomorphic
function and $|f(z)|\leq M$ for all $z\in \gamma$. Prove that
$|f(z)|\leq M$ for all $z\in U$.


**Question 106**

Compute the following integrals. 

(i) $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$, $0< a < n$

(ii) $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$


**Question 107**

Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that for
any $s<r$, there exists a constant $c>0$ such that
$$\|f\|_{(\infty, s)} \leq c \|f\|_{(1, r)},$$ where
$\displaystyle \|f\|_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$
and $\displaystyle \|f\|_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.


**Question 108**

Let $u(x,y)$ be harmonic and have continuous partial derivatives of
order three in an open disc of radius $R>0$.

(a) Let two points $(a,b), (x,y)$ in this disk be given. Show that
the following integral is independent of the path in this disk
joining these points:
$$v(x,y) = \int_{a,b}^{x,y} ( -\frac{\partial u}{\partial y}dx +  \frac{\partial u}{\partial x}dy).$$\

(b) \hfill

    (i) Prove that $u(x,y)+i v(x,y)$ is an analytic function in this disc.

    (ii) Prove that $v(x,y)$ is harmonic in this disc.


**Question 109**

(a) $f(z)= u(x,y) +i v(x,y)$ be analytic in a domain
$D\subset {\mathbb C}$. Let $z_0=(x_0,y_0)$ be a point in $D$ which
is in the intersection of the curves $u(x,y)= c_1$ and $v(x,y)=c_2$,
where $c_1$ and $c_2$ are constants. Suppose that $f'(z_0)\neq 0$.
Prove that the lines tangent to these curves at $z_0$ are
perpendicular.

(b) Let $f(z)=z^2$ be defined in ${\mathbb C}$. 
  (i)   Describe the
        level curves of $\mbox{\textrm Re}{(f)}$ and of $\mbox{Im}{(f)}$.
  
  (ii)  What are the angles of intersections between the level curves
        $\mbox{\textrm Re}{(f)}=0$ and $\mbox{\textrm Im}{(f)}$? Is your answer in
        agreement with part a) of this question?


**Question 110**

(a) Let $f: D\rightarrow \mathbb C$ be a continuous function, where
$D\subset \mathbb C$ is a domain. Let $\alpha:[a,b]\rightarrow D$
be a smooth curve. Give a precise definition of the *complex line
integral* $$\int_{\alpha} f.$$

(b) Assume that there exists a constant $M$ such that
$|f(\tau)|\leq M$ for all $\tau\in \mbox{\textrm Image}(\alpha$). Prove
that
$$\big | \int_{\alpha} f \big |\leq M \times \mbox{\textrm length}(\alpha).$$

(c) Let $C_R$ be the circle $|z|=R$, described in the
counterclockwise direction, where $R>1$. Provide an upper bound for
$\abs{ \int_{C_R} \dfrac{\log{(z)} }{z^2} }$ which depends
*only* on $R$ and other constants.


**Question 111**

(a) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire
function. Assume the existence of a non-negative integer $m$, and of
positive constants $L$ and $R$, such that for all $z$ with $|z|>R$
the inequality $$|f(z)| \leq L |z|^m$$ holds. Prove that $f$ is a
polynomial of degree $\leq m$.

(b) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire
function. Suppose that there exists a real number M such that for
all $z\in {\mathbb C}$ $$\mbox{\textrm Re} (f) \leq M.$$ Prove that $f$
must be a constant.


**Question 112**

Prove that all the roots of the complex polynomial
$$z^7 - 5 z^3 +12 =0$$ lie between the circles $|z|=1$ and $|z|=2$.


**Question 113**

Let $F$ be an analytic function inside and on a simple closed
curve $C$, except for a pole of order $m\geq 1$ at $z=a$ inside $C$.
Prove that

$$
\frac{1}{2 \pi i}\oint_{C} F(\tau) d\tau = 
\lim_{\tau\rightarrow a} \frac{d^{m-1}}{d\tau^{m-1}}\big((\tau-a)^m F(\tau))\big)
.$$


**Question 114**

Find the conformal map that takes the upper half-plane comformally
onto the half-strip $\{
w=x+iy:\ -\pi/2<x<\pi/2\ y>0\}$.


**Question 115**

Compute the integral
$\displaystyle{\int_{-\infty}^{\infty} \frac{e^{-2\pi ix\xi}}{\cosh\pi x}dx}$
where $\displaystyle{\cosh z=\frac{e^{z}+e^{-z}}{2}}$.


**Question 116**

Use residues to compute the integral
\begin{align*}
\int_{0}^{\infty} \dfrac{\cos x}{(x^2+1)^2} \mathrm{d}x
\end{align*}


**Question 117**

State and prove the Cauchy integral formula for holomorphic
functions.


**Question 118**

Let $f$ be an entire function and suppose that $|f(z)| \leq A|z|^2$
for all $z$ and some constant $A$. Show that $f$ is a polynomial of
degree $\leq 2$.


**Question 119**

1.  State the Schwarz lemma for analytic functions in the unit disc.

2.  Let $f: \mathbb{D} \to \mathbb{D}$ be an analytic map from the
    unit disc $\mathbb{D}$ into itself. Use the Schwarz lemma to
    show that for each $a\in \mathbb{D}$ we have
    \begin{align*}
    \dfrac{|f'(a)|}{1-|f(a)|^2} \leq \dfrac{1}{1-|a|^2}
    \end{align*}


**Question 120**

State the Riemann mapping theorem and prove the uniqueness part.


**Question 121**

Compute the integrals
\begin{align*}
\int_{|z-2|=1} \dfrac{e^z}{z(z-1)^2} \,
\mathrm{d}z, \quad \int_0^\infty \dfrac{\cos 2x}{x^2 + 2} \, \mathrm{d}x
\end{align*}


**Question 122**

Let $(f_n)$ be a sequence of holomorphic functions in a domain $D$.
Suppose that $f_n \to f$ uniformly on each compact subset of $D$.
Show that

-   $f$ is holomorphic on $D$.

-   $f_n' \to f'$ uniformly on each compact subset of $D$.


**Question 123**

If $f$ is a non-constant entire function, then $f(\mathbb{C})$ is
dense in the plane.


**Question 124**

1.  State Rouche's theorem.

2.  Let $f$ be analytic in a neighborhood of $0$, and satisfying
    $f'(0) \neq 0$. Use Rouche's theorem to show that there exists a
    neighborhood $U$ of $0$ such that $f$ is a bijection in $U$.


**Question 125**

Let $f$ be a meromorphic function in the plane such that
\begin{align*}
\lim_{|z|\to\infty} |f(z)| = \infty
\end{align*}

1.  Show that $f$ has only finitely many poles.

2.  Show that $f$ is a rational function.

# Topology (1 Questions)

**Question 1**

Something something $G$.
