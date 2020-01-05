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


df = pd.read_csv('world_data.csv',index_col="world_data",encoding='gbk')
df1 = pd.read_csv('Children_0_14_living_with_HIV.csv',encoding='gbk')
df2 = pd.read_csv("Adults_ages_15_newly_infected_with_HIV.csv", encoding='gbk')
df3 = pd.read_csv("Birth_rate_crude.csv", encoding='gbk')
df4 = pd.read_csv('GNI_per_capita_Atlas_method.csv',encoding='gbk')
df5 = pd.read_csv('Primary_completion_rate_total.csv')
df6 = pd.read_csv('Children_ages_0_14_newly_infected_with_HIV.csv')
regions_available = list(df2.country.dropna().unique())
birth_rate = list(df3.country.dropna().unique())
gdp = list(df4.country.dropna().unique())
Birth_rate_crude = list(df.loc["Birth_rate_crude"].values)[-19:]
GNI_per_capita_Atlas_method = list(df.loc["GNI_per_capita_Atlas_method"].values)[-19:]
Primary_completion_rate_total = list(df.loc["Primary_completion_rate,_total"].values)[-19:]
Antiretroviral_therapy_coverage = list(df.loc["Antiretroviral_therapy_coverage"].values)[-19:]
Children_0_14_living_with_HIV = list(df.loc["Children_0_14_living_with_HIV"].values)[-19:]
Children_ages_0_14_newly_infected_with_HIV = list(df.loc["Children_ages_0_14_newly_infected_with_HIV"].values)[-19:]
Adults_ages_15_newly_infected_with_HIV = list(df.loc["Adults_ages_15_newly_infected_with_HIV"].values)[-19:]
Children_0_14_living_with_HIV_2018 = list(zip(list(df1.country),list(df1.year_2018.fillna(0))))

app = Flask(__name__, static_folder="templates")

#首页表格
@app.route('/', methods=['GET'])
def hu_run_2019():
    data_str = df1.to_html()
    return render_template('results2.html',
                           the_res=data_str,
                           the_select_region=regions_available)


@app.route('/tochart', methods=['POST'])
def region_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    dfs = df1.query("country=='{}'".format(the_region))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=regions_available,
                           )

#出生率表格
@app.route('/result1', methods=['GET'])
def birth_rate2019():
    data_str = df3.to_html()
    e = (
        Bar()
            .add_xaxis(
            ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018"])
            .add_yaxis("Birth_rate_crude", Birth_rate_crude, color=Faker.rand_color())
            .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return render_template('results1.html',
                           the_res=data_str,
                           bar_data=e.dump_options(),
                           the_title="出生率",
                           the_select_region=birth_rate,
                           the_action="/tochart2",)


@app.route('/tochart2',methods=['POST'])
def birth_rate_select() -> 'html':
    birth_rate = request.form["the_region_selected"]
    print(birth_rate)  # 检查用户输入
    dfs = df3.query("country=='{}'".format(birth_rate))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()
    return render_template('result3.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=birth_rate,
                           the_action="/tochart2",
                           the_title=birth_rate+' birth_rate',
                           )

#gdp表格
@app.route('/gdp', methods=['GET'])
def gdp2019():
    data_str = df4.to_html()
    d = (
        Bar()
            .add_xaxis(
                ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
                 "2013", "2014", "2015", "2016", "2017", "2018"])
                .add_yaxis("GNI_per_capita_Atlas_method", GNI_per_capita_Atlas_method, color=Faker.rand_color())
                .set_global_opts(
                title_opts=opts.TitleOpts(title=""),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            )
        )
    return render_template('results1.html',
                           the_res=data_str,
                           bar_data = d.dump_options(),
                           the_select_region=gdp,
                           the_action="/tochart3",
                           the_title="GNI_per_capita_Atlas_method ")

@app.route('/tochart3',methods=['POST'])
def gdp_select() -> 'html':
    gdp = request.form["the_region_selected"]
    print(gdp)  # 检查用户输入
    dfs = df4.query("country=='{}'".format(gdp))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()
    return render_template('result3.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=gdp,
                           the_action="/tochart3",
                           the_title= gdp+' GNI_per_capita_Atlas_method '
                           )

# 受教育率
@app.route('/index2', methods=['GET'])
def index21():
    data_str = df5.to_html()
    c = (
        Bar()
            .add_xaxis(
            ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018"])
            .add_yaxis("Primary_completion_rate_total", Primary_completion_rate_total, color=Faker.rand_color())
            .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return render_template('results1.html',
                           the_res=data_str,
                           bar_data = c.dump_options(),
                           the_select_region=gdp,
                           the_action="/tochart4",
                           the_title=" Primary_completion_rate_total")

@app.route('/tochart4',methods=['POST'])
def b1() -> 'html':
    gdp = request.form["the_region_selected"]
    print(gdp)  # 检查用户输入
    dfs = df6.query("country=='{}'".format(gdp))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()
    return render_template('result3.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=gdp,
                           the_action="/tochart4",
                           the_title=gdp+" Primary_completion_rate"
                           )



#0-14岁新感染
@app.route('/index', methods=['GET'])
def index1():
    data_str = df6.to_html()
    c = (
        Line()
            .add_xaxis(
            ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018"])
            .add_yaxis("Children_ages_0_14_newly_infected_with_HIV", Children_ages_0_14_newly_infected_with_HIV)
            .set_global_opts(title_opts=opts.TitleOpts(title="HIV新增感染人数"))

    )
    return render_template('results1.html',
                           the_res=data_str,
                           bar_data = c.dump_options(),
                           the_select_region=gdp,
                           the_action="/a",
                           the_title=" Children_ages_0_14_newly_infected_with_HIV")

@app.route('/a',methods=['POST'])
def a1() -> 'html':
    gdp = request.form["the_region_selected"]
    print(gdp)  # 检查用户输入
    dfs = df6.query("country=='{}'".format(gdp))
    fig = dfs.iplot(kind="bar", x="country", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()
    return render_template('result3.html',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=gdp,
                           the_action="/a",
                           the_title=gdp+"GNI_per_capita_Atlas_method "
                           )

#图表代码
@app.route("/chart")
def line_base() -> Scatter:
    a = (
        Line()
            .add_xaxis(
            ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018"])
            .add_yaxis("Adults_ages_15_newly_infected_with_HIV", Adults_ages_15_newly_infected_with_HIV)
            .add_yaxis("Children_ages_0_14_newly_infected_with_HIV", Children_ages_0_14_newly_infected_with_HIV)
            .set_global_opts(title_opts=opts.TitleOpts(title="HIV新增感染人数"))

    )
    c = (
        Scatter()
            .add_xaxis(
            ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018"])
            .add_yaxis("Children_0_14_living_with_HIV", Children_0_14_living_with_HIV)
            .add_yaxis("Antiretroviral_therapy_coverage", Antiretroviral_therapy_coverage)
            .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=90, min_=2),
        )
    )
    return render_template(
        "show_pyecharts.html",
        bar_data=a.dump_options(),
        bar_data2 = c.dump_options(),
        desc1 ='小结:2000年-2018年，0-14岁群体的艾滋病人数总体呈减少趋势,2000年-2018年，抗逆转录病毒治疗覆盖率正逐年提高。,因此，笔者初步判断，抗病毒治疗对治疗艾滋病具有极大的作用',
    desc2='小结:从图表中可以看出,在2000年到2018年间，0-14岁的群体中，新增感染HIV的人数是在逐年减少的, 在2000年到2018年间，15岁以上的群体中，新增感染HIV的人数也是在逐年减少的')

@app.route('/show_pyecharts')
def bar_datazoom_both() -> Bar:
    a = (
        Bar()
        .add_xaxis(["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"])
        .add_yaxis("Birth_rate_crude", Birth_rate_crude, color=Faker.rand_color())
        .add_yaxis("Primary_completion_rate_total", Primary_completion_rate_total, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    c = (
        Bar()
            .add_xaxis(
            ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012",
             "2013", "2014", "2015", "2016", "2017", "2018"])
            .add_yaxis("GNI_per_capita_Atlas_method", GNI_per_capita_Atlas_method, color=Faker.rand_color())
            .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return render_template(
        "show_pyecharts1.html",
        bar_data = a.dump_options(),
        bar_data2 = c.dump_options()
    )

#地图代码
@app.route("/map")
def map_world() -> Map:
    b = (
        Map()
        .add("Children_0_14_living_with_HIV_2018", [list(z) for z in zip(df1.country, df1.year_2018)], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Children_0_14_living_with_HIV_2018"),
            visualmap_opts=opts.VisualMapOpts(max_=140000,min_=100),
        )
    )
    return render_template("map.html")

@app.route("/map2")
def map_world2() -> Map:
    return render_template("map2.html")

if __name__ == "__main__":
    app.run()
