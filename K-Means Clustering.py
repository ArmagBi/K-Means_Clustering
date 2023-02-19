import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # for data visualization
import seaborn as sns # for statistical data visualization

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

data = '/input/facebook-live-sellers-in-thailand-uci-ml-repo/Live.csv'

df = pd.read_csv(data)

df.shape

df.head()

df.info()

df.isnull().sum()

df.drop(['Column1', 'Column2', 'Column3', 'Column4'], axis=1, inplace=True)

df.info()

df.describe()

# view the labels in the variable

df['status_id'].unique()


# view how many different types of variables are there

len(df['status_id'].unique())

# view the labels in the variable

df['status_published'].unique()

