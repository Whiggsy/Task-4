'''This is a calculator for determining which award would
be granted upon the user entering their specific timings'''

# variables
qualifying_time = 100
swimming = int(input("What was your swimming time?\n"))
cycling = int(input("what was your cycling time?\n"))
running = int(input("What was your running time?\n"))

# determining the award based upon total time
total_time = swimming + cycling + running
print(f"Total time is {total_time}")
if total_time <= qualifying_time:
    print("Award is Provincial Colours")
elif total_time <= qualifying_time + 5:
    print("Award is Provincial Half colours")
elif total_time <= qualifying_time +10:
    print("Award is Provincial Scroll")
else:
    print("No Award")