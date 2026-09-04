Use this command to generate PDF:

python -m sphinx -a -E -b latex . _build/latex && cd _build/latex && xelatex doc_example.tex && xelatex doc_example.tex