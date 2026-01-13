\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{float}

% 1. theorem‐style environments
\theoremstyle{plain}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{theorem}{Theorem}[section]
\theoremstyle{definition}
\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]

% 2. declare an algorithm float for \caption
\floatstyle{plain}
\newfloat{algorithm}{htbp}{loa}
\floatname{algorithm}{Algorithm}

\begin{document}

\section{Extracting Binary Digits of \(\pi\)}

\begin{proposition}
The Leibniz series for \(\pi\) is


\[
  \pi \;=\; 4\,\sum_{k=0}^\infty \frac{(-1)^k}{2k+1}.
\]


\end{proposition}

\begin{definition}
We write the binary expansion of \(\pi\) as


\[
  \pi \;=\;\sum_{n=0}^{\infty}b_n\,2^{\,1-n},
  \quad b_n\in\{0,1\},
\]


so that \(b_0\) is the units‐bit, \(b_1\) the \(2^{-1}\)‐bit, and so on.
\end{definition}

\begin{theorem}
The \(n\)th binary digit \(b_n\) of \(\pi\) is


\[
  b_n \;=\;\bigl\lfloor 2^n\,\pi \bigr\rfloor \bmod 2.
\]


\end{theorem}

\begin{proof}
Multiply the series
\(\displaystyle
  \pi = 4\sum_{k\ge0}\frac{(-1)^k}{2k+1}
\)
by \(2^n\):


\[
  2^n\,\pi
  =
  4\,\sum_{k=0}^\infty \frac{(-1)^k\,2^n}{2k+1}.
\]


Truncate at \(k=M\) so that the tail
\(\displaystyle 4\sum_{k=M+1}^\infty\frac{2^n}{2k+1}\)<1.
Then
\(\displaystyle
  S \;=\;\sum_{k=0}^{M}4\,\frac{(-1)^k\,2^n}{2k+1}
\)
satisfies \(0\le2^n\pi - S<1\), hence
\(\lfloor S\rfloor = \lfloor2^n\pi\rfloor\).  Writing
\(\lfloor2^n\pi\rfloor\) in binary encodes the first \(n+1\) bits,
and reducing mod 2 extracts the least significant one, namely \(b_n\).
\end{proof}

\begin{algorithm}
\caption{Compute the first \(N\) binary digits of \(\pi\).}
\begin{enumerate}
  \item Fix \(N\).  Choose \(M\) so that
    \(\displaystyle 4\sum_{k=M+1}^\infty\frac{2^N}{2k+1}<1\).
  \item Compute the truncated sum
    

\[
      S \;=\; \sum_{k=0}^{M}
      4\,\frac{(-1)^k\,2^N}{2k+1},
      \qquad A=\lfloor S\rfloor.
    \]


  \item For each \(n=0,1,\dots,N\),
    

\[
      b_n
      =\bigl\lfloor 2^n\pi\bigr\rfloor\bmod2
      = \bigl\lfloor A / 2^{\,N-n}\bigr\rfloor \bmod2.
    \]


\end{enumerate}
\end{algorithm}

\begin{example}
Compute the first \(9\) bits of \(\pi\) (\(b_0\) through \(b_8\)):

\begin{itemize}
  \item Take \(N=8\).  One finds that choosing \(M=50\) makes the tail small.
  \item Numerically,
    

\[
      S \;=\;\sum_{k=0}^{50}
      4\,\frac{(-1)^k\,2^8}{2k+1}
      \;\approx\;804.2470,
      \quad
      A=\lfloor S\rfloor=804.
    \]


  \item Writing \(804_{10} = (1100100100)_2\) (ten bits)
    and truncating to the nine least‐significant bits gives
    

\[
      (b_0,b_1,\dots,b_8)
      =(1,0,0,1,0,0,1,0,0).
    \]


\end{itemize}

Thus


\[
  \pi \approx 11.00100100_2.
\]


\end{example}

\medskip\noindent
\textbf{Note.}  You will see a “Label(s) may have changed” warning on the first run. 
Rerun \LaTeX\ until all cross‐references stabilize.

\end{document}
