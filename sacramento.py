import pandas as pd
import statsmodels.api as sm

# Load the Sacramento csv file
data = pd.read_csv('sacramento.csv')

# Create a new variable for whether or not the house has 1 or more than one bathroom
data['Bathrooms'] = data.baths.apply(lambda x: 0 if x == 1 else 1)

# Create the X and y variables for logistic regression
X = data[['beds', 'sqft', 'price']]
y = data['Bathrooms']

# Add a constant for logistic regression
X = sm.add_constant(X)

# Fit the model
mod = sm.Logit(y, X).fit()

# Print the results
print(mod.params.round(2))
print(mod.pvalues.round(2))
print('The smallest p-value is for sqft')