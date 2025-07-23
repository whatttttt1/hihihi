from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1=Bar()
bar1.add_xaxis(["chian","us","uk"])
bar1.add_yaxis("gdp",[30,20,10],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2=Bar()
bar2.add_xaxis(["chian","us","uk"])
bar2.add_yaxis("gdp",[60,30,20],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3=Bar()
bar3.add_xaxis(["chian","us","uk"])
bar3.add_yaxis("gdp",[90,50,40],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline=Timeline(
    {"theme": ThemeType.LIGHT}
)

timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")
timeline.add_schema(
    play_interval=500,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)
timeline.render("基础时间线绘图.html")

