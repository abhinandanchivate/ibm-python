## Employee Management System - Case Study

### Overview
This case study focuses on building an Employee Management System using **FastAPI** as the backend and **Angular** as the frontend. The system will include five entities, each with at least five attributes. This project will demonstrate CRUD operations, relationships between entities, JWT authentication, and role-based access control (RBAC).

### Technologies Used
- **Backend:** FastAPI (Python), SQLAlchemy, PostgreSQL
- **Frontend:** Angular 18
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Deployment:** Docker, Nginx

### Entities and Attributes

#### 1. Employee
- `id` (Primary Key, Integer)
- `first_name` (String, Required)
- `last_name` (String, Required)
- `email` (String, Required, Unique)
- `phone` (String, Required)
- `department_id` (Foreign Key to Department)
- `role_id` (Foreign Key to Role)

#### 2. Department
- `id` (Primary Key, Integer)
- `name` (String, Required, Unique)
- `location` (String, Required)
- `description` (String)
- `manager_id` (Foreign Key to Employee)

#### 3. Project
- `id` (Primary Key, Integer)
- `name` (String, Required, Unique)
- `description` (String)
- `start_date` (Date, Required)
- `end_date` (Date)
- `department_id` (Foreign Key to Department)

#### 4. Attendance
- `id` (Primary Key, Integer)
- `employee_id` (Foreign Key to Employee)
- `date` (Date, Required)
- `status` (String, Required - Present, Absent, Leave)
- `remarks` (String)

#### 5. Role
- `id` (Primary Key, Integer)
- `name` (String, Required, Unique)
- `description` (String)
- `permissions` (String, JSON format)
- `created_at` (DateTime, Auto-generated)
- `updated_at` (DateTime, Auto-generated)

### Database Structure Definitions

#### Employee Table
```sql
CREATE TABLE Employee (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) NOT NULL,
    department_id INTEGER REFERENCES Department(id),
    role_id INTEGER REFERENCES Role(id)
);
```

#### Department Table
```sql
CREATE TABLE Department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    location VARCHAR(100) NOT NULL,
    description TEXT,
    manager_id INTEGER REFERENCES Employee(id)
);
```

#### Project Table
```sql
CREATE TABLE Project (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    department_id INTEGER REFERENCES Department(id)
);
```

#### Attendance Table
```sql
CREATE TABLE Attendance (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES Employee(id),
    date DATE NOT NULL,
    status VARCHAR(10) NOT NULL,
    remarks TEXT
);
```

#### Role Table
```sql
CREATE TABLE Role (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    permissions JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Entity Relationship Diagram (ERD)

1. **Employee - Department:** One-to-Many (One department can have many employees, but an employee belongs to one department.)
2. **Employee - Role:** One-to-Many (One role can be assigned to many employees, but an employee has only one role.)
3. **Employee - Attendance:** One-to-Many (An employee can have multiple attendance entries.)
4. **Department - Project:** One-to-Many (One department can have multiple projects, but a project belongs to one department.)

### Summary
This case study now includes detailed database structure definitions for each entity. Let me know if you need more additions or improvements.

