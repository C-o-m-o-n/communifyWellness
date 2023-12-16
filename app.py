# app.py
import streamlit as st

def create_challenge():
    st.header("Create a New Challenge")

    # Form inputs
    challenge_name = st.text_input("Challenge Name")
    duration_days = st.number_input("Duration (in days)", min_value=1, value=7)
    goal_description = st.text_area("Challenge Goal Description")

    # Button to create the challenge
    if st.button("Create Challenge"):
        # Process the form data (you can save it to a database, etc.)
        st.success(f"Challenge '{challenge_name}' created successfully!")

def main():
    st.title("Wellness Challenge Community Platform")

    # Sidebar navigation
    menu_choice = st.sidebar.radio("Select a Page", ["Create Challenge", "User Participation", "Dashboard"])

    # Display the selected page
    if menu_choice == "Create Challenge":
        create_challenge()
    elif menu_choice == "User Participation":
        st.write("User Participation Page (To be implemented)")
    elif menu_choice == "Dashboard":
        st.write("Dashboard Page (To be implemented)")

if __name__ == "__main__":
    main()
