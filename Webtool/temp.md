---
title: Qualifying Exam
---

## Question 1 (UGA 2018 #5)

Let $f \geq 0$ be a measurable function on $\RR$.
Show that
$$
\int_{\mathbb{R}} f=\int_{0}^{\infty} m(\{x: f(x)>t\}) d t
$$


\newpage## Question 2 (UGA 2016 #5)

Let $\phi\in L^\infty(\RR)$. Show that the following limit exists and satisfies the equality
$$
\lim _{n \rightarrow \infty}\left(\int_{\mathbb{R}} \frac{|\phi(x)|^{n}}{1+x^{2}} d x\right)^{\frac{1}{n}} = \norm{\phi}_\infty.
$$


\newpage## Question 3 (UGA 2015 #6)

Let $f: [0, 1] \to \RR$ be continuous.
Show that
$$
\sup \left\{\|f g\|_{1} \suchthat g \in L^{1}[0,1],~~ \|g\|_{1} \leq 1\right\}=\|f\|_{\infty}
$$


\newpage## Question 4 (Emory 0 #0)

State and prove Fatou's Lemma on a general measurable space.


\newpage## Question 5 (UGA 2018 #5)

Suppose that

- $f_n, f \in L^1$,
- $f_n \to f$ almost everywhere, and
- $\int\left|f_{n}\right| \rightarrow \int|f|$.

Show that $\int f_{n} \rightarrow \int f$


\newpage## Question 6 (UGA 2016 #4)

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


\newpage## Question 7 (NUS 1970 #4)

Prove or disprove each of the following statements.

(a) If $f : [0, 1] → \mathbb{R}$ is a measurable function, then given any $\varepsilon > 0$, there exists a compact set $K \subset [0, 1]$ such that $f$ is continuous on $K$ relative to $K$.

(c) If f is Borel measurable on $\mathbb{R} × \mathbb{R}$, then for any $x \in \mathbb{R}$, the function $g(y) = f(x, y)$ is also Borel measurable on $\mathbb{R}$.

(d) If $E \subset \mathbb{R}$, then $E$ is measurable if and only if given any $\varepsilon > 0$, there exist a closed set $F$ and an open set $G$ such that $F \subset E \subset G$ and the measure of $G-F$ is less than $\varepsilon$.


\newpage## Question 8 (Emory 0 #0)

Let $f$ be a continuous function on $[0,1]$. Show that the following
statements are equivalent.

1.  $f$ is absolutely continuous.

2.  For any $\epsilon > 0$ there exists $\delta > 0$ such that
    $m(f(E)) < \epsilon$ for any set $E\subseteq [0,1]$ with
    $m(E) < \delta$.

3.  $m(f(E)) = 0$ for any set $E \subseteq [0,1]$ with $m(E)=0$.


\newpage## Question 9 (UGA 2019 #4)

Let $f$ be a non-negative function on $\RR^n$ and $\mathcal A = \{(x, t) \in \RR^n × \RR : 0 ≤ t ≤ f (x)\}$.

Prove the validity of the following two statements:

a. $f$ is a Lebesgue measurable function on $\RR^n \iff  \mathcal A$ is a Lebesgue measurable subset of $\RR^{n+1}$

b. If $f$ is a Lebesgue measurable function on $\RR^n$, then
$$
m(\mathcal{A})=\int_{\mathbb{R}^{n}} f(x) d x=\int_{0}^{\infty} m\left(\left\{x \in \mathbb{R}^{n}: f(x) \geq t\right\}\right) d t
$$


\newpage## Question 10 (UGA 2015 #5)

Let $\mathcal H$ be a Hilbert space.

1. Let $x\in \mathcal H$ and $\theset{u_n}_{n=1}^N$ be an orthonormal set.
  Prove that the best approximation to $x$ in $\mathcal H$ by an element in $\spanof_\CC\theset{u_n}$ is given by
  $$
  \hat x \definedas \sum_{n=1}^N \inner{x}{u_n}u_n.
  $$
2. Conclude that finite dimensional subspaces of $\mathcal H$ are always closed.


\newpage