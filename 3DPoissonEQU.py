import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建三维网格/
n = 50
U = np.zeros((n, n, n))
source = np.zeros((n, n, n))

# 添加源项 - 比如在空间中心
source[n//2, n//2, n//2] = 100

# 迭代求解
for _ in range(500):
    U[1:-1, 1:-1, 1:-1] = (U[:-2, 1:-1, 1:-1] + U[2:, 1:-1, 1:-1] +
                            U[1:-1, :-2, 1:-1] + U[1:-1, 2:, 1:-1] +
                            U[1:-1, 1:-1, :-2] + U[1:-1, 1:-1, 2:] -
                            source[1:-1, 1:-1, 1:-1]) / 6

# 使用matplotlib可视化中间一层的解
X, Y = np.meshgrid(range(n), range(n))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, U[:, :, n // 2], cmap='viridis')
plt.show()

