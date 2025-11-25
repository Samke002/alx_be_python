# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to handle priority levels
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Adjust message if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority == "low" and time_bound == "no":
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder)
