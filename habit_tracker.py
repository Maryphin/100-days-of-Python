from datetime import date

habits = {
    "Prayer": {"type": "binary"},
    "Bible Study": {"type": "binary"},
    "100 Days of Code": {"type": "binary"},
    "Steps": {"type": "quantity", "target": 30, "unit": "meters"},
    "Workouts": {"type": "quantity", "target": 30, "unit": "minutes", "days_per_week": 5},
    "Cardio": {"type": "quantity", "target": 10, "unit": "minutes"},
    "Drink Water": {"type": "quantity", "target": 2.0, "unit": "liters"},
    "Reading": {"type": "quantity", "target": 30, "unit": "minutes"},
    "Communication Skills": {"type": "quantity", "target": 20, "unit": "minutes"}
}

today = date.today()
print(f"\n📅 Today: {today.strftime('%B %d, %Y')}")
print("Daily Habit Check-in\n")

results = {}

for habit, info in habits.items():
    print(f"➡️ {habit}")

    if info["type"] == "binary":
        answer = input("Did you complete this today? (yes/no): ").strip().lower()
        results[habit] = 1 if answer == "yes" else 0

    elif info["type"] == "quantity":
        while True:
            try:
                amount = float(input(f"How much did you do today ({info['unit']}): ").strip())
                break
            except ValueError:
                print("Please enter a number.")
        
        target = info["target"]
        percentage = min((amount / target) * 100, 100)
        results[habit] = percentage

    print()

print("\n📊 Daily Summary\n")

for habit, value in results.items():
    if isinstance(value, int):
        status = "✔" if value == 1 else "✘"
        print(f"{habit}: {status}")
    else:
        print(f"{habit}: {value:.0f}%")

print("\nGreat job showing up today 🌱")
