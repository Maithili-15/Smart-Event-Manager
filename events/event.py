from datetime import datetime      
import uuid  # to generate unique IDs

class Event:
    def __init__(self, name, date, time, type_, location=None, event_id=None):
        self.id = event_id or str(uuid.uuid4())  # unique ID
        self.name = name
        self.date = date        # string format: DD-MM-YYYY
        self.time = time        # string format: HH:MM
        self.type = type_
        self.location = location or "Not specified"
        self.created_at = datetime.now().strftime("%d-%m-%Y %H:%M")

    def to_dict(self):
        """Convert event object to dictionary (for JSON)."""
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "type": self.type,
            "location": self.location,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        """Rebuild Event object from dictionary."""
        return Event(
            name=data["name"],
            date=data["date"],
            time=data["time"],
            type_=data["type"],
            location=data.get("location"),
            event_id=data["id"]
        )
