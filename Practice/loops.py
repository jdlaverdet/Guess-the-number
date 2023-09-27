#while loop
value = 1
while value <= 10:
    print(value)
    value += 1 #increment the value to do not have an infitite loop
    
print('')    

value = 1
while value <= 10:
    print(value)
    if value == 5: #breaks the loop at 5
        break
    value += 1 #increment the value    
