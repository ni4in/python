"""
Create a function that calculates the acceleration given initial velocity v1 , final velcity v2, start time t1 and end time t2. 
a = v2-v1/t2-t1
To test your solution , call the function by inputting values 0, 10, 0, 20 for v1, v2, t1 and t2 respectively
"""


def get_acceleration(initial_veloxity, final_velocity, start_time, end_time):
    return (final_velocity - initial_veloxity) / (end_time - start_time)

print(get_acceleration(0,10,0,20))
