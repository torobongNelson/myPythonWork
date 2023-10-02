class ShowCallDurationMenu:
    def __init__(self):
        self.scanner = input

    def display(self):
        print("Show call duration:\n"
              + "1. Last call duration"
              + "2. All calls’ duration"
              + "3. Received calls’ duration"
              + "4. Dialled calls’ duration"
              + "5. Clear timers"
              )

        choice = int(input())

        if choice == 1:
            print("Last call duration")
        elif choice == 2:
            print("All calls duration")
        elif choice == 3:
            print("Received calls duration")
        elif choice == 4:
            print("Dialled calls duration")
        elif choice == 5:
            print("Clear timers")
