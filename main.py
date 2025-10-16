import random

print(" Welcome to the Band Name Generator!")

# Ask user for inputs
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

# List of random adjectives
adjectives = ["Brave", "Electric", "Jumpy", "Wiseass", "Golden", "Fierce"]

# List to store favorites
favorites = []

# Generate 5 band names automatically
for i in range(5):
    adj = random.choice(adjectives)
    band_name = f"The {adj} {city} {pet}"
    print(f"Option {i+1}: {band_name}")

    # Ask user if they want to save this as a favorite
    save = input("Do you want to save this as a favorite? (yes/no): ").lower()
    if save == "yes":
        favorites.append(band_name)

# Show all saved favorites
if favorites:
    print("\nYour favorite band names are:")
    for name in favorites:
        print("-", name)
else:
    print("\nYou didn't save any favorites this time!")


