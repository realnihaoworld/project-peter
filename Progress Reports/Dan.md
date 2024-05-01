24.04.15
Began working on google extension part of program

24.04.16
Got google extension to read url and display it with html

24.04.24
Began work on creating a backend server using flask
Had to setup the virtual environment and install everything that is required
My next step is to start processing HTTP request data
VENV - helps you manage all your dependencies, in this case, Flask

24.04.29
Group met in the IESB to go over project and have a 2 hour sprint
Went to Hobby Lobby to buy board supplies

24.04.30
Office Hour with Mr. Coriell to figure out http post request problems, and gpio work

# DOCUMENTATION:
*** Make sure the venv is activated while you are doing all of this

python -m venv venv - to create
venv\Scripts\activate - to activate
deactivate - to deactivate

pip freeze > requirements.txt - to create pip requirements
pip install -r requirements.txt - install every requirement

# To run flask server
cd into server folder
flask --app server run
