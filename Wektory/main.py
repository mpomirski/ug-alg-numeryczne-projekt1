import math
import numpy as np
import matplotlib.pyplot as plt
from typing import Any

def calc_circumference(n: int) -> float:
    theta: float = 2*math.pi/n
    w0: np.matrix = np.matrix([math.cos(theta) - 1, math.sin(theta)]).T
    rotation: np.matrix = np.matrix([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    circumference: float = 0.0
    for i in range(n):
        circumference += float(np.linalg.norm(w0))
        w0 = np.dot(rotation, w0)
    return circumference

def print_sum_diffs() -> None:
    for i in [1,10,100,1000,10000,100000]:
        print(i)
        print(calc_sum_diff(i))

def calc_diffs() -> None:
    circumfereces = [calc_circumference(x) for x in [1,10,100,1000,10000,100000]]
    diffs = [circumference - 2*math.pi for circumference in circumfereces]
    relative_diffs = [abs(diff)/2*math.pi for diff in diffs]
    print(*zip([1,10,100,1000,10000,100000], relative_diffs), sep="\n")

def calc_sum_diff(n: int) -> np.ndarray:
    theta: float = 2*math.pi/n
    w0: np.matrix[Any, Any] = np.matrix([math.cos(theta) - 1, math.sin(theta)]).T
    w0_copy: np.matrix[Any, Any] = w0
    rotation: np.matrix[Any, Any] = np.matrix([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])
    sum_wi: np.matrix[Any, Any] = np.matrix([0.0, 0.0]).T
    for i in range(n+1):
        np.add(sum_wi, w0, out=sum_wi)
        w0 = np.dot(rotation, w0)
    return (np.abs(sum_wi - w0_copy).round(16))

def main() -> None:
    print("Błędy względem 2pi, a obliczonej wartości dla n = 1, 10, 100, 1000, 10000, 100000")
    calc_diffs()
    print("Błędy względem wektora w0, a obliczonymi wartościami dla n = 1, 10, 100, 1000, 10000, 100000")
    print_sum_diffs()
    print("Wykres obliczonej wartości obwodu dla n = 1, 2, ..., 20")
    xs = list(range(1,21))
    ys: list[float] = [calc_circumference(x) for x in xs]
    plt.plot(xs, ys)
    plt.xlabel("n")
    plt.xlim(1, 20)
    plt.xticks(list(range(1,21)))
    plt.ylabel("Circumference")
    plt.plot(list(range(1,21)), [2*math.pi for _ in range(1,21)], label="2pi", linestyle="--")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()