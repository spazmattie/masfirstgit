import matplotlib.pyplot as plt

labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [24202, 10161, 12856, 30766]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Common Core Algebra 2015 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [34764, 13364, 17021, 46019]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Common Core Algebra 2016 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [36328, 13874, 17361, 49988]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Common Core Algebra 2017 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [34873, 14255, 17669, 49889]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Common Core Algebra 2018 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [34404, 14617, 17871, 51714]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Common Core Algebra 2019 Racial Makeup')

plt.show()