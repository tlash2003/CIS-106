start_value = int(input("Enter the start value: "))
stop_value = int(input("Enter the stop value: "))
incvalue = int(input("Enter the increment value: "))

if incvalue == 0:
    print("Increment value cannot be zero.")
else:
    while start_value <= stop_value:
        print(start_value)
        start_value = start_value + incvalue
        #start_value + incvalue <= stop_value




