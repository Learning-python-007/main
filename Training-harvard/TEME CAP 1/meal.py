
def main():
    # Prompt the user for input
    time = input("Enter a time (in 24-hour format): ")

    # Convert the time to a float representing the number of hours
    hours = convert(time)

    # Check if it's breakfast time (7:00 - 9:59)
    if 7 <= hours < 10:
        print("It's breakfast time!")
    # Check if it's lunch time (12:00 - 14:59)
    elif 12 <= hours < 15:
        print("It's lunch time!")
    # Check if it's dinner time (18:00 - 21:59)
    elif 18 <= hours < 22:
        print("It's dinner time!")

def convert(time):
    # Split the time into hours and minutes
    hours, minutes = time.split(":")

    # Convert the hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Calculate the number of hours as a float
    return hours + minutes / 60

# Run the main function
main()