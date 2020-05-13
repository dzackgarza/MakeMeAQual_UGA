---
title: Emory Quals
author: Santiago Arango
---


Algebra
=======

Groups
------

1.  Classify the groups of order $182 = 2 \cdot 7 \cdot 13$.

2.  Let $G$ be a finite group of order $p^nm$ where $p$ is a prime and
    $m$ is not divisible by $p$. Prove that if $H$ is a subgroup of $G$
    of order $p^k$ for some $k<n$, then the normalizer of $H$ in $G$
    properly contains $H$.

3.  Let $H$ be a subgroup of $S_n$ of index $n$. Prove:

    1.  There is an isomorphism $f: S_n \to S_n$ such that $f(H)$ is the
        subgroup of $S_n$ stabilizing $n$. In particular, $H$ is
        isomorphic to $S_{n-1}$.

    2.  The only subgroups of $S_n$ containing $H$ are $S_n$ and $H$.

4.  -   Prove that a group of order $351=3^3\cdot 13$ cannot be simple.

    -   Prove that a group of order $33$ must be cyclic.

5.  1.  Let $G$ be a group, and $Z(G)$ the center of $G$. Prove that if
        $G/Z(G)$ is cyclic, then $G$ is abelian.

    2.  Prove that a group of order $p^n$, where $p$ is a prime and
        $n \geq 1$, has non-trivial center.

    3.  Prove that a group of order $p^2$ must be abelian.

6.  Let $G$ be a finite group.

    1.  Prove that if $H < G$ is a proper subgroup, then $G$ is not the
        union of conjugates of $H$.

    2.  Suppose that $G$ acts transitively on a set $X$ with $|X| > 1$.
        Prove that there exists an element of $G$ with no fixed points
        in $X$.

7.  Classify all groups of order $15$ and of order $30$.

8.  Count the number of $p$-Sylow subgroups of $S_p$.

9.  1.  Let $G$ be a group of order $n$. Suppose that for every divisor
        $d$ of $n$, $G$ contains at most one subgroup of order $d$. Show
        that $G$ is clyclic.

    2.  Let $F$ be a field. Show that every finite subgroup of the group
        of units $F^\times$ is cyclic.

Fields and Galois Theory
------------------------

1.  Let $K$ and $L$ be finite fields. Show that $K$ is contained in $L$
    if and only if $\# K = p^r$ and $\# L = p^s$ for the same prime $p$,
    and $r \leq s$.

2.  Let $K$ and $L$ be finite fields with $K \subseteq L$. Prove that
    $L$ is Galois over $K$ and that $\mathrm{Gal}(L/K)$ is cyclic.

3.  Fix a field $F$, a separable polynomial $f\in F[x]$ of degree
    $n \geq 3$, and a splitting field $L$ for $f$. Prove that if
    $[L:F] = n!$ then:

    1.  $f$ is irreducible.

    2.  For each root $r$ of $f$, $r$ is the unique root of $f$ in
        $F(r)$.

    3.  For every root $r$ of $f$, there are no proper intermediate
        fields $F \subset L \subset F(r)$.

4.  1.  Show that $\sqrt{2+\sqrt{2}}$ is a root of
        $p(x) = x^2 - 4x^2 + 2 \in \mathbf{Q}[x]$.

    2.  Prove that $\mathbf{Q}(\sqrt{2 + \sqrt{2}})$ is a Galois
        extension of $\mathbf{Q}$ and find its Galois group. (Hint: note
        that $\sqrt{2 - \sqrt{2}}$ is another root of $p(x)$).

    3.  Let $f(x) = x^3 - 5$. Determine the splitting field $K$ of
        $f(x)$ over $\mathbf{Q}$ and the Galois group of $f(x)$. Give an
        example of a proper sub-extension
        $\mathbf{Q} \subset L \subset K$, such that $L/\mathbf{Q}$ is
        Galois.

Rings
-----

1.  An integral domain $R$ is said to be an *Euclidean domain* if there
    is a function $N: R \to \{n\in\mathbf{Z} \mid n\geq 0\}$ such that
    $N(0)=0$ and for each $a,b\in R$ with $b\neq 0$, there exist
    elements $q,r\in R$ with $$\begin{aligned}
            a = qb + r, \quad \text{and} \quad r = 0 \, \text{ or } \, N(r) < N(b).
        \end{aligned}$$ Prove:

    1.  The ring $F[[x]]$ of power series over a field $F$ is an
        Euclidean domain.

    2.  Every Euclidean domain is a PID.

2.  Let $F$ be a field, and let $R$ be the subring of $F[X]$ of
    polynomials with $X$ coefficient equal to $0$. Prove that $R$ is not
    a UFD.

3.  $R$ is a commutative ring with 1. Prove that if $I$ is a maximal
    ideal in $R$, then $R/I$ is a field. Prove that if $R$ is a PID,
    then every nonzero prime ideal in $R$ is maximal. Conclude that if
    $R$ is a PID and $p\in R$ is prime, then $R/(p)$ is a field.

Linear Algebra
--------------

1.  Prove that any square matrix is conjugate to its transpose matrix.
    (You may prove it over $\mathbf{C}$).

2.  Determine the number of conjugacy classes of $16 \times 16$ matrices
    with entries in $\mathbf{Q}$ and minimal polynomial
    $(x^2+1)^2(x^3+2)^2$.

3.  Let $V$ be a vector space over a field $F$. The evaluation map
    $e\colon V \to (V^\vee)^\vee$ is defined by
    $e(v)(f) \colonequals f(v)$ for $v\in V$ and $f\in V^\vee$.

    1.  Prove that $e$ is an injection.

    2.  Prove that $e$ is an isomorphism if and only if $V$ is finite
        dimensional.

4.  Let $R$ be a principal ideal domain that is not a field, and write
    $F$ for its field of fractions. Prove that $F$ is not a finitely
    generated $R$-module.

5.  Carefully state Zorn's lemma and use it to prove that every vector
    space has a basis.

Analysis
========

Complex Analysis
----------------

1.  Use residues to compute the integral $$\begin{aligned}
            \int_{0}^{\infty} \dfrac{\cos x}{(x^2+1)^2} \mathrm{d}x \, .
        \end{aligned}$$

2.  State and prove the Cauchy integral formula for holomorphic
    functions.

3.  Use the Cauchy integral formula to prove the maximal principle for
    analytic functions.

4.  Let $f$ be an entire function and suppose that $|f(z)| \leq A|z|^2$
    for all $z$ and some constant $A$. Show that $f$ is a polynomial of
    degree $\leq 2$.

5.  1.  State the Schwarz lemma for analytic functions in the unit disc.

    2.  Let $f: \mathbf{D} \to \mathbf{D}$ be an analytic map from the
        unit disc $\mathbf{D}$ into itself. Use the Schwarz lemma to
        show that for each $a\in \mathbf{D}$ we have $$\begin{aligned}
                 \dfrac{|f'(a)|}{1-|f(a)|^2} \leq \dfrac{1}{1-|a|^2} \, .
             \end{aligned}$$

6.  State the Riemann mapping theorem and prove the uniqueness part.

7.  Compute the integrals $$\begin{aligned}
            \int_{|z-2|=1} \dfrac{e^z}{z(z-1)^2} \, 
            \mathrm{d}z, \quad \int_0^\infty \dfrac{\cos 2x}{x^2 + 2} \, \mathrm{d}x \, .
        \end{aligned}$$

8.  Let $(f_n)$ be a sequence of holomorphic functions in a domain $D$.
    Suppose that $f_n \to f$ uniformly on each compact subset of $D$.
    Show that

    -   $f$ is holomorphic on $D$.

    -   $f_n' \to f'$ uniformly on each compact subset of $D$.

9.  If $f$ is a non-constant entire function, then $f(\mathbf{C})$ is
    dense in the plane.

10. 1.  State Rouche's theorem.

    2.  Let $f$ be analytic in a neighborhood of $0$, and satisfying
        $f'(0) \neq 0$. Use Rouche's theorem to show that there exists a
        neighborhood $U$ of $0$ such that $f$ is a bijection in $U$.

11. Let $f$ be a meromorphic function in the plane such that
    $$\begin{aligned}
           \lim_{|z|\to\infty} |f(z)| = \infty \, .
       \end{aligned}$$

    1.  Show that $f$ has only finitely many poles.

    2.  Show that $f$ is a rational function.

Real Analysis
-------------

1.  Describe the process that extends a measure on an algebra
    $\mathcal{A}$ of subsets of $X$, to a complete measure defined on a
    $\sigma$-algebra $\mathcal{B}$ containing $\mathcal{A}$. State the
    corresponding definitions and results (without proofs).

2.  State and prove Fatou's Lemma on a general measurable space.

3.  1.  State the Dominated Convergence Theorem for Lebesgue integrals.

    2.  Let $\{f_n\}$ be a sequence of measurable functions on a
        Lebesgue measurable set $E$ which converges *in measure* to a
        function $f$ on $E$. Suppose that for every $n$, $|f_n| \leq g$
        with $g$ integrable on $E$. Using the above theorem show that
        $$\begin{aligned}
                    \int_E |f_n-f| \longrightarrow 0 \, .
                \end{aligned}$$

4.  Let $f\in L^1([0,1])$. Show that

    1.  The limit $\lim_{p\to 0^+} \| f \|_p$ exists.

    2.  If $m \{x : f(x) = 0\} > 0$, then the above limit is zero.

5.  Let $f$ be a continuous function on $[0,1]$. Show that the following
    statements are equivalent.

    1.  $f$ is absolutely continuous.

    2.  For any $\epsilon > 0$ there exists $\delta > 0$ such that
        $m(f(E)) < \epsilon$ for any set $E\subseteq [0,1]$ with
        $m(E) < \delta$.

    3.  $m(f(E)) = 0$ for any set $E \subseteq [0,1]$ with $m(E)=0$.
