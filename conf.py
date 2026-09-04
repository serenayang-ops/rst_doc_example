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
language = 'zh_CN'

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX / PDF output ------------------------------------------

latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'extraclassoptions': 'openany,oneside',

    # 1. 封面修复 (直接引用 logo.pdf，去除 figs/ 前缀)
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

    # 2. 导言区修复
    'preamble': r'''
        \usepackage{ctex}
        \usepackage{geometry}
        \geometry{top=2.5cm, bottom=2.2cm, left=2.2cm, right=2.2cm}
        
        \usepackage{graphicx}
        \usepackage{xcolor}
        \usepackage{colortbl}
        \usepackage{array}

        % 定义主色调
        \definecolor{GigaBlue}{RGB}{0, 81, 237}          
        \definecolor{GigaDark}{RGB}{33, 37, 41}          
        \definecolor{GigaGray}{RGB}{108, 117, 125}       
        \definecolor{GigaLightGray}{RGB}{245, 246, 248}  

        % -----------------------------------------------------------------
        % 页眉页脚修复 (强制覆盖 normal 和 plain 样式，确保每一页都有 Logo)
        % -----------------------------------------------------------------
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
        
        % 默认应用 normal 样式
        \pagestyle{normal}

        % -----------------------------------------------------------------
        % 修复报错：重写一级标题，使用稳定的 colorbox 替代 TikZ node
        % -----------------------------------------------------------------
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

    'latex_use_xindy': False,
    'figure_align': 'htbp',
}

# 静态资源拷贝：确保将根目录下 figs/ 中的 logo.pdf 拷贝到编译目录
latex_additional_files = ['figs/logo.pdf']

# -----------------------------------------------------------------
# 声明附录文件：告诉 Sphinx 将这两个文件作为 PDF 的附录 (Appendix A, B)
# -----------------------------------------------------------------
latex_appendices = [
    'revision_history',
    'terms',
]

latex_documents = [
    (
        'index',                 
        'doc_example.tex',       
        'Technical Specification Of\\\\Containerized Diesel Generator DCP3000kW', 
        'SerenaYang',            
        'manual'                 
    ),
]