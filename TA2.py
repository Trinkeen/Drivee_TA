import numpy as np
import random

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) #Используем Манхэттенскую метрику

def find_suitable_orders(orig_order, orders):
    orig_order_start, orig_order_end = orig_order
    orig_dist = get_dist(orig_order_start, orig_order_end)
    suitable_orders = []

    for order in orders:
        order_start, order_end = order

        dist_to_order_start = get_dist(orig_order_start, order_start)
        dist_to_order_end = get_dist(orig_order_end, order_end) 
        dist_to_order = get_dist(order_start, order_end)

        additional_distance = dist_to_order_start + dist_to_order + dist_to_order_end - orig_dist
        total_dist = additional_distance + orig_dist
        if additional_distance*2 <= orig_dist:
            suitable_orders.append((order, additional_distance))
            
    suitable_orders.sort(key=lambda x: x[1])
  
    return suitable_orders

def get_coords(line):
  x1, y1, x2, y2 = list(map(int, line.strip().split()))
  points= ((x1, y1), (x2, y2))
  return points

with open("input.txt", "r") as file:
    lines = file.readlines()

orig_order = get_coords(lines[0])

num_orders = int(lines[1])
orders = []
for i in range(2, 2 + num_orders):
  orders.append(np.array(get_coords(lines[i])))

suitable_orders = find_suitable_orders(orig_order, orders)

with open("output.txt", "w") as file:
    file.write("SUITABLE ORDERS:\n")
    for order, additional_distance in suitable_orders:
        order_index = np.where(np.all(orders == order, axis=(1, 2)))[0][0]
        file.write(f"\nOrder: #{order_index+1}\n{order}\n")
        file.write(f"Additional Distance = {additional_distance}\n")
