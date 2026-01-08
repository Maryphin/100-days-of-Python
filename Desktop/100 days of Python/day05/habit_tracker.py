import json
import os
from datetime import date, datetime

# -------------------------------
# Ensure JSON is in the same folder as this Python file
# -------------------------------
DATA_FILE = os.path.join(os.path.dirname(__file__), "habit_data.json")

# -------------------------------
# Define habits
# -------------------------------
habits = {
    "Prayer": {"type": "binary"},
    "Bible Study": {"type": "binary"},
    "100 Days of Code": {"type": "binary"},
    "Steps": {"type": "quantity", "target": 10000, "unit": "steps"},
    "Workouts": {
        "type": "quantity",
        "target": 30,
        "unit": "minutes",
        "days_per_week": 5
    },
    "Cardio": {"type": "quantity", "target": 10, "unit": "minutes"},
    "Drink Water": {"type": "quantity", "target": 2.0, "unit": "liters"},
    "Reading": {"type": "quantity", "target": 30, "unit": "minutes"},
    "Communication Skills": {"type": "quantity", "target": 20, "unit": "minutes"}
}

# -------------------------------
# Load existing data or create blank
# -------------------------------
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        try:
            habit_data = json.load(file)
        except json.JSONDecodeError:
            habit_data = {}
else:
    habit_data = {}

# -------------------------------
# Daily check-in
# -------------------------------
today = date.today().isoformat()
print(f"\n📅 Today: {date.today().strftime('%B %d, %Y')}")
print("Daily Habit Check-in\n")

today_results = {}

for habit, info in habits.items():
    print(f"➡️ {habit}")

    if info["type"] == "binary":
        answer = input("Did you complete this today? (yes/no): ").strip().lower()
        today_results[habit] = 1 if answer == "yes" else 0

    elif info["type"] == "quantity":
        while True:
            try:
                amount = float(
                    input(f"How much did you do today ({info['unit']}): ").strip()
                )
                today_results[habit] = amount
                break
            except ValueError:
                print("Please enter a number.")

    print()

# -------------------------------
# Save today’s results
# -------------------------------
habit_data[today] = today_results

with open(DATA_FILE, "w") as file:
    json.dump(habit_data, file, indent=2)

# -------------------------------
# Daily Summary
# -------------------------------
print("\n📊 Daily Summary\n")

for habit, value in today_results.items():
    info = habits[habit]

    if info["type"] == "binary":
        status = "✔" if value == 1 else "✘"
        print(f"{habit}: {status}")

    else:
        target = info["target"]
        if value >= target:
            print(f"{habit}: ✔ Goal met ({value}/{target} {info['unit']})")
        else:
            print(f"{habit}: ✘ {value}/{target} {info['unit']}")

# -------------------------------
# Weekly Workouts
# -------------------------------
if "Workouts" in habits:
    week_count = 0
    today_date = datetime.strptime(today, "%Y-%m-%d")

    for day, data in habit_data.items():
        day_date = datetime.strptime(day, "%Y-%m-%d")
        if (today_date - day_date).days < 7:
            if data.get("Workouts", 0) >= habits["Workouts"]["target"]:
                week_count += 1

    print(
        f"\n🏋️ Weekly Workouts: {week_count}/{habits['Workouts']['days_per_week']} days"
    )

print("\nGreat job showing up today 🌱")
