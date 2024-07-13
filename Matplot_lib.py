import matplotlib.pyplot as pot
import numpy as py
import seaborn as sc
# from sklearn.datasets import load_iris 
#data
# x = [1,2,3,4,5]
# y = [2,3,5,7,11] 
# pot.plot(x,y,linestyle="dotted",color="red",lw=2,marker="*",mec="r",mfc="b",ms="20")#//can use ls insted of linestyle
# pot.xlabel('X-axis')
# pot.ylabel('Y-axis')
# pot.title('Simple Line Plot')
# pot.show()


# Y1 = py.array([1,2,3,4])
# y2 = py.array([5,6,7,8,2])
# pot.plot(y2)
# pot.plot(Y1)
# pot.show()



#     //---------SCATTER PLOT
# x =[1,2,3,4,5]
# y=[2,4,6,9,7]

# pot.scatter(x,y)
# pot.xlabel('sales')
# pot.ylabel('Y-axis')
# pot.title("Scatter plot")
# pot.show()


#      //---------- BAR PLOT

# cat = ['A','B','C','D']
# val =[4,7,8,1]

# pot.bar(cat,val,color="black",width ="0.1",height="0.1")
# pot.xlabel('Cat')
# pot.ylabel('Val')
# pot.title('Bar Plot')
# pot.show()


# //-------------histogram 

# data = [1,2,2,3,3,3,4,4,4,4]
# pot.hist(data,bins=4)
# pot.show()


#  //------------SUBPLOT 
# x = [1,2,3,4,5]
# x1 =[1,4,23,14,15]
# y=[2,4,6,9,7]

# fig,axd =pot.subplots(2)
# axd[0].plot(x,x1)
# axd[0].set_title("First Plot")
# axd[1].plot(x,y,'tab:orange')
# axd[1].set_title('Second plot')

# pot.tight_layout()
# pot.show()


#  //-------ANNOTATION

# x= [1,2,3,4,5]
# y=[2,3,5,7,11]

# pot.plot(x,y)
# pot.annotate('peek',xy=(5,11),xytext=(4,10),
#              arrowprops=dict(facecolor='black',shrink=0.5 ))
# pot.show()



# x =[1,2,3,4,5]
# y=[2,4,6,9,7]

# # sc.lineplot(x=x,y=y)
# # sc.scatterplot(x=x,y=y)
# sc.barplot(x=x,y=y)
# pot.show()


# iris =  load_iris()
# iris_data = sc.load_dataset("iris")

# sc.pairplot(iris_data , hue = 'species')
# pot.title("Pair plot with seaborn")
# pot.show()

data = py.random.rand(10,12)
sc.heatmap(data)
pot.show()


