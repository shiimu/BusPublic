import time

# I somehow feel like this is not a create way of implementing this.
#The main idea is to have a selfupdating display of both bus times.
#Dont know what design to use so its hard for me to aim somewhere.
#Get the program to repeat every 30 seconds. dont show seconds in time left.
#Negative arrival time causes error in time formatting.

# Get which way the bus goes.
print('Current time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print('Choose which way the bus goes:')
print ('1. Kontula\n2. Mellunmäki')
choice = input()

def oneway():
    print("Kontula")
    import CallApi
def otherway():
    print("Mellunmäki")
    import CallOther
# The numerical choices were strings not ints. Had problems with that.
def choices():
    if choice == "1":
        oneway()
    elif choice == "2":
        otherway()

while choice == "1" or choice == "2":
    # execute CallApi.py
    choices()
    break
else:
    print('Please press 1 or 2')

