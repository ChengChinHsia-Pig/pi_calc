import time
import math
from mpmath import mp
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.ticker import StrMethodFormatter

num_sides = 2
size = 12
times = 0
prev_pi_value = None
floatnum = 32768

def calculate_pi(num_sides, num):
    mp.dps = num # 精準度(小數點後幾位)
    radius = mp.mpf('1.0')
    side_length = 2 * radius * mp.sin(mp.pi / num_sides)
    perimeter = num_sides * side_length
    pi_estimate = perimeter / (2 * radius)
    return pi_estimate

def draw():
    fig, ax = plt.subplots(figsize=(size, size))
    polygon = RegularPolygon((0.5, 0.5), num_sides, 0.4, fill=False, color='green')
    circle = Circle((0.5, 0.5), 0.4, fill=False, color='blue')
    ax.add_patch(circle)
    ax.add_patch(polygon)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    ax.legend(['Circle', f'Eval:{num_sides} sides'])
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:.10f}'))
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:.10f}'))
    plt.show()

# 計算迴圈
while True:
    times += 1
    num_sides = num_sides * 2
    pi_value = calculate_pi(num_sides, floatnum)
    # 計算差異
    if prev_pi_value is not None:
        max_difference = abs(pi_value - prev_pi_value)
        print("第 {} 圈計算 用 {} 邊形所推估出的圓周率為：{:.30f} 最大差異值：{:.100f} 精度： {} ".format(times-1, num_sides, float(pi_value), float(max_difference), str(floatnum)))
        with open("pi.txt", "a", encoding="utf-8") as f:
            f.write(f'第{times-1}圈計算\n圓周率:{pi_value}\n差異值:{max_difference}\n')
    if times >= 15:
        a = 1+1
        # draw() # 畫圖
    else:
        pass

    prev_pi_value = pi_value