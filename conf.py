# -*- coding: utf-8 -*-

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Technical Specification Of Containerized Diesel generator DCP3000kW'
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

    # Keep Sphinx's own chapter/section mechanism.
    # Do NOT use titlesec here: it previously caused the PDF body to disappear
    # during XeLaTeX compilation.

    'maketitle': r'''
        \begin{titlepage}
            \raggedright
            \includegraphics[height=1.8cm]{logo.pdf} \\[0.5cm]

            {\color{GigaBlue}\rule{\textwidth}{3pt}} \\[2.5cm]

            \centering
            {\Huge \bfseries \color{GigaDark} Technical Specification Of} \\[0.5cm]
            {\Huge \bfseries \color{GigaBlue} Containerized Diesel Generator} \\[0.3cm]
            {\LARGE \bfseries \color{GigaDark} DCP3000kW} \\[3cm]

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

        % Map missing symbols to Windows default symbol font
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
        %
        % IMPORTANT:
        % We intentionally do not load titlesec.
        % Sphinx's native chapter commands remain untouched for stability.
        %
        % The Sphinx-generated chapter/section title color is controlled by
        % sphinxsetup below.
        % ------------------------------------------------------------------

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
        %
        % Sphinx standard tables provide the visible grid/borders.
        % The table header is styled separately below.
        % ------------------------------------------------------------------
        \renewcommand{\arraystretch}{1.15}

        % GIGA Engineering table borders
        % Keep Sphinx's standard table layout, but use GIGA Blue for all rules.
        \arrayrulecolor{GigaBlue}
        \setlength{\arrayrulewidth}{0.5pt}

        % GIGA Engineering table header text
        % Standard table borders remain GIGA Blue; header text is also GIGA Blue.
        \renewcommand{\sphinxstyletheadfamily}{%
            \sffamily\bfseries\color{GigaBlue}%
        }



    ''',
}

# ---------------------------------------------------------------------------
# Table configuration
# ---------------------------------------------------------------------------
#
# "standard" keeps the complete table grid.
latex_table_style = ['standard']
latex_use_latex_multicolumn = True

# Sphinx's LaTeX setup supports these colors for table rows.
# Keep the values as brand colors rather than introducing gray body fills.
latex_elements['sphinxsetup'] = 'TitleColor={RGB}{0,81,237}'

# ---------------------------------------------------------------------------
# Other LaTeX settings
# ---------------------------------------------------------------------------

figure_align = 'htbp'

latex_additional_files = ['figs/logo.pdf']

latex_documents = [
    (
        'index',
        'doc_example.tex',
        'Technical Specification Of\\\\Containerized Diesel Generator DCP3000kW',
        'SerenaYang',
        'manual'
    ),
]
