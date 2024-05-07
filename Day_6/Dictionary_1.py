# Creating a dictionary
crew_details = {
    "Pilot": "Kumar",
    "Co-Pilot": "Raghav",
    "Head-Stewardess": "Malini",
    "Stewardess": "Mala"
}

# Accessing a specific value
print("Pilot:", crew_details["Pilot"])

print("\nIterating the dictionary using items function")
for key, value in crew_details.items():
    print(f"{key}: {value}")

print("\nIterating the dictionary using keyword 'in'")
for key in crew_details:
    if "Pilot" in key or "Co-Pilot" in key:
        print(crew_details[key])


crew_details["Pilot"] = "James"  # Here the value for key "Pilot" is being updated to "James"
print("\nAfter modifying the value of Pilot:", crew_details["Pilot"])

print("------------------------------------------------------------------")
print("Before update:")
print("Co-pilot:", crew_details.get("Co-Pilot"))

crew_details.update({"Flight Attendant": "Jane", "Co-Pilot": "Henry"})

print("\nAfter update:")
print(f"Co-pilot: {crew_details.get('Co-Pilot')}")
print(f"Flight Attendant: {crew_details['Flight Attendant']}")
