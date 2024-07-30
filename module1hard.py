grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a_=(sum(grades[0])/len(grades[0]))
b_=(sum(grades[1])/len(grades[1]))
j_=(sum(grades[2])/len(grades[2]))
k_=(sum(grades[3])/len(grades[3]))
s_=(sum(grades[4])/len(grades[4]))
students=tuple(sorted(students))
averaga=({students[0]:a_,students[1]:b_,students[2]:j_,students[3]:k_,students[4]:s_})
print(averaga)


