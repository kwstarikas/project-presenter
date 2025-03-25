# Project Presenter App 

### Run without docker
1. Make sure you have python installed in your system 

    - **Windows**/ **Linux** : open cmd or powershell / Terminal and type `python --version` / `python3 --version`  
    If python is not installed installed with this guide:  <a href="https://kinsta.com/knowledgebase/install-python/" tittle="Install Python"> Install Python </a>
---

2. Next create a virtual environment and activate it: 
    - Create the virtual environment by typint `python -m venv <your virtual environment name>` / `python3 -m venv <your virtual environment name>` for linux 
    - Activate you virtual environment 
    Windows : `./<your virtual environment name>/Scripts/activate`
    Linux : `source <your virtual environment name>/bin/activate`
---

3. Install required libraries for the project: 
    `pip install -r requirements.txt`
---

4. Make django migrations: 
    - `python manage.py makemigrations`
    - `python manage.py migrate`
--- 

5. Load data in the data base by typing 
    - `python manage.py loaddata technology.json` 
    - `python manage.py loaddata project_data.json` 
---

6. Run the django app by typing : `python manage.py runserver <specify port number if needed>`

7. Visit `127.0.0.1:<your port, default 8000>/auto-swagger` and view the implemented REST Endpoints
--- 

### You can run unit test by running 
`coverage run manage.py test ; coverage html ; coverage report`

This run all the unit tests and generate a report in terminal and a report in HTML Format. 

### Run with Docker

1. Make sure you have docker installed in your machine. 

Make sure you are in the same directory as docker compose and run  `docker compose up -d `, use -d to run the container detached  

