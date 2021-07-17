# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import os
import matplotlib.pyplot as plt
import datetime
import pandas as pd


# %%
def getDate(DateString):
    date = DateString.split("-")[0]
    return datetime.datetime.strptime(date, '%Y %b %d')

# %% [markdown]
# # Party Affiliation Data
#
# ## Data from Gallup Surveys
# * Source: https://news.gallup.com/poll/15370/party-affiliation.aspx


# %%
df = pd.read_csv('party.csv')
df.columns = ["Date", "Republican", "Independent", "Democrat"]
df["Date"] = df["Date"].apply(getDate)
for year in range(2021, 2003, -1):
    select_years = df[df['Date'].dt.year == year]
    display(select_years.loc[select_years["Date"] ==
                             select_years["Date"][select_years.index[0]]])

# %% [markdown]
# # Line Graphs of Party affilation in the US over time

# %%
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")

# Graph of all parties
all_parties = df.plot(x="Date", y=["Republican", "Independent", "Democrat"], color=[
                      "red", "orange", "blue"], ylabel="Part Affiliation %")

# Graph of Republicans
df_r = df[["Date", "Republican"]]
plot_r = df_r.plot(x="Date", y="Republican", color="red",
                   ylabel="Part Affiliation %")

# Graph of Independent
df_i = df[["Date", "Independent"]]
plot_i = df_i.plot(x="Date", y="Independent",
                   color="orange", ylabel="Part Affiliation %")

# Graph of Democrats
df_d = df[["Date", "Democrat"]]
plot_d = df_d.plot(x="Date", y="Democrat", color="blue",
                   ylabel="Part Affiliation %")

# Annotate Plots
np = df.to_numpy()
li = (list(np[0]))
# Republican Annotate
all_parties.annotate(str(li[1]) + "%", (li[0], li[1]))
plot_r.annotate(str(li[1]) + "%", (li[0], li[1]))
# Independent Annotate
all_parties.annotate(str(li[2]) + "%", (li[0], li[2]))
plot_i.annotate(str(li[2]) + "%", (li[0], li[2]))
# Democrat Annotate
all_parties.annotate(str(li[3]) + "%", (li[0], li[3]))
plot_d.annotate(str(li[3]) + "%", (li[0], li[3]))

# %% [markdown]
# # Pie Graphs of party affiliation in selected years (2008,2012,2016,2020)

# %%


def getPie(years):
    for year in years:
        include = df[df['Date'].dt.year == year]
        i = len(include)-1  # Get the last index for the given year
        df1 = pd.DataFrame(include.T[include.index[i]], index=[
                           "Republican", "Independent", "Democrat"])
        plt = df1.plot.pie(subplots=True, ylabel="Party Affilation in " + str(df["Date"][include.index[i]])[
                           :10], autopct='%1.1f%%', labeldistance=None, colors=["red", "orange", "blue"])


# %%
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")
getPie(range(2008, 2021, 4))


# %%
# Auto Generate HTML
os.system('jupyter nbconvert --to html PartyAnalysis.ipynb')
