# Simple Django Blog
This is a simple Django blog and I am using `Function-based views`, later I will create advanced blog using `Class-base views` and upload it to my GitHub.
In this project, the user can create, read, update and delete a blog.

![Django Blog](https://github.com/user-attachments/assets/1444be6b-b5c1-4291-930f-a7ef0706851e)


## How to Install and Run the Project
To get this repository, run the following command inside your git enabled terminal.
```
$ git clone https://github.com/HelloWorldIsNotDefined/Simple-Django-Blog.git
```

Before installing the required packages, it is recommended to create a `virtual environment`.

If you don't have the `virtual environment` installed:
```
$ python -m pip install virtualenv
```

Create the Virtual Environment: Run the following command, replacing `env` with the name you want for your environment:

```
$ python -m venv env
```

Activate the Virtual Environment: To activate the environment, use:

  + Windows:
    ```
    env\scripts\activate
    ```
  
  + Mac:
    ```
    source env/bin/activate
    ```
Deactivate the Virtual Environment: When you're done working, you can deactivate the environment with:
```
deactivate
```


After installing and activating the `virtual environment`, run the following command to install all required packages.
```
$ pip install -r requirements.txt
```
## How to Use the Project
In the same directory where `manage.py` is located, run this command to start the servre.
```
$ py manage.py runserver
```
Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and click `Sign up` or `Login` in the navigation bar.

The default superuser is:
+ username = _admin_
+ password = _admin_

Once you're logged in, go to `My Blog` in the navigation bar, where you can manage your blog.

![Django Blog 1](https://github.com/user-attachments/assets/5ec5d7fd-e743-44d5-8a78-7c153d750832)


# Goodbye!
Thank you for taking the time to explore this simple Django blog project. I hope you find it helpful and informative as you learn more about Django and web development. If you have any questions, feel free to reach out. Happy coding, and goodbye!


  
