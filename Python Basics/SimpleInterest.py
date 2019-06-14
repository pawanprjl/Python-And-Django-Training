#inputs 
principal = int(input("Enter your principal: "))
rate = int(input("Enter your rate: "))
time = int(input("Enter your time: "))

#calculation of simple interest
simpleInterest = principal * rate * time / 100

#output
print('Required interest is ', simpleInterest)