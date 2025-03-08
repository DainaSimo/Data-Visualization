import pandas as pd
import numpy as np
import dash
from dash import html, dcc, Dash
from jupyter_dash import JupyterDash
import plotly.express as px

data= pd.read_csv("ds_salaries.csv")
data.head()

data.info()

data["work_year"]= data["work_year"].astype(object)

data["job_title"].unique()

data.info()

job_title1 = px.histogram(data.query("job_title in ['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="work_year", y="salary_in_usd",hover_data = ["work_year", "company_location"])
job_title1.update_yaxes(title="salary in usd")
job_title1.show()

job_title2 = px.pie(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), values='salary_in_usd', names='job_title', title=' job title repartition', hover_data = ["work_year", "company_location", "company_size"], hole = .3,template="seaborn")
job_title2

fun = px.funnel(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x = "salary_in_usd", y="job_title", color ="company_size")
fun.show()

year = px.histogram(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="experience_level", y="salary_in_usd",hover_data = ["work_year", "company_location"])
year.update_yaxes(title="salary in usd")
year.show()

year1 = px.histogram(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="company_size", y="salary_in_usd",hover_data = ["work_year", "company_location"])
year1.update_yaxes(title="salary in usd")
year1.show()

year2 = px.histogram(data.query("job_title in ['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="work_year", y="remote_ratio",hover_data = ["work_year", "company_location"])
year2.update_yaxes(title="remote ratio")
year2.show()

data["employee_residence"].unique()

app1 =Dash(__name__)

app1.layout = html.Div([
    html.H1("Dashboard of job data", id = "titre"),
    html.Div([
        html.Div([
            dcc.Graph(id="graph1", figure = job_title1),
            dcc.Graph(id="graph2", figure = job_title2)
           
        ], id="container1"),
        html.Div([
             dcc.Graph(id="graph3", figure = fun),
            dcc.Graph(id="graph6", figure = year2)
        ], id="container2"),
        
        ], id="container3"),
            
    ],id="container4")


server = app1.server
    
 
