#import statsmodel
import statsmodels.api as sm
import pandas as pd

#read the csv file
data = pd.read_csv('fastfood.csv')

#add the constant
data = sm.add_constant(data)

#fit the model
model = sm.OLS(data['calories'], data[['const', 'total_fat', 'sat_fat', 'cholesterol', 'sodium']]).fit()

#print the outputs
print(model.mse_total.round(2))
print(model.rsquared.round(2))
print(model.params.round(2))
print(model.pvalues.round(2))