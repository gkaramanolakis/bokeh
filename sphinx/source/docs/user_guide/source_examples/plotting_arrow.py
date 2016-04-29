from bokeh.plotting import figure, output_file, show
from bokeh.models import Arrow, Open, Normal, Vee

output_file("arrow.html", title="arrow.py example")

p = figure(plot_width=600, plot_height=600, x_range=(-0.1,1.1), y_range=(-0.1,0.8))

p.circle(x=[0, 1, 0.5], y=[0, 0, 0.7], radius=0.1, color=["navy", "yellow", "red"], fill_alpha=0.1)

p.add_annotation(Arrow(end=Open(), x_start=0, y_start=0, x_end=1, y_end=0))
p.add_annotation(Arrow(end=Normal(), x_start=1, y_start=0, x_end=0.5, y_end=0.7))
p.add_annotation(Arrow(end=Vee(), x_start=0.5, y_start=0.7, x_end=0, y_end=0))

show(p)
