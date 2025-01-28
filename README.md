### **Database Structure**
The database can include the following fields for each student:

1. **Personal Information**
   - `id`: Unique student ID (integer).
   - `name`: Full name of the student (string).
   - `age`: Age of the student (integer).
   - `gender`: Gender of the student (string: "Male", "Female", or "Other").
   - `contact`: Contact number (string).

2. **Academic Records**
   - `grade_level`: Current grade or year (string, e.g., "Grade 10", "Grade 11").
   - `subjects`: A dictionary of subjects and their respective scores.
     ```python
     {
         "math": 85,
         "science": 90,
         "english": 88
     }
     ```

3. **Attendance**
   - `attendance`: Percentage of attendance (float).

4. **Extracurricular Activities**
   - `activities`: List of extracurricular activities (e.g., ["Basketball", "Debate Club"]).

5. **Address**
   - `address`: A nested dictionary with:
     - `street`: Street name (string).
     - `city`: City (string).
     - `state`: State or region (string).
     - `zip_code`: ZIP or postal code (string).

---

### **Example Student Record**
Here’s how a single student record might look:
```python
{
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
```
