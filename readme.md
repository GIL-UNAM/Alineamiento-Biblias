# ¿Qué es el alineamiento de biblias?

Es la forma de comparar los versículos de dos biblias con el objetivo de encontrar la mayor cantidad de similitudes o pares semánticos, esto consiste en obtener pares de palabras que se utilizan una en lugar de otra para decir lo mismo en un cierto contexto. El contexto, en este caso, son un par de versículos de la Biblia que provienen de dos versiones distintas.


# ¿Qué hace el programa?

Su objetivo es realizar el alineamiento de versículos de la Biblia, para ello se requiere que se haga referencia al mismo versículo en distintas biblias. Como resultado retorna el alineamiento y los pares en sus respectivas carpetas.
Para lograr esto el programa realiza los siguientes pasos:

Alinea los versículos con base en la distancia de Levenshtein, cuyos valores pasan por la matriz de costos de Wagner Fisher.

Posteriormente, encuentra los pares semánticos, esto funciona gracias a un algoritmo de programación dinámica que prueba las rutas con los costos mínimos en base al uso de recursión, es decir, por cada ruta que observe que tiene un costo mínimo el algoritmo crea una búsqueda con la finalidad de encontrar una ruta válida basada en estos costos. 

Con esto se puede obtener el coeficiente que determina el grado de similitud entre pares semánticos LCC.

### Rutas Múltiples

Las rutas múltiples fueron implementadas en la parte de la alineación de pares semánticos, esto se debe a que esta parte del algoritmo nos permite ver todas las alineaciones posibles que se pueden generar en un mismo versículo. Actualmente este algoritmo está limitado a dieciséis rutas múltiples encontradas, y solo se revisan las primeras doscientas rutas, estas limitaciones existen para evitar tiempos largos de ejecución y para lograr una mayor optimización del programa.

### Inversión conjuntiva y consecutiva

Estas se implementan después de las rutas múltiples.Cuando el programa reconoce que en los versículos alineados se encuentran dos palabras consecutivas o separadas por una disyunción, las invierte, para que de esta manera las palabras coincidan en el orden y así el algoritmo las logre reconocer como palabras iguales.


# Corpus

El [corpus](https://github.com/GIL-UNAM/SpanishParaphraseCorpora/tree/main/Biblias) para este proyecto son los evangelios sinópticos ([Marcos](https://github.com/GIL-UNAM/Alineamiento-Biblias/tree/main/ProgramaPares/Biblias/BibliasAlineadas/Marcos), [Lucas](https://github.com/GIL-UNAM/Alineamiento-Biblias/tree/main/ProgramaPares/Biblias/BibliasAlineadas/Lucas), [Mateo](https://github.com/GIL-UNAM/Alineamiento-Biblias/tree/main/ProgramaPares/Biblias/BibliasAlineadas/Mateo)). Se utilizan cuatro versiones: Nueva Biblia Española (versión publicada en españa), Nacar Colunga, Latinoamericana y Jünemann.

| Codigo | Biblia | Año | Libros |
| --- | --- | --- | --- |
| JNM | Jünemann | 1928 | <ul><li>[Marcos](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Marcos/JNMMAR.txt)</li> <li>[Lucas](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Lucas/JNMLUC.txt)</li> <li>[Mateo](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Mateo/JNMMAT.txt)</li></ul> |
| NAC | Nacar Colunga | 1944 |  <ul><li>[Marcos](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Marcos/NACMAR.txt)</li> <li>[Lucas](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Lucas/NACLUC.txt)</li> <li>[Mateo](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Mateo/NACMAT.txt)</li></ul>  |
| LAT | Latinoamericana | 1972 |  <ul><li>[Marcos](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Marcos/LATMAR.txt)</li> <li>[Lucas](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Lucas/LATLUC.txt)</li> <li>[Mateo](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Mateo/LATMAT.txt)</li></ul>  |
| ESE | Nueva Biblia Española (Schökel) | 1975 |  <ul><li>[Marcos](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Marcos/ESEMAR.txt)</li> <li>[Lucas](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Lucas/ESELUC.txt)</li> <li>[Mateo](https://github.com/GIL-UNAM/Alineamiento-Biblias/blob/main/ProgramaPares/Biblias/BibliasAlineadas/Mateo/ESEMAT.txt)</li></ul>  |
