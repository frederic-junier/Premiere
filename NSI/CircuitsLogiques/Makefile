FILE=$(wildcard *source.md)
TARGET=$(FILE:source.md=.pdf) $(FILE:source.md=.tex) $(FILE:source.md=git.md)  $(FILE:source.md=.html)  

all: $(TARGET)

%.pdf: %source.md
	pandoc -s $< --listings --template="/home/fjunier/Pandoc/template-pandocV1.tex" --filter ~/Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes --toc -V toc-title:"Table des matières" -o $@
	
%.tex: %source.md
	pandoc -s $< --listings --template="/home/fjunier/Pandoc/template-pandocV1.tex" --filter ~/Pandoc/filtre.py -V colorlinks -f markdown+table_captions+link_attributes --toc -V toc-title:"Table des matières" -o $@
	
%.html: %source.md
	pandoc -s   -c ~/Pandoc/style_nsi.css  --toc  -V toc-title:"Table des matières" $< -o $@
	
%git.md: %source.md
	pandoc -s   --filter ~/Pandoc/filtre.py   -V colorlinks --toc  -V toc-title:"Table des matières" -t gfm  $<  -o $@

