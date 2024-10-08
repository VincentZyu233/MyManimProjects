import numpy as np
from scipy.optimize import newton

def equation(x, k):
    return np.exp(x) - k*x

# 解方程的参数
ks = [3, 4, 5, 6, 7]

for k in ks:
    # 初始猜测值
    guess1 = 0.5  # 第一个初始猜测值
    guess2 = 2.0  # 第二个初始猜测值
    
    # 使用牛顿法求解方程，获得第一个解
    solution1 = newton(equation, guess1, args=(k,))
    print(f"Solution 1 for k = {k}: {solution1:.2f}")
    
    # 使用牛顿法求解方程，获得第二个解
    solution2 = newton(equation, guess2, args=(k,))
    print(f"Solution 2 for k = {k}: {solution2:.2f}")
