import streamlit as st
import subprocess 
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO usertable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username = ? AND password = ? ',(username,password))
    conn.commit()
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM usertable')
    data = c.fetchall()
    return data

def main():
    """SIMPLE LOGIN PAGE"""

    st.title("Welcome To Air Fare Recommendation ")
    header = ["Home","Login","Sign Up"]

    choice = st.sidebar.selectbox("Header",header)

    if choice == "Home":
        st.subheader("Home")
    
    elif choice == "Login":
        st.subheader("LOGIN section")
    
        username = st.text_input("User Name")
        password = st.text_input("Password",type='password')

        if st.button("Login"):
            create_usertable()
            result = login_user(username,password)
            if result:
                st.success("Login In as {}".format(username))
               subprocess.Popen(["streamlit", "run", "st.py"])

            else:
                st.warning("Incorrect Password")       
                
    elif choice == "Sign Up":
        st.subheader("SignUp section")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,new_password)
            st.success("You have successfully created valid Account")
            st.info("Go to Login Menu to login")

if __name__ == '__main__':
    main()


   
