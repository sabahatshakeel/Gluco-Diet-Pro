import streamlit as st
import anthropic


api_key = st.secrets["claude_api_key"]

def get_meal_plan(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences):
    client = anthropic.Anthropic(api_key=api_key)

    prompt = (
        f"My fasting sugar level is {fasting_sugar} mg/dL"
        f"my pre-meal sugar level is {pre_meal_sugar} mg/dL"
        f"and my post-meal sugar level is {post_meal_sugar} mg/dL"
        f"My dietary preferences are {dietary_preferences} mg/dL"
    )

    message = client.messages.create(
        model= "claude-3-5-sonnet-20240620",
        max_tokens= 500,
        temperature= 0.7,
        system="You are a world-class nutritionist who spescalizes in diabetes managment.",
        messages= [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    raw_context = message.content
    itinerary = raw_context[0].text
    return itinerary

st.title("GlucoGuide")
st.write('Welcome to **GlucoGuide** your personal assistant in managing diabetes with tailored meal plans. Whether you are trying to keep your sugar levels in check or simply seeking healthier dietary choices, GlucoGuide is here to help. By providing your blood sugar levels and dietary preferences, you will receive a personalized meal plan designed to keep your glucose levels')

st.sidebar.header("Enter Your Details")

fasting_sugar = st.sidebar.number_input("Fasting Sugar Level (mg/dL)", min_value=0, max_value=500, step= 1)
pre_meal_sugar = st.sidebar.number_input("Pre-meal Sugar Level (mg/dL)", min_value=0, max_value=500, step= 1)
post_meal_sugar = st.sidebar.number_input("Post-meal Sugar Level (mg/dL)", min_value=0, max_value=500, step= 1)

dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., Vegetarian, Low-carb, etc.)")


if st.sidebar.button("Generate Meal Plan"):
    meal_plan = get_meal_plan(api_key, fasting_sugar, pre_meal_sugar, post_meal_sugar, dietary_preferences)
    st.write("Based on your sugar levels and dietry preferences, here is a personalized meal plan")
    st.markdown(meal_plan)








