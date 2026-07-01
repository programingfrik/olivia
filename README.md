
Olivia
======

Olivia es una super aplicación web que maneja todos tus contactos. La idea es que sea como una especie de repositorio central de contactos.

Olvia está hecha en python y django.

Esto es una aplicación de ejemplo para demostrar que podemos hacer una aplicacioncillas web en python con bonitura y felicidá.

Siguiendo el tutorial de django
-------------------------------

Este proyecto fue creado siguiendo el tutorial de django para la versión 6.0 de este framework, pero en el tutorial se trata de crear una aplicación de encuestas y olivia es un proyecto de una agenda de contactos, así que se hacen los siguientes reemplazos:

 - djangotutorial -> olivia_project
 - mysite -> olivia_site
 - polls -> olivia_app

Para hacer funcionar el proyecto
--------------------------------

 1. Acceder al directorio del proyecto: cd x/olivia/src/olivia_project/
 2. Crear un ambiente virtual: python -m venv ./env
 3. Activar el ambiente: source env/bin/activate
 4. Recuperar paquetes dependencias: pip install -r requirements.txt
 5. Construir la base de datos: python manage.py migrate
 6. Hacer migraciones pendientes: python manage.py makemigrations olivia_app
 7. Ejecutar la construcción de la base de datos: python manage.py sqlmigrate olivia_app 0001
 8. Crear un super usuario: python manage.py createsuperuser
 9. Iniciar el servidor: python manage.py runserver


Para acceder al shell
---------------------

python manage.py shell

En este shell se pueden crear objetos de los tipos creados en forma de modelos.

Para poner las dependencias
---------------------------

Hacer los cambios en el ambiente y luego guardar los paquetes que estan actualmente instalados:

pip freeze > requirements.txt
