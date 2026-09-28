# -*- coding: utf-8 -*-

import os
import sys

project = 'Technical Specification Of Containerized Diesel generator DCP3000kW'
copyright = '2026, GIGA'
author = 'SerenaYang'
release = '1.0'

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
html_static_path = ['_static']

latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'extraclassoptions': 'openany,oneside',

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
                \rowcolor{GigaLightGray}
                \textbf{\color{GigaDark} Product model} & Gen Set \\ \hline
                \textbf{\color{GigaDark} Version} & 1.0 \\ \hline
                \rowcolor{GigaLightGray}
                \textbf{\color{GigaDark} Date} & July 14th, 2026 \\ \hline
                \textbf{\color{GigaDark} Serial Number} & 1110X \\ \hline
            \end{tabular}
            \vspace*{1.5cm}
        \end{titlepage}
        \clearpage
    ''',

    'preamble': r'''
        \usepackage[scheme=plain]{ctex}
        \usepackage{geometry}
        \geometry{top=2.5cm, bottom=2.2cm, left=2.2cm, right=2.2cm}
        
        \usepackage{fontspec}
        \setmainfont{IBM Plex Sans}
        \setsansfont{IBM Plex Sans}

        \usepackage{graphicx}
        \usepackage{xcolor}
        \usepackage{colortbl}
        \usepackage{array}

        \definecolor{GigaBlue}{RGB}{0, 81, 237}          
        \definecolor{GigaDark}{RGB}{33, 37, 41}          
        \definecolor{GigaGray}{RGB}{108, 117, 125}       
        \definecolor{GigaLightGray}{RGB}{245, 246, 248}  

        \setlength{\headheight}{28pt}
        \addtolength{\topmargin}{-16pt}
        \xeCJKDeclareCharClass{CJK}{"2605, "25B2}

        % =========================================================
        % 注意：这里已暂时移除引起崩溃的 \rowcolor / \cellcolor 代码
        % 仅保留对表头文字加粗的处理，确保安全编译
        % =========================================================
        \renewcommand{\sphinxstyletheadfamily}{\bfseries}

        \usepackage{fancyhdr}
        \fancypagestyle{normal}{
            \fancyhf{}
            \fancyhead[L]{\raisebox{-0.15cm}{\includegraphics[height=0.7cm]{logo.pdf}}}
            \fancyhead[R]{\small\color{GigaGray}\leftmark}
            \renewcommand{\headrulewidth}{0.8pt}
            \renewcommand{\headrule}{\hbox to\headwidth{\color{GigaBlue}\makebox[\headwidth]{\hrulefill}}}
            \fancyfoot[C]{\color{GigaDark}\thepage}
        }
        \fancypagestyle{plain}{
            \fancyhf{}
            \fancyhead[L]{\raisebox{-0.15cm}{\includegraphics[height=0.7cm]{logo.pdf}}}
            \fancyhead[R]{\small\color{GigaGray}\leftmark}
            \renewcommand{\headrulewidth}{0.8pt}
            \renewcommand{\headrule}{\hbox to\headwidth{\color{GigaBlue}\makebox[\headwidth]{\hrulefill}}}
            \fancyfoot[C]{\color{GigaDark}\thepage}
        }
        \pagestyle{normal}

        \usepackage{titlesec}
        \titleformat{\chapter}[hang]
            {\normalfont\huge\bfseries\color{GigaBlue}}
            {\colorbox{GigaBlue}{\color{white}\thechapter}}
            {1em}
            {}
            
        \titleformat{\section}
            {\normalfont\large\bfseries\color{GigaBlue}}
            {\thesection}{0.8em}{}
            [\color{GigaBlue}\hrule height 0.5pt]

        \makeatletter
        \g@addto@macro\appendix{
            \titleformat{\chapter}[hang]
                {\normalfont\huge\bfseries\color{GigaGray}}
                {\colorbox{GigaGray}{\color{white}Appendix \thechapter}}
                {1em}
                {}
        }
        \makeatother

        \hypersetup{
            colorlinks=true,
            linkcolor=GigaBlue,
            citecolor=GigaBlue,
            urlcolor=GigaBlue
        }
        \renewcommand{\arraystretch}{1.3}
    ''',
    'figure_align': 'htbp',
}

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