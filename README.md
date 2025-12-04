# Flask_Mega_Learning_Progress
This will contain files and documentation representing the different actions performed during the Flask Mega learning process

# Displaying Hello world ! on website
## Installation Instructions
* Update and Ugrade your PC
`sudo apt update & upgrade`
* Create and activate  virtual conda environment so that it will not broke the existing environment
`conda create -n flash_mega python & conda activate  flash_mega`
* Once environment is activated, install Flask :
`sudo apt install python3-flask`

## Hello World Displaing App building
* we will do this by the example:
   * create the main directory called **microblog** like `mkdir microblog`
   * In this directory create a subdirectory call it **app**, usinng `mkdir app` and this to be an application it must have the **__init__.py** file under its directory, after filling we create a decorator file in it which **routes.py** file

   * In the parent directory we also create file **microblog.py** which will be used to call the app.

### How to run an app

* Exort file which will run an application like this:
`export FLASK_APP=microblog.py`
* To run an application: `flask run`

