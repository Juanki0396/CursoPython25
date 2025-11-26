# Curso Python 25/26

Este es el repositorio del módulo de programación de DAW Intensivo del centro IES Pío Baroja.
Aquí se pueden encontrar los distintos ejemplos que vamos realizando en clase.
Todo el código se encuentra en la carpeta src. Cada ejemplo tendrá localizado su propia
carpeta.

Todo el código está pensado para usarse con python3.13 y ejecutado desde un sistema Ubuntu. 
También se puede usar en windows pero tendrá que adaptar los comandos a windows.

Para determinar si tiene python3.13 instalado puede probar a lanzar el siguiente comando.

    python3.13 -V

Si devulve un error quiere decir que debe instalar Python 13. Para ello deberá añadir el
repositorio de deadsnakes primero. Los siguientes comandos se encargarán de todo:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update 
    sudo apt install python3.13 python3.13-venv

## Clonar el repositorio

Para poder tener el código es tu ordenador primero deberás clonar el repositorio. Si tienes
configurada una llave ssh en github prueba:

    git clone git@github.com:Juanki0396/CursoPython25.git

Si no tienes ssh prueba:

    git clone https://github.com/Juanki0396/CursoPython25.git

Cada vez que haya una actualización en el repositorio de Github debería correr el siguiente
comando para actualizar tu repositorio local:

    git pull

Recuerda que **cualquier comando de git debe ejecutarse desde dentro del directorio**. Para 
asegurarte, el siguiente comando deberia devolver la ruta del directorio:

    pwd

En caso de que no te encuentres en el directorio del repositorio, utiliza el siguiente comando
para cambiar:

    cd RutaAlRepositorio

## Creación de un entorno virtual

Para poder ejecutar el código debemos instalar una serie de paquetes. La mejor forma de hacerlo es 
crear un entorno de python virtual. De esta manera no contaminaremos la instalación global de python.
para ello correremos el siguiente comando desde el directorio raiz del repositorio:

    python3.13 -m venv .venv

De esta manera se nos creará un entorno virtual en nuestra carpeta del repositorio. Para usar el entorno
debemos activarlos en primer lugar. Esto se hará cada vez que abras una nueva terminal y quieras correr 
cualquier ejemplo del repositorio.

    source .venv/bin/activate

Si el repositorio de activa correctamente veremos que al principio de cada línea en la terminal ahora pone:
(.venv)

## Instalación de paquetes

Los paquetes que necesita el repositorio estarán especificados en el archivo requirements.txt. Para poder instalarlos
primero debemos activar el entorno virtual. Una vez activado, debemos correr el siguiente comando:

    pip install -r requirements.txt

## Ejecutar ejemplos

Para ejecutar cualquier ejemplo, lo haremos de la siguiente manera:

    python13.3 src/<dirEjemplo>/<archivoEjemplo.py>

Debemos sustituir los valores entre <> por las rutas de cada ejemplo.

