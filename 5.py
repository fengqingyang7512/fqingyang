import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.figure_factory as ff
import matplotlib
from matplotlib import pyplot as plt
from collections import namedtuple #修改后的代码如下：
import math

matplotlib.use('TkAgg')
matplotlib.get_backend()
plt.switch_backend('TkAgg')


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

import streamlit as st
st.markdown(r"# 我的第一个Streamlit网站")

st.markdown("""
欢迎来到我的Streamlit实验项目! 这个项目帮助我学习和理解这个强大的工具。
这里是一些我学到的有趣的事情:
- Streamlit 允许我们以与传统的Web开发完全不同的方式思考和构建Web应用程序。这使得我们可以将更多的精力投入到实现功能上，而不是布局和设计。
- 使用Python，我们可以很快地实现强大的机器学习应用程序，并通过Streamlit与其他人分享。
感谢你的访问，希望你觉得有趣！
""")
#st.title(r"我的第一个streamlit网站")
option = st.sidebar.selectbox(
    "请在下拉列表选择需要呈现的页面",
    ['Home', 'Matplotlib', 'Plotly', 'Altair'])
#st.sidebar.write('你选择了', option)

if option == 'Home':
    st. header('')
    #video_file = open('video1.mp4','rb')
    ##st.video(video_Bytes)
#数据表
    st.write('数据表')
    chart_data = pd.DataFrame(
    np.random.randn(20,7),
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    chart_data
#条形图
    st.write('条形图')
    st.bar_chart([0,1,2,3,4,5,6,7])

elif option== 'Matplotlib':
    #a = np.random.rand(100)
    #plt.ylim(0, 15)
    #st.pyplot(plt)
   #st.write('没办法，改不好')
    total_points = st.slider("螺旋点数", 1, 5000, 2000)
    num_turns = st.slider("螺旋旋转次数", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
                    .mark_circle(color='#0068c9', opacity=0.5)
                    .encode(x='x:Q', y='y:Q'))

elif option == 'Plotly':
    st.header('Plotly图表')
    x1 = np.random.randn( 100)- 2
    tt=type(x1)
    print(tt)
    x2 = np.random.randn( 100)
    x3 = np.random.randn( 100)+ 2
    #分组
    hist_data = [x1, x2, x3]
    group_labels =['项目1', '项目2', '项目3']#创建图表标签
    fig = ff.create_distplot(
    hist_data, group_labels, bin_size =[.1, .25, .5])#调用ff.create_distplot()函数创建直方图。该函数需要传入三个参数：数据源、标签和分组大小。其中，数据源就是之前定义的hist_data,标签就是group_labels,分组大小则是bin_size =[.1, .25, .5],表示将数据分成四个区间进行展示。
    # Plot!
    st.plotly_chart(fig)
else:
    st.header('Altair图表')
    data = pd.DataFrame({
    'a':['A','B','C','D','E','F','G','H','I'],
    'b':[28,55,43,91,81,53,19,87,52]
    })
    c1 = alt.Chart(data).mark_bar(
         color = "red"
    ).encode(
        x='a',
        y='b'
    ).properties(
    width =500,
    height =300
    )
    st.altair_chart(c1)
