 **Banking SQL Practice Questions** categorized by operation:

---

## 🏦 **Entities and Attributes**
1. **Customers**
   - `customer_id` (INT, Primary Key)
   - `name` (VARCHAR)
   - `email` (VARCHAR)
   - `phone` (VARCHAR)
   - `address` (TEXT)

2. **Accounts**
   - `account_id` (INT, Primary Key)
   - `customer_id` (INT, Foreign Key)
   - `account_type` (VARCHAR)
   - `balance` (DECIMAL)
   - `created_date` (DATE)

3. **Transactions**
   - `transaction_id` (INT, Primary Key)
   - `account_id` (INT, Foreign Key)
   - `amount` (DECIMAL)
   - `transaction_type` (VARCHAR)
   - `transaction_date` (DATE)

4. **Loans**
   - `loan_id` (INT, Primary Key)
   - `customer_id` (INT, Foreign Key)
   - `loan_type` (VARCHAR)
   - `amount` (DECIMAL)
   - `loan_status` (VARCHAR)

5. **Cards**
   - `card_id` (INT, Primary Key)
   - `customer_id` (INT, Foreign Key)
   - `card_type` (VARCHAR)
   - `card_limit` (DECIMAL)
   - `expiry_date` (DATE)

---

## ✅ **Create Table Questions**
1. Create the `Customers` table with customer_id, name, email, phone, and address.
2. Create the `Accounts` table with account_id, customer_id, account_type, balance, and created_date.
3. Create the `Transactions` table with transaction_id, account_id, amount, transaction_type, and transaction_date.
4. Create the `Loans` table with loan_id, customer_id, loan_type, amount, and loan_status.
5. Create the `Cards` table with card_id, customer_id, card_type, card_limit, and expiry_date.

---

## 🔧 **Alter Table Questions**
6. Add a new column `branch_name` to the `Accounts` table.
7. Modify the `balance` column in `Accounts` to increase its precision.
8. Drop the column `loan_status` from the `Loans` table.
9. Add a unique constraint to the `card_id` in the `Cards` table.
10. Rename the column `account_type` to `acc_type` in the `Accounts` table.

---

## 📥 **Insert Data Questions**
11. Insert a new customer into the `Customers` table.
12. Insert a new account for an existing customer.
13. Add a new transaction into the `Transactions` table.
14. Insert a loan record into the `Loans` table.
15. Issue a new card for a customer in the `Cards` table.

---

## ✏️ **Update Data Questions**
16. Update the balance of an account after a transaction.
17. Change the phone number of a customer.
18. Update the loan amount for a specific loan ID.
19. Increase the card limit for premium cardholders.
20. Update the account type from 'Saving' to 'Current' for specific customers.

---

## ❌ **Delete Data Questions**
21. Delete a customer record by customer_id.
22. Delete an account by account_id.
23. Delete all transactions older than a specific date.
24. Remove loan records with status 'Closed'.
25. Delete cards that have expired.

---

