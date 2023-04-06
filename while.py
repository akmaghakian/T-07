# We first define the sum and count variables
total = 0
count = 0

# We secondly loop until the user enters -1 by applyting a While True Formula
while True:
    # ask the user to enter a number
    num = int(input("Enter a number (-1 to stop): "))
    
    # Thirdly we add a break where: if the user enters -1, break out of the loop
    if num == -1:
        break
    
    # Fourthly we add the number to the total and increment the count
    total += num
    count += 1

# We finally calculate the average, excluding the -1
if count > 0:
    average = total / count
    print("The average of the numbers entered is:", average)
else:
    print("No numbers were entered.")