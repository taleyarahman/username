#student attendance tracker
monday = {"Ravi", "Sneha", "Arjun", "Divya", "Kiran"}
tuesday = {"Sneha", "Arjun", "Meera", "Divya"}

# Prints students who attended both days (intersection)
present_on_bothdays = monday.intersection(tuesday)
# print(monday.intersection(tuesday))
print("students present on both days:", present_on_bothdays)

# Prints students who attended only Monday (difference)
present_only_on_monday = monday.difference(tuesday)
print("students present only on monday:", present_only_on_monday)

# Prints students who attended either day (union) — with no duplicates, obviously
present_on_either_day = monday.union(tuesday)
print("students present on either day:", present_on_either_day)

# Builds a dictionary called attendance_count where each student maps to how many of the two days they attended (1 or 2) — e.g. {"Ravi": 1, "Sneha": 2, ...}
attendance_count ={    }

for student in present_on_either_day:
   count = 0
   if student in monday:
      count += 1
   if student in tuesday:
        count += 1
   attendance_count[student] = count
    
# Prints only the students who attended both days, using a loop over the dictionary and an if check on the value
print("attendance count:", attendance_count)

for name in attendance_count:
    if attendance_count[name] == 2:
        print(name, "was present on both days")
        