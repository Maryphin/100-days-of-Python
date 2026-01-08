start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
n = int(input("Enter divisor n: "))

count = 0  # initialize counter

print(f"\nNumbers divisible by {n} between {start} and {end}:")

for x in range(start, end + 1):
    if x % n == 0:
        print(x, end=" ")
        count += 1

        # Print a new line after every 5 numbers
        if count % 5 == 0:
            print()

print(f"\n\nTotal: {count} numbers")
