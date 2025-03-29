import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df = data.frame
print(df.head(3))

from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
df_scaled = pd.DataFrame(scalar.fit_transform(df), columns=df.columns)
# print(df_scaled.head(5))
# print(df.head(5))

Q1 = df['MedInc'].quantile(0.25)
Q3 = df['MedInc'].quantile(0.75)
IQR = Q3 - Q1

l_b = Q1 - 1.5 * IQR
u_b = Q3 + 1.5 * IQR

df = df[(df['MedInc'] >= l_b) & (df['MedInc'] <= u_b)]  
print(df_scaled.head(3))

df['Population_density']= df['Population']/df['AveRooms']

df['Lat_long']= df['Latitude']*df['Longitude']

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.heatmap(df.corr() , annot=True, cmap='coolwarm')
plt.show()

df.drop(columns= ['AveBedrms'] , inplace=True)

from sklearn.decomposition import PCA
pca = PCA(n_components=5)
df_reduced(df.drop(columns=['MedHouseVal']))

# Train test Split
from sklearn.model_selection import train_test_split
x_train , y_train , x_test , y_test= train_test_split(X,y, test_size=0.2 , random_state=42)

# Finding outliers for even count
# 5 7 8 12 13 15 18 21 22 25

# 1) check the data is in ascending order
# 2) iqr = 13
# outlier-> datapoints below q1-1.5*iqr or above q3+1.5*iqr are outliers

# For odd count of numbers 
# 5 7 8 12 13 15 18 21 22
# median = 13
# first half = 5 7 8 12    median = 9.5(q1)
# second half = 15 18 21 22  median = 19.5(q3)
# iqr = q3-q1 = 19.5-9.5 = 10