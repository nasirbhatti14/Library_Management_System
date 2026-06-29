import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host = os.getenv("db_host"),
    user = os.getenv("db_username"),
    password = os.getenv("db_password"),
    database = os.getenv("db_database")
)


while True:
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("\n1. Member Registration")
    print("2. Issue Book")
    print("3. Display all Issued Books")
    print("4. Member's Issued Books")
    print("5. Return Book")
    print("6. Exit\n")

    try:
        user = int(input("Choose option: "))
    except ValueError:
        print("Enter valid number 1 - 6")
        continue

    

    if user == 1:
        m_name = input("Member's name: ")

        
        while True:
            m_email = input("Email: ")
            cursor3 = conn.cursor(dictionary=True)
            cursor3.execute("select 1 from members where email = %s", (m_email,))
            result = cursor3.fetchone()
            cursor3.close()
            if result:
                print("Email Already Registered, Please try again with new email!")
                
            else:
                break
            


        while True:
            m_gender = input("Gender(male / female / other): ").strip().lower()
            if m_gender in ["male", "female", "other"]:
                break
            print("Invalid gender! Please enter Male/Female/Other")
        
        cursor = conn.cursor()
        cursor.execute("Insert into members (name, email, gender) values (%s, %s, %s)",
                       (m_name, m_email, m_gender))
        conn.commit()
        print("\n ====== Registeration Succeed! ======")
        cursor.close()


    elif user == 2:
        members_id = int(input("Member's Id: "))
        books_id = int(input("Book's Id "))
        cursor1 = conn.cursor()
        cursor1.execute("Insert into issued_books (member_id, book_id) values(%s, %s)",
                        (members_id, books_id))
        conn.commit()
        print("\n ====== Book Issued! ======")
        cursor1.close()

    elif user == 3:
        print("\n         ====== All Issued Books! ======\n")
        cursor2 = conn.cursor(dictionary=True)
        cursor2.execute("Select issued_books.id, books.Title from issued_books join books on issued_books.book_id = books.id")
        for row in cursor2:
            print(f"{row['id']}. {row['Title']}")
        cursor2.close()


    elif user == 4:
        print("\n         ====== Member's Issued Books! ======\n")
        member_id = int(input("Member's Id: "))
        cursor4 = conn.cursor(dictionary=True)
        cursor4.execute("select members.name, books.Title, count(*) as Total_books from issued_books join members on issued_books.member_id = members.id join books on issued_books.book_id = books.id where members.id = %s group by members.id, members.name, books.Title, books.id;", (member_id,))

        records = cursor4.fetchall()
        if records:
            print(f"\nMembers: {records[0]['name']}")
            for r in records:
                print(f"{r['Title']} - {r['Total_books']} copies")
        else:
            print("No books issued by this member!")
        cursor4.close()



    elif user == 5:
        print("\n         ====== Return Book ======\n")
        member1_id = int(input("Member's Id: "))
        book1_id = int(input("Book Id: "))

        cursor5 = conn.cursor()
        cursor5.execute("delete from issued_books where member_id = %s and book_id = %s", (member1_id, book1_id))
        if cursor5.rowcount == 0:
            print("No such Issued books record found! ")
        else:
            conn.commit()
            print("------ Book Returned! ------\n")
        cursor5.close()

    elif user == 6:
        print(" ------ Program Exit ------")
        conn.close()
        break



