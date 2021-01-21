import math
f = open("party.in", 'r')
h_x, h_y = f.readline().split(' ')
h_x, h_y = int(h_x), int(h_y)
e_x, e_y = f.readline().split(' ')
e_x, e_y = int(e_x), int(e_y)
distance = math.sqrt(((e_x-h_x)**2) + ((e_y-h_y)**2))
speed = int(f.readline())
start_e, start_p = f.readline().split(' ')
start_e, start_p = int(start_e), int(start_p)
durr_e, durr_p = f.readline().split(' ')
durr_e, durr_p = int(durr_e), int(durr_p)
total_parents_time = ((distance/speed)*2) + durr_e + start_e
total_plan_time = start_p + durr_p
if total_parents_time > total_plan_time:
    print('YES')
else:
    print('NO')
