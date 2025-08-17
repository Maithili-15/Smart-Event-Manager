# 🎉 Smart Event Manager

Welcome to **Smart Event Manager** 🗓️ – your one-stop solution for creating, managing, and analyzing events with ease.

---

## ✨ Features

### 👤 User & Admin

* 🔐 **User Authentication** (Register/Login/Logout)
* 👑 **Admin Role** → Only admins can **Add/Edit/Delete events**
* Normal users can only **view & analyze events**

### 📅 Event Management

* ➕ Add events with **date, time, type & location**
* ✏️ Edit existing events
* ❌ Delete events
* 🔍 Prevents **duplicate events at the same date & time**
* 💾 Stores events in `events.json`

### 📊 Analytics

* 📌 Total number of events
* 📂 Events grouped by **type**
* ⏳ Upcoming 5 events
* 🌍 Location statistics

### 📧 Notifications *(optional / extendable)*

* Email reminder support (`emailer.py`)

---

## 📂 Project Structure

```
smart-event-manager/
│── config/
│   └── settings.py          # App configuration
│── events/
│   ├── event.py             # Event model
│   ├── manager.py           # Event manager (CRUD)
│   └── views.py             # Event display functions
│── storage/
│   └── json_storage.py      # JSON storage handler
│── utils/
│   ├── analytics.py         # Analytics reports
│   ├── auth.py              # Authentication system
│   └── emailer.py           # Email utility
│── events.json              # Event database
│── users.json               # User database
│── main.py                  # Entry point
│── requirements.txt         # Dependencies
│── README.md                # Documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone <repo-link>
cd smart-event-manager
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the project

```bash
python main.py
```

---

## 🔑 Admin Access

* Register a user named **admin** → this user will have full privileges 👑
* Other users can only view events & analytics

---

## 🖥️ Example Usage

**Add Event (Admin Only)**

```
Enter Event Name: Workshop
Enter Date (dd-mm-yyyy): 20-08-2025
Enter Time (HH:MM): 15:30
Enter Type: Education
Enter Location: Delhi
✅ Event added successfully!
```

**View Analytics**

```
Total Events: 5
Events by Type: {"Education": 3, "Meeting": 2}
Upcoming Events: [...]
```

---

## 💡 Future Plans

* 🌐 Web dashboard
* 📱 Mobile notifications
* 📆 Google Calendar integration
* 📤 Auto email reminders

---

## 🤝 Contributing

Pull requests are welcome! Fork the repo and submit your improvements 🚀

---

## 👨‍💻 Authors

Made with ❤️ by **Your Team**

---

👉 Ab dono ke paas ek-ek **full detailed README** hoga, bas style alag (tera formal, uska emoji + friendly).

Bhai chaahta hai mai abhi tere dost ke liye ye **ready file bana ke de du** (README.md text final)?
