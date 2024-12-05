import pandas
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

baby_df = pandas.read_csv('../../data/历年出生人口数量.csv')
# 自定义key值
baby_df.rename(columns={'年份': 'year', '人数（单位：万）': 'total', '说明': 'remark'}, inplace=True)
baby_dict_list = baby_df.to_dict(orient='records')

graduate_df = pandas.read_csv('../../data/全国普通高等学校毕业人数.csv')
# 自定义key值
graduate_df.rename(columns={'年份': 'year', '人数（单位：万）': 'total'}, inplace=True)
graduate_dict_list = graduate_df.to_dict(orient='records')

# 绘制时间范围 2000-2025
start_year = 2000
end_year = 2025
# 毕业年龄
graduate_years = 22
year_x = [str(i) for i in range(start_year, end_year + 1)]
baby_y_curr_year = [e['total'] for e in baby_dict_list if start_year <= e['year'] <= end_year]
baby_y_before22 = [e['total'] for e in baby_dict_list if e['year'] >= start_year - graduate_years]
graduate_y = [e['total'] for e in graduate_dict_list if e['year'] >= start_year]
# 数值范围1-100 数值太小，不适合放到一个图表中
# graduate_rate_y = [round(num / baby_y[i] * 100, 2) for i, num in enumerate(graduate_y)]

line_chart = Line(init_opts=opts.InitOpts(width="1200px"))
line_chart.add_xaxis(year_x)
line_chart.add_yaxis("应届毕业生", graduate_y, is_smooth=True,
                     label_opts=opts.LabelOpts(
                         is_show=True,
                         font_size=10,
                     ),)
line_chart.add_yaxis(series_name="22年前新生儿", y_axis=baby_y_before22, is_smooth=True,
                     label_opts=opts.LabelOpts(
                         is_show=True,
                         font_size=10,
                     ),)
line_chart.add_yaxis(series_name="当年新生儿", y_axis=baby_y_curr_year, is_smooth=True,
                     label_opts=opts.LabelOpts(
                         is_show=True,
                         font_size=10,
                     ),)
# line_chart.add_yaxis("应届生占比", graduate_rate_y, is_smooth=True)

line_chart.set_global_opts(title_opts=opts.TitleOpts(title="年份与人口关系图", is_show=False),
                           tooltip_opts=opts.TooltipOpts(trigger="axis"),
                           yaxis_opts=opts.AxisOpts(name="人数（单位：万）"),
                           xaxis_opts=opts.AxisOpts(name="年份"))

# 渲染图表为HTML
html_file_path = line_chart.render('人口趋势.html')

# 需要安装 snapshot_selenium
make_snapshot(snapshot, html_file_path, "人口趋势.png")
