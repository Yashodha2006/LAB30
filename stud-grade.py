import sys

if len(sys.argv) == 6:
    # Script name + 5 marks
    script_name = sys.argv[0]
    m1 = float(sys.argv[1])
    m2 = float(sys.argv[2])
    m3 = float(sys.argv[3])
    m4 = float(sys.argv[4])
    m5 = float(sys.argv[5])
    print("User provided marks:")
else:
    script_name = sys.argv[0]
    # Default marks if not provided
    m1, m2, m3, m4, m5 = 80, 75, 65, 55, 60
    print("No input given – using default marks.")

# Calculate average
average = (m1 + m2 + m3 + m4 + m5) / 5

# Determine grade
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 40:
    grade = 'D'
else:
    grade = 'Fail'

# Display results
print("\nScript Name:", script_name)
print("Marks:", m1, m2, m3, m4, m5)
print("Average Marks:", average)
print("Grade:", grade)