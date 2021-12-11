import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.core.numeric import count_nonzero

PI2 = math.pi * 2

sample = [2.2, 5, 9, 9, 7.5, 3.2, 2.5, 7, 7.5, 7, 9.5, 9, 3, 2.5, 1.5, 6, 8, 5.7, 11, 10.5, 7.5, 3.5, 9.5, 5.5]
sample = np.array(sample)

total_diameter = 34.0
double_ring_size = 1.0
triple_ring_size = 1.0
single_bulls_eye_size = 1.0
bulls_eye_diameter = 1.5

fields = {
    20: (351, 9),
    1:  (9, 27),
    18: (27, 45),
    4:  (45, 63),
    13: (63, 81),
    6:  (81, 99),
    10: (99, 117),
    15: (117, 135),
    2:  (135, 153),
    17: (153, 171),
    3:  (171, 189),
    19: (189, 207),
    7:  (207, 225),
    16: (225, 243),
    8:  (243, 261),
    11: (261, 279),
    14: (279, 297),
    9:  (297, 315),
    12: (315, 333),
    5:  (333, 351)
}

fields_by_idx = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]


def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y)


n = 100000

throws = (
    np.random.normal(loc=np.mean(sample), scale=np.std(sample), size=n),
    np.random.uniform(size=n) * PI2
)

def calculate_score(throws):
    score = 0
    for distance_to_center, angle in zip(*throws):
        if distance_to_center < 1.75:
            if distance_to_center < 0.75:
                count = 50
            else:
                count = 25
        else:
            deg = (angle / PI2) * 360
            idx = int(((deg+9)%360) / 18)
            field = fields_by_idx[idx]
            factor = 1
            if distance_to_center >= 9.75 and distance_to_center < 10.75:
                factor = 3
            elif distance_to_center >= 16 and distance_to_center < 17:
                factor = 2
            elif distance_to_center >= 17:
                factor = 0
            count = field * factor
        score += count
    return score

def calculate_avg_score(throws):
    return calculate_score(throws) / len(throws[0])

def show_throws(throws):
    plt.xlim([0-34/2, 0+34/2])
    plt.ylim([0-34/2, 0+34/2])
    x, y = pol2cart(throws[0], throws[1])
    plt.scatter(x, y)
    plt.show()

print(calculate_avg_score(throws))