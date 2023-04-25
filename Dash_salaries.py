import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
from jupyter_dash import JupyterDash
import plotly.express as px

data= pd.read_csv("ds_salaries.csv")
print(data.head())

data.info()

data["work_year"]= data["work_year"].astype(object)

data["job_title"].unique()

data.info()

job_title1 = px.histogram(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="work_year", y="salary_in_usd",hover_data = ["work_year", "company_location"])
job_title1.update_yaxes(title="salary_in_usd")
job_title1.update_layout(paper_bgcolor='rgba(211,211,211,0)')



job_title2 = px.pie(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), values='salary_in_usd', names='job_title', title=' job title repartition', hover_data = ["work_year", "company_location", "company_size"], hole = .3,template="seaborn")
job_title2.update_layout(paper_bgcolor='rgba(0,0,0,0)')

fun = px.funnel(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x = "salary_in_usd", y="job_title", color ="company_size")
fun.update_layout(paper_bgcolor='rgba(0,0,0,0)')

year = px.histogram(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="experience_level", y="salary_in_usd",hover_data = ["work_year", "company_location"])
year.update_yaxes(title="salary_in_usd")
year.update_layout(paper_bgcolor='rgba(0,0,0,0)')



year1 = px.histogram(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="company_size", y="salary_in_usd",hover_data = ["work_year", "company_location"])
year1.update_yaxes(title="salary_in_usd")
year1.update_layout(paper_bgcolor='rgba(0,0,0,0)')



year2 = px.histogram(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), x="job_title", color="work_year", y="remote_ratio",hover_data = ["work_year", "company_location"])
year2.update_yaxes(title="remote_ratio")
year2.update_layout(paper_bgcolor='rgba(0,0,0,0)')

#fig = px.choropleth(data.query("job_title==['Principal Data Scientist', 'ML Engineer', 'Data Scientist','Applied Scientist', 'Data Analyst', 'Data Modeler','Research Engineer', 'Analytics Engineer','Business Intelligence Engineer', 'Machine Learning Engineer','Data Strategist', 'Data Engineer', 'Computer Vision Engineer']"), locations="company_location",
                    #color="job_title", # lifeExp is a column of gapminder
                    #hover_name="company_location", # column to add to hover information
                    #color_continuous_scale=px.colors.sequential.Plasma)
#fig.show()


print(data["employee_residence"].unique())


########################## DASH APP #######################

app1 =JupyterDash(__name__)

app1.layout = html.Div([
    html.H1("Dashboard of data jobs", id = "titre"),
    html.Div([
        html.Div([
            dcc.Graph(id="graph1", figure = job_title1,style={ 'border-radius':'15px', 'background-color':'LightGrey'}),
            dcc.Graph(id="graph2", figure = job_title2, style={ 'border-radius':'15px', 'background-color':'LightGrey'})
            
        ], id="container1"),
        html.Div([
            dcc.Graph(id="graph3", figure = fun, style={ 'border-radius':'15px', 'background-color':'LightGrey'}),
            dcc.Graph(id="graph6", figure = year2, style={ 'border-radius':'15px', 'background-color':'LightGrey'})
        ], id="container2")
            
    ],id="container3")
    
],id="container4")
 
    
if __name__== "__main__":
    app1.run_server(debug=True)
    