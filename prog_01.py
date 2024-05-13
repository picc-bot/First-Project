# Rectangle Area and Perimeter Calculator

# Get user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display the results
print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")