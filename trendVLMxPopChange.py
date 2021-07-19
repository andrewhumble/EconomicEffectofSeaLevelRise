import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import numpy as np

# Demos a linear regression plot

df = pd.read_csv("Source 2 Filtering - Valid Rows Only.csv")
d = np.polyfit(df['Trend - VLM'],df['Annual % Change'],1)
f = np.poly1d(d)
df.insert(6,'Treg', f(df['Trend - VLM']))
ax = df.plot(y='Annual % Change', x='Trend - VLM', kind = 'scatter')
df.plot(x='Trend - VLM', y='Treg', color='Red', legend=False, ax=ax)
plt.show()