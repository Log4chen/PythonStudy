import pandas, numpy

'''
Pandas 可以从各种文件格式比如 CSV、JSON、SQL、Microsoft Excel 导入数据。
Pandas 可以对各种数据进行运算操作，比如归并、再成形、选择，还有数据清洗和数据加工特征。
Pandas 广泛应用在学术、金融、统计学等各个数据分析领域。

Pandas 提供了丰富的功能，包括：
    数据清洗：处理缺失数据、重复数据等。
    数据转换：改变数据的形状、结构或格式。
    数据分析：进行统计分析、聚合、分组等。
    数据可视化：通过整合 Matplotlib 和 Seaborn 等库，可以进行数据可视化。
'''

'''
pandas中两种数据结构：DataFrame 和 Series
- Series 类似于一维数组或列表，Series 可以看作是 DataFrame 中的一列，也可以是单独存在的一维数据结构。
- DataFrame： 类似于一个二维表格，DataFrame 可以看作是由多个 Series 按列排列构成的表格
'''

list = ['China', 'Japan', 'Korea']

s = pandas.Series(list)
print(s)
'''
索引  数据
0    China
1    Japan
2    Korea
dtype: object 数据类型
'''
s = pandas.Series(list, index=['x', 'y', 'z']) # 指定index
print(s['x'])

# 通过字典创建
pandas.Series({'x': 'China', 'y': 'Japan', 'z': 'Korea'})


# 创建DataFrame
df = pandas.DataFrame([['Google', 10], ['Runoob', 12], ['Wiki', 13]], columns=['Site', 'Age'])
# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)
print(df)

# 使用字典创建
df = pandas.DataFrame({'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]})
print(df)


# 创建一个包含网站和年龄的二维ndarray
ndarray_data = numpy.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])
# 使用DataFrame构造函数创建数据帧
df = pandas.DataFrame(ndarray_data, columns=['Site', 'Age'])
# 打印数据帧
print(df)

# csv文件
df = pandas.read_csv('../data/2023年北京积分落户数据.csv')  # DataFrame
print(df)  # 输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替
print(df.to_string())  # 输出所有

# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

# 字典
dt = {'name': nme, 'site': st, 'age': ag}

df = pandas.DataFrame(dt)

# 保存 dataframe
df.to_csv('../data/site.csv', index=False)  # index False 不输出索引行号

# pandas 处理excel文件，依赖openpyxl库
df = pandas.read_excel('../data/2023年北京积分落户数据.xlsx')
print(df.head(5))  # 输出head头 + 前5行数据

# json
df = pandas.read_json('../data/site.json')
print(df.to_string())

# 数据过滤
df = pandas.read_csv('../data/property-data.csv')
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())
#  Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型
na_values = ["n/a", "na", "NA", "--"]
df = pandas.read_csv('../data/property-data.csv', na_values=na_values)
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())

# 删除空行
df_new = df.dropna(inplace=False)  # inplace 是否修改源数据DataFrame

# 移除 ST_NUM 列中字段值为空的行
df.dropna(subset=['ST_NUM'], inplace=True)

# 给某一列的空行填充值
df['NUM_BEDROOMS'].fillna(12345, inplace=True)


