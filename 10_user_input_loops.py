# Keep asking input until user enters 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Program stopped")
        break
    print("You entered:", num)
