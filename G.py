marks = [float(input("Enter mark of subject {}: ".format(i+1))) for i in range(5)]
avg = sum(marks) / 5
if avg >= 85:
    grade = 'A'
elif avg >= 70:
    grade = 'B'
elif avg >= 55:
    grade = 'C'
elif avg >= 40:
    grade = 'D'
else:
    grade = 'Fail'
print("Average:", avg)
print("Grade:", grade)