 **Ecommerce database schema** with 5 entities (each with 5 attributes) and a list of **questions** based on `CREATE TABLE`, `ALTER TABLE`, `INSERT`, `UPDATE`, and `DELETE` operations:

---

### 📦 Entities with Attributes

1. **Customers**
   - `customer_id` (INT, Primary Key)
   - `name` (VARCHAR)
   - `email` (VARCHAR)
   - `phone` (VARCHAR)
   - `address` (TEXT)

2. **Products**
   - `product_id` (INT, Primary Key)
   - `product_name` (VARCHAR)
   - `description` (TEXT)
   - `price` (DECIMAL)
   - `stock_quantity` (INT)

3. **Orders**
   - `order_id` (INT, Primary Key)
   - `customer_id` (INT, Foreign Key)
   - `order_date` (DATE)
   - `total_amount` (DECIMAL)
   - `status` (VARCHAR)

4. **OrderItems**
   - `order_item_id` (INT, Primary Key)
   - `order_id` (INT, Foreign Key)
   - `product_id` (INT, Foreign Key)
   - `quantity` (INT)
   - `item_price` (DECIMAL)

5. **Payments**
   - `payment_id` (INT, Primary Key)
   - `order_id` (INT, Foreign Key)
   - `payment_method` (VARCHAR)
   - `payment_date` (DATE)
   - `amount_paid` (DECIMAL)

---

### 📝 SQL Practice Questions

#### ✅ **Create Table**
1. Write a SQL statement to create the `Customers` table with appropriate data types and primary key.
2. Create the `Products` table with a constraint on `price` to be greater than 0.
3. Create the `Orders` table with a foreign key reference to the `Customers` table.
4. Create the `OrderItems` table with foreign keys referencing both `Orders` and `Products`.
5. Create the `Payments` table with a foreign key to `Orders`.

#### 🔧 **Alter Table**
6. Add a new column `zipcode` to the `Customers` table.
7. Modify the column `phone` in `Customers` to increase its length.
8. Drop the column `description` from the `Products` table.
9. Add a unique constraint to `email` in the `Customers` table.
10. Rename the column `amount_paid` to `paid_amount` in the `Payments` table.

#### 📥 **Insert Data**
11. Insert a new customer into the `Customers` table.
12. Add a new product into the `Products` table.
13. Insert an order with values into the `Orders` table for a given customer.
14. Add an item into the `OrderItems` table for a given order.
15. Insert a payment for an existing order using `Payments`.

#### ✏️ **Update Data**
16. Update the stock quantity of a product after an order is placed.
17. Change the email address of a customer.
18. Update the order status to "Shipped" for a given order ID.
19. Increase the product price by 10% for all products below a certain price.
20. Update the payment method for a specific payment ID.

#### ❌ **Delete Data**
21. Delete a customer by customer_id.
22. Delete a product from the catalog by product_id.
23. Remove an order and all its associated order items using cascading.
24. Delete payments made before a certain date.
25. Delete all products that are out of stock (i.e., stock_quantity = 0).

---
