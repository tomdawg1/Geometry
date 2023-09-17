import math
x_one=7
y_one=5
x_two=9
y_two=2
x_three=16
y_three=2
slope=(y_two - y_one)/(x_two - x_one)
b=abs((slope*x_one)-y_one)
midpoint_x=(x_one+x_two)/2
midpoint_y=(y_one+y_two)/2
midpoint=midpoint_x, midpoint_y
parallel_slope=slope
perpendicular_slope=-abs(1/slope)
distance=math.sqrt((x_two-x_one)**2 + (y_two-y_one)**2)
point_a=(x_one, y_one)
point_b=(x_two, y_two)
perpendicular_b=abs((perpendicular_slope*x_three)-y_three)



