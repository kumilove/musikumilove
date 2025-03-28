# MusiKumiLove

## **How to run MusiKumiLove locally**
1. To run MusiKumiLove locally, clone this repository, then inside the `musikumilove` directory, run in your terminal (ensure the terminal is inside the `musikumilove` directory):
```
python -m venv env
```
This command creates an isolated and controlled Python environment for this project. With this environment, you should not have any dependency or system issues regarding this project. Wait for the command to complete.

2. Then, run
```
source env/bin/activate
```
or
```
source env/bin/Activate.ps1
```
if you are running on a Windows machine.
(To deactivate the server, simply type `deactivate` to deactivate it.)

3. Your terminal should now have the `(env)` before your prompt, indicating that you have successfully entered the Python virtual environment.

4. Perform a 
```
pip install --upgrade pip
```
to ensure that you have the latest `pip` version.

5. After that, run 
```
pip install flask
``` 

to install the Flask packages required to deploy the server.

    - If you want, you can run ```pip install -r requirements.txt``` to install the necessary packages to run the Python files yourself

6. Navigate to the ```src``` directory. Inside it, run 
```
export FLASK_APP=app.py
```
or,
```
setup FLASK_APP=app.py
``` 

if on a Windows machine, to import environmental variables into `app.py` when you later attempt to deploy the server.

7. Finally (whilst still in the ```src``` directory), run 
```
flask run
```
to deploy the server.

8. Navigate to the local server `http://127.0.0.1:5000/` and view our project locally.
