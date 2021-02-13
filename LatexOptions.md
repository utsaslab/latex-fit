# Latex Options

## `\textfloatsep`

Distance between floats on the top or the bottom and the text.

Default value (article class): `20.0pt plus 2.0pt minus 4.0pt`

## `\floatsep`

Distance between two floats.

Default value (article class): `12.0pt plus 2.0pt minus 2.0pt`

## `\intextsep`

Distance between floats inserted inside the page text and the text proper.

Default value (article class): `12.0pt plus 2.0pt minus 2.0pt`

## `\dltextfloatsep`

Distance between a float spannign both columns and text.

Default value: `20.0pt plus 2.0pt minus 4.0pt`

## `\dlfloatsep`

Distance between two floats spanning both columns.

Default value: `12.0pt plus 2.0pt minus 2.0pt`

## `\abovedisplayshortskip`

Amount of space to place above a display equation.

Default value: `0.0pt plus 3.0pt`

## `\belowdisplayshortskip`

Amount of space to place below a display equation.

Default value: `6.0pt plus 3.0pt minus 3.0pt`

## `\abovedisplayskip`

Amount of space to place above a display equation.

Default value: `10.0pt plus 2.0pt minus 5.0pt`

## `\belowdisplayskip`

Amount of space to place below a display equation.

Default value: `10.0pt plus 2.0pt minus 5.0pt`

## `\parskip`

Amount of space between paragraphs

## `\parindent`

Paragraph indentation.

## `\linespread`

Inter-line spacing.

Default: `\linespread{1.0}`

## Compact Lists

Include `paralist` package

Replace `\begin{itemize}` with `\begin{compactitem}`

Replace `\begin{enumerate}` with `\begin{compactenum}`

## Space around Section headings

Include `titlesec` package

To change spacings: 
```
\titlespacing{\section}{0pt}{2ex}{1ex}
\titlespacing{\subsection}{0pt}{1ex}{0ex}
\titlespacing{\subsubsection}{0pt}{0.5ex}{0ex}
```

Docs: `http://tug.ctan.org/tex-archive/macros/latex/contrib/titlesec/titlesec.pdf`


## Sources

`https://robjhyndman.com/hyndsight/squeezing-space-with-latex/`

`https://tex.stackexchange.com/questions/387572/techniques-to-reduce-the-number-of-pages-in-a-compiled-pdf`

`https://www.silverf0x00.com/shrinking-a-latex-paper-to-fit-under-the-page-limits/`