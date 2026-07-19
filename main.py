import mysql.connector
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()


@st.cache_resource
def get_connection():

    return mysql.connector.connect(
        host = os.getenv("db_host"),
        user = os.getenv("db_username"),
        port = os.getenv("db_port"),
        password = os.getenv("db_password"),
        database = os.getenv("db_database"),
        ssl_ca = "ca.pem",
        ssl_verify_cert = True
        )
  
conn = get_connection()

try:
    conn.ping(reconnect=True, attempts=3, delay=2)
except:
    st.cache_resource.clear()
    conn = get_connection()

st.title("LIBRARY MANAGEMENT SYSTEM")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.form("login_form"):
        st.info(f"Demo Access Code:  **{os.getenv('app_password')}**")
        password = st.text_input("Enter access code:", type="password")
        login_btn = st.form_submit_button("Login")

    if login_btn:
        if password == os.getenv("app_password"):
            st.session_state.authenticated = True
            st.rerun()   
        else:
            st.error("Incorrect access code. Please try again.")

    st.stop()

password = st.text_input("Enter access code: ", type="password")

if True:

    st.sidebar.title("Library Menu:")
    menu = st.sidebar.selectbox("Menu", ["Member Registration","View all registered members", "Available Books", "Issue Book", "Display all Issued Books", "Member's Issued Books", "Return Book"])
    
    if menu == "Member Registration":
        st.header("Member Registration") 

        m_name = st.text_input("Member's name: ")
        
        m_email = st.text_input("Email: ")
        m_gender = st.radio("Select gender", ["male", "female", "other"])

        cursor3 = conn.cursor(dictionary=True)

        result = None

        if m_email:
            cursor3.execute("select 1 from members where email = %s", (m_email,))
            result = cursor3.fetchone()
                 
            
        with st.form("Register"):
            submitted = st.form_submit_button("Register")

        if submitted:    

            if not m_name or not m_email:
                st.error("Please fill all fields")
            elif result:
                st.error("Email Already Registered, Please try again with new email!")
            else:

                cursor = conn.cursor()
                cursor.execute("Insert into members (name, email, gender) values (%s, %s, %s)",
                       (m_name, m_email, m_gender))
                conn.commit()
                st.success("\n ====== Registeration Succeed! ======")
                cursor.close()
        cursor3.close()




    if menu == "View all registered members":
        st.header("Registered Members")
        cursor7 = conn.cursor(dictionary=True)
        cursor7.execute("select * from members;")
        mem = cursor7.fetchall()
        st.dataframe(mem)
        cursor7.close()
        
        
    if menu == "Available Books":
        st.header("Available Books")
        cursor6 = conn.cursor(dictionary=True)
        cursor6.execute("Select * from books")
        all_books = cursor6.fetchall()
        st.dataframe(all_books)
        cursor6.close()



    if menu == "Issue Book":
        st.header("Issue Book")
        members_id = st.number_input("Member's ID:", min_value=1, step=1)
        books_id = st.number_input("Book ID:", min_value=1, step=1)

        if st.button("Issue"):
            cursor1 = conn.cursor()
            try:
                cursor1.execute("Insert into issued_books (member_id, book_id) values(%s, %s)",
                        (members_id, books_id))
                conn.commit()
                st.success("Book Issued!")
            except mysql.connector.Error as e:
                st.error(e)
            finally:
                cursor1.close()
    

    if menu == "Display all Issued Books":
        st.header("All Issued Books!")
        cursor2 = conn.cursor(dictionary=True)
        cursor2.execute("Select issued_books.member_id, books.Title from issued_books join books on issued_books.book_id = books.id")
        row = cursor2.fetchall()
        st.dataframe(row)
        cursor2.close()


    if menu == "Member's Issued Books":
        st.header("Member's Issued Books!")
        member_id = st.number_input("Member's ID:", min_value=1, step=1)
        cursor4 = conn.cursor(dictionary=True)
        cursor4.execute("select members.name, books.Title, count(*) as Total_books from issued_books join members on issued_books.member_id = members.id join books on issued_books.book_id = books.id where members.id = %s group by members.id, members.name, books.Title, books.id;", (member_id,))

        records = cursor4.fetchall()
        if records:
            st.text(f"Member: {records[0]['name']}")
            for r in records:
                st.success(f"Book: {r['Title']} - {r['Total_books']} copies")
        else:
            st.error("No books issued by this member!")
        cursor4.close()



    if menu == "Return Book":
        st.header("Return Book")
        # member1_id = int(input("Member's Id: "))
        member1_id = st.number_input("Member's ID:", min_value=1, step=1)
        # book1_id = int(input("Book Id: "))
        book1_id = st.number_input("Book ID:", min_value=1, step=1)

        if st.button("Return"):
            cursor5 = conn.cursor()
            cursor5.execute("delete from issued_books where member_id = %s and book_id = %s", (member1_id, book1_id))
            if cursor5.rowcount == 0:
                st.error("No such Issued books record found! ")
            else:
                conn.commit()
                st.success("------ Book Returned! ------\n")
            cursor5.close()
else:
    st.warning("Please enter correct access code")
    st.stop()