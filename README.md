Cool&Smart Blog&Marketplace is a web aplication/online shop with cool and collectible stuff for all ages, developed using python with Django framework.
1. Descriere
Cool&Smart Blog&Marketplace is a cool online webplace where users can find their most desirable and cool items.

3. Screenshots Cool&Smart Blog&Marketplace

![Captură de ecran 2024-01-31 232532](https://github.com/gmcg95/CoolandSmart_marketplace/assets/145259154/085030a2-c3c7-48bf-a39e-2ddc0b5dbb4f)



![image](https://github.com/gmcg95/CoolandSmart_marketplace/assets/145259154/b074468d-851d-4c7d-9772-674d8e3c9a35)


3. Download and Install

clone this repository locally:

 git clone https://github.com/gmcg95/CoolandSmart_marketplace.git

To install dependencies, run:

 pip install -r requirements.txt
 
4. Project creating using Django framework:

   Django framework install - you should make sure you have Django installed.
   Use this command:

  pip install django

5. Project creating using Django - in terminal/comand promp, use this command:

  django-admin startproject nume_proiect

6. To run the app you should use this command in terminal:

  python manage.py startapp nume_aplicatie

7. After the app is created, you need to make the app settings in settings.py and to name the database
8. Models defining - after defining the database models in the models.py file, you will run this command:

  python manage.py makemigrations

  python manage.py migrate

9. App runs with this command:

  python manage.py runserver

10. Creating superuser - that's how you have acces to the Django admin interface

python manage.py createsuperuser
