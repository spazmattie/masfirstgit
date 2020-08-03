import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2 as ps
import plotly.express as px4

# df = pd.read_excel('Physics.xlsx')

# print(df.head())

labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [387, 231, 306, 390]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Algebra 2/Trig 2015 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [398, 241, 286, 397]
explode = (0.1, 0, 0, 0)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Algebra 2/Trig 2016 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [178, 84, 117, 196]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Algebra 2/Trig 2017 Racial Makeup')

plt.show()



