import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 波动方程参数
speed = 1.0  # 波速
dx = 0.1  # 空间步长
dt = 0.01  # 时间步长
size = 50  # 空间网格大小

# 创建空间网格
x = np.arange(0, size * dx, dx)
y = np.arange(0, size * dx, dx)
z = np.arange(0, size * dx, dx)
X, Y, Z = np.meshgrid(x, y, z)

# 定义了一个初始条件表示波动的初始状态，使用高斯函数表示一个集中与空间中心的波源
initial_condition = np.exp(-((X - size * dx / 2) ** 2 + (Y - size * dx / 2) ** 2 + (Z - size * dx / 2) ** 2))

# 初始化波动场
wavefield = initial_condition.copy()
wavefield_past = initial_condition.copy()
wavefield_future = np.zeros_like(wavefield)


# 进行一步波动方程的迭代（step_wave函数是一个用于进行波动方程迭代的函数。它使用有限差分方法计算下一时间步的波动场。这里的波动方程是三维的，包括二阶偏导数的 Laplacian 部分。）
def step_wave(wavefield, wavefield_past, speed, dt, dx):
    # 使用有限差分方法计算下一时间步
    laplacian = (np.roll(wavefield, 1, axis=0) + np.roll(wavefield, -1, axis=0) +
                 np.roll(wavefield, 1, axis=1) + np.roll(wavefield, -1, axis=1) +
                 np.roll(wavefield, 1, axis=2) + np.roll(wavefield, -1, axis=2) -
                 6 * wavefield) / dx ** 2

    wavefield_future = 2 * wavefield - wavefield_past + speed ** 2 * dt ** 2 * laplacian
    return wavefield_future


# 进行几步迭代
steps = 10  # 演示中我们只进行少量迭代
for _ in range(steps):
    wavefield_future = step_wave(wavefield, wavefield_past, speed, dt, dx)
    wavefield_past = wavefield.copy()
    wavefield = wavefield_future.copy()

# 选择一个二维切面进行可视化
wavefield_slice = wavefield[:, :, size // 2]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
X2, Y2 = np.meshgrid(x, y)
ax.plot_surface(X2, Y2, wavefield_slice, cmap='viridis')
plt.show()

