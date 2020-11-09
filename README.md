# Todo-django Web Application


User can create, read and delete a task using this application. 

This project uses django.

Clone this repository using this command:-

   `git clone https://github.com/Thakursim/Todo-List`

# Getting up and running.
 Get inside the Todo-List using this command.
 
 `cd Todo-List` 

This steps below will get you up and running with a local development environment. We assume you have the following installed:

  - pip
  - virtualenv

First make sure to create and activate a virtialenv, then open a terminal at the project root and install the requirements for local development.

    $ pip install -r requirements.txt 

When you have installed all the required modules, get inside the src folder using this command. 

`cd src`

Now you have to run a command to login into the database. 
```sh
$ python manage.py createsuperuser
```
  You have to give a username, email address, and a password. By doing this you are good to go for the next step. 
 After getting inside of the src folder run this command to open the web page on the browser. 
 ```sh
 $ python manage.py runserver
 ```

Copy the http address visible on your shell, while pasting it in your browser add **/admin**.
 Over there you can see a login page, give the userid and password and you can see the **Task** present there. 
 
You can add a task there manually or if you want to do that in a web page then just add **/todo/** after the port in url.
Here you can see the tasks saved in the database and you can delete or add any task just by clicking on **Add** or **Delete** buttons. 


