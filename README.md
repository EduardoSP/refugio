"# refugio" 
Video tutorial Django de codigo facilito 
https://www.youtube.com/playlist?list=PLsRdPvQ2xMkH8c2BOnQ_O1KZ9lyyL_eGB

video 9
https://docs.djangoproject.com/en/2.0/

crear entorno virtual
python -m env test19

activar entorno virtual 
ir a la carpeta Scripts 

activate
//---------------------------------------------------------------------------
Crear proyecto

django-admin.py startproject refugio //Nombre del proyecto
Para crear las aplicaciones de crea la carpeta apps y se escibe el siguiente comando

django-admin.py startapp mascota //comando para crear app


//---------------------------------------------------------------------------

python manage.py makemigrations  (crea migraciones del modelo en archivos .py)

python manage.py migrate  (pasa las migraciones a la bd)

//---------------------------------------------------------------------------
Para crear super usuario

manage.py createsuperuser

//---------------------------------------------------------------------------

para correr servidor

manage.py runserver
ir al admin
http://localhost:8000/admin/login/?next=/admin/

para correr el proyecto en otro puerto por ejemplo el 8080 entonces manage.py runserver 0.0.0.0:8080
//----------------------------------------------------------------------------
ingresar al shell de django para hacer pruebas
manage.py shell
//-----------------------------------------------------------------------------