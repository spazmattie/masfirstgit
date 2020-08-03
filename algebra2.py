import matplotlib.pyplot as plt

labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [7539, 6487, 10250, 10395]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Algebra 2/Trig 2015 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [7202, 5836, 9997, 10180]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Algebra 2/Trig 2016 Racial Makeup')

plt.show()


labels = 'Black', 'White', 'Asian', 'Hispanic/Latino'
sizes = [964, 416, 705, 1331]
explode = (0, 0, 0, 0.1)  

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')  

plt.title('Algebra 2/Trig 2017 Racial Makeup')

plt.show()