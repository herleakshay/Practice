from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\herle\\Downloads\\haberman (2).csv')
df.info()
heading = ['Age', 'Operation_Year',
           'Number_of_Axillary_Nodes', 'Survival_Status']
df.columns = heading

print(df)

# converting the column of operation_year to str format
df['Operation_Year'] = df["Operation_Year"].astype(str)

# as the data did not have the complete year, adding 19 to all the year
df['Operation_Year'] = '19' + df['Operation_Year']

# converting back to integer format
df['Operation_Year'] = df['Operation_Year'].astype(int)


plt.figure(1)
df.plot(kind='scatter', x='Operation_Year', y='Age', title='Scatter Plot')


plt.figure(2)
df.plot(kind='scatter', x='Age',
        y='Number_of_Axillary_Nodes', title='Scatter Plot')


plt.figure(3)
sns.set_style('whitegrid')
sns.FacetGrid(df, hue='Survival_Status', height=5, aspect=1).map(
    plt.scatter, 'Age', 'Number_of_Axillary_Nodes').add_legend()


plt.figure(4)
sns.set_style('whitegrid')
sns.pairplot(df, hue='Survival_Status', vars=[
             'Number_of_Axillary_Nodes', 'Operation_Year', 'Age'], height=4, aspect=1)


plt.figure(5)
sns.set(rc={'figure.figsize': (15, 8)})
sns.boxplot(data=df, x='Age', y='Number_of_Axillary_Nodes')


plt.figure(6)
sns.jointplot(x="Operation_Year", y="Age", data=df, kind="kde")

fig = plt.figure(7)
ax = plt.axes(projection='3d')
ax = plt.axes(projection='3d')
plt.xlabel = 'Age'
plt.ylabel = 'Number of Axillary Nodes'
plt.zlabel = 'Operation Year'


zdata = df['Operation_Year']
xdata = df['Age']
ydata = df['Number_of_Axillary_Nodes']
ax.scatter3D(xdata, ydata, zdata, c=xdata, cmap='Greens')

plt.show()
