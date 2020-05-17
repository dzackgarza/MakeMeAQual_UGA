  # Fall 2009

---
	  (1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$
    converges in $|z| < R$. Show that for $r <R$,
    $$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
    \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

    (2) Deduce Liouville's theorem from (1).

---
	  Let $f$ be a continuous function in the region
    $$D=\{z \suchthat  \abs{z}>R, 0\leq \arg z\leq \theta\}\quad\text{where}\quad
    1\leq \theta \leq 2\pi.$$ If there exists $k$ such that
    $\displaystyle{\lim_{z\to\infty} zf(z)=k}$ for $z$ in the region
    $D$. 
    Show that $$\lim_{R'\to\infty} \int_{L} f(z) dz=i\theta k,$$
    where $L$ is the part of the circle $|z|=R'$ which lies in the
    region $D$.

---
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

---
	  Evaluate $$\displaystyle{ \int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \,
    dx }.$$

---
	  Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
    partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
    that
    $$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
    \frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$

---
	  Show that $\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n}
    dx=\frac{\pi}{n\sin \frac{a\pi}{n}}$ using complex analysis, $0< a <
    n$. Here $n$ is a positive integer.

---
	  For $s>0$, the **gamma function** is defined by
    $\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

    1.  Show that the gamma function is analytic in the half-plane
        $\Re (s)>0$, and is still given there by the integral formula
        above.

    2.  Apply the formula in the previous question to show that
        $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

    > Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.

---
	  Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra: If
    $$P_n(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + a_nz^n\quad  (a_n \neq 0)$$
    is a polynomial of degree n, then it has n zeros in $\mathbb C$.

---
	  Suppose $f$ is entire and there exist $A, R >0$ and natural number
    $N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show
    that 
    (i) $f$ is a polynomial and 
    (ii) the degree of $f$ is at least $N$.

---
	 Let $f: {\mathbb C} \rightarrow {\mathbb C}$ be an injective
    analytic (also called *univalent*) function. Show that there exist
    complex numbers $a \neq 0$ and $b$ such that $f(z) = az + b$.

---
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

---
	 Find a conformal map from $D = \{z :\  |z| < 1,\ |z - 1/2| > 1/2\}$
    to the unit disk $\Delta=\{z: \ |z|<1\}$.

---
	 Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded*
open set $\Omega$. Show without using Picard's theorems that $f(z)$ is a
constant.

---
	  (1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$ converges
    in $|z| < R$. Show that for $r <R$,
    $$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta
    = \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

    (2) Deduce Liouville's theorem from (1).

---
	 Let $f(z)$ be entire and assume that $f(z) \leq M |z|^2$ outside some
disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of
degree $\leq 2$.

---
	 Let $a_n(z)$ be an analytic sequence in a domain $D$ such that
$\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$. Show that
$\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on
bounded and closed sub-regions of $D$.

---
    Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a
    point $z_0$ inside $\Omega$. Show that if $f(z)$ is bounded in near
    $z_0$, then $\displaystyle \int_\Delta f(z) dz = 0$ for all triangles
    $\Delta$ in $\Omega$.

---
	 Assume $f$ is continuous in the region:
$0< |z-a| \leq R, \; 0 \leq \arg(z-a) \leq \beta_0$
($0 < \beta_0 \leq 2 \pi$) and the limit
$\displaystyle \lim_{z \rightarrow a} (z-a) f(z) = A$ exists. Show that
$$\lim_{r \rightarrow 0} \int_{\gamma_r} f(z) dz  = i A \beta_0 \; , \; \;$$
where
$\gamma_r : = \{ z \; | \; z = a + r e^{it}, \; 0 \leq  t \leq \beta_0 \}.$


---
	 Show that $f(z) = z^2$ is uniformly continuous in any open disk
$|z| < R$, where $R>0$ is fixed, but it is not uniformly continuous on
$\mathbb C$.

---
	  (1) Show that the function $u=u(x,y)$ given by
    $$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
    is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for
    the Laplace equation
    $$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
    u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$
    (2) Show that there exist points $(x,y)\in D$ such that
    $\displaystyle{\limsup_{n\to\infty} |u(x,y)|=\infty}$.
   

# Fall 2011

---
	  (1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$
    converges in $|z| < R$. Show that for $r <R$,
    $$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
    \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

    (2) Deduce Liouville's theorem from (1).

---
	  Let $f$ be a continuous function in the region
    $$D=\{z\ |  |z|>R, 0\leq \arg Z\leq \theta\}\quad\text{where}\quad
    0\leq \theta \leq 2\pi.$$ If there exists $k$ such that
    $\displaystyle{\lim_{z\to\infty} zf(z)=k}$ for $z$ in the region
    $D$. Show that $$\lim_{R'\to\infty} \int_{L} f(z) dz=i\theta k,$$
    where $L$ is the part of the circle $|z|=R'$ which lies in the
    region $D$.

---
	  Suppose that $f$ is an analytic function in the region $D$ which
    contains the point $a$. Let
    $$F(z)= z-a-qf(z),\quad \text{where}\quad q \ \text{is a complex
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

---
	  Evaluate $\displaystyle{ \int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \,
    dx }$.

---
	  Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
    partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
    that
    $$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
    \frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$

---
	  Show that $\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n}
    dx=\frac{\pi}{n\sin \frac{a\pi}{n}}$ using complex analysis, $0< a <
    n$. Here $n$ is a positive integer.

---
	  For $s>0$, the **gamma function** is defined by
    $\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

    1.  Show that the gamma function is analytic in the half-plane
        $\Re (s)>0$, and is still given there by the integral formula
        above.

    2.  Apply the formula in the previous question to show that
        $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

    > Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.

---
	  Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra: If
    $$P_n(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + a_nz^n\quad  (a_n \neq 0)$$
    is a polynomial of degree n, then it has n zeros in $\mathbb C$.

---
	  Suppose $f$ is entire and there exist $A, R >0$ and natural number
    $N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show
    that (i) $f$ is a polynomial and (ii) the degree of $f$ is at least
    $N$.

---
    Let $f: {\mathbb C} \rightarrow {\mathbb C}$ be an injective
    analytic (also called univalent) function. Show that there exist
    complex numbers $a \neq 0$ and $b$ such that $f(z) = az + b$.

---
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

---
	 Find a conformal map from $D = \{z :\  |z| < 1,\ |z - 1/2| > 1/2\}$
    to the unit disk $\Delta=\{z: \ |z|<1\}$.

---
	 Let $f(z)$ be entire and assume values of $f(z)$ lie outside a
    *bounded* open set $\Omega$. Show without using Picard's theorems
    that $f(z)$ is a constant.

---
	  Let $f(z)$ be entire and assume values of $f(z)$ lie outside a *bounded*
    open set $\Omega$. Show without using Picard's theorems that $f(z)$ is a
    constant.

---
	  (1) Assume $\displaystyle f(z) = \sum_{n=0}^\infty c_n z^n$ converges
    in $|z| < R$. Show that for $r <R$,
    $$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta
    = \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

    (2) Deduce Liouville's theorem from (1).

---
	  Let $f(z)$ be entire and assume that $f(z) \leq M |z|^2$ outside some
    disk for some constant $M$. Show that $f(z)$ is a polynomial in $z$ of
    degree $\leq 2$.

---
	  Let $a_n(z)$ be an analytic sequence in a domain $D$ such that
    $\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on
    bounded and closed sub-regions of $D$. Show that
    $\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on
    bounded and closed sub-regions of $D$.

---
	  Let $f(z)$ be analytic in an open set $\Omega$ except possibly at a
    point $z_0$ inside $\Omega$. Show that if $f(z)$ is bounded in near
    $z_0$, then $\displaystyle \int_\Delta f(z) dz = 0$ for all triangles
    $\Delta$ in $\Omega$.

---
	  Assume $f$ is continuous in the region:
    $0< |z-a| \leq R, \; 0 \leq \arg(z-a) \leq \beta_0$
    ($0 < \beta_0 \leq 2 \pi$) and the limit
    $\displaystyle \lim_{z \rightarrow a} (z-a) f(z) = A$ exists. Show that
    $$\lim_{r \rightarrow 0} \int_{\gamma_r} f(z) dz  = i A \beta_0 \; , \; \;$$
    where
    $\gamma_r : = \{ z \; | \; z = a + r e^{it}, \; 0 \leq  t \leq \beta_0 \}.$


---
	  Show that $f(z) = z^2$ is uniformly continuous in any open disk
    $|z| < R$, where $R>0$ is fixed, but it is not uniformly continuous on
    $\mathbb C$.

    (1) Show that the function $u=u(x,y)$ given by
        $$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
        is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for
        the Laplace equation
        $$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
        u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$
    (2) Show that there exist points $(x,y)\in D$ such that
        $\displaystyle{\limsup_{n\to\infty} |u(x,y)|=\infty}$.

# Spring 2014

---
	  The question provides some insight into Cauchy's theorem. Solve the
    problem without using the Cauchy theorem.

    1.  Evaluate the integral $\displaystyle{\int_{\gamma} z^n dz}$ for
        all integers $n$. Here $\gamma$ is any circle centered at the
        origin with the positive (counterclockwise) orientation.

    2.  Same question as (a), but with $\gamma$ any circle not
        containing the origin.

    3.  Show that if $|a|<r<|b|$, then
        $\displaystyle{\int_{\gamma}\frac{dz}{(z-a)(z-b)} dz=\frac{2\pi i}{a-b}}$.
        Here $\gamma$ denotes the circle centered at the origin, of
        radius $r$, with the positive orientation.

---
	  (1) Assume the infinite series
    $\displaystyle  \sum_{n=0}^\infty c_n z^n$ converges in $|z| < R$
    and let $f(z)$ be the limit. Show that for $r <R$,
    $$\frac{1}{2 \pi} \int_0^{2 \pi} |f(r e^{i \theta})|^2 d \theta =
    \sum_{n=0}^\infty |c_n|^2 r^{2n} \; .$$

    (2) Deduce Liouville's theorem from (1). Liouville's theorem: If
    $f(z)$ is entire and bounded, then $f$ is constant.

---
	  Let $f$ be a continuous function in the region
    $$D=\{z\ |  |z|>R, 0\leq \arg Z\leq \theta\}\quad\text{where}\quad
    0\leq \theta \leq 2\pi.$$ If there exists $k$ such that
    $\displaystyle{\lim_{z\to\infty} zf(z)=k}$ for $z$ in the region
    $D$. Show that $$\lim_{R'\to\infty} \int_{L} f(z) dz=i\theta k,$$
    where $L$ is the part of the circle $|z|=R'$ which lies in the
    region $D$.

---
	  Evaluate $\displaystyle{ \int_{0}^{\infty}\frac{x\sin x}{x^2+a^2} \,
    dx }$.

---
	  Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
    partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
    that
    $$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
    \frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$

---
	  Show that $\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n}
    dx=\frac{\pi}{n\sin \frac{a\pi}{n}}$ using complex analysis, $0< a <
    n$. Here $n$ is a positive integer.

---
	  For $s>0$, the **gamma function** is defined by
    $\displaystyle{\Gamma(s)=\int_0^{\infty} e^{-t}t^{s-1} dt}$.

    -   Show that the gamma function is analytic in the half-plane
        $\Re (s)>0$, and is still given there by the integral formula
        above.

    -   Apply the formula in the previous question to show that
        $$\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin \pi s}.$$

    > Hint: You may need $\displaystyle{\Gamma(1-s)=t \int_0^{\infty}e^{-vt}(vt)^{-s} dv}$ for $t>0$.

---
	  Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra: If
    $$P_n(z) = a_0 + a_1z + \cdots + a_{n-1}z^{n-1} + a_nz^n\quad  (a_n \neq 0)$$
    is a polynomial of degree n, then it has n zeros in $\mathbf C$.

---
	  Suppose $f$ is entire and there exist $A, R >0$ and natural number
    $N$ such that $$|f(z)| \geq A |z|^N\ \text{for}\ |z| \geq R.$$ Show
    that (i) $f$ is a polynomial and (ii) the degree of $f$ is at least
    $N$.

---
    Let $f: {\mathbb C} \rightarrow {\mathbb C}$ be an injective
    analytic (also called univalent) function. Show that there exist
    complex numbers $a \neq 0$ and $b$ such that $f(z) = az + b$.

---
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

---
	 Find a conformal map from $D = \{z :\  |z| < 1,\ |z - 1/2| > 1/2\}$
    to the unit disk $\Delta=\{z: \ |z|<1\}$.

# Fall 2015

---
	  Let $a_n \neq 0$ and assume that $\displaystyle
    \lim_{n \rightarrow \infty} \frac{|a_{n+1}|}{|a_n|} = L$. Show that
    $\displaystyle
    \lim_{n \rightarrow \infty}
    \sqrt[n]{|a_n|} = L.
    %p_n^{\frac{1}{n}} = L.$ In particular, this shows that when
    applicable, the ratio test can be used to calculate the radius of
    convergence of a power series.

---
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

---
	  Use $n$-th roots of unity (i.e. solutions of $z^n - 1 =0$) to show
    that
    $$2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n}
    = n
    \; .$$ 
    
    > Hint: $1 - \cos 2 \theta = 2 \sin^2 \theta,\; \sin 2 \theta = 2 \sin \theta \cos \theta$.

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

---
	  Assume $f$ is continuous in the region:
    $x \geq x_0, \; 0 \leq y \leq b$ and the limit
    $$\displaystyle \lim_{x \rightarrow + \infty} f(x + iy) = A$$ exists
    uniformly with respect to $y$ (independent of $y$). Show that
    $$\lim_{x \rightarrow + \infty} \int_{\gamma_x} f(z) dz  = iA b \; , \; \;$$
    where $\gamma_x : = \{ z \; | \; z = x + it, \; 0 \leq  t \leq b\}.$

---
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

---
	  Let $f(z)$ be bounded and analytic in $\mathbb C$. Let $a \neq b$ be
    any fixed complex numbers. Show that the following limit exists
    $$\lim_{R \rightarrow \infty} \int_{|z|=R} \frac{f(z)}{(z-a)(z-b)} dz.$$
    Use this to show that $f(z)$ must be a constant (Liouville's
    theorem).

---
	  Prove by *justifying all steps* that for all $\xi \in {\mathbb C}$
    we have $\displaystyle
    e^{- \pi \xi^2} = \int_{- \infty}^\infty e^{- \pi x^2} e^{2 \pi i x \xi} dx \; .$

    > Hint: You may use that fact in Example 1 on p. 42 of the textbook
    without proof, i.e., you may assume the above is true for real
    values of $\xi$.

---
	  Suppose that $f$ is holomorphic in an open set containing the closed
    unit disc, except for a pole at $z_0$ on the unit circle. Let
    $\displaystyle
    %f(z) = \sum_{n = 1}^\infty a_n z^n
    f(z) = \sum_{n = 1}^\infty c_n z^n$ denote the the power series in
    the open disc. Show that (1) $c_n \neq 0$ for all large enough
    $n$'s, and (2)
    $\displaystyle \lim_{n \rightarrow \infty} \frac{c_n}{c_{n+1}}= z_0$.

---
	  Let $f(z)$ be a non-constant analytic function in $|z|>0$ such that
    $f(z_n) = 0$ for infinite many points $z_n$ with
    $\lim_{n \rightarrow \infty} z_n =0$. Show that $z=0$ is an
    essential singularity for $f(z)$. (An example of such a function is
    $f(z) = \sin (1/z)$.)

---
	 Let $f$ be entire and suppose that
    $\lim_{z \rightarrow \infty} f(z) = \infty$. Show that $f$ is a
    polynomial.

---
	 Expand the following functions into Laurent series in the indicated
    regions:

    (a)
    $\displaystyle f(z) = \frac{z^2 - 1}{ (z+2)(z+3)}, \; \; 2 < |z| < 3$,
    $3 < |z| < + \infty$.

    (b)
    $\displaystyle f(z) = \sin \frac{z}{1-z}, \; \; 0 < |z-1| < + \infty$

---
    Assume $f(z)$ is analytic in region $D$ and $\Gamma$ is a
    rectifiable curve in $D$ with interior in $D$. Prove that if $f(z)$
    is real for all $z \in \Gamma$, then $f(z)$ is a constant.

---
	 Find the number of roots of $z^4 - 6z + 3 =0$ in $|z|<1$ and
    $1 < |z| < 2$ respectively.

---
	 Prove that $z^4 + 2 z^3 - 2z + 10 =0$ has exactly one root in each
    open quadrant.

---
    (1) Let $f(z) \in H({\mathbb D})$, $\text{Re}(f(z)) >0$,
    $f(0)= a>0$. Show that $$|\frac{f(z)-a}{f(z)+a}| \leq |z|, \; \; \;
    |f'(0)| \leq 2a.$$

    (2) Show that the above is still true if $\text{Re}(f(z)) >0$ is
    replaced with $\text{Re}(f(z)) \geq 0$.

---
    Assume $f(z)$ is analytic in ${\mathbb D}$ and $f(0)=0$ and is not a
    rotation (i.e. $f(z) \neq e^{i \theta} z$). Show that
    $\displaystyle \sum_{n=1}^\infty f^{n}(z)$ converges uniformly to an
    analytic function on compact subsets of ${\mathbb D}$, where
    $f^{n+1}(z) = f(f^{n}(z))$.

---
    Let $f(z) = \sum_{n=0}^\infty c_n z^n$ be analytic and one-to-one in
    $|z| < 1$. For $0<r<1$, let $D_r$ be the disk $|z|<r$. Show that the
    area of $f(D_r)$ is finite and is given by
    $$S = \pi \sum_{n=1}^\infty n |c_n|^2 r^{2n}.$$ (Note that in
    general the area of $f(D_1)$ is infinite.)

---
    Let $f(z) = \sum_{n= -\infty}^\infty c_n z^n$ be analytic and
    one-to-one in $r_0< |z| < R_0$. For $r_0<r<R<R_0$, let $D(r,R)$ be
    the annulus $r<|z|<R$. Show that the area of $f(D(r,R))$ is finite
    and is given by
    $$S = \pi \sum_{n=- \infty}^\infty n |c_n|^2 (R^{2n} - r^{2n}).$$

# Spring 2015

---
	  Let $a_n(z)$ be an analytic sequence in a domain $D$ such that
    $\displaystyle \sum_{n=0}^\infty |a_n(z)|$ converges uniformly on
    bounded and closed sub-regions of $D$. Show that
    $\displaystyle \sum_{n=0}^\infty |a'_n(z)|$ converges uniformly on
    bounded and closed sub-regions of $D$.

---
	  Let $f_n, f$ be analytic functions on the unit disk ${\mathbb D}$.
    Show that the following are equivalent.

    (i) $f_n(z)$ converges to $f(z)$ uniformly on compact subsets in
    $\mathbb D$.

    (ii) $\int_{|z|= r} |f_n(z) - f(z)| \, |dz|$ converges to $0$ if
    $0< r<1$.

---
	  Let $f$ and $g$ be non-zero analytic functions on a region $\Omega$.
    Assume $|f(z)| = |g(z)|$ for all $z$ in $\Omega$. Show that
    $f(z) = e^{i \theta} g(z)$ in $\Omega$ for some
    $0 \leq \theta < 2 \pi$.

---
	  Suppose $f$ is analytic in an open set containing the unit disc
    $\mathbb D$ and $|f(z)| =1$ when $|z|$=1. Show that either
    $f(z) = e^{i \theta}$ for some $\theta \in \mathbb R$ or there are
    finite number of $z_k \in \mathbb D$, $k \leq n$ and
    $\theta \in \mathbb R$ such that
    $\displaystyle f(z) = e^{i\theta} \prod_{k=1}^n \frac{z-z_k}{1 - \bar{z}_k z } \, .$
    
    > Also cf. Stein et al, 1.4.7, 3.8.17

---
	  (1) Let $p(z)$ be a polynomial, $R>0$ any positive number, and
    $m \geq 1$ an integer. Let
    $M_R = \sup \{ |z^{m} p(z) - 1|: |z| = R  \}$. Show that $M_R>1$.

    (2) Let $m \geq 1$ be an integer and
    $K = \{z \in {\mathbb C}: r \leq |z| \leq R \}$ where $r<R$.
    Show (i) using (1) as well as, (ii) without using (1) that there
    exists a positive number $\varepsilon_0>0$ such that for each
    polynomial $p(z)$,
    $$\sup \{|p(z) - z^{-m}|: z \in K  \} \geq \varepsilon_0 \, .$$

---
	  Let $\displaystyle f(z) = \frac{1}{z} + \frac{1}{z^2 -1}$. Find all
    the Laurent series of $f$ and describe the largest annuli in which
    these series are valid.

---
	  Suppose $f$ is entire and there exist $A, R >0$ and natural number
    $N$ such that $|f(z)| \leq A |z|^N$ for $|z| \geq R$. Show that (i)
    $f$ is a polynomial and (ii) the degree of $f$ is at most $N$.

---
	  Suppose $f$ is entire and there exist $A, R >0$ and natural number
    $N$ such that $|f(z)| \geq A |z|^N$ for $|z| \geq R$. Show that (i)
    $f$ is a polynomial and (ii) the degree of $f$ is at least $N$.

---
	  (1) Explicitly write down an example of a non-zero analytic
    function in $|z|<1$ which has infinitely zeros in $|z|<1$.

    (2) Why does not the phenomenon in (1) contradict the uniqueness
    theorem?

---
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

---
	 Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that
    for any $s<r$, there exists a constant $c>0$ such that
    $$||f||_{(\infty, s)} \leq c ||f||_{(1, r)},$$ where
    $\displaystyle |f||_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$
    and $\displaystyle ||f||_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.

    > Note: Exercise 3.8.20 on p.107 in Stein et al is a
    straightforward consequence of this stronger result using the
    integral form of the Cauchy-Schwarz inequality in real analysis.

---
	 (1) Let $f$ be analytic in $\Omega: 0<|z-a|<r$ except at a
    sequence of poles $a_n \in \Omega$ with
    $\lim_{n \rightarrow \infty} a_n = a$. Show that for any
    $w \in \mathbb C$, there exists a sequence $z_n \in \Omega$ such
    that $\lim_{n \rightarrow \infty} f(z_n) = w$.

    (2) Explain the similarity and difference between the above
    assertion and the Weierstrass-Casorati theorem.

---
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

---
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

---
    Let $0<r<1$. Show that polynomials
    $P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in
    $|z|<r$ for all sufficiently large $n$'s.

---
    Let $f$ be an analytic function on a region $\Omega$. Show that $f$
    is a constant if there is a simple closed curve $\gamma$ in $\Omega$
    such that its image $f(\gamma)$ is contained in the real axis.

---
    (1) Show that $\displaystyle \frac{\pi^2}{\sin^2 \pi z}$ and
    $\displaystyle g(z) = \sum_{n = - \infty}^{ \infty} \frac{1}{(z-n)^2}$
    have the same principal part at each integer point.

    (2) Show that
    $\displaystyle h(z) = \frac{\pi^2}{\sin^2 \pi z} - g(z)$ is bounded
    on $\mathbb C$ and conclude that
    $\displaystyle \frac{\pi^2}{\sin^2 \pi z} = \sum_{n = - \infty}^{ \infty} \frac{1}{(z-n)^2} \, .$

---
    Let $f(z)$ be an analytic function on
    ${\mathbb C} \backslash \{ z_0 \}$, where $z_0$ is a fixed point.
    Assume that $f(z)$ is bijective from
    ${\mathbb C} \backslash \{ z_0 \}$ onto its image, and that $f(z)$
    is bounded outside $D_r(z_0)$, where $r$ is some fixed positive
    number. Show that there exist $a, b, c, d \in \mathbb C$ with
    $ad-bc \neq 0$, $c \neq 0$ such that
    $\displaystyle f(z) = \frac{az + b}{cz + d}$.

---
    Assume $f(z)$ is analytic in ${\mathbb D}: |z|<1$ and $f(0)=0$ and
    is not a rotation (i.e. $f(z) \neq e^{i \theta} z$). Show that
    $\displaystyle \sum_{n=1}^\infty f^{n}(z)$ converges uniformly to an
    analytic function on compact subsets of ${\mathbb D}$, where
    $f^{n+1}(z) = f(f^{n}(z))$.

---
	 Let $f$ be a non-constant analytic function on $\mathbb D$ with
    $f(\mathbb D) \subseteq \mathbb D$. Use $\psi_{a} (f(z))$ (where
    $a=f(0)$, $\displaystyle \psi_a(z) = \frac{a - z}{1 - \bar{a}z}$) to
    prove that $\displaystyle
    \frac{|f(0)| - |z|}{1 + |f(0)||z|} \leq |f(z)| \leq
    \frac{|f(0)| + |z|}{1 - |f(0)||z|}$.

---
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

---
	 Let $C$ and $C'$ be two circles and let $z_1 \in C$, $z_2 \notin C$,
    $z'_1 \in C'$, $z'_2 \notin C'$. Show that there is a unique
    fractional linear transformation $f$ with $f(C) = C'$ and
    $f(z_1) = z'_1$, $f(z_2) = z'_2$.

---
	 Assume $f_n \in H(\Omega)$ is a sequence of holomorphic functions on
    the region $\Omega$ that are uniformly bounded on compact subsets
    and $f \in H(\Omega)$ is such that the set
    $\displaystyle \{z \in \Omega: \lim_{n \rightarrow \infty} f_n(z) = f(z) \}$
    has a limit point in $\Omega$. Show that $f_n$ converges to $f$
    uniformly on compact subsets of $\Omega$.

---
	 Let
    $\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
    with $|\alpha|<1$ and ${\mathbb D}=\{z:\ |z|<1\}$. Prove that

    -   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}|^2 dx dy =1}$.

    -   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}| dx dy =\frac{1-|\alpha|^2}{|\alpha|^2}
        \log \frac{1}{1-|\alpha|^2}}$.

---
	 Prove that
    $\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$ is a
    conformal map from half disc $\{z=x+iy:\ |z|<1,\ y>0\}$ to upper
    half plane ${\mathbb H}=\{z=x+iy:\ y>0\}$.

---
	 Let $\Omega$ be a simply connected open set and let $\gamma$ be a
    simple closed contour in $\Omega$ and enclosing a bounded region $U$
    anticlockwise. Let $f: \ \Omega \to {\mathbb C}$ be a holomorphic
    function and $|f(z)|\leq M$ for all $z\in \gamma$. Prove that
    $|f(z)|\leq M$ for all $z\in U$.

---
	 Compute the following integrals. (i)
    $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$,
    $0< a < n$ (ii)
    $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$

---
	 Let $0<r<1$. Show that polynomials
    $P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in
    $|z|<r$ for all sufficiently large $n$'s.

---
	 Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that
    for any $s<r$, there exists a constant $c>0$ such that
    $$\|f\|_{(\infty, s)} \leq c \|f\|_{(1, r)},$$ where
    $\displaystyle \|f\|_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$
    and $\displaystyle \|f\|_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.

---
	 Let $\displaystyle{\psi_{\alpha}(z)=\frac{\alpha-z}{1-\bar{\alpha}z}}$
    with $|\alpha|<1$ and ${\mathbb D}=\{z:\ |z|<1\}$. Prove that

    -   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}|^2 dx dy =1}$.

    -   $\displaystyle{\frac{1}{\pi}\iint_{{\mathbb D}} |\psi'_{\alpha}| dx dy =\frac{1-|\alpha|^2}{|\alpha|^2}
        \log \frac{1}{1-|\alpha|^2}}$.

    Prove that $\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$
    is a conformal map from half disc $\{z=x+iy:\ |z|<1,\ y>0\}$ to upper
    half plane $\mathbb H=\{z=x+iy:\ y>0\}$.

---
	  Let $\Omega$ be a simply connected open set and let $\gamma$ be a simple
    closed contour in $\Omega$ and enclosing a bounded region $U$
    anticlockwise. Let $f: \ \Omega \to {\mathbb C}$ be a holomorphic
    function and $|f(z)|\leq M$ for all $z\in \gamma$. Prove that
    $|f(z)|\leq M$ for all $z\in U$.

---
	  Compute the following integrals. (i)
    $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$, $0< a < n$
    (ii) $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$

---
	  Let $0<r<1$. Show that polynomials
    $P_n(z)  = 1 + 2z + 3 z^2 + \cdots + n z^{n-1}$ have no zeros in $|z|<r$
    for all sufficiently large $n$'s.

---
	  Let $f$ be holomorphic in a neighborhood of $D_r(z_0)$. Show that for
    any $s<r$, there exists a constant $c>0$ such that
    $$\|f\|_{(\infty, s)} \leq c \|f\|_{(1, r)},$$ where
    $\displaystyle \|f\|_{(\infty, s)} = \text{sup}_{z \in D_s(z_0)}|f(z)|$
    and $\displaystyle \|f\|_{(1, r)} = \int_{D_r(z_0)} |f(z)|dx dy$.

# Fall 2016

---
	  Let $u(x,y)$ be harmonic and have continuous partial derivatives of
    order three in an open disc of radius $R>0$.

    (a) Let two points $(a,b), (x,y)$ in this disk be given. Show that
    the following integral is independent of the path in this disk
    joining these points:
    $$v(x,y) = \int_{a,b}^{x,y} ( -\frac{\partial u}{\partial y}dx +  \frac{\partial u}{\partial x}dy).$$\
    
    (b) \hfill

        (i) Prove that $u(x,y)+i v(x,y)$ is an analytic function in this
    disc.

        (ii) Prove that $v(x,y)$ is harmonic in this disc.

---
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

---
	  (a) $f: D\rightarrow {\mathbb C}$ be a continuous function, where
    $D\subset {\mathbb C}$ is a domain.Let $\alpha:[a,b]\rightarrow D$
    be a smooth curve. Give a precise definition of the *complex line
    integral* $$\int_{\alpha} f.$$

    (b) Assume that there exists a constant $M$ such that
    $|f(\tau)|\leq M$ for all $\tau\in \mbox{\textrm Image}(\alpha$). Prove
    that
    $$\big | \int_{\alpha} f \big |\leq M \times \mbox{\textrm length}(\alpha).$$

    (c) Let $C_R$ be the circle $|z|=R$, described in the
    counterclockwise direction, where $R>1$. Provide an upper bound for
    $\big | \int_{C_R} \dfrac{\log{(z)} }{z^2} \big |,$ which depends
    [only]{.underline} on $R$ and other constants.

---
	  (a) Let Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire
    function. Assume the existence of a non-negative integer $m$, and of
    positive constants $L$ and $R$, such that for all $z$ with $|z|>R$
    the inequality $$|f(z)| \leq L |z|^m$$ holds. Prove that $f$ is a
    polynomial of degree $\leq m$.

    (b) Let $f:{\mathbb C}\rightarrow {\mathbb C}$ be an entire
    function. Suppose that there exists a real number M such that for
    all $z\in {\mathbb C}$ $$\mbox{\textrm Re} (f) \leq M.$$ Prove that $f$
    must be a constant.

---
	  Prove that all the roots of the complex polynomial
    $$z^7 - 5 z^3 +12 =0$$ lie between the circles $|z|=1$ and $|z|=2$.

---
	  (a) Let $F$ be an analytic function inside and on a simple closed
    curve $C$, except for a pole of order $m\geq 1$ at $z=a$ inside $C$.
    Prove that

    $$\frac{1}{2 \pi i}\oint_{C} F(\tau) d\tau = 
    \lim_{\tau\rightarrow a} \frac{d^{m-1}}{d\tau^{m-1}}\big((\tau-a)^m F(\tau))\big).$$

    (b) Evaluate $$\oint_{C}\frac{e^{\tau}}{(\tau^2+\pi^2)^2}d\tau$$
    where $C$ is the circle $|z|=4$.

---
	  Find the conformal map that takes the upper half-plane comformally
    onto the half-strip $\{
    w=x+iy:\ -\pi/2<x<\pi/2\ y>0\}$.

---
	  Compute the integral
    $\displaystyle{\int_{-\infty}^{\infty} \frac{e^{-2\pi ix\xi}}{\cosh\pi x}dx}$
    where $\displaystyle{\cosh z=\frac{e^{z}+e^{-z}}{2}}$.
