import streamlit as st

st.title("Student Registration Form")

with st.form("student_form"):   
    
    col1, col2 = st.columns(2)

    name1 = col1.text_input("Enter your first name")
    name2 = col2.text_input("Enter your last name")

    email = st.text_input("Enter Email")

    password = st.text_input("Enter your password", type="password")
    confirm_password = st.text_input("Confirm your password", type="password")
    address = st.text_area("Enter your address")
    submit = st.form_submit_button(" Submit")

    if submit:
        if password == confirm_password:
            st.success("Registration Successful ✅")
        else:
            st.error("Passwords do not match ❌")