 **Health Care Case Study**
---

### 🔍 **Case Study Title**: *Hospital Management System (Mini Version)*

#### 📊 **Entities:**

---

### 🏥 Entity 1: **Patient**
| Attribute Name | Data Type      | Description                        |
|----------------|----------------|------------------------------------|
| patient_id     | INT PRIMARY KEY| Unique ID for each patient         |
| name           | VARCHAR(100)   | Full name of the patient           |
| gender         | VARCHAR(10)    | Gender of the patient              |
| date_of_birth  | DATE           | Date of birth                      |
| contact_number | VARCHAR(15)    | Contact number                     |

---

### 🧑‍⚕️ Entity 2: **Appointment**
| Attribute Name   | Data Type      | Description                             |
|------------------|----------------|-----------------------------------------|
| appointment_id   | INT PRIMARY KEY| Unique appointment ID                   |
| patient_id       | INT            | Foreign key linking to Patient          |
| doctor_name      | VARCHAR(100)   | Name of the consulting doctor           |
| appointment_date | DATE           | Date of the appointment                 |
| department       | VARCHAR(50)    | Department (e.g., Cardiology, ENT)      |

---

### 🧾 **SQL Table DDL**

```sql


CREATE TABLE Appointment (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_name VARCHAR(100),
    appointment_date DATE,
    department VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
);
```

---

### ✅ **15 SQL-Based Questions**

#### 📌 *DDL & DML (5 Questions)*

1. **Create** a table for Patient with constraints.
2. **Alter** the Appointment table to add a new column `status VARCHAR(20)`.
3. **Insert** sample data into both tables for 5 patients and 5 appointments.
4. **Update** the department of an appointment where appointment_id = 2 to 'Neurology'.
5. **Delete** the patient whose `name = 'John Doe'`.

---

#### 📌 *SELECT & JOIN (5 Questions)*

6. Retrieve all patient names along with their appointment date and doctor name.
7. List all patients who have appointments in the 'Cardiology' department.
8. Get patient details who have an appointment with doctor 'Dr. Smith'.
9. Display appointment details where the patient's age is greater than 60.
10. Find patients who have more than one appointment (use GROUP BY and HAVING).

---

#### 📌 *SUBQUERY & FUNCTIONS (5 Questions)*

11. Find the patient(s) who have the most number of appointments.
12. List patients who do **not** have any appointments.
13. Show the name and age of all patients (calculate age from `date_of_birth`).
14. List appointments made in the **last 30 days** from today’s date.
15. Count the number of appointments per department.

---
Sure! Here are the **6 tough SQL questions (only the questions)** based on the Health Care case study:

---

### 🧠 ** SQL Questions (Only 5 Questions)**

1. **Find the name(s) of patient(s) who have taken appointments in all departments available in the Appointment table.**

2. **Retrieve the patient(s) who had their first-ever appointment with doctor 'Dr. Smith'.**

3. **Find the doctors who have consulted at least 3 different patients across more than one department.**

4. **Identify patients who had appointments in the last week of each month for the past 3 months.**

5. **List the top 3 patients who have had the highest number of appointments.**

6. **Detect patients who had a gap of more than 60 days between any two of their consecutive appointments.**

---


