import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# Création du dataset
x = np.linspace(20, 30)
y = np.linspace(100, 300, 50)
X, Y = np.meshgrid(x, y)
X = X.flatten()
Y = Y.flatten()
Z = 2*X+3*Y
model = pd.DataFrame({'X': X, 'Y': Y, 'Z': Z})
print(model)

## Entrainement du model
ols = smf.ols('Z ~ X+Y', model).fit()

## Résultats
print(ols.params)