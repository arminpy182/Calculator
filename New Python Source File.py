from datetime import datetime

history = []

while True:

    print("\n===== MENU =====")
    print("c - Calculator")
    print("h - History")
    print("e - Exit")

    choice = input("Choose: ")

    if choice == "e":
        break

    elif choice == "h":

        print("\n===== HISTORY =====")

        if len(history) == 0:
            print("No history found.")

        else:
            for item in history:
                print(item)

        input("\nPress Enter to return...")

    elif choice == "c":

        a = int(input("First number: "))
        amal = input("Operation (+,-,*,/): ")
        b = int(input("Second number: "))

        if amal == "+":
            result = a + b

        elif amal == "-":
            result = a - b

        elif amal == "*":
            result = a * b

        elif amal == "/":
            result = a / b

        else:
            print("Invalid operation")
            continue

        print("Result:", result)

        now = datetime.now()

        record = (
            f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"Calculation: {a} {amal} {b} = {result}"
        )

        history.append(record)

    else:
        print("Invalid choice")
        
        
        


