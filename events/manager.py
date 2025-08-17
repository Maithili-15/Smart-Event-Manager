from datetime import datetime
from storage.json_storage import load_events, save_events
from events.event import Event

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validate_time(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def add_event():
    events = load_events()

    name = input("Enter event name: ")
    date = input("Enter date (DD-MM-YYYY): ")
    if not validate_date(date):
        print("❌ Invalid date format!")
        return

    time = input("Enter time (HH:MM): ")
    if not validate_time(time):
        print("❌ Invalid time format!")
        return

    type_ = input("Enter event type: ")
    location = input("Enter location (optional): ")

    # Prevent duplicates (same name + date + time)
    for e in events:
        if e.name.lower() == name.lower() and e.date == date and e.time == time:
            print("⚠️ Duplicate event found! Not adding.")
            return

    new_event = Event(name, date, time, type_, location)
    events.append(new_event)
    save_events(events)
    print("✅ Event added successfully!")

def edit_event():
    events = load_events()
    if not events:
        print("❌ No events to edit.")
        return

    target = input("Enter Event ID or Name to edit: ")
    found = None
    for e in events:
        if e.id == target or e.name.lower() == target.lower():
            found = e
            break

    if not found:
        print("❌ Event not found.")
        return

    print(f"Editing {found.name} ({found.date} {found.time})")
    new_name = input(f"New name (leave blank to keep {found.name}): ") or found.name
    new_date = input(f"New date (DD-MM-YYYY, blank to keep {found.date}): ") or found.date
    if new_date != found.date and not validate_date(new_date):
        print("❌ Invalid date format!")
        return

    new_time = input(f"New time (HH:MM, blank to keep {found.time}): ") or found.time
    if new_time != found.time and not validate_time(new_time):
        print("❌ Invalid time format!")
        return

    new_type = input(f"New type (blank to keep {found.type}): ") or found.type
    new_location = input(f"New location (blank to keep {found.location}): ") or found.location

    # Update fields
    found.name = new_name
    found.date = new_date
    found.time = new_time
    found.type = new_type
    found.location = new_location

    save_events(events)
    print("✅ Event updated successfully!")

def delete_event():
    events = load_events()
    if not events:
        print("❌ No events to delete.")
        return

    target = input("Enter Event ID or Name to delete: ")
    new_events = [e for e in events if not (e.id == target or e.name.lower() == target.lower())]

    if len(new_events) == len(events):
        print("❌ Event not found.")
    else:
        save_events(new_events)
        print("✅ Event deleted successfully!")
