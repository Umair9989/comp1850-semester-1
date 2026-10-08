# Week 1.2, Session 2: Task 6
machine_temperature = input("Enter the temperature of the machine: ")
psi = input("Please enter the the machine's pressure in PSI: ")
op_status = input("Please enter the machine's operational status (1 for operating, 0 for stopped): ")

if int(machine_temperature) >= 80:
    print("The temperature is too high, shut down the machine.")
    if int(op_status) == 1:
        print("The machine is running in unsafe conditions, please shut-down")
    else:
         print("The machine is stopped and no immediate actions are required")
elif int(machine_temperature) >= 50 and machine_temperature < 80:
    print("The temperature is within safe limits")
elif int(machine_temperature) < 50:
    print("The machine temperature is low and no action is needed")

if int(psi) > 100:
    print("HIgh pressure has been detected, maintenance required")
    if int(op_status) == 1:
            print("The machine is running in unsafe conditions, please shut-down")
    else:
             print("The machine is stopped and no immediate actions are required")
elif int(psi) >= 70 and int(psi) <= 100:
    print("The pressure is stable")
elif int(psi) < 70:
    print("The pressure is low and the machine is operating as normal")

