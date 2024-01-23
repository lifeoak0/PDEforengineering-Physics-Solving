import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# 定义向量函数 f(x)，这里以 x 和 x^2 为例
def f(x):
    return np.array([x, x**2])

# 定义积分函数
def integral_f(a, b):
    integral_components = []
    for i in range(len(f(0))):
        # 对每个分量进行积分
        integral_comp, _ = integrate.quad(lambda x: f(x)[i], a, b)
        integral_components.append(integral_comp)
    return np.array(integral_components)

# 定义积分区间
a, b = 0, 1

# 计算积分
integral_result = integral_f(a, b)

# 输出积分结果
print("积分结果:", integral_result)

# 可视化
x = np.linspace(a, b, 100)
vec_f = np.array([f(val) for val in x])  # 计算每个点的函数值

plt.figure(figsize=(12, 6))

# 绘制原函数的分量
plt.subplot(1, 2, 1)
plt.plot(x, vec_f[:, 0], label='f(x)[0] = x')
plt.plot(x, vec_f[:, 1], label='f(x)[1] = x^2')
plt.title('Original Vector Function Components')
plt.legend()

# 绘制积分结果作为水平线
plt.subplot(1, 2, 2)
plt.hlines(integral_result[0], a, b, colors='r', label=f'Integral of f(x)[0]: {integral_result[0]:.2f}')
plt.hlines(integral_result[1], a, b, colors='b', label=f'Integral of f(x)[1]: {integral_result[1]:.2f}')
plt.title('Integral Results')
plt.legend()

plt.tight_layout()
plt.show()
