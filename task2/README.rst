Intive Patronage 2019
======================

Recruitment Task No. 2 Machine Learning & Big Data
--------------------------------------------------
Implement data and solved data problem to the Django Framework.
Informations used during solving the task 1.

Installation
--------------------------------------------------
Use the package manager pip to install requirements.

``pip install -r requirements.txt``

Use the RunScript 
if you want to load the database from CSV file.

``python manage.py runscript load_data``

if you want to estimate the data.

``python manage.py runscript estimate_data``

Roadmap
----------------

Home: This page is Welcome page with Project logo

Data Tables: This page have tables with data from database.
Left table have learning data.
Right table have the data after Linear Regression process.

Charts: This page have charts, histograms etc.
Left Chart have informations about training data - point scatter. -> color:orange
Right Chart have informations about predicting data - point/linear scatter. -> color:aqua

In the scripts folder are two scripts:
load_data -> loading database from csv files (this make auto remove csv files)
estimate_data -> solving the problem from task 1

Autors
-----------------
Paweł Kalicki