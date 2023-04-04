import pandas as pd
import statsmodels.api as sm

# Load the dataset
data = pd.read_csv('german_credit_data.csv')

# Rename the column 'Credit amount'
data = data.rename(columns={'Credit amount': 'Credit_amount'})

# Create the X and y matrices
X = data[['Age', 'Duration']]
y = data['Credit_amount']

# Add a constant to the X matrix
X = sm.add_constant(X)

# Fit the OLS model
model = sm.OLS(y, X).fit()

# Print the parameters and R-squared
print(model.params.round(2)) 
print(model.rsquared.round(2))