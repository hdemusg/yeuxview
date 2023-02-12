# Imports

import smtplib
import streamlit as st
import requests
import streamlit as st
from io import StringIO
import os
import openai
from twilio.rest import Client
import time
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Keys

openai.api_key = os.environ.get("OPENAI_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

# Functions

def send_email(message, to_email):
    email = "tempyeuxview@gmail.com"
    password = "ktarwxzahkucehsq"
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to_email, msg=f"Subject:Your YeuxView Reports!\n\n{message}")


def send_sms(to, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(  
        messaging_service_sid='MGe4610eaf3d8fb74280f75613d5633724', 
        body=message,
        to=to 
    ) 
    print(f"PDF sent to {to}")


def save_uploadedfile(uploadedfile, A, B):
     with open(A + "image" + B + "." + uploadedfile.type[6:],"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))


def gpt_treatment(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"You are a medical advisor and eye-doctor. The patient is suffering from an eye disease called {prompt}. Recommend possible treatments and precautions they must take. Respond in less than 100 words.",
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].text


# Title and Camera Input

st.title("Welcome To YeuxView! :eye:")
st.info("Early Eye-Disease Diagnosis and Preventive Care")

st.info("Upload an iris scan to process.")
right_uploaded_file = st.file_uploader("Right Eye", type=['png', 'jpg'])
left_uploaded_file = st.file_uploader("Left Eye", type=['png', 'jpg'])

gender = st.radio("What's your gender?", ('Male', 'Female'))
age = st.slider('How old are you?', 0, 100, 0)

st.info("If you'd like reports to be mailed / texted, fill in the following information.")

name = st.text_input("Enter your name.")
email = st.text_input("Enter your email.")
phone_no = st.number_input('Phone Number: ', min_value=1000000000, max_value=9999999999)

if (st.button("Process!")):
    if (right_uploaded_file is not None) and (left_uploaded_file is not None) and (age != 0):
        A = str(random.randint(1, 100))
        B = str(random.randint(2, 2000))
        C = str(random.randint(1, 100))
        D = str(random.randint(2, 2000))

        save_uploadedfile(right_uploaded_file, A, B)
        save_uploadedfile(left_uploaded_file, C, D)

        images = {
            'right_image': open(A + "image" + B + "." + right_uploaded_file.type[6:], 'rb'),
            'left_image': open(C + "image" + D + "." + left_uploaded_file.type[6:], 'rb'),
            'age': (None, age),
            'gender': (None, gender),
        }

        st.title("Your Information: ")
        st.subheader("Gender: " + gender)
        st.subheader("Age: " + str(age))
        if(name != ""):
            st.subheader("Name: " + name)
        if(email != ""):
            st.subheader("Email: " + email)
        if(phone_no != 1000000000):
            st.subheader("Phone Number: " + str(phone_no))


        st.image([A + "image" + B + "." + right_uploaded_file.type[6:], C + "image" + D + "." + left_uploaded_file.type[6:]], width=350)

        with st.spinner('Processing Your Data.'):
            st.title("Your Results: ")
            
            # url = "https://yeuxview-backend-dot-yeuxview.uk.r.appspot.com/pipeline"            
            # r = requests.post(url, files=images)

            # st.title("Possible Treatments")
            # treatment = gpt_treatment("High Myopia")
            # st.write(treatment)

            # if(phone_no != 1000000000):
            #     send_sms(phone_no, "Your YeuxView reports are in!\n" + "Here's the prescribed treatment:\n" + treatment)
            # if(email != ""):
            #     send_email(treatment, email)

    else:
        st.warning("Please enter the required information!")







