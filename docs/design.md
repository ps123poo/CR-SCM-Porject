# Course Registration System – Design

## 1. System Architecture

The system follows a Client-Server architecture:

Client (Postman/Browser)
        |
        v
     Flask Server
        |
        v
      SQLite Database

---

## 2. Database Design

### Table: students

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER | Primary Key |
| name | TEXT | Student name |

---

### Table: courses

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER | Primary Key |
| name | TEXT | Course name |

---

### Table: registrations

| Field | Type | Description |
|-------|------|-------------|
| id | INTEGER | Primary Key |
| student_id | INTEGER | Foreign Key (students) |
| course_id | INTEGER | Foreign Key (courses) |

---

## 3. API Design

| Endpoint | Method | Description |
|----------|--------|-------------|
| /students | POST | Add student |
| /students | GET | View students |
| /courses | GET | View courses |
| /register | POST | Register course |
| /registrations | GET | View registrations |

---

## 4. Data Flow

1. User sends request to Flask API.
2. Flask processes request.
3. Data is stored/retrieved from SQLite.
4. Flask sends JSON response to user.