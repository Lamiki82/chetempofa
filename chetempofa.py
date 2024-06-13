import streamlit as st 
import pandas as pd


st.title('C h e t e m p o f a')
st.write('Quale città vuoi esplorare?')
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2023/08/06/18/37/sunset-8173575_1280.jpg");
            background-attachment: fixed;
            background-size: cover;
            color: white; /* Colore del testo principale */
        }}
        h1 {{
            color: white; /* Colore dei titoli h1 */
        }}
        p {{
            color: lightblue; /* Colore dei paragrafi */
        }}
        a {{
            color: red; /* Colore dei link */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

city_name= st.text_input('inserire città')
import requests

if city_name:
    API_key ='a6878e89c0a397b5639a277635dc225c'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result= requests.get(url)
    json=result.json()
    temperature = round(json['main']['temp']-273.15)
    temp_min = round(json['main']['temp_min']-273.15)
    temp_max = round(json['main']['temp_max']-273.15)
    st.write('temperature',temperature, 'min',temp_min, 'max', temp_max)
    pressure = json['main']['pressure']
    humidity = json['main']['humidity']
    st.write('pressure',pressure,'Humidity',humidity)
    wind_speed = json['wind']['speed']
    wind_deg = json['wind']['deg']
    st.write('wind speed',wind_speed, 'wind deg',wind_deg)
    sunrise = json['sys']['sunrise']
    sunset = json['sys']['sunset']
    st.write('sunrise',sunrise,'sunset',sunset)
    lat = json['coord']['lat']
    lon = json['coord']['lon']

    st.map(pd.DataFrame({'lon':[lon],'lat':[lat]}))




from PIL import Image
image = Image.open('michela bernardini.jpg')
st.sidebar.image(image, caption='Created by LaMiki',width=150)

def show_footer():
    st.markdown("***")
    st.markdown(""" **like this?** Follow me on
                [Linkedin](https://www.linkedin.com/in/michela-bernardini-38053a3a).""")

show_footer()