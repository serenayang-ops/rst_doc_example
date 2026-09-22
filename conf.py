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

# =========================================================
# [修改] 强制 Sphinx 使用英文输出
# =========================================================
language = 'en'

# =========================================================
# [新增] 开启图表、表格、代码块的自动编号及引用，使 :numref: 生效
# =========================================================
numfig = True

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
        % =========================================================
        % 增加 scheme=plain 参数，防止 ctex 将 Figure 翻译成"图"
        % =========================================================
        \usepackage[scheme=plain]{ctex}
        \usepackage{geometry}
        \geometry{top=2.5cm, bottom=2.2cm, left=2.2cm, right=2.2cm}
        
        % =========================================================
        % 字体设置：使用 IBM Plex Sans 作为西文字体
        % =========================================================
        \usepackage{fontspec}
        \setmainfont{IBM Plex Sans}
        \setsansfont{IBM Plex Sans}

        \usepackage{graphicx}
        \usepackage{xcolor}
        \usepackage{colortbl}
        \usepackage{array}

        % 定义主色调
        \definecolor{GigaBlue}{RGB}{0, 81, 237}          
        \definecolor{GigaDark}{RGB}{33, 37, 41}          
        \definecolor{GigaGray}{RGB}{108, 117, 125}       
        \definecolor{GigaLightGray}{RGB}{245, 246, 248}  

        % =========================================================
        % 修复页眉高度不足的警告
        % =========================================================
        \setlength{\headheight}{28pt}
        \addtolength{\topmargin}{-16pt}

        % =========================================================
        % 修复特殊符号 (★ 和 ▲) 缺失导致的字体报错
        % =========================================================
        \xeCJKDeclareCharClass{CJK}{"2605, "25B2}

        % =========================================================
        % 表格全局样式：首行 GIGA蓝色背景，白色字体
        % =========================================================
        \renewcommand{\sphinxstyletheadfamily}{\bfseries\color{white}}
        
        \let\oldsphinxtoprule\sphinxtoprule
        \renewcommand{\sphinxtoprule}{\oldsphinxtoprule\rowcolor{GigaBlue}}
        % =========================================================

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
        
        \pagestyle{normal}

        % -----------------------------------------------------------------
        % 重写一级标题，使用稳定的 colorbox 替代 TikZ node
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

    'figure_align': 'htbp',
}

# 静态资源拷贝：确保将根目录下 figs/ 中的 logo.pdf 拷贝到编译目录
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