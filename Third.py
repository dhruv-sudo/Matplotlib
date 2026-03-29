#We have a data of a bakery which shows about the no. of the sales per week 
import matplotlib.pyplot as plt
x=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']#This is the vertical line
y=[10,35,26,78,69,13]#This is the vertical line

plt.plot(x,y)

plt.title('Bakery Sales in a week')
plt.xlabel('Day of the week')
plt.ylabel('Sales on each day')

plt.show()
