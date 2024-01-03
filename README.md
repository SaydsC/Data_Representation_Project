# Data Representation Project

#### ATU AW 2023 - higher diploma in Science in Data Analytics
__Author__: Sadie Concannon - G00411297

### This repository contains the following files:
1. server.py - Flask server application
2. requirements.txt - text file wirh requirements to run the applications
3. installRequirements.py - a python script to install the packages in the requirements text file
4. staticpages - contains html, img and css files
5. humanresourcesDAO.py - Data Access Object file to interact with data base
6. configTemplate.py - template to create config.py file with own login credentials to MySQL
7. .gitignore - GitHub gitignore file
8. README 

Local files also contain:
*config.py* - configuration file with MySQL database details - not on GitHub as input into gitignore

### Python
Python 3.9.13 was used in this project. The latest version of Python can be downloaded from https://www.python.org/downloads/ but any version of Python 3 can be used.

### Database
MySQL is the relational database system used in this project. It can be downloaded from https://www.mysql.com/downloads/.

### How to Set Up the Application

1. Install Python3
2. Install MySQL
3. Clone this repository
4. Run installRequirements.py to install the required Python packages. If this does not work, the packages required can be found in the requirements.txt file
5. Create a config.py file by adapting the configTemplate.py file using your own MYSQL username and password
6. Run server.py
7. When the server is up and running, open http://127.0.0.1:5000/ in web browser
    - http://127.0.0.1:5000/HRinterface.html
    - http://127.0.0.1:5000/employees
### Description of Project
The project involved writing a Flask program to consume a restful API and create a web interface in order to interact with the database.

I also hosted this project on Pythonanywhere:
- Github repository: https://github.com/SaydsC/deploytopythonanywhere
- pythonanywhere:  https://sadieconcannon.pythonanywhere.com/
                    https://sadieconcannon.pythonanywhere.com/HRinterface.html
