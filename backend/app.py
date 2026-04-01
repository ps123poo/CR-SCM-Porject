from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data (no database for simplicity)
students = []
courses = [
    {"id": 1, "name": "Data Structures"},
    {"id": 2, "name": "Database Systems"},
    {"id": 3, "name": "Operating Systems"}
]
registrations = []


# ------------------ STUDENT APIs ------------------

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    student = {
        "id": len(students) + 1,
        "name": data["name"]
    }
    students.append(student)
    return jsonify({"message": "Student added", "student": student})


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# ------------------ COURSE APIs ------------------

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)


# ------------------ REGISTRATION APIs ------------------

@app.route('/register', methods=['POST'])
def register_course():
    data = request.json
    student_id = data["student_id"]
    course_id = data["course_id"]

    registration = {
        "student_id": student_id,
        "course_id": course_id
    }
    registrations.append(registration)

    return jsonify({"message": "Course registered successfully", "registration": registration})


@app.route('/registrations', methods=['GET'])
def get_registrations():
    return jsonify(registrations)


# ------------------ RUN APP ------------------

if __name__ == '__main__':
    app.run(debug=True)