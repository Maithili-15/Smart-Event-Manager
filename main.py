from events.manager import add_event, edit_event, delete_event
from events.views import view_day, view_week, view_month, search_event, filter_event
from events.views import upcoming_events, sort_events, view_day, view_week, view_month, search_event, filter_event

def main():
    print("🎉 Smart Event Manager CLI starting...")

if __name__ == "__main__":
    main()

def show_menu():
    print("\n===== Smart Event Manager =====")
    print("1. Add Event")
    print("2. Edit Event")
    print("3. Delete Event")
    print("4. View Day")
    print("5. View Week")
    print("6. View Month")
    print("7. Search Event")
    print("8. filter Events")
    print("9. Upcoming Events")
    print("10. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            edit_event()
        elif choice == "3":
            delete_event()
        elif choice == "4":
            view_day()
        elif choice == "5":
            view_week()
        elif choice == "6":
            view_month()
        elif choice == "7":
            search_event()
        elif choice == "8":
            filter_event()
        elif choice == "9":
            upcoming_events()
        elif choice == "10":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
