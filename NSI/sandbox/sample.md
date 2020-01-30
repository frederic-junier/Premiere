---
title : Test pandoc
author : Frédéric Junier
numbersections: true
fontsize: 11pt
---


# Section 1

## Sous-Section

--------------------
### Exercice 1

1. question 1
2. question2

<div id="exemple" latex="true" class="exercice">

* Here is a paragraph.
* And another.
* Un lien [mon site](https://frederic-junier.org/)


~~~python
for k in range(3):
    print(k)
~~~


</div>



![une image](image.png)

![On rajoute un backslash après l'image pour qu'elle ne soit pas une figure](image.png){ width=50% }\



<div latex="true" class="theoreme">
Here is a paragraph.

And another.
</div>


<div latex="true" class="definition">
Here is a paragraph.

And another.
</div>

### Un exemple de tableau 

[http://www.tablesgenerator.com/markdown_tables#](http://www.tablesgenerator.com/markdown_tables#)

| a | b | a and b |
|:-:|:-:|:-------:|
| 0 | 0 |    0    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |
