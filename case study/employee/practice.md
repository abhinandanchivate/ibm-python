**case study on an eCommerce database system**, including:

1. **Schema overview with 5 entities**
2. **15 SQL-based questions**, categorized:
   - 5 questions on `CREATE TABLE` and `ALTER TABLE`
   - 5 questions on `INSERT`, `UPDATE`, `DELETE`
   - 5 questions on `JOIN`, `SELECT`, `subqueries`

---

### 📘 **Case Study: eCommerce Database System**

Your eCommerce system manages:

| Entity        | Attributes                                                                 |
|---------------|----------------------------------------------------------------------------|
| Customer      | `id`, `name`, `email`, `phone`, `address`, `created_at`                   |
| Product       | `id`, `name`, `description`, `price`, `stock`, `category`                 |
| Order         | `id`, `customer_id`, `order_date`, `status`, `total_amount`               |
| OrderItem     | `id`, `order_id`, `product_id`, `quantity`, `unit_price`                  |
| Payment       | `id`, `order_id`, `payment_mode`, `amount_paid`, `payment_status`, `paid_on` |

#### 🗂 Relationships:
- A **Customer** can place multiple **Orders**
- An **Order** can have multiple **OrderItems**
- **OrderItem** maps a **Product** to an **Order**
- **Payment** is made **per Order**

---

### 🧠 **15 SQL Questions**

#### 🧱 Category 1: CREATE and ALTER Table (5 questions)

1. **Create a table for `Customer`** with primary key and a `created_at` timestamp.
2. **Create a table for `Product`** and add a check constraint to ensure price > 0.
3. **Create a table for `OrderItem`** with foreign keys referencing `Order` and `Product`.
4. **Alter the `Customer` table** to add a column `loyalty_points INT DEFAULT 0`.
5. **Alter the `Product` table** to rename the column `category` to `product_category`.

---

#### ✍️ Category 2: INSERT, UPDATE, DELETE (5 questions)

6. Insert a new product into the `Product` table with sample data.
7. Update the stock of a product after an order is placed.
8. Delete an order and cascade delete corresponding `OrderItems`.
9. Insert a payment record linked to a particular order.
10. Update the status of a customer’s order from 'Pending' to 'Shipped'.

---

#### 🔍 Category 3: SELECT, JOIN, Subqueries (5 questions)

11. Get the list of all orders with the customer name and order total.
12. List all products that are out of stock (stock = 0).
13. Find all customers who haven’t placed any orders yet.
14. Get top 3 customers who have spent the most money (based on total payments).
15. Get the details of the highest value order (max total_amount).

---
