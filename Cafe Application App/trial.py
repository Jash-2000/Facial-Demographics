import matplotlib.pyplot as plt 
  
x = [0:100:0.1] 

y =  100*(1 - exp(-x-0.1))
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 

# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 