# Simulating a do-while loop in Python..............................................................................

while True:
    # Code to be executed inside the loop

    user_input = input("Do you want to continue? (yes/no): ")

    if user_input.lower() != 'yes':
        break

# Code outside the loop
print("End of the program.")
