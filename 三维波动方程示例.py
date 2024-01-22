import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设定参数
size = 20  # 空间尺寸
duration = 10  # 时间长度
dx = 1.0  # 空间步长
dt = 0.1  # 时间步长
c = 1.0  # 波速
c1 = (c * dt / dx)**2

# 初始化波场
u = np.zeros((size, size, size))
u_previous = np.zeros((size, size, size))
u_next = np.zeros((size, size, size))

# 初始条件：在中间位置放置一个波源
mid = size // 2
u[mid, mid, mid] = 10

# 执行时间步进
for t in range(1, duration):
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            for k in range(1, size - 1):
                u_next[i, j, k] = (2 * u[i, j, k] - u_previous[i, j, k] +
                                   c1 * (u[i+1, j, k] + u[i-1, j, k] +
                                         u[i, j+1, k] + u[i, j-1, k] +
                                         u[i, j, k+1] + u[i, j, k-1] -
                                         6 * u[i, j, k]))
    u_previous, u = u, u_next

# 可视化在特定时间点的波动状态
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 选择一个时间点的波场数据可视化
u_plot = u_next[:, :, mid]  # 选择中间切片

# 创建X, Y网格
x, y = np.meshgrid(range(size), range(size))

# 使用wireframe来表示波动
ax.plot_wireframe(x, y, u_plot)

# 设置视图角度
ax.view_init(elev=40., azim=120)

# 设置标签
ax.set_title("3D Wave Propagation")
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Wave Amplitude')

# 显示图形
plt.show()
