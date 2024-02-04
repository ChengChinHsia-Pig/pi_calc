from mpmath import mp
from concurrent.futures import ProcessPoolExecutor

floatnum = 128
mp.dps = floatnum
autokeep = True

def calculate_pi(num_sides, num):
    mp.dps = num
    radius = mp.mpf('1.0')
    num_sides = mp.mpf(num_sides)
    side_length = 2 * radius * mp.sin(mp.pi / num_sides)
    perimeter = num_sides * side_length
    pi_estimate = perimeter / (2 * radius)
    return pi_estimate

def worker(num_sides, floatnum):
    pi_value = calculate_pi(num_sides, floatnum)
    return pi_value

if __name__ == '__main__':
    with open("pi.txt", "w", encoding="utf-8") as f:
        f.write("Pi Calculating\n")

    num_sides = 2
    times = 0
    prev_pi_value = None

    with ProcessPoolExecutor(max_workers=16) as executor:
        while True:
            times += 1
            num_sides *= 2
            future = executor.submit(worker, num_sides, floatnum)
            pi_value = future.result()
            
            if prev_pi_value is not None:
                max_difference = abs(pi_value - prev_pi_value)
                print_output = f"第 {times-1} 圈計算 以 {num_sides//2} 邊形所推估出的圓周率為：{pi_value} 最大差異值：{max_difference} 精度: {floatnum}"
                print(print_output)
                if max_difference == mp.mpf('0'):
                    with open("pi.txt", "a", encoding="utf-8") as f:
                        f.write(print_output + "\n")
                    if autokeep:
                        floatnum *= 2
                        mp.dps = floatnum
                        print(f"目前精度修改為: {floatnum}")
                    else:
                        print(f"""
                            1)繼續計算(位數翻倍 目前:{floatnum}位 翻倍後:{floatnum * 2})
                            2)停止計算(共{floatnum}位)
                            """)
                        ask = input("請選擇:")
                        if ask == "1":
                            floatnum *= 2
                            mp.dps = floatnum
                            print(f"目前精度修改為: {floatnum}")
                        else:
                            break
            prev_pi_value = pi_value
