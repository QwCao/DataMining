import csv
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
import scipy.stats as stats

#包含数据清洗和预处理两个部分
data = pd.read_csv('./data/Building_Permits.csv', encoding='gbk', header=0, engine='python')

drop_col = [k for k,v in dict(data.isnull().sum(axis=0)).items() if v > 120000]
data = data.drop(drop_col, axis=1)

for c1,c2 in cor_col.items():
    condition = (data[c1].isnull()) & (data[c2].notnull())
    data.loc[condition, c1] = data.loc[condition, c2]
    condition = (data[c2].isnull()) & (data[c1].notnull())
    data.loc[condition, c2] = data.loc[condition, c1]

for col in mode_col:
    mode = data[col].dropna().mode()[0]
    data[col] = data[col].fillna(mode)

data = data.fillna(none_col)

data = data.dropna()

def isNumeric(feature):
    return True


def dataAbstract(feature):
    if isNumeric(feature):
        numdf=pd.DataFrame(df[feature])
        numdf.dropna().describe()
    else:
        nomdf=pd.DataFrame(df[feature])
        nomdf.groupby(feature).size()


def dataVisual(feature):
    if isNumeric():
        # Histogram
        df[feature].hist(bins=50)
        # Quantile-Quantile Plot
        stats.probplot(df[feature], dist='norm', plot=pylab)
        pylab.show()
        # Box Plot
        plt.boxplot(df[feature].dropna())
        plt.title(feature)
        plt.show()


def dataProcess(feature):
    df[feature].dropna() #drop NAN
    df[feature].fillna(df[feature].mode()[0]) # fill NAN by mode
data.to_csv('./data/new_Building_Permits.csv', index=False)

df=pd.DataFrame(pd.read_csv('./data/Building_Permits.csv', encoding='gbk', header=0, engine='python'))

