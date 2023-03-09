import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

matplotlib.rc("font", family='YouYuan')

train = pd.read_csv(r'D:\python学习\train.csv')
# train.info()
pd.set_option('display.max_columns', None)    # 图表全展开
# print(train.describe())

# 饼图看男女生还率
n = train.value_counts(train['Survived'])     # 存储生还状况
# print(n)
plt.figure(figsize=(6, 6))    # 创造“纸”
plt.pie(n, explode=[0, 0.1], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4,
        labeldistance=0.6, shadow=True, textprops=dict(size=15))         # 画大饼
plt.title("总体生还率")
# plt.show()

# 男女分情况
sex_count = train.groupby('Sex')['Survived'].value_counts()          # 分组,但是注意female是1在前，male是0在前？？？
# print(sex_count)
plt.figure(figsize=(12, 6))
axis1 = plt.subplot(1, 2, 1)            # 第一个大饼
axis1.pie(sex_count.loc['female'][::-1], explode=[0, 0.1], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4,
          labeldistance=0.6, shadow=True, textprops=dict(size=15))      # .loc按列取值
axis1.set_title('女性生还率')
axis2 = plt.subplot(1, 2, 2)            # 第二个大饼
axis2.pie(sex_count.loc['male'], explode=[0, 0.1], autopct='%.2f%%', labels=['死亡', '存活'], pctdistance=0.4,
          labeldistance=0.6, shadow=True, textprops=dict(size=15))
axis2.set_title('男性生还率')
# plt.show()

# 柱状图查看不同年龄生还率
age_range = train['Age']    # 看年龄范围
# print(age_range.min(),age_range.max())
age_num = np.histogram(age_range, range=[0, 80], bins=16)   # 看各区间数量（按80/16分割）
# print(age_num)
age_survived = []   # 各年龄段生存情况
for age in range(5, 81, 5):
    survived_num = train.loc[(age_range >= age-5) & (age_range <= age)]['Survived'].sum()
    age_survived.append(survived_num)
# print(age_survived)
plt.figure(figsize=(12, 6))
plt.bar(np.arange(2, 78, 5)+0.5, [40,  22,  16,  86, 114, 106,  95,  72,  48,  41,  32,  16,  15,   4,   6,   1],
        width=5, label='总人数', alpha=0.8)   # 创造柱状图设置宽度，标题，深度
plt.bar(np.arange(2, 78, 5)+0.5, [31, 11, 11, 37, 45, 48, 51, 39, 23, 21, 15, 8, 6, 0, 0, 1],
        width=5, label='生还人数')  # ps:不知道为什么用age_num传高度显示错误= =
plt.xticks(range(0, 81, 5))  # 设置坐标轴坐标
plt.yticks(range(0, 121, 10))
plt.xlabel('年龄', position=(0.95, 0), fontsize=15)  # 设置坐标轴标识
plt.ylabel('人数', position=(0, 0.95), fontsize=15)
plt.title('各年龄阶段人数和生还人数')
plt.grid(True, linestyle=':', alpha=0.6)    # 创建网络格
# plt.show()

# 以票价来判断生还情况
fare_count = train.groupby(by='Fare')['Survived'].value_counts()
# print(type(fare_count))       <class 'pandas.core.series.Series'>
Fare_count = pd.DataFrame(fare_count)
# print(type(Fare_count))       <class 'pandas.core.frame.DataFrame'>
Fare_count.rename(columns={'Survived': 'Number'}, inplace=True)   # 补齐列表名
Fare_count.reset_index(inplace=True)    # 将index恢复为Survived列
# print(Fare_count)
fare_num = Fare_count.groupby(by='Fare')['Number'].sum()
Fare_num = pd.DataFrame(fare_num)
Fare_num.rename(columns={'Number': 'Total'}, inplace=True)
# Fare_num.reset_index(inplace=True)    不需要，若加上的话后面统计会乱
# print(Fare_num)
fare_survived = Fare_count.loc[Fare_count['Survived'] == 1]
fare_survived = fare_survived.merge(Fare_num, left_on='Fare', right_index=True, how='inner')   # 缝合两个DataFrame
# print(fare_survived)
survived_rate = fare_survived['Number'].div(fare_survived['Total'])     # 相除
# print(type(survived_rate))      是列表吖
survived_rate.index = fare_survived['Fare']     # 偷天换日
# print(survived_rate)

# 创建散点图
plt.figure(figsize=(20, 6))
axes3 = plt.subplot(1, 2, 1)
axes3.scatter(survived_rate.index, survived_rate, marker='o')    # 创造散点图
axes3.set_title('乘客生还率和票价关系散点图')
plt.show()  # 展示成果
