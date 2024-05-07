def max_speciality(visits):
    specialities = {
        "P": "Pediatrics",
        "O": "Orthopedics",
        "E": "ENT"
    }
    count = {}
    
    # Counting visits for each speciality
    for visit in visits:
        if visit in count:
            count[visit] += 1
        else:
            count[visit] = 1
    
    # Finding the speciality with maximum visits
    max_visits = max(count.values())
    max_speciality = [key for key, value in count.items() if value == max_visits][0]
    
    return specialities[max_speciality]

# Test cases
test_cases = [
    [101, 'P', 102, 'O', 302, 'P', 305, 'P'],
    [101, 'O', 102, 'O', 302, 'P', 305, 'E', 401, 'O', 656, 'O'],
    [101, 'O', 102, 'E', 302, 'P', 305, 'P', 401, 'E', 656, 'O', 987, 'E']
]

for visits in test_cases:
    print(max_speciality(visits))
