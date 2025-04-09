Ecommerce database schema with 5 entities (each with 5 attributes) and a list of questions based on CREATE TABLE, ALTER TABLE, INSERT, UPDATE, and DELETE operations:

📦 Entities with Attributes
Customers

customer_id (INT, Primary Key)

name (VARCHAR)

email (VARCHAR)

phone (VARCHAR)

address (TEXT)

Products

product_id (INT, Primary Key)

product_name (VARCHAR)

description (TEXT)

price (DECIMAL)

stock_quantity (INT)

Orders

order_id (INT, Primary Key)

customer_id (INT, Foreign Key)

order_date (DATE)

total_amount (DECIMAL)

status (VARCHAR)

OrderItems

order_item_id (INT, Primary Key)

order_id (INT, Foreign Key)

product_id (INT, Foreign Key)

quantity (INT)

item_price (DECIMAL)

Payments

payment_id (INT, Primary Key)

order_id (INT, Foreign Key)

payment_method (VARCHAR)

payment_date (DATE)

amount_paid (DECIMAL)

📝 SQL Practice Questions
✅ Create Table
Write a SQL statement to create the Customers table with appropriate data types and primary key.

Create the Products table with a constraint on price to be greater than 0.

Create the Orders table with a foreign key reference to the Customers table.

Create the OrderItems table with foreign keys referencing both Orders and Products.

Create the Payments table with a foreign key to Orders.

🔧 Alter Table
Add a new column zipcode to the Customers table.

Modify the column phone in Customers to increase its length.

Drop the column description from the Products table.

Add a unique constraint to email in the Customers table.

Rename the column amount_paid to paid_amount in the Payments table.

📥 Insert Data
Insert a new customer into the Customers table.

Add a new product into the Products table.

Insert an order with values into the Orders table for a given customer.

Add an item into the OrderItems table for a given order.

Insert a payment for an existing order using Payments.

✏️ Update Data
Update the stock quantity of a product after an order is placed.

Change the email address of a customer.

Update the order status to "Shipped" for a given order ID.

Increase the product price by 10% for all products below a certain price.

Update the payment method for a specific payment ID.

❌ Delete Data
Delete a customer by customer_id.

Delete a product from the catalog by product_id.

Remove an order and all its associated order items using cascading.

Delete payments made before a certain date.

Delete all products that are out of stock (i.e., stock_quantity = 0).
