# -*- coding: utf-8 -*-

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Technical Specification of Containerized Diesel generator DCP3000kW'
copyright = '2026, GIGA'
author = 'SerenaYang'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'
numfig = True

html_theme = 'alabaster'

# _static is intentionally disabled because it is not present in the project.
# html_static_path = ['_static']

# -- Options for LaTeX / PDF output ------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'extraclassoptions': 'openany,oneside',
    'fncychap': '',
    
    # 强制图片不浮动，必须放在 latex_elements 字典内
    'figure_align': 'H',

    # Keep Sphinx's own chapter/section mechanism.
    # Do NOT use titlesec here: it previously caused the PDF body to disappear
    # during XeLaTeX compilation.

    'maketitle': r'''
        \begin{titlepage}
            \raggedright
            \includegraphics[height=1.8cm]{logo.pdf} \\[0.5cm]

            {\color{GigaBlue}\rule{\textwidth}{3pt}} \\[2.5cm]

            \centering
            {\Huge \bfseries \color{black} Technical Specification } \\[0.5cm]
            {\Huge \bfseries \color{black} of Containerized Diesel generator DCP3000kW} \\[0.5cm]

            \vfill

            \begin{tabular}{|p{4.5cm}|p{7.5cm}|}
                \hline
                \textbf{\color{GigaDark} Product model} & Gen Set \\ \hline
                \textbf{\color{GigaDark} Version} & 1.0 \\ \hline
                \textbf{\color{GigaDark} Date} & July 14th, 2026 \\ \hline
                \textbf{\color{GigaDark} Serial Number} & 1110X \\ \hline
            \end{tabular}
            \vspace*{1.5cm}
        \end{titlepage}
        \clearpage
    ''',

    'preamble': r'''
        % ------------------------------------------------------------------
        % Basic page layout
        % ------------------------------------------------------------------
        \usepackage{geometry}
        \geometry{top=2.5cm, bottom=2.2cm, left=2.2cm, right=2.2cm}

        % ------------------------------------------------------------------
        % Fonts
        % ------------------------------------------------------------------
        \usepackage{fontspec}
        \setmainfont{IBM Plex Sans}
        \setsansfont{IBM Plex Sans}

        % Map missing symbols to Windows default symbol font (Fixed corrupted encoding)
        \usepackage{newunicodechar}
        \newfontfamily{\symfont}{Segoe UI Symbol}
        \newunicodechar{★}{{\symfont ★}}
        \newunicodechar{▲}{{\symfont ▲}}

        % ------------------------------------------------------------------
        % Packages
        % ------------------------------------------------------------------
        \usepackage{graphicx}
        \usepackage{xcolor}
        \usepackage{array}
        \usepackage{colortbl}
        \usepackage{float}

        % ------------------------------------------------------------------
        % GIGA brand colors
        % ------------------------------------------------------------------
        \definecolor{GigaBlue}{RGB}{0,81,237}
        \definecolor{GigaDark}{RGB}{33,37,41}
        \definecolor{GigaGray}{RGB}{108,117,125}
        \definecolor{GigaLightGray}{RGB}{245,246,248}

        % ------------------------------------------------------------------
        % Header / footer
        % ------------------------------------------------------------------
        \setlength{\headheight}{28pt}
        \addtolength{\topmargin}{-16pt}

        \usepackage{fancyhdr}

        \fancypagestyle{normal}{
            \fancyhf{}
            \fancyhead[L]{%
                \raisebox{-0.15cm}{\includegraphics[height=0.7cm]{logo.pdf}}%
            }
            \fancyhead[R]{%
                \small\color{GigaGray}\leftmark
            }
            \renewcommand{\headrulewidth}{0.5pt}
            \renewcommand{\headrule}{%
                \hbox to\headwidth{%
                    \color{GigaBlue}\makebox[\headwidth]{\hrulefill}%
                }%
            }
            \fancyfoot[C]{\color{GigaDark}\thepage}
        }

        \fancypagestyle{plain}{
            \fancyhf{}
            \fancyhead[L]{%
                \raisebox{-0.15cm}{\includegraphics[height=0.7cm]{logo.pdf}}%
            }
            \fancyhead[R]{%
                \small\color{GigaGray}\leftmark
            }
            \renewcommand{\headrulewidth}{0.5pt}
            \renewcommand{\headrule}{%
                \hbox to\headwidth{%
                    \color{GigaBlue}\makebox[\headwidth]{\hrulefill}%
                }%
            }
            \fancyfoot[C]{\color{GigaDark}\thepage}
        }

        \pagestyle{normal}

        % ------------------------------------------------------------------
        % GIGA Engineering chapter / section appearance
        % ------------------------------------------------------------------
        \usepackage{sectsty}
        \chapterfont{\color{GigaBlue}}

        % ------------------------------------------------------------------
        % Hyperlinks
        % ------------------------------------------------------------------
        \hypersetup{
            colorlinks=true,
            linkcolor=GigaBlue,
            citecolor=GigaBlue,
            urlcolor=GigaBlue
        }

        % ------------------------------------------------------------------
        % Tables
        % ------------------------------------------------------------------
        \renewcommand{\arraystretch}{1.15}

        % GIGA Engineering table borders
        \arrayrulecolor{GigaBlue}
        \setlength{\arrayrulewidth}{0.5pt}

        % GIGA Engineering table header text
        \renewcommand{\sphinxstyletheadfamily}{%
            \sffamily\bfseries\color{GigaBlue}%
        }
    ''',
}

# ---------------------------------------------------------------------------
# Table configuration
# ---------------------------------------------------------------------------
# "standard" keeps the complete table grid.
latex_table_style = ['standard']
latex_use_latex_multicolumn = True

# Sphinx's LaTeX setup supports these colors for table rows.
# Keep the values as brand colors rather than introducing gray body fills.
latex_elements['sphinxsetup'] = 'TitleColor={RGB}{0,81,237}'

# ---------------------------------------------------------------------------
# Other LaTeX settings
# ---------------------------------------------------------------------------

latex_additional_files = ['figs/logo.pdf']

latex_documents = [
    (
        'index',
        'doc_example.tex',
        'Technical Specification of\\\\Containerized Diesel Generator DCP3000kW',
        'SerenaYang',
        'manual'
    ),
]

# ---------------------------------------------------------------------------
# Appendix configuration
# ---------------------------------------------------------------------------
# 填入你附录文件的名称（不需要加 .rst 后缀），如果有多个可以逗号隔开
latex_appendices = ['terms', 'revision_history']

# Cover trial: preserve all body/header/footer settings.
# 封面布局：标题、型号、版本、日期和编号在下方 LaTeX 中修改。
latex_elements["maketitle"] = r'''

\begin{titlepage}
\thispagestyle{empty}
\begingroup
\setlength{\parindent}{0pt}
\raggedright
\includegraphics[width=3.57cm]{logo.pdf}\par
\vspace{4mm}
{\color{GigaCoverBlue}\rule{\textwidth}{9mm}}\par
\vspace{14mm}
{\fontsize{33}{45}\selectfont\mdseries\color[HTML]{0E0F0D}
 Technical Specification\par
 of Containerized Diesel Generator DCP3000kW\par}
\vspace{9mm}
\noindent
\begin{minipage}[t]{4mm}
\vspace{0pt}{\color{GigaCoverBlue}\rule{4mm}{42mm}}
\end{minipage}\hspace{2mm}%
\begin{minipage}[t]{\dimexpr\textwidth-6mm\relax}
\vspace{0pt}
\fontsize{13.5}{18}\selectfont\mdseries\color[HTML]{333333}
\setlength{\tabcolsep}{0pt}
\renewcommand{\arraystretch}{1}
\begin{tabular}{@{}p{0.56\linewidth}>{\centering\arraybackslash}p{0.44\linewidth}@{}}
\rule[-3mm]{0pt}{10.5mm}PRODUCT MODEL & Gen Set \\
\rule[-3mm]{0pt}{10.5mm}VERSION & 1.0 \\
\rule[-3mm]{0pt}{10.5mm}DATE & July 14th, 2026 \\
\rule[-3mm]{0pt}{10.5mm}SERIAL NUMBER & 1110X
\end{tabular}
\end{minipage}
\endgroup
\end{titlepage}
\clearpage

'''

# 只覆盖有编号的一级章节；保留页眉、页脚及其他标题设置。
latex_elements["preamble"] += r'''
% Cover and numbered top-level chapter headings only.
\definecolor{GigaCoverBlue}{HTML}{014EEB}
\makeatletter
\AtBeginDocument{%
\renewcommand{\@makechapterhead}[1]{%
  \vspace*{12pt}%
  {\parindent\z@\raggedright\normalfont
   \fontsize{16.5}{21}\selectfont\sffamily\bfseries\color{black}%
   \interlinepenalty\@M
   \hangindent=12pt\hangafter=1
   \noindent
   {\color{GigaCoverBlue}\rule[-3pt]{2.25pt}{20pt}}\hspace{8pt}%
     \ifnum\c@secnumdepth>\m@ne
       \if@mainmatter\thechapter.\enspace\fi
     \fi
     #1\par
   \par\nobreak\vskip 15pt}%
}}
\makeatother

'''
