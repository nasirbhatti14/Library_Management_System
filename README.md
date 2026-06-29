# 📚 Library Management System

A command-line based Library Management System built with **Python** and **MySQL**. This project demonstrates real-world database operations including member registration, book issuing, and return tracking — all secured with environment variables and parameterized queries.

---

## ✨ Features

- 📋 **Member Registration** — Register new members with name, email, and gender (with duplicate email validation)
- 📖 **Issue Book** — Assign books to registered members
- 📑 **Display All Issued Books** — View a complete list of all currently issued books
- 👤 **Member's Issued Books** — View all books issued to a specific member
- 🔄 **Return Book** — Process book returns and update records
- 🔒 **Secure Credentials** — Database credentials stored in `.env` file, never hardcoded

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3 | Core application logic |
| MySQL | Database storage |
| mysql-connector-python | Python-MySQL connection |
| python-dotenv | Secure environment variable management |

---

## 📁 Project Structure

```
library-management-system/
│
├── main.py               # Main application file
├── .env                  # Environment variables (not pushed to GitHub)
├── .env.example          # Template for environment variables
├── .gitignore            # Ignores .env and other sensitive files
└── README.md             # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/nasirbhatti14/Library_Management_System.git
cd Library_Management_System
```

### 2. Install Dependencies
```bash
pip install mysql-connector-python python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:
```
db_host=localhost
db_username=your_mysql_username
db_password=your_mysql_password
db_database=your_database_name
```

### 4. Set Up the Database

Run the following SQL to create the required tables:

```sql
CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender ENUM('male', 'female', 'other') NOT NULL
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL
);

CREATE TABLE issued_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    book_id INT,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
```

### 5. Run the Application
```bash
python main.py
```

---

## 🖥️ Usage

After running the program, a menu will appear:

```
========== LIBRARY MANAGEMENT SYSTEM ==========

1. Member Registration
2. Issue Book
3. Display all Issued Books
4. Member's Issued Books
5. Return Book
6. Exit
```

Simply enter a number (1–6) to navigate the system.

---

## 🔐 Security

- All database credentials are stored in a `.env` file and loaded via `python-dotenv`
- All SQL queries use **parameterized statements** to prevent SQL injection
- The `.env` file is listed in `.gitignore` — credentials are never pushed to GitHub

---

## 🚀 Future Improvements

- [ ] Add book inventory management (add/remove books)
- [ ] Track issue date and due date for returns
- [ ] Add fine calculation for late returns
- [ ] Export reports to CSV
- [ ] Build a GUI with Tkinter or a web interface with Flask

---

## 👤 Author

**Nasir**
- GitHub: [@nasirbhatti14](https://github.com/nasirbhatti14/Library_Management_System)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).