import numpy as np

one_dim_arr = np.arange(15)  # 一维数组

two_dim_arr = np.arange(15).reshape(3, 5)  # 二维数组 3行5列

three_dim_arr = np.arange(24).reshape(2, 3, 4)  # 三维数组
print(three_dim_arr.shape) # (2, 3, 4)
print(three_dim_arr.ndim) # 维度 dimension 输出3
print(three_dim_arr)