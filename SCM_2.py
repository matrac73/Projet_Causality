import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

## Création du dataset
ux = np.linspace(20, 30, 10000)
uy = np.linspace(100, 300, 10000)
uz = np.linspace(1, 10, 10000)
X = ux
Y = 3*X + 2*uy
Z = Y/2 + 5*uz
model = pd.DataFrame({'ux': ux, 'uy': uy, 'uz': uz, 'X': X, 'Y': Y, 'Z': Z})
print(model)

## Entrainement du model
olsx = smf.ols('X ~ ux', model).fit()
olsy = smf.ols('Y ~ uy+X', model).fit()
olsz = smf.ols('Z ~ uz+Y', model).fit()

## Résultats
print(olsx.params)
print(olsy.params)
print(olsz.params)