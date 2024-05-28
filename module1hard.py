grades = [[2, 5, 4, 2], [5, 4, 3, 4], [5, 4, 4, 4]]
students = {'Masha', 'Alina', 'Maksim'}
average = []
for i in range(len(grades)):
    avr = sum(grades[i])/len(grades[i])
    average.append(avr)
    continue
students_1 = sorted(students)
result = {}
for j in range(len(average)):
    result[students_1[j]] = average[j]
print(result)