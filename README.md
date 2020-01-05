# flask-echart项目：艾滋病新增人数与生育率、经济的关系

### 项目展示
- [Pythonanywhere链接](http://18101303036.pythonanywhere.com/)
- [github仓库](https://github.com/tang-yuqing/python_echart/)

### 研究目的
- 分析艾滋病新增感染人数的变化趋势，可帮助人们作出判断，以便采取适当行动预防情况的发生
- 找出艾滋病新增感染人数下降/上升的原因，根据原因及时寻找解决的方法
- 根据艾滋病发病率的下降/上升，判断抗逆转录病毒疗法的有效性

### 页面功能展示
1. 首页:共分三栏，分别展示表格数据、图表和地图、下面为主要数据表格


![首页](https://github.com/tang-yuqing/python_echart/blob/master/img/p1.jpg?raw=true)


2. 表格页:返回数据和由数据构成的图表，图表可交互


![表格页](https://github.com/tang-yuqing/python_echart/blob/master/img/p2.jpg?raw=true)


3. 交互图表页:数据页可实现交互，筛选国家及返回条形图


![交互图表页](https://github.com/tang-yuqing/python_echart/blob/master/img/p3.jpg?raw=true)


4. 地图页：返回两份数据地图


![地图页](https://github.com/tang-yuqing/python_echart/blob/master/img/p5.jpg?raw=true)

#### html文档介绍
 - results2.html: 首页html
 - results1.html: 表格页面html
 - result3.html: 表格筛选返回页html
 - base.html: jinja2标准，使用基模板
 - show_pyechart.html: 交互图表页html
 - map.html: 地图html

#### python代码
- 使用模块：flask、pandas、pyecharts、numpy、cufflinks、plotly
- 读取数据：使用pandas读取csv文件，并以提取country值
- 处理数据：共使用了6个csv表格
- python 文档与html文档的数据交互：利用传值，结合html模板返回标题和国家数据

#### app route与html模板的使用
- /tochart return results2.html
- /result1、/gdp、/index2、/index return results1.html
- /tochart2、/tochart3、/tochart4、/a return results3.html
- /chart return show_pyecharts.html
- /map return map.html


 
### 负责部分介绍
#### 项目完成内容
- web html界面设计
- html代码
- python图表代码连接到web显示
- 共完成两个表格加图表的数据返回和筛选、一个纯图表返回页面、一张地图
- html框架
- css样式bootstrap使用
- 数据传递

#### 网站页面url
1. [出生率表格](http://18101303036.pythonanywhere.com/result1)
2. [人均GDP](http://18101303036.pythonanywhere.com/gdp)
3. [图表：新感染情况](http://18101303036.pythonanywhere.com/chart)
4. [地图：Children_0_14_living_with_HIV_2018](http://18101303036.pythonanywhere.com/map)

