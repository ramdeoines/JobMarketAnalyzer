import matplotlib.pyplot as plt

def plot_bar_chart(df, x_col, y_col, title, xlabel, ylabel):
    """
    Plots a vertical bar chart using the specified DataFrame columns.

    Args:
        df (pd.DataFrame): Data for plotting.
        x_col (str): Column for x-axis.
        y_col (str): Column for y-axis.
        title (str): Chart title.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.

    Returns:
        matplotlib.figure.Figure: The resulting plot figure.
    """
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col], color="skyblue")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_time_series(df, x_col, y_col, title, xlabel, ylabel):
    """
    Plots a time series line chart using the specified DataFrame columns.

    Args:
        df (pd.DataFrame): Data for plotting.
        x_col (str): Column for x-axis (usually datetime).
        y_col (str): Column for y-axis.
        title (str): Chart title.
        xlabel (str): Label for x-axis.
        ylabel (str): Label for y-axis.

    Returns:
        matplotlib.figure.Figure: The resulting plot figure.
    """
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker='o', linestyle='-', color='green')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig
