import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itineary Planner")
st.write("Plan your day trip itineary by emtering your city and interests")

load_dotenv()#we are loading it her also even if it is in  config.py we only give one endpoint to your docker file ,so that your one application will run,if config.py is not running then environment variables will not be able to load environment variables properly(to make it more secure to not face any error)

with st.form("planner_form"):
    city = st.text_input("Enter the city name for your trip")
    interests =st.text_input("Enter your interests (comma-seperated)")
    submitted =st.form_submit_button("Generate itineary")

    if submitted:
        if city and interests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itineary = planner.create_itineary()

            st.subheader("📄 Your Itineary")
            st.markdown(itineary)
        else:
            st.warning("Please fill city and interest to move forward")
