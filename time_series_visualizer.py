import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Імпорт даних
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# 2. Очистка даних (верхні та нижні 2,5%)
df = df[(df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))]

# 3. Лінійний графік
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    fig.savefig("line_plot.png")
    return fig

# 4. Стовпчикова діаграма
def draw_bar_plot():
    # Копія даних
    df_bar = df.copy()
    
    # Додати рік і місяць
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    # Групування за роками і місяцями та обчислення середнього
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Побудова графіка
    fig = df_grouped.plot(kind='bar', figsize=(15,7)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    
    fig.savefig("bar_plot.png")
    return fig

# 5. Коробкові графіки
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')  # скорочена назва місяця
    df_box['month_num'] = df_box['date'].dt.month  # для сортування
    
    fig, axes = plt.subplots(1, 2, figsize=(20,7))
    
    # Коробковий графік по роках
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    # Коробковий графік по місяцях
    sns.boxplot(x='month', y='value', data=df_box.sort_values('month_num'), ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    fig.savefig("box_plot.png")
    return fig
