#student attendance tracker
monday = {"Ravi", "Sneha", "Arjun", "Divya", "Kiran"}
tuesday = {"Sneha", "Arjun", "Meera", "Divya"}

present_on_bothdays = monday.intersection(tuesday)
# print(monday.intersection(tuesday))
print("students present on both days:", present_on_bothdays)

present_only_on_monday = monday.difference(tuesday)
print("students present only on monday:", present_only_on_monday)

present_on_either_day = monday.union(tuesday)
print("students present on either day:", present_on_either_day)

attendance_count ={    }

for student in present_on_either_day:
   count = 0
   if student in monday:
      count += 1
   if student in tuesday:
        count += 1
   attendance_count[student] = count
    

print("attendance count:", attendance_count)

for name in attendance_count:
    if attendance_count[name] == 2:
        print(name, "was present on both days")
        