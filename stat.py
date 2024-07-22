import pandas as pa
import numpy as np
import scipy.stats as stat
import matplotlib.pyplot as pot
data = {
    'Age' : [25,23,26,23,21,27,50,30],
    'Salary' : [20000,323424,234253,436543,345233,34555,345345,345345]
}

df = pa.DataFrame(data)
print(df.head(8))
age_mean = df['Age'].mean()
salary_mean = df['Salary'].mean() 

print("Mean of age",age_mean)
print("Mean of salary",salary_mean)

age_median = df['Age'].median()
salary_median = df['Salary'].median()
print("Median of age " , age_median)
print("Median of Salary",salary_median)

mode_age = df['Age'].mode()[0]
mode_salary = df['Salary'].mode()[0]
print("Mode of age",mode_age)
print("Mode of salary",mode_salary)

std_age = df['Age'].std()
std_salary = df['Salary'].std()
print("Standard Deveiation of Age",std_age)
print("Standard Deviation of Salary",std_salary)

var_age = df['Age'].var() 
var_salary = df['Salary'].var()
print("Variance of Age",var_age)
print("Variance of Salary",var_salary)


mu , sigma = 1,0.1
s =  np.random.normal(mu,sigma,100)

count , bins , ignored = pot.hist(s,30,density=True)
pot.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/(2*sigma**2)),linewidth = 2,color='r')
pot.title("Normal distribution")
pot.show() 

n, p =10,0.5
bino = np.random.binomial(n,p,1000)
pot.hist(bino , bins=10,density =True,alpha=0.6,color='b')
pot.show()


#--Quartiles(Divide a dataset into four eqaul part)

data = [1,2,3,4,5,6,7,8,9,10]
Q1 = np.percentile(data,25)
Q2 = np.median(data)
Q3= np.percentile(data,75)
Q4 = Q3-Q1

print(f"Q1 : {Q1}")
print(f"Q2 : {Q2}")
print(f"Q3 : {Q3}")
print(f"Q4 : {Q4}")
 

