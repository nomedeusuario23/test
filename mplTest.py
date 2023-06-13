import pandas as pd
from pandas import Series, DataFrame

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#matplotlib inline

titanic_df = pd.read_csv("titanic.csv")



#sns.countplot(x = 'Sex', data = titanic_df)
#sns.factorplot('Pclass', 'Survived', data = titanic_df)
sns.catplot(x='Pclass', y='Survived', data=titanic_df, kind='bar')
sns.catplot(x = 'Pclass', y = 'Survived', data = titanic_df, hue = 'person', kind='bar')
#x = np.linspace(0, 3*np.pi,500)
#plt.plot(x, np.sin(x**2))
#plt.title('Jupiter Notes ist doof')
plt.show()