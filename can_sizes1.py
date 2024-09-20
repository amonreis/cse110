import math

def compute_volume(radius, height):
    """This function computes and returns the volume of a cylinder"""
    volume = math.pi * (radius **2) * height
    return volume


def compute_surface_area(radius, height):
    """This function computes and returns the surface area of a cylinder"""
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def storage_efficiency(volume, surface_area):
    """"""
    strg_efficiency = volume / surface_area
    return strg_efficiency


def compute_cost_efficiency(volume, cost):
    """This function computes the cost efficiency of each steel can size"""
    cost_efficiency = volume / cost
    return cost_efficiency

def main():
    names = [
    "1 Picninc", 6.83, 10.16, .28,
    "1 Tall", 7.78, 11.91, .43,
    "2", 8.73, 11.59, .45,
    "2.5", 10.32, 11.91, .61,
    "3 Cylinder", 10.79, 17.78, .86,
    "5", 13.02, 14.29, .83,
    "6Z", 5.40, 8.89, .22,
    "8Z short", 6.83, 7.62, .26,
    "10", 15.72, 17.78, 1.53,
    "211", 6.83, 12.38, .34,
    "300", 7.62, 11.27, .38,
    "303", 8.10, 11.11, .42
    ]

    volume = compute_volume(names[1], names[2])
    surface_area = compute_surface_area(names[1], names[2])
    storage = storage_efficiency(volume, surface_area)
    cost = compute_cost_efficiency(volume, names[3])

    print(f"{names[0]} {round(storage, 2)} Cost efficiency: {round(cost, 2)}")



"""def main():
    name = "1 Picnic"
    radius = 6.83
    height = 10.16
    cost = .28
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    strg_efficiency = storage_efficiency(volume, surf_area)
    cost_efficiency = compute_cost_efficiency(volume, cost)
    print(f"#{name} {strg_efficiency:.2f}")
    print(f"Cost_efficiency: {cost_efficiency:.2f}")

    name = "1 Tall"
    radius = 7.78
    height = 11.91
    cost = 0.43
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)
    strg_efficiency = storage_efficiency(volume, surf_area)
    print(f"#{name} {strg_efficiency:.2f}")
"""

main()

