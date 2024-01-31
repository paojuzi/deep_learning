# 导入 pytorch
import torch


# 使用 arrange 创建一个行向量（从零开始的前 12 个整数）
x = torch.arange(12)
print(x)
print('----------------')


# 通过张量的 shape 属性来访问张量（沿每个轴的长度）的形状
print(x.shape)
print('----------------')


# 通过调用 numel 函数检查张量的大小，即形状的所有元素乘积
print(x.numel())
print('----------------')


# 通过调用 reshape 函数改变张量的形状（不改变元素数量和元素值，也不会改变张量的大小）
X = x.reshape(3,4)
print(X)
# 可以通过 -1 自动计算出另外一个维度
X = x.reshape(-1,4)
print(X)
X = x.reshape(3,-1)
print(X)
print('----------------')


# 创建一个所有元素全为 0 的张量
print(torch.zeros((2, 3, 4)))
print('----------------')


# 创建一个所有元素全为 1 的张量
print(torch.ones((2, 3, 4)))
print('----------------')


# 创建一个张量，张量的每个元素都从均值为 0 、标准差为 1 的标准高斯分布（正态分布）中随机采样
print(torch.randn(3, 4))
print('----------------')


# 创建一个张量，每个元素取自 python 列表中的确定值
# 最外层列表对应轴 0 ，内层列表对应轴 1
print(torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))
print('----------------')