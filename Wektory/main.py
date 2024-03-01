import math
import numpy as np
import matplotlib.pyplot as plt

def calc_circumference(n: int) -> float | np.floating:
    theta = math.pi/n
    w0 = np.matrix([math.cos(theta) - 1, math.sin(theta)]).T
    rotation = np.matrix([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    circumference = 0.0
    for i in range(n):
        circumference += np.linalg.norm(w0)
        w0 = rotation @ w0
    return circumference

def main():
    n = 20
    circumference = calc_circumference(n)
    print(f"Circumference for n = {n} is {circumference}")
    xs = list(range(1,20))
    ys = [calc_circumference(x) for x in xs]
    plt.plot(xs, ys)
    plt.xlabel("n")
    plt.xlim(1, 20)
    plt.xticks(list(range(1,21)))
    plt.ylabel("Circumference")
    plt.plot(list(range(1,20)), [math.pi for _ in range(1,20)], label="pi", linestyle="--")
    plt.legend()
    plt.grid()
    plt.show()



if __name__ == "__main__":
    main()