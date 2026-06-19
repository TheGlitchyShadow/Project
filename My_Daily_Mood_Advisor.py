import datetime
now = datetime.datetime.now()
name = input("Enter your name")
mood = input("How are you feeling taday (happy/sad/stressed/excited): ")
energy = int(input("Enter your energy level (1-10): "))
print(now)
if mood == "happy":
    print("Great! Keep spreading positivity today.")
elif mood == "sad":
    print("Take some time for yourself and do something you enjoy.")
elif mood == "stressed":
    print("Try taking a short break and practice deep breathing.")
elif mood == "excited":
    print("Awesome! Use that excitement to achieve something great today.")
else:
    print("Every day is a new opportunity. Stay positive!")

if energy >= 8:
    print("Your energy is high. A productive day is ahead!")
elif energy >= 5:
    print("Your energy is moderate. Pace yourself and stay focused.")
else:
    print("Your energy seems low. rest well and stay hydrated.")