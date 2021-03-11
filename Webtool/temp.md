---
title: Qualifying Exam
---

# Question 1 (UGA 2014 #5)

Let $f, g \in L^1([0, 1])$ and for all $x\in [0, 1]$ define
$$
F(x):=\int_{0}^{x} f(y) d y \quad \text { and } \quad G(x):=\int_{0}^{x} g(y) d y.
$$

Prove that
$$
\int_{0}^{1} F(x) g(x) d x=F(1) G(1)-\int_{0}^{1} f(x) G(x) d x
$$


\newpage# Question 2 (NUS 1970 #1fg)

Prove or disprove each of the following statements.

(f) If $E \subset \mathbb{R}$ and 

    $\mu(E) = \inf\{\sum_{I_i \in S} |I_i| : S = \{I_i\}_{i=1}^n \text{ such that } E \subset \union_{i=1}^n I_i \text{ for some } n \in \mathbb{N}\}$

    then $\mu$ coincides with the outer measure of $E$.

(g) If $E$ is a Borel set and $f$ is a measurable function, then $f^{-1}(E)$ is also measurable.


\newpage# Question 3 (Emory 0 #0)

State and prove Fatou's Lemma on a general measurable space.


\newpage# Question 4 (UGA 2016 #4)

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


\newpage# Question 5 (NUS 1970 #1)

If $\limsup_{n\rightarrow \infty} a_n\leq l$, show that $\limsup_{n\rightarrow \infty}\sum_{i=1}^n{a_i/n}\leq l$.  


\newpage# Question 6 (UGA 2015 #4)

Let $f: [1, \infty) \to \RR$ such that $f(1) = 1$ and
$$
f^{\prime}(x)= \frac{1} {x^{2}+f(x)^{2}}
$$

Show that the following limit exists and satisfies the equality
$$
\lim _{x \rightarrow \infty} f(x) \leq 1 + \frac \pi 4
$$


\newpage# Question 7 (UGA 2018 #5)

Let $f \geq 0$ be a measurable function on $\RR$.
Show that
$$
\int_{\mathbb{R}} f=\int_{0}^{\infty} m(\{x: f(x)>t\}) d t
$$


\newpage# Question 8 (UGA 2018 #2)

Let
$$
f_{n}(x):=\frac{x}{1+x^{n}}, \quad x \geq 0.
$$

a. Show that this sequence converges pointwise and find its limit. Is the convergence uniform on $[0, \infty)$?

b. Compute 
$$
\lim _{n \rightarrow \infty} \int_{0}^{\infty} f_{n}(x) d x
$$


\newpage# Question 9 (UGA 2015 #4)

Define
$$
f(x, y):=\left\{\begin{array}{ll}{\frac{x^{1 / 3}}{(1+x y)^{3 / 2}}} & {\text { if } 0 \leq x \leq y} \\ {0} & {\text { otherwise }}\end{array}\right.
$$

Carefully show that $f \in L^1(\RR^2)$.


\newpage# Question 10 (UGA 2018 #3)

Suppose $f(x)$ and $xf(x)$ are integrable on $\RR$.
Define $F$ by
$$
F(t):=\int_{-\infty}^{\infty} f(x) \cos (x t) d x
$$
Show that 
$$
F'(t)=-\int_{-\infty}^{\infty} x f(x) \sin (x t) d x.
$$


\newpage