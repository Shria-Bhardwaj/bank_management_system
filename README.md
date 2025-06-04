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
- [👨‍💻 Author](#-author)
- [🪪 License](#-license)
- [🌟 Feedback](#-feedback)

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
