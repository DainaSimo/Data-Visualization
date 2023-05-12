import numpy as np
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from jupyter_dash import JupyterDash
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import mysql.connector

mysql = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database = "ds_salaries"
    )


mycursor = mysql.cursor()

print("==mycursor==> ",mycursor)
        
#query = 'SELECT * FROM ds_salaries '
query = 'SELECT * FROM ds_salaries WHERE experience_level = "SE" AND job_title = "Data Scientist" ORDER BY salary ASC'
print("==query===> ",query)
mycursor.execute(query)
data = mycursor.fetchall()
#for row in data:
    #print("==row===> ",row)
#print(data)  


data = pd.DataFrame(data, columns=["Number","work_year","experience_level","employment_type","job_title","salary","salary_currency","salary_in_usd","employee_residence","remote_ratio","company_location","company_size"
])
print(data) 