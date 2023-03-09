import numpy as np
import pandas as pd
import matplotlib as mp
import warnings
warnings.filterwarnings('ignore')


def title(name):
    str1 = name.split(',')[1]
    str2 = str1.split('.')[0]
    str3 = str2.strip()
    return str3


# from sklearn.linear_model import  LogisticRegression
test = pd.read_csv(r'D:\python学习\test.csv')
train = pd.read_csv(r'D:\python学习\train.csv')
# print(test.describe())
# print("训练数据集：{}测试数据集：{}".format(train.shape, test.shape))
# test.info()
# print(train.head())
pd.set_option('display.max_columns', None)
# print(train)
# full = train.append(test, ignore_index=True)
# print(full.head())
# print("处理前")
# test.info()
test['Age'] = test['Age'].fillna(np.mean(test['Age']))      # Df.fillna用于填充空白值
test['Fare'] = test['Fare'].fillna(np.mean(test['Fare']))
test['Cabin'] = test['Cabin'].fillna('unknown')
# print('处理后')
# test.info()
# print(test.head(5))
sex_mapDict = {"male": 0, "female": 1}
train['Sex'] = train['Sex'].map(sex_mapDict)
# print(train.head())
newEmbarked = pd.get_dummies(train['Embarked'], prefix='Embarked')      # get_dummies用于实现one hot encode
train = pd.concat([train, newEmbarked], axis=1)     # concat 连接表
train.drop('Embarked', axis=1, inplace=True)        # 删除表
newPclass = pd.get_dummies(train['Pclass'], prefix='Pclass')
train = pd.concat([train, newPclass], axis=1)
train.drop('Pclass', axis=1, inplace=True)
titleDf = pd.DataFrame()
titleDf['title'] = train['Name'].map(title)    # map函数内可传入函数，且不需要给自定义函数传值
title_mapDict = {                               # "偷取"数据 = =
                    "Capt":       "Officer",
                    "Col":        "Officer",
                    "Major":      "Officer",
                    "Jonkheer":   "Royalty",
                    "Don":        "Royalty",
                    "Sir":       "Royalty",
                    "Dr":         "Officer",
                    "Rev":        "Officer",
                    "the Countess": "Royalty",
                    "Dona":       "Royalty",
                    "Mme":        "Mrs",
                    "Mlle":       "Miss",
                    "Ms":         "Mrs",
                    "Mr":        "Mr",
                    "Mrs":       "Mrs",
                    "Miss":      "Miss",
                    "Master":    "Master",
                    "Lady":      "Royalty"
                    }
titleDf['title'] = titleDf['title'].map(title_mapDict)
newtitleDf = pd.get_dummies(titleDf['title'])
train = pd.concat([train, newtitleDf], axis=1)
train.drop('Name', axis=1, inplace=True)
# print(train.head(10))
print(test)
