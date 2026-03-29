#This code shows that how to save our program in a png pdf and other formats 
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1000,600,200,1800]

#Use of the different functions in the matplotlib
plt.plot(x,y,color='blue',marker='o')
plt.title('Simple linear plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.savefig('line_plot.png',dpi=300)#This line helps to generate a file of the given image iin the form of the png format 
plt.savefig('line_plot.pdf',dpi=300)
plt.show()
