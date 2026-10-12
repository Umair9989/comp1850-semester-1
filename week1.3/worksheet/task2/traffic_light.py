"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Mohammed Umair Ahmed
"""

states = { "red": 4, "red_amber": 3, "green": 5, "amber": 3 }

maxtime = int(input())  # read an integer number of steps (>0)

for systime in range(maxtime + 1):
    if systime % 15 < states["red"]:
        state = "red"
    elif systime % 15 < states["red"] + states["red_amber"]:
        state = "red_amber"
    elif systime % 15 < states["red"] + states["red_amber"] + states["green"]:
        state = "green"
    else:
        state = "amber"

    print(f"Time {systime:03d} State {state}")
# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14
