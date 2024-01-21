import math

import numpy as np
from matplotlib import pyplot as plt


U1 = lambda t: 100 * math.sin(2 * math.pi * 50 * t)
R1 = 5
R2 = 4
L1 = 0.01
C1 = 300e-6
C2 = 150e-6

def modified_euler_method_system(f, x0, t0, tn, h):
    num_steps = int((tn - t0) / h)
    t_values = np.linspace(t0, tn, num_steps + 1)
    x_values = np.zeros((len(t_values), len(x0)))
    x_values[0] = x0

    for i in range(num_steps):
        x = x_values[i]
        t = t_values[i]
        x_star = x + h * f(x, t)
        f_star = f(x_star, t + h)
        x_next = x + 0.5 * h * (f(x, t) + f_star)
        x_values[i + 1] = x_next

    return t_values, x_values

def f(x, t):
    dxdt = (U1(t) - x[0] + x[1] * R1 - x[2]) * C1 / (R1 + R2)
    dydt = ((((U1(t) - x[0] + x[1] * R1 - x[2]) / (R1 + R2)) - x[1]) * R2 + x[2]) / L1
    dzdt = (((U1(t) - x[0] + x[1] * R1 - x[2]) / (R1 + R2)) - x[1]) / C2
    return np.array([dxdt, dydt, dzdt])

t0 = 0
tn = 0.2
x0 = np.array([0, 0, 0])
h = 10 ** (-5)

t_values, x_values = modified_euler_method_system(f, x0, t0, tn, h)



u2_values = [4*elem for elem in  x_values[:, 2]]
u1_values = [100 * math.sin(2 * math.pi * 50 * t) for t in t_values]

plt.figure(figsize=(10, 6))
plt.plot(t_values, u1_values, label='u1')
plt.plot(t_values, u2_values, label='u2')


plt.xlabel('Time (t)')
plt.ylabel('Values')
plt.legend()
plt.title('System of Differential Equations')
plt.grid(True)
plt.show()