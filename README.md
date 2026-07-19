# 📚 Library Management System

A web-based Library Management System built with **Streamlit** and **MySQL**, allowing librarians to manage members, books, and issued/returned records through a simple, interactive dashboard.

🔗 **Live Demo:** [https://librarymanages.streamlit.app/]

---

## ✨ Features

- **Member Registration** — Register new library members with name, email, and gender (with duplicate email validation)
- **View Registered Members** — Browse all registered members in a searchable table
- **Available Books** — View the full catalog of books available in the library
- **Issue Book** — Issue a book to a member by ID
- **Display All Issued Books** — See a complete list of currently issued books
- **Member's Issued Books** — Look up which books a specific member currently holds
- **Return Book** — Process book returns and update records
- **Access Code Protection** — Simple authentication layer to restrict access to authorized users
- **Secure Cloud Database** — Connects to a managed MySQL instance over SSL with automatic reconnect handling

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | [Streamlit](https://streamlit.io) |
| Backend Language | Python |
| Database | MySQL (hosted on [Aiven](https://aiven.io)) |
| DB Connector | `mysql-connector-python` |
| Environment Config | `python-dotenv` |
| Deployment | Streamlit Community Cloud |

---

## 📂 Project Structure

```
library-management-system/
├── main.py              # Main application file
├── requirements.txt      # Python dependencies
├── ca.pem                 # SSL certificate for secure DB connection
├── .env                    # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation (Local)

### 1. Clone the repository
```bash
git clone https://github.com/nasirbhatti14/Library_Management_System.git
cd Library_Management_System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file in the project root with the following:

```
db_host=your-database-host
db_port=your-database-port
db_username=your-database-username
db_password=your-database-password
db_database=your-database-name
app_password=your-chosen-access-code
```

### 4. Add the SSL certificate
Download your database provider's SSL CA certificate and place it in the project root as `ca.pem`.

### 5. Run the app
```bash
streamlit run main.py
```

---

## ☁️ Deployment

This app is deployed on **Streamlit Community Cloud**. To deploy your own instance:

1. Push the repository to GitHub (`.env` and `ca.pem` handling as per your provider's requirements)
2. Go to [share.streamlit.io](https://share.streamlit.io) and create a new app from your repo
3. Set the **Main file path** to `main.py`
4. Add your credentials under **Advanced settings → Secrets** in TOML format:

```toml
db_host = "your-database-host"
db_port = "your-database-port"
db_username = "your-database-username"
db_password = "your-database-password"
db_database = "your-database-name"
app_password = "your-chosen-access-code"
```

5. Deploy — the app will automatically redeploy on every future push to `main`

---

## 🗄️ Database Schema (Overview)

- **members** — stores registered member details (id, name, email, gender)
- **books** — stores the library's book catalog
- **issued_books** — tracks which books are issued to which members

---

## 🚀 Future Improvements

- Role-based authentication (Admin vs Member accounts)
- Book stock/availability tracking
- Search and filter functionality for members and books
- Due dates and fine calculation for late returns
- Email notifications for issued/due books

---

## 👤 Author

**Nasir Iqbal**
Software Engineering Student | Backend Developer (Python, Django)

- GitHub: https://github.com/nasirbhatti14/
- Portfolio: https://nasir-iqbal.netlify.app/

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
