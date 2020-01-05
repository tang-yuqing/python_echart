from flask import Flask,render_template,request
from jinja2 import Markup
import pandas as pd
from pyecharts import options as opts
import pyecharts.options as opts
from pyecharts.faker import  Faker
from pyecharts.charts import Bar,Tab,Line,Map,Timeline,Grid,Scatter,Pie
import numpy as np
from pyecharts.globals import ChartType, SymbolType
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go


df = pd.read_csv('Adults_ages_15_newly_infected_with_HIV.csv')


def value():
    """get max value and min value"""
    Adults_ages_15_newly_infected_with_HIV_2018 = list(zip(list(df.country),list(df.year_2018.fillna(0))))
    max=df.year_2018.max()
    min=df.year_2018.min()
    return max,min

print(max)
