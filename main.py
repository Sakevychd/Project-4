from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# 1. Лінійний графік
fig_line = draw_line_plot()
print("Лінійний графік збережено як line_plot.png")

# 2. Стовпчикова діаграма
fig_bar = draw_bar_plot()
print("Стовпчикова діаграма збережена як bar_plot.png")

# 3. Коробкові графіки
fig_box = draw_box_plot()
print("Коробкові графіки збережені як box_plot.png")

# 4. Опційно: відобразити графіки
import matplotlib.pyplot as plt
fig_line.show()
fig_bar.show()
fig_box.show()
