#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

from pyecharts import Bar


def pyecharts_demo1():
    bar = Bar("我的第一个图表", "这里是副标题")

    # 自 0.5.2+ 起，pyecharts 支持更换主体色系。下面是跟换为 'dark' 的例子：
    bar.use_theme('dark')

    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
            [5, 20, 36, 10, 75, 90], is_more_utils=True)
    # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
    bar.render('render.html')  # 生成本地 HTML 文件


def pyecharts_demo2():
    CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    clothes_v1 = [5, 20, 36, 10, 75, 90]
    clothes_v2 = [10, 25, 8, 60, 20, 80]

    (Bar('柱状图数据堆叠示例')
     .add("商家A", CLOTHES, clothes_v1, is_stack=True)  # is_stack=True 将两个商家合在一起显示
     .add("商家B", CLOTHES, clothes_v2, is_stack=True)
     .render())

def pyecharts_demo2_2():
    CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    clothes_v1 = [5, 20, 36, 10, 75, 90]
    clothes_v2 = [10, 25, 8, 60, 20, 80]

    (Bar('柱状图数据堆叠示例')
     .add("商家A", CLOTHES, clothes_v1, mark_point=['average'])  # is_stack=True 将两个商家合在一起显示
     .add("商家B", CLOTHES, clothes_v2, mark_line=['min','max'])
     .render('demo2_2.html'))
    print('pyecharts_demo2_2')


# pyecharts 重构了渲染的内部逻辑，改善效率。推荐使用以下方式显示多个图表
from pyecharts import Line
from pyecharts.engine import create_default_environment


def pyecharts_demo3():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
            [5, 20, 36, 10, 75, 90],is_convert=True)#is_convert=True x轴y轴交换

    line = Line("我的第一个图表", "这里是副标题")
    line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
             [5, 20, 36, 10, 75, 90])

    env = create_default_environment('html')
    # 为渲染创建一个默认配置环境
    # create_default_environment(file_type)
    # file_type: 'html', 'svg','png','jpeg','gif',or 'pdf'

    env.render_chart_to_file(bar, path='bar.html')#柱状图
    env.render_chart_to_file(line, path='line.html')#拆线图


def pyecharts_demo4():
    from pyecharts import Bar3D

    bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
    x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
              "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
    y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
    data = [[0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0],
            [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2], [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3],
            [0, 16, 4], [0, 17, 6], [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
            [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0], [1, 8, 0],
            [1, 9, 0], [1, 10, 5], [1, 11, 2], [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
            [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2], [2, 0, 1], [2, 1, 1],
            [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3],
            [2, 11, 2], [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5], [2, 18, 5],
            [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4], [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0],
            [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4], [3, 12, 7],
            [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5], [3, 18, 5], [3, 19, 10], [3, 20, 6],
            [3, 21, 4], [3, 22, 4], [3, 23, 1], [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
            [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4], [4, 12, 2], [4, 13, 4], [4, 14, 4],
            [4, 15, 14], [4, 16, 12], [4, 17, 1], [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3],
            [4, 23, 0], [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0],
            [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1], [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11],
            [5, 17, 6], [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0], [6, 0, 1], [6, 1, 0],
            [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1],
            [6, 11, 0], [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0], [6, 18, 0], [6, 19, 0],
            [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
              visual_range=[0, 20], visual_range_color=range_color, grid3d_width=200, grid3d_depth=80)

    bar3d.render("range.html")

# Pandas&Numpy 简单示例
import numpy as np
import pandas as pd
def PadasNumpy():
    title = 'bar chart'
    index = pd.date_range('23/3/2019',periods=6, freq='M')
    df1 = pd.DataFrame(np.random.randn(6), index=index)
    df2 = pd.DataFrame(np.random.randn(6), index=index)

    dtvalue1 = [i[0] for i in df1.values]
    print([i[0] for i in df1.values])
    dtvalue2 = [i[0] for i in df1.values]
    _index = [i for i in df1.index.format()]

    bar = Bar(title, 'Profit and loss situation')
    bar.add('profit', _index, dtvalue1)
    bar.add('loss',_index, dtvalue2)
    bar.render('pandasNumpy.html')


# dataZoom 效果，'slider' 类型
import random
def dataZoom_demo():
    attr = ["{}天".format(i) for i in range(30)]
    print(attr)
    v1 = [random.randint(1,30) for _ in range(30)]
    print(v1)
    bar = Bar("Bar - datazoom - slider 示例")
    bar.add("",attr,v1, is_label_show=True, is_datazoom_show=True)
    bar.render('datazoom.html')


# Kline/Candlestick（K线图） 红涨蓝跌
from pyecharts import Kline

def candLestick_mode():
    v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
          [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
          [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
          [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
          [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
          [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
          [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
          [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
          [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
          [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
          [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
          [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
          [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
          [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
          [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
          [2255.77, 2270.28, 2253.31, 2276.22]]
    kline = Kline("K 线图示例")
    kline.add("日K", ["2019/1/{}".format(i + 1) for i in range(31)], v1)
    kline.render('kline.html')



if __name__ == '__main__':
    # pyecharts_demo2()
    # pyecharts_demo3()
    # pyecharts_demo4()
    # PadasNumpy()
    # pyecharts_demo2_2()
    # dataZoom_demo()
    candLestick_mode()