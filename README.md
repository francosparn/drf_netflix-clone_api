# :rocket: Netflix Clone REST API

**Netflix** clone API developed in **Django REST Framework**.

![image](https://i.imgur.com/XqcqGXs.png)

**Some of the API features:**

* User registration and login.
* User authentication with **[JSON Web Token](https://jwt.io/)**.
* Custom access permissions.
* Pagination of films, series, actors, genres and languages.
* Creation, update and deletion of films, series, actors, genres and languages.
* Give ratings to films and series.
* Select favorite films and series.
* API Documentation available.

## Project run

To run this project you will need to have **Python** installed on your computer. The first thing we will do is download the project and open it in our preferred editor. Although not required, it is recommended that you create a **virtual environment** to store your project dependencies separately.

To install a **virtual environment**, run the following command:

```
pip install virtualenv
```

If your operating system is **Windows**, open **Command Prompt** or **Powershell** and run the following command:

```
env/Scripts/activate
```

If your operating system is **Linux** or **Mac**, open **"Terminal"** and run:

```
source env/bin/activate
```

Next, install the project dependencies with:

```
pip install -r requirements.txt
```

It is almost ready, now it only remains to execute the project with the following command:

```
python manage.py runserver
```

That would be it, now is the time to test the API. 🙂
