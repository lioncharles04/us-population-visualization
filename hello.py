from preswald import connect, get_df, text, plotly
import plotly.express as px

connect()
df = get_df("my_dataset")

text("# U.S. Population Growth Dashboard")
text("## Population Trends")
text("This visualization shows the population growth in the U.S. over the last 5 years.")

fig = px.line(df, x="year", y="population", title="Population Over Time")
plotly(fig)
