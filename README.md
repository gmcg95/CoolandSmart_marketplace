**Cool&Smart Blog&Marketplace**

Cool&Smart Blog&Marketplace is a web application/online shop with cool and collectible stuff for all ages, developed using python along with Django framework.
  
    Description
Cool&Smart Blog&Marketplace is a cool online web-place where users can find their most desirable and cool items.


![image](https://github.com/gmcg95/CoolandSmart_marketplace/assets/145259154/b6e1ba8e-cd3f-47cb-a57a-ad75f5f5e3ba)



![image](https://github.com/gmcg95/CoolandSmart_marketplace/assets/145259154/ff378d1f-4580-4046-977c-83c8c481396d)



![image](https://github.com/gmcg95/CoolandSmart_marketplace/assets/145259154/83ef995b-7ea9-449c-9879-8cc6c808197a)
  

      Download and Install

1. Install Pycharm Community Edition:		
    https://www.jetbrains.com/pycharm/download/
2. Install Python:						
    https://www.python.org/downloads/
3. Clone the repository locally:\
    git clone https://github.com/gmcg95/CoolandSmart_marketplace.git
4. Navigate to the project directory:\
    cd path\repository 
5. Install dependencies:\
    pip install -r requirements.txt 
6. Set up the database:\
    python manage.py migrate 
7. Create a superuser (admin):\
    python manage.py createsuperuser 
8. Run the development server:\
    python manage.py runserver

⇒ starting with "4.", the prompts needs to be executed in the terminal (Pycharm/Command Prompt).   
  *also "3." should be executed in the Command Prompt after navigating (cd) in the desired local path.\
  ** to use git command for "3." you also need to have git(github) installed

        Usage

1. Access the marketplace:\
    Open your web browser and navigate (or click the link from terminal after **runserver**) to http://localhost:8000 (http://127.0.0.1:8000/)
2. Login as admin:\
    Use the superuser credentials you created earlier to access the admin dashboard (http://localhost:8000/admin) and manage the marketplace. 
3. Explore and use the marketplace:\
    Browse through the marketplace, add/remove products, manage users, etc.
4. Note that to add/delete products to/from cart and sent orders you need to create first a user and to be logged.


         Stucture and functionality

 **CoolandSmart_marketplace** is the main project package.\
    Here we configure the paths/urls from the other implemented apps in the project, the database, login and logout redirects, cookies, installing apps and other useful settings.

 **CSapp** is the app in which was developed the CRUD methods along with the frontend response (what every button do), also the frontend 'looks' are defined and connected with the views.py and urls.py through the html templates we find here.\
    We find here functionalities like: create order, add to cart and delete product with login required (we used here decorator), checkout, shopping cart and also contact and home view.\
    In this app we, as well, have models which define the view and registration in the database. We have models for order, order-item and message (contact) functionality. 

 **products_app** have python files, templates as for CSapp and accounts_app, but because the web-application is linked to a database, it is necessary to have the models package in which we define the attributes for the models (necessary for the rows and columns of the tables in the database)\
    In this category, we see developed, the view for the products, the upload for products, products details, categories, manufacturers etc.

 **accounts_app** have the register, login and profile functionalities.\
    Again, we used, as for the other developed apps in this web-application, python files which are connected with the html templates.

**other files** we find in the project are:\
    static folder, in which we find the css file for styling the frontend interface\
    images for carousel functionality\
    javascript file used for the deletion of the products and cookies\
    requirements.txt in which are the dependencies that are required to install for the project to run without problems\
    readme.md file in which the project is presented and installation and usage directions/suggestions are made\
    manage.py, the file that is used for running the project\
    database file\
    gitignore file
 
