#inputs 
principal = int(input("Enter your principal: "))
rate = int(input("Enter your rate: "))
time = int(input("Enter your time: "))

#calculation of interest
compoundInterest = principal * ((1 + rate/100)**time - 1)

#output
print('Required interest is ', compoundInterest)