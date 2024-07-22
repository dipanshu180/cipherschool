import pandas as pa
import numpy as np
from tabulate import tabulate
np.random.seed(42)

data = {
    'Age' : np.random.normal(30,10,100).astype(int),
    'AnnualIncome' : np.random.normal(50,20,100).astype(int),
    'SpendingScore' : np.random.randint(1,100,100),
    'YearWithCompany':np.random.normal(5,2,100).astype(int)
    
}
df= pa.DataFrame(data)
# print(df)

correlation_mat = df.corr()
print(tabulate(correlation_mat , headers= "keys" , tablefmt= "grid" , numalign= "right", floatfmt= ".2f"))
