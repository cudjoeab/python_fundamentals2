# # make some code DRY

# #function to input the distance and time

# print("How far did they run (in metres)?")
# distance = float(input())
# print("How long (in minutes) did they run take to run {} metres?".format(distance))
# time = float(input())

# def distance_time(runner):
#     return distance , time 


# print(distance_time(runner))

# def speed(runner):
#     speed = distance / (time * 60)
#     return speed 

# print (speed(runner))

#create method, cleans up the first question
def get_speed(person_number):
   print(f"How far did person {person_number} run (in metres)?") #using float string 
   distance = float(input())

   print(f"How long (in minutes) did person 1 run take to run {distance} metres?")
   mins = float(input())

   secs = mins * 60
   speed = distance / secs 

   return speed

speed1 = get_speed(1)
speed2 = get_speed(2)
speed3 = get_speed(3)


if speed3 > speed2 and speed3 > speed1:
  print("Person 3 was the fastest at {} m/s".format(speed3))
elif speed2 > speed3 and speed2 > speed1:
  print("Person 2 was the fastest at {} m/s".format(speed2))
elif speed1 > speed3 and speed1 > speed2:
  print("Person 1 was the fastest at {} m/s".format(speed1))
elif speed1 == speed2 and speed2 == speed3:
  print("Everyone tied at {} m/s".format(speed1))
else:
  print("Well done everyone!")


    