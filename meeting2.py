#Create a class named Meeting which will keep track of 
# the number of people joining and leaving a meeting. 
# It should have methods to increase the number of people in the meeting if 
# a new attendee joins, and to decrease the number of people in the meeting 
# if someone leaves. Write a program that will display a welcome message and the number of people currently in 
# the meeting every time a new Meeting object is created.

def choice_valid():
    while True:
        choice = input("Enter your choice (y/n): ")
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid choice")

class Meeting:
    attendees_count = 0
    attendees_names = []

    def __init__(self, name):
        self.name = name
        if name not in Meeting.attendees_names:
            Meeting.attendees_names.append(name)
            Meeting.attendees_count += 1
            print(f"Welcome, {name}! You have joined the meeting. Current number of people in the meeting: {Meeting.attendees_count}")
        else:
            print(f"{name} is already in the meeting.")

    
    def leave( name):
        if name in Meeting.attendees_names:
            Meeting.attendees_names.remove(name)
            Meeting.attendees_count -= 1
            print(f"{name} has left the meeting.")
        else:
            print(f"{name} is not in the meeting.")
    

# Main Program
while True:
    print("Would someone like to join the meeting?")
    if choice_valid():
        name = input("Enter the name of the person joining: ")
        new_meeting = Meeting(name)  # Create a new Meeting object for each attendee
    else:
        print("Would someone like to leave the meeting?")
        if choice_valid():
            name = input("Enter the name of the person leaving: ")
            Meeting.leave(name)

        else:
            print(','.join(Meeting.attendees_names))
            print("Exiting the program.")
            break
