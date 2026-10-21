dog = {}
dog["name"] = "Poskie"
dog["age"] = 3
dog["color"] = "brown"
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "male",
    "is_married": False,
    "skills": ["Python", "JavaScript", "HTML"], 
    "country": "USA",
    "city": "New York",
    "address": "123 Main Street"
}
print(type(student.get("skills")))
print(student.get("skills"))
student["skills"].append("CSS")
print(student.keys())
print(student.values())
print(student.items())
student.pop("is_married")
del dog
