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
        if additional_distance/2 <= orig_dist:
            suitable_orders.append((order, additional_distance))
            
    suitable_orders.sort(key=lambda x: x[1])
  
    return suitable_orders
orig_order = ((0, 0), (50, 50))
print("ORIGINAL ORDER:\n", orig_order)

num_orders = 15
min_coord = 0
max_coord = 100
orders = np.array([
    [(random.randint(min_coord, max_coord), random.randint(min_coord, max_coord)),
     (random.randint(min_coord, max_coord), random.randint(min_coord, max_coord))] 
    for _ in range(num_orders)
])

suitable_orders = find_suitable_orders(orig_order, orders)
print("SUITABLE ORDERS:")
for order, additional_distance in suitable_orders:
    order_index = np.where(np.all(orders == order, axis=(1, 2)))[0][0]
    print("\nOrder: #", order_index+1,'\n', order)
    print("Additional Distance =", additional_distance)
print("\nLIST OF ORDERS:\n")  
for id, order in enumerate(orders):
    print("\nOrder: #", id+1, '\n', order)
