# ¿Cómo instalar el programa?
Descargue el código de git en su computadora y colóquelo en el directorio que usted prefiera.

Instale python version 3
Se requieren las siguientes bibliotecas: numpy, tabule, inidecode y reuests, para instalar puede usar pip:

`pip install numpy tabulate unidecode requests`

El programa se encuentra en el directorio `ProgramaPares` y el script que debe ejecutar se llama `main.py`

`python main.py`

# ¿Cómo correr el programa?

***Si su sistema operativo es `linux`, debe ser cuidadoso con las mayusculas y minusculas, de lo contrario el programa no localizará los archivos.***

Para correr el programa es necesario indicar primero si se desean obtener los pares semánticos de las biblias alineadas a mano (1) o las biblias sin alineamiento (0). 

Si se elige la opción de correr las biblias alineadas a mano será necesario:

   1. Indicar el nombre del libro. *Tiene que ser el nombre de una carpeta dentro de **`./Biblias/BibliasAlineadas`**, por ejemplo MATEO*
   
   2. Indicar los códigos del libro I y el libro II. *El código del libro tiene la siguiente estructura `ABCXYZ`, donde `ABC` indica el código de la traducción (por ejemplo ESP para Biblia Española o JNM para Junemann) y `XYZ` indica el código del libro (por ejemplo CNT para Cantar de los cantares o NUM para Números). De esta manera pueden alinearse `LATMAT` y `JNMMAT`. Además en la carpeta del libro tiene que existir el archivo `ABCXYZ.txt`, en este caso `LATMAT.txt` y `JNMMAT.txt`*

Si se elige la opción de correr las biblias sin alineamiento:

   1. Hay que considerar que en ocasiones distintas traducciones de las biblias tienen una diferente distribución de versículos, para elegir a dos traducciones del mismo libro que tengan los mismos versículos, es importante leer `resumenBíblicoCorrecto.txt` y elegir dos traducciones del mismo grupo en el libro a considerar. Si esto no se realiza, puede existir un error por ArrayOutofIndex.
   
   2. Indicar la traducción 1. Tiene que ser el nombre de una carpeta dentro de **`./Biblias`**
   
   3. Indicar la traducción 2. Tiene que ser el nombre de una carpeta dentro de **`./Biblias`**
   
   4. Indicar el código 1. Las primeras 3 letras del código 1 deben coincidir con el código de la traducción 1
   
   5. Indicar el código 2. Las primeras 3 letras del código 2 deben coincidir con el código de la traducción 2
  
**Es importante notar que las últimas 3 letras del código 1 deben coincidir con las últimas 3 letras del código 2, esto es natural ya que hay que comparar a dos traducciones de un mismo libro.**
