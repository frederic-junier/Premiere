# Génération de fichiers aux formats `pdf`, `markdown`, `html`, `slide-html` à partir d'un seul fichier source `***-source.md` 

* Sources documentaires : 
  * Markdown et Pandoc : <https://enacit.epfl.ch/cours/markdown-pandoc/>
  * Pandoc Guide : [https://pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html)
  * Filtres Pandoc : 
    * [https://pandoc.org/filters.html](https://pandoc.org/filters.html)
    * Filtres en Python : [pandocfilters](https://github.com/jgm/pandocfilters)
* Placer le fichier `Makefile` contenu dans ce répertoire dans le même répertoire que le fichier source  `***-source.md`


~~~
FILE=$(wildcard *source.md)
TARGET=$(FILE:source.md=.pdf) $(FILE:source.md=.tex) $(FILE:source.md=git.md)  $(FILE:source.md=.html)   $(FILE:source.md=slidy.html) 

all: $(TARGET)

%.pdf: %source.md
	pandoc -s $< --listings --template="/home/fjunier/Pandoc/template-pandocV1.tex" --filter ~/Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@
	
%.tex: %source.md
	pandoc -s $< --listings --template="/home/fjunier/Pandoc/template-pandocV1.tex" --filter ~/Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes+multiline_tables --toc -V toc-title:"Table des matières" -o $@
	
%.html: %source.md
	pandoc -s   -c "../Pandoc/style_nsi.css"  --mathjax --toc  -V toc-title:"Table des matières" -f markdown+table_captions+link_attributes+multiline_tables $< -o $@

%slidy.html: %source.md
	pandoc -s  -V geometry:margin=1.5cm --mathjax -t slidy  -c "../Pandoc/style_nsi.css" -f markdown+table_captions+link_attributes+multiline_tables $< -o $@

%git.md: %source.md
	pandoc -s   --filter ~/Pandoc/filtre.py --webtex  -V colorlinks --toc  -V toc-title:"Table des matières" -f markdown+table_captions+link_attributes+multiline_tables -t gfm  $<  -o $@
~~~

* Modifier éventuellement les chemins relatifs, pour que dans chaque répertoire où s'effectue la compilation, le `Makefile` puisse retrouver les templates qu ise trouvent dans le répertoire `Pandoc` :
 
~~~

├── Architecture
│   ├── images
│   ├── Makefile
│   ├── NSI-ArchitectureVonNeumann-Cours2020V1.pdf
│   ├── NSI-ArchitectureVonNeumann-Cours2020V1.tex
│   ├── NSI-ArchitectureVonNeumann-Cours2020V1.thm
│   └── ressources
├── CircuitsLogiques
│   ├── circuits_logisim
│   ├── cours-circuits-logiques-git.md
│   ├── cours-circuits-logiques-.html
│   ├── cours-circuits-logiques-.pdf
│   ├── cours-circuits-logiques-slidy.html
│   ├── cours-circuits-logiques-source.md
│   ├── cours-circuits-logiques-.tex
│   ├── images
│   ├── Makefile
│   └── notebook
├── HTTP
│   ├── http-git.md
│   ├── http-.html
│   ├── http-.pdf
│   ├── http-slidy.html
│   ├── http-source.md
│   ├── http-.tex
│   ├── images
│   ├── Makefile
│   └── ressources
├── LICENSE
├── Pandoc
│   ├── filtre.py
│   ├── Makefile
│   ├── MANUAL.pdf
│   ├── old
│   ├── pandoc-latex.pdf
│   ├── README.MD
│   ├── sandbox
│   ├── style_nsi.css
│   ├── template-pandoc-beamerV1.tex
│   └── template-pandocV1.tex
└── PHP-Flask
    ├── images
    ├── Makefile
    ├── php-flask-git.md
    ├── php-flask-.html
    ├── php-flask-.pdf
    ├── php-flask-slidy.html
    ├── php-flask-source.md
    ├── php-flask-.tex
    └── ressources
~~~
