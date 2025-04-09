
---

### 🔹 **Basic SELECT Queries**
1. Retrieve all employees with their department names.
2. List all projects along with the department name they belong to.
3. Find all employees working in the "IT" department.
4. Display names and emails of all employees with the role of 'Manager'.
5. List all attendance records for 'John Doe'.
6. Get a list of departments along with their manager's full name.
7. Retrieve all roles and their permission levels.
8. Find the number of employees in each department.
9. List all employees who were absent on ‘2025-04-07’.
10. Show the start and end dates for all projects.

---

### 🔹 **JOINs and Multi-Table Queries**
11. Get all employee details along with role name and permissions.
12. Show employee details with project name (based on department mapping).
13. List attendance with employee names and their department.
14. Get department name, manager name, and number of employees.
15. Retrieve employee details where department manager is not assigned (manager_id is null).
16. Find which employees have not been assigned a role.
17. List projects and their respective department manager names.
18. List each role and how many employees have that role.
19. Get employee name, role name, and the department they belong to.
20. Show employee names with their attendance status and remarks on ‘2025-04-07’.

---

### 🔹 **Aggregations and Grouping**
21. Count number of departments in each location.
22. Find total number of employees in the organization.
23. Count how many employees were present on ‘2025-04-07’.
24. Get the average number of employees per department.
25. Find department with the maximum number of projects.
26. List how many employees have each role.
27. Count how many times each attendance status was recorded.
28. Show number of employees in departments located in 'London'.
29. Count the number of projects that started in April 2025.
30. Find the department with the least employees.

---

### 🔹 **Subqueries and Nested Queries**
31. Find employees who belong to the department with the most employees.
32. Get the names of employees who do not appear in the Attendance table.
33. List departments where no projects are currently assigned.
34. Retrieve employees whose role has all permissions set to true.
35. Find the second highest number of employees in a department.
36. Get employees who are managers of a department.
37. Retrieve roles assigned to more than one employee.
38. List the department(s) whose manager is also an employee in the same department.
39. List departments that have more than one project.
40. Find employees working on projects that end after September 2025.

---

### 🔹 **Data Manipulation (DML) and Constraints**
41. Insert a new employee and assign them to the ‘Finance’ department and ‘Employee’ role.
42. Update a manager for a department that has no manager.
43. Delete an employee and ensure cascading effects (how would you design this?).
44. Add a constraint to ensure `status` in Attendance can only be 'Present', 'Absent', or 'WFH'.
45. Change the phone number of an employee by ID.
46. Insert a new project under the 'HR' department with today’s date as start date.
47. Update the description of the ‘Admin’ role.
48. Add a new permission field to all existing role permissions (`"export": true`).
49. Delete all attendance records older than a specific date.
50. Add an employee and assign them as the manager of the 'IT' department.

---

