# make some code DRY

#function to input the distance and time

print("How far did they run (in metres)?")
distance = float(input())
print("How long (in minutes) did they run take to run {} metres?".format(distance))
time = float(input())

def distance_time(runner):
    return distance , time 


print(distance_time(runner))

def speed(runner):
    speed = distance / (time * 60)
    return speed 

print (speed(runner))


    