<h1 align="center">🏦 Bank Management System 🧮</h1>

<p align="center">
  A simple yet effective command-line banking solution powered by Python and MySQL.<br>
  ✨ Create accounts, manage balances, and securely store everything in a database.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Database-MySQL-blue?style=for-the-badge&logo=mysql">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge&logo=checkmarx">
</p>

---

## 📖 Table of Contents
- [📌 Overview](#-overview)
- [🧰 Tech Stack](#-tech-stack)
- [🚀 Features](#-features)
- [📦 Installation & Setup](#-installation--setup)
- [🧪 Usage Guide](#-usage-guide)
- [💾 Data Persistence](#-data-persistence)
- [📸 Screenshots](#-screenshots)
---

## 📌 Overview
The **Bank Management System** is a menu-driven command-line application built with Python that lets users  
- ✅ Create new accounts with random account numbers  
- 💰 Deposit and withdraw money  
- 🗑️ Delete accounts with confirmation  
- 💾 Persist data to **MySQL** on exit  

Perfect for practicing CRUD operations, database interaction, and menu-based apps.

---

## 🧰 Tech Stack

| Component | Technology |
|-----------|------------|
| Language  | Python 3.x 🐍 |
| Database  | MySQL 🐬 |
| Libraries | `mysql-connector-python`, `random` |

---

## 🚀 Features
- 🔐 Unique 6-digit account numbers on creation  
- 🧾 Secure login using username + account number  
- 💳 Deposit & withdraw with balance validation  
- ❌ Account deletion with double-check prompt  
- 🔄 Auto-save all data to MySQL when exiting  
- 📋 Clean, interactive menu interface  

---

## 📦 Installation & Setup

### 🔧 MySQL Setup
1. Start MySQL server.  
2. Execute:  
   ~~~sql
   CREATE DATABASE bankdb;
   USE bankdb;

   CREATE TABLE accounts (
     acc_no   VARCHAR(10),
     username VARCHAR(100),
     balance  INT
   );
   ~~~

### 🐍 Python Setup
1. Clone the repo  
   ~~~bash
   git clone https://github.com/your-username/bank-management-system.git
   cd bank-management-system
   ~~~
2. Install dependency  
   ~~~bash
   pip install mysql-connector-python
   ~~~
3. Run the app  
   ~~~bash
   python bank.py
   ~~~

---

## 🧪 Usage Guide
--- Bank Management System ---
1. Create Account
2. Existing User Login
3. Exit and Save to MySQL

## 💾 Data Persistence
Uses **parameterized queries** for security:
~~~python
cursor.execute(
    "INSERT INTO accounts (acc_no, username, balance) VALUES (%s, %s, %s)",
    (acct_no, data["username"], data["balance"])
)
~~~
On exit, the script commits every in-memory account to `bankdb.accounts`.

---

## 📸 Screenshots
# 1. Importing files and database connectivity
![1](https://github.com/user-attachments/assets/865f622b-0a8a-46f7-92a7-b3716036e864)

# 2. Saving user input in sql database
![2](https://github.com/user-attachments/assets/e82d3177-04c8-4b36-b828-c44784cf65e1)

# 3. Main menu
![3](https://github.com/user-attachments/assets/a355a058-a937-4955-8b1b-0541ac071ea7)

![7](https://github.com/user-attachments/assets/884eaa1f-1596-4975-91fa-cb2509c0e504)

![8](https://github.com/user-attachments/assets/8fde588b-ddcd-421a-9ce8-459e32ce5296)

# 4. Transaction menu 
![4](https://github.com/user-attachments/assets/e90fbde5-ced7-4054-8a6f-432b07de547c)

![9](https://github.com/user-attachments/assets/29c22574-02c6-45e0-9fc0-a097b4dfedbe)


# 5. Verify/ Deposit/ Withdraw/ Save and exit
![5](https://github.com/user-attachments/assets/88155ef2-abcb-4df3-b423-3f29eec9bcbb)

![6](https://github.com/user-attachments/assets/ed987927-47d2-435e-9690-ef9afb70aed3)

![11](https://github.com/user-attachments/assets/7a88cc94-eca3-4238-a77e-276c64d75da6)

![10](https://github.com/user-attachments/assets/5f9ccb9d-ff93-4e10-9ae5-c19113bdac4e)




