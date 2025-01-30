from tinydb import TinyDB, Query

# Create or connect to the database
db = TinyDB('students.json')

# Reference the default table
students_table = db.table('students')

# Insert a new student
studentnumber1 = {
    "id": 101,
    "name": "John Doe",
    "age": 16,
    "gender": "Male",
    "contact": "123-456-7890",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 85,
        "science": 90,
        "english": 88
    },
    "attendance": 92.5,
    "activities": ["Basketball", "Debate Club"],
    "address": {
        "street": "123 Main St",
        "city": "Springfield",
        "state": "IL",
        "zip_code": "62704"
    }
}
students_table.insert(studentnumber1)
studentnumber2 = {
    "id": 102,
    "name": "John Smith",
    "age": 15,
    "gender": "Male",
    "contact": "586-869-1234",
    "grade_level": "Grade 9",
    "subjects": {
        "math": 95,
        "science": 92,
        "english": 98
    },
    "attendance": 98.5,
    "activities": ["Math", "IT"],
    "address": {
        "street": "20 Square St",
        "city": "New York",
        "state": "USA",
        "zip_code": "69834"
    }
}
students_table.insert(studentnumber2)
studentnumber3 = {
    "id": 103,
    "name": "Anna Taylor",
    "age": 17,
    "gender": "famale",
    "contact": "586-553-8657",
    "grade_level": "Grade 11",
    "subjects": {
        "math": 99,
        "science": 85,
        "english": 89
    },
    "attendance": 95.4,
    "activities": ["Soccer", "Chess Club"],
    "address": {
        "street": "69 Full St",
        "city": "London",
        "state": "UK",
        "zip_code": "69965"
    }
}
students_table.insert(studentnumber3)
studentnummber4 = {
    "id": 104,
    "name": "Katiana Smith",
    "age": 16,
    "gender": "Female",
    "contact": "536-195-3654",
    "grade_level": "Grade 8",
    "subjects": {
        "math": 75,
        "science": 80,
        "english": 90
    },
    "attendance": 82.5,
    "activities": ["Basketball", "Debate Club"],
    "address": {
        "street": "58 Main St",
        "city": "Ottawa",
        "state": "Kanada",
        "zip_code": "58694"
    }
}
students_table.insert(studentnummber4)
studentnumber5 ={
    "id": 105,
    "name": "Forest Gump",
    "age": 15,
    "gender": "Male",
    "contact": "745-685-8695",
    "grade_level": "Grade 7",
    "subjects": {
        "math": 96,
        "science": 83,
        "english": 77
    },
    "attendance": 88.3,
    "activities": ["Voleyball", "Debate Club"],
    "address": {
        "street": "58 Main St",
        "city": "Ottawa",
        "state": "Kanada",
        "zip_code": "58694"
        }
}
students_table.insert(studentnumber5)
studentnumber6 = {
    "id": 106,
    "name": "Lara Croft",
    "age": 11,
     "gender": "Famale",
    "contact": "745-325-5863",
    "grade_level": "Grade 5",
    "subjects": {
        "math": 84,
        "science": 93,
        "english": 90
    },
    "attendance": 77.5,
    "activities": ["Tennis", "eenglish"],
    "address": {
        "street": "65 Rever St",
        "city": "Ottawa",
        "state": "Kanada",
        "zip_code": "58694"
        }
}
students_table.insert(studentnumber6)
studentnumber7 = {
    "id": 107,
    "name": "Grace Harris",
    "age": 14,
    "gender": "Female",
    "contact": "135-791-2468",
    "grade_level": "Grade 8",
    "subjects": {
        "math": 85,
        "science": 88,
        "english": 82
    },
    "attendance": 89.5,
    "activities": ["Art Club", "Volleyball"],
    "address": {
        "street": "482 Cedar Avenue",
        "city": "New York",
        "state": "New York",
        "zip_code": "10001"
    }
}
students_table.insert(studentnumber7)