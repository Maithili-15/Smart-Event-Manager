# main.py (top)
from utils.emailer import (
    read_attendees_from_xlsx,
    get_upcoming_events,
    send_reminders_for_events
)

from events.manager import add_event, edit_event, delete_event
from events.views import view_day, view_week, view_month, search_event, filter_event
from events.views import upcoming_events, sort_events, view_day, view_week, view_month, search_event, filter_event
from storage import read_events, write_events

from datetime import datetime, timedelta

def get_upcoming_events(events, within_hours=None, specific_date=None):
    now = datetime.now()
    selected = []

    for ev in events:
        try:
            ev_dt = datetime.strptime(f"{ev.date} {ev.time}", "%d-%m-%Y %H:%M")
        except Exception:
            continue  # agar parsing fail ho jaye to skip

        if within_hours is not None:
            end_time = now + timedelta(hours=within_hours)
            if now <= ev_dt <= end_time:
                selected.append(ev)

        elif specific_date is not None:
            if ev.date == specific_date:
                selected.append(ev)

    return selected


def send_reminders_cli():
    print("\n--- Send Reminders ---")
    # load all events from your existing read_events() function
    try:
        all_events = read_events()   # assumes read_events() exists in main.py
    except NameError:
        print("read_events() not found in main.py. Make sure your file has read_events() to load events.")
        return

    if not all_events:
        print("No events available to send reminders for.")
        return

    mode = input("Send for upcoming hours or a specific date? (type 'hours' or 'date'): ").strip().lower()
    selected = []
    if mode == "hours":
        val = input("Enter hours from now (e.g., 24): ").strip()
        try:
            hours = int(val)
        except ValueError:
            print("Invalid number.")
            return
        selected = get_upcoming_events(all_events, within_hours=hours)
    elif mode == "date":
        date = input("Enter date (DD-MM-YYYY): ").strip()
        # basic validation
        try:
            datetime.strptime(date, "%d-%m-%Y")
        except Exception:
            print("Invalid date.")
            return
        selected = get_upcoming_events(all_events, specific_date=date)
    else:
        print("Invalid option.")
        return

    if not selected:
        print("No events matched your selection.")
        return

    path = input("Path to attendees Excel (default 'attendees.xlsx'): ").strip() or "attendees.xlsx"
    try:
        attendees = read_attendees_from_xlsx(path)
    except Exception as ex:
        print(f"Error loading attendees: {ex}")
        return

    dry = input("Dry-run? (y/n) [y]: ").strip().lower() or "y"
    dry_run = dry.startswith("y")
    print(f"\nFound {len(selected)} event(s); {len(attendees)} attendee rows loaded. Dry-run={dry_run}")
    sent = send_reminders_for_events(selected, attendees, dry_run=dry_run)
    print(f"\nDone. {len(sent)} email entries processed (printed or sent).")

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
    print("10. Send Reminders")
    print("11. Exit.")

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
            send_reminders_cli()
        elif choice == "11":
            print("Exiting... 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
