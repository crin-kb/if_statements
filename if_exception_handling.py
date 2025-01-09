try:
      x = int(input("Enter a number: "))
    if x > 0:
        print("you entered a positive number")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
