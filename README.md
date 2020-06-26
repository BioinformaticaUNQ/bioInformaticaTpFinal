# Tp Final BioInformatica

* Deploy a heroku
  - heroku git:remote -a tpbioinformatica
  - git push -u heroku master
  
* Deploy a Git
  - git push -u origin master
  
* Cuando se agrega una dependecia correr:
  - pip freeze > requirements.txt
  
* Correr migraciones en Heroku:
  - heroku run python manage.py makemigrations
  - heroku run python manage.py migrate
