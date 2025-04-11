 Query-Based on JOINs & Subqueries (20 Questions)**

---

**1. What does the following query return?**  
```sql
SELECT e.name, d.name 
FROM Employees e 
JOIN Departments d ON e.department_id = d.id;
```  
A) All employees, regardless of department  
B) All departments and their managers  
C) Employees with their department names  
D) Departments with employee counts  

---

**2. What type of JOIN is used in the following query?**  
```sql
SELECT * 
FROM Orders o 
LEFT JOIN Customers c ON o.customer_id = c.id;
```  
A) INNER JOIN  
B) RIGHT JOIN  
C) FULL JOIN  
D) LEFT JOIN  

---

**3. Identify the correct output of the below SQL:**  
```sql
SELECT e.name 
FROM Employees e 
WHERE e.salary > (SELECT AVG(salary) FROM Employees);
```  
A) Employees earning below average  
B) All employees  
C) Employees earning above average  
D) Employees earning the exact average  

---

**4. What does the query below retrieve?**  
```sql
SELECT name 
FROM Students 
WHERE id NOT IN (SELECT student_id FROM Attendance);
```  
A) Students who have perfect attendance  
B) Students who were absent at least once  
C) Students never marked in attendance  
D) All students with attendance  

---

**5. What kind of subquery is used here?**  
```sql
SELECT * 
FROM Products 
WHERE price = (SELECT MAX(price) FROM Products);
```  
A) Correlated  
B) Scalar  
C) Inline  
D) EXISTS  

---

**6. What is the output of this JOIN operation?**  
```sql
SELECT s.name, c.course_name 
FROM Students s 
JOIN Enrollments e ON s.id = e.student_id 
JOIN Courses c ON e.course_id = c.id;
```  
A) Students not enrolled in courses  
B) All students and their courses  
C) Students and all available courses  
D) Courses with no students  

---

**7. What does the query return?**  
```sql
SELECT * 
FROM Employees e 
WHERE EXISTS (
    SELECT 1 FROM Projects p WHERE p.manager_id = e.id
);
```  
A) All employees  
B) Employees who manage at least one project  
C) Employees without any project  
D) Employees assigned as interns  

---

**8. How many rows will a `CROSS JOIN` return between two tables with 5 and 4 rows?**  
A) 5  
B) 4  
C) 9  
D) 20  

---

**9. What’s the purpose of this query?**  
```sql
SELECT name 
FROM Customers 
WHERE id IN (
    SELECT customer_id 
    FROM Orders 
    WHERE order_date >= '2024-01-01'
);
```  
A) Customers with orders before 2024  
B) Customers with orders in 2024 or later  
C) Customers without orders  
D) All customers  

---

**10. Which JOIN type is used to find unmatched records?**  
```sql
SELECT a.id 
FROM TableA a 
LEFT JOIN TableB b ON a.id = b.a_id 
WHERE b.a_id IS NULL;
```  
A) INNER JOIN  
B) RIGHT JOIN  
C) LEFT JOIN  
D) FULL OUTER JOIN  

---

**11. What is the purpose of this SQL?**  
```sql
SELECT d.name, COUNT(e.id) 
FROM Departments d 
LEFT JOIN Employees e ON d.id = e.department_id 
GROUP BY d.name;
```  
A) Employees in each department  
B) Only non-empty departments  
C) All departments with employee counts (including 0)  
D) Department names only  

---

**12. What does this correlated subquery achieve?**  
```sql
SELECT name 
FROM Students s 
WHERE grade > (
    SELECT AVG(grade) FROM Students WHERE class = s.class
);
```  
A) Students with grade above school average  
B) Students with grade below average  
C) Students with grade above their class average  
D) All students  

---

**13. What will be the result?**  
```sql
SELECT e.name 
FROM Employees e 
WHERE e.id NOT IN (
    SELECT manager_id FROM Departments WHERE manager_id IS NOT NULL
);
```  
A) All employees  
B) Employees who are also managers  
C) Employees who are not managers  
D) Employees managing 2+ departments  

---

**14. What kind of result is expected here?**  
```sql
SELECT c.name 
FROM Customers c 
FULL JOIN Orders o ON c.id = o.customer_id 
WHERE o.id IS NULL;
```  
A) Customers who placed orders  
B) Customers without any order  
C) Orders without customers  
D) Orders made in 2024  

---

**15. Identify the best JOIN to use: “List employees who have not submitted attendance.”**  
A) INNER JOIN  
B) RIGHT JOIN  
C) LEFT JOIN with `WHERE attendance.id IS NULL`  
D) FULL JOIN  

---

**16. Which query gives the department(s) with the maximum number of employees?**  
A) Subquery with MAX  
B) JOIN with WHERE clause  
C) GROUP BY with ORDER BY LIMIT 1  
D) SELECT DISTINCT  

---

**17. What does the subquery do here?**  
```sql
SELECT name 
FROM Employees 
WHERE department_id = (
    SELECT id FROM Departments WHERE name = 'IT'
);
```  
A) Finds department name for all employees  
B) Lists employees in IT department  
C) Deletes employees from IT  
D) Updates IT employee names  

---

**18. What will this query do?**  
```sql
SELECT name 
FROM Products 
WHERE category_id IN (
    SELECT id FROM Categories WHERE type = 'Electronics'
);
```  
A) Products in all categories  
B) Products in Electronics category  
C) Products with NULL category  
D) Category names  

---

**19. How would you list employees with a salary above the average salary of their own department?**  
A) Use EXISTS  
B) Use JOIN  
C) Use Correlated Subquery  
D) Use GROUP BY only  

---

**20. What’s the output of this subquery-based query?**  
```sql
SELECT * 
FROM Orders 
WHERE amount > ALL (
    SELECT amount FROM Orders WHERE customer_id = 101
);
```  
A) Orders less than customer 101  
B) Orders equal to customer 101  
C) Orders more than all of customer 101’s orders  
D) Orders made by customer 101  

---

