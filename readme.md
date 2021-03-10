# Como correr el programa

Si su sistema operativo es linux, debe ser cuidadoso con las mayusculas y minusculas, de lo contrario el programa no localizará los archivos.

Para correr el programa es necesario indicar primero si se desean obtener los pares semánticos de las biblias alineadas a mano (1) o las biblias sin alineamiento (0). 

|Si se elige la opción de correr las biblias alineadas será necesario:
   |1- Indicar el nombre del libro. Tiene que ser el nombre de una carpeta dentro de ./Biblias/BibliasAlineadas, por ejemplo MATEO
   |2- Indicar los códigos del libro I y el libro II. El código del libro tiene la siguiente estrusctura ABCXYZ, donde ABC indica el código de la tracucción (por ejemplo ESP para Biblia Española o JNM para Junemann) y XYZ indica el código del libro (por ejemplo CNT para Cantar de los cantares o NUM para Números). De esta manera pueden alinearse LATMAT y JNMMAT. Además en la carpeta del libro tiene que existir el archivo ABCXYZ.txt, en este caso LATMAT.txt y JNMMAT.txt 

Si se elige la opción de correr las biblias sin alineamiento: 
   |1- Hay que considerar que en ocasiones distintas traducciones de las biblias tienen una diferente distribución de versículos, para elegir a dos traducciones del mismo libro que tengan los mismos versículos, es importante leer resumenBíblicoCorrecto.txt y elegir dos traducciones del mismo grupo en el libro a considerar. Si esto no se realiza, puede existir un error por ArrayOutofIndex.
   |2- Indicar la traducción 1. Tiene que ser el nombre de una carpeta dentro de ./Biblias
   |3- Indicar la traducción 2. Tiene que ser el nombre de una carpeta dentro de ./Biblias
   |4- Indicar el código 1. Las primeras 3 letras del código 1 deben coincidir con el código de la traducción 1
   |5- Indicar el código 2. Las primeras 3 letras del código 2 deben coincidir con el código de la traducción 2
  
Es importante notar que las últimas 3 letras del código 1 deben coincidir con las últimas 3 letras del código 2, esto es natural ya que hay que comparar a dos traducciones de un mismo libro.


# Como leer los resultados del programa
Los resultados del programa estarán en la carpeta ./Resultados. En ella estarán las carpetas 'Pares' y 'Alineaciones'. Cada una tendrá por su cuenta una serie de carpetas que son 'Normal', 'Inversion', 'POS', 'Seminull' y 'POSsemi'. Cada una contiene los resultados obrenidos considerando el programa sin modificaciones, considerando las inversiones, considerando el eriquetado POS, considerando pares seminulos y considerando pares seminulos y etiquetado POS, respectivamente.

En el caso de los pares:

Si están en la carpeta 'Normal', no tendrán ningun prefijo. En cualquier otra carpeta tendrán como prefijo el nombre de la carpeta.

Si la comparación se hizo con biblias alineadas, después del nombre de la carpeta, estará el indicador ALN - (de alineadas)

Después está indicado el código del Libro

Después esta indicado el codigo de la traducción 1 

Al último esta indicado el codigo de la traduccion 2

Ejemplos: 

POSsemiCNT-EMN-LAT: Son los pares obtenidos, considerando pares seminulos y etiquetado POS, del Cantar de los cantares, comparando las traducciones de Evaristo Nieto y la traducción Latinoamericana

ALNHAG-ESP-SER : Son los pares obtenidos, considerando el programa sin modificaciones, de Hageo, comparando las traducciones Española y Serafín de Ausejo.

En el caso de las alineaciones:

Es igual que en el caso de los pares, pero siempre con el prefijo alineaciones.

Ejemplo:

alineacionesSeminiull-1TM-NAC-JNM: Son las alineaciones obtenidas, considerando los pares seminulos, del Libro I de Timoteo, considerando las traducciones Nacar Colunga y Junemann.

# Corpus

El [corpus](https://github.com/GIL-UNAM/SpanishParaphraseCorpora/tree/main/Biblias) para este proyecto son los evangelios sinópticos ([Marcos](https://github.com/GIL-UNAM/SpanishParaphraseCorpora/tree/main/Biblias/Marcos), Lucas, Mateo). Se utilizan cuatro versiones: Nueva Biblia Española, Nacar Colunga, Latinoamericana y Jünemann.

| Codigo | Biblia | Año | Libros |
| --- | --- | --- | --- |
| JNM | Jünemann | 1928 | <ul><li>[Marcos](https://github.com/GIL-UNAM/SpanishParaphraseCorpora/blob/main/Biblias/Marcos/JNMMAR.txt)</li> <li>Lucas</li> <li>Mateo</li></ul> |
| NAC | Nacar Colunga | 1944 |  <ul><li>[Marcos](https://github.com/GIL-UNAM/SpanishParaphraseCorpora/blob/main/Biblias/Marcos/NACMAR.txt)</li> <li>Lucas</li> <li>Mateo</li></ul>  |
| LAT | Latinoamericana | 1972 |  <ul><li>[Marcos](https://github.com/GIL-UNAM/SpanishParaphraseCorpora/blob/main/Biblias/Marcos/LATMAR.txt)</li> <li>Lucas</li> <li>Mateo</li></ul>  |
| ESP | Nueva Biblia Española (Schökel) | 1975 |  <ul><li>[Marcos](https://github.com/GIL-UNAM/SpanishParaphraseCorpora/blob/main/Biblias/Marcos/ESPMAR.txt)</li> <li>Lucas</li> <li>Mateo</li></ul>  |
