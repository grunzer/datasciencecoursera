import math
#largest = None
#smallest = None
num = []
while True:
    number = raw_input("Enter a number: ")
    if number == "done":
        break
    try:
        number = int(number)
    except:
        print "Invalid input"
        continue
    num.append(number)
   
print "Maximum is", max(num)
print "Minimum is", min(num)
