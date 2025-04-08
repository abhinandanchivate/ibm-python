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

### Entity Relationship Diagram (ERD)

1. **Employee - Department:** One-to-Many (One department can have many employees, but an employee belongs to one department.)
2. **Employee - Role:** One-to-Many (One role can be assigned to many employees, but an employee has only one role.)
3. **Employee - Attendance:** One-to-Many (An employee can have multiple attendance entries.)
4. **Department - Project:** One-to-Many (One department can have multiple projects, but a project belongs to one department.)

### REST API Constraints

- **RESTful Principles:**
  - Stateless communication between client and server.
  - Resources identified by URIs (Uniform Resource Identifiers).
  - JSON format used for request and response bodies.

- **HTTP Methods:**
  - `GET`: Retrieve data from the server (e.g., Fetch employee list).
  - `POST`: Submit data to the server (e.g., Add a new employee).
  - `PUT`: Update existing data (e.g., Modify employee details).
  - `DELETE`: Remove data from the server (e.g., Delete an employee record).

- **Response Codes:**
  - `200 OK`: Successful operation.
  - `201 Created`: Successfully created resource.
  - `204 No Content`: Successful deletion or update without a response body.
  - `400 Bad Request`: Invalid request parameters.
  - `401 Unauthorized`: Authentication failure.
  - `403 Forbidden`: Authorization failure.
  - `404 Not Found`: Resource not found.
  - `500 Internal Server Error`: Server-side error.

- **Validation Rules:**
  - Unique constraints on email and department name.
  - Required fields: Employee name, email, phone, role, department.
  - Role permissions must be valid JSON.
  - Attendance status must be one of: `Present`, `Absent`, `Leave`.

- **Security Considerations:**
  - JWT tokens for securing API endpoints.
  - Role-based access control for various functionalities.

### Role-Based Access Control (RBAC)
- **Purpose:** To provide fine-grained control over what different users can access and modify within the system.
- **Implementation:**
  - **Roles Table:** Stores various roles (e.g., Admin, Manager, Employee) with specific permissions.
  - **Permissions:** Defined in JSON format for each role, specifying allowed actions (`create`, `read`, `update`, `delete`) on entities (`Employee`, `Department`, `Project`, `Attendance`).
  - **Middleware:** FastAPI middleware to check user permissions based on JWT token payload.
  - **Frontend Enforcement:** Angular route guards to restrict user interface elements based on roles.

### API Endpoints Listing

#### Employee Endpoints
- `GET /employees` - Retrieve list of all employees.
- `POST /employees` - Add a new employee.
- `GET /employees/{id}` - Retrieve employee details by ID.
- `PUT /employees/{id}` - Update employee details.
- `DELETE /employees/{id}` - Delete an employee.

#### Department Endpoints
- `GET /departments` - Retrieve list of all departments.
- `POST /departments` - Add a new department.
- `GET /departments/{id}` - Retrieve department details by ID.
- `PUT /departments/{id}` - Update department details.
- `DELETE /departments/{id}` - Delete a department.

#### Project Endpoints
- `GET /projects` - Retrieve list of all projects.
- `POST /projects` - Add a new project.
- `GET /projects/{id}` - Retrieve project details by ID.
- `PUT /projects/{id}` - Update project details.
- `DELETE /projects/{id}` - Delete a project.

#### Attendance Endpoints
- `GET /attendance` - Retrieve attendance records.
- `POST /attendance` - Add attendance entry.
- `GET /attendance/{id}` - Retrieve attendance by ID.
- `PUT /attendance/{id}` - Update attendance details.
- `DELETE /attendance/{id}` - Delete attendance record.

#### Role Endpoints
- `GET /roles` - Retrieve list of all roles.
- `POST /roles` - Add a new role.
- `GET /roles/{id}` - Retrieve role details by ID.
- `PUT /roles/{id}` - Update role details.
- `DELETE /roles/{id}` - Delete a role.
