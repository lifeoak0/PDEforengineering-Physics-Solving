import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数
L = 10  # 杆的长度
T = 2   # 总时间
N = 100  # 空间分割数
M = 250  # 时间分割数
dx = L / N  # 空间步长
dt = T / M  # 时间步长

# 热传导系数
alpha = 0.01

# 初始化温度分布
u = np.zeros((N, M))

# 初始条件：杆的中间为热源
u[N//2, 0] = 2

# 计算
for m in range(0, M-1):
    for n in range(1, N-1):
        u[n, m+1] = u[n, m] + alpha * (u[n+1, m] - 2*u[n, m] + u[n-1, m])

# 创建网格
x = np.linspace(0, L, N)
t = np.linspace(0, T, M)
X, T = np.meshgrid(x, t)

# 绘制3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T, X, u.T, cmap='hot')

ax.set_xlabel('Time')
ax.set_ylabel('Position')
ax.set_zlabel('Temperature')
ax.set_title('3D Visualization of Heat Equation Solution')
plt.show()
