# Imports

import smtplib
import requests
import streamlit as st
from io import StringIO
import os
import openai
from twilio.rest import Client
import time
import random
from os.path import join, dirname
from dotenv import load_dotenv
import pandas as pd

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


def gpt_treatment(ld, rd):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"You are a medical advisor and eye-doctor. The patient has just gone an eye analysis and their test results have indicated {ld} in the left eye, and {rd} in the right eye. Recommend possible treatments and precautions they must take for each eye. Respond in less than 100 words.",
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].text


# Title and Camera Input

st.title("Welcome To YeuxView! :eye:")
st.info("Early Eye-Disease Diagnosis and Preventive Care")

st.info("Upload an iris scan to process.")
left_uploaded_file = st.file_uploader("Left Eye", type=['png', 'jpg'])
right_uploaded_file = st.file_uploader("Right Eye", type=['png', 'jpg'])

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

        with st.spinner('Processing Your Data.'):
            st.title("Your Results: ")
            
            url = "https://002f-2610-148-1f00-4000-3cbf-cc26-bae5-952c.ngrok.io/pipeline"            
            r = requests.post(url, files=images)

            image1data = r.json()['image1']
            image2data = r.json()['image2']

            preds1 = [0, 1, 2, 3, 4, 5, 6, 7]
            preds2 = [0, 1, 2, 3, 4, 5, 6, 7]
            probs1 = [image1data['probs'][0], image1data['probs'][1], image1data['probs'][2], image1data['probs'][3], image1data['probs'][4], image1data['probs'][5], image1data['probs'][6]]
            probs2 = [image2data['probs'][0], image2data['probs'][1], image2data['probs'][2], image2data['probs'][3], image2data['probs'][4], image2data['probs'][5], image2data['probs'][6]]

            disease_names = {
            0: 'Normal',
            1: 'Diabetes',
            2: 'Glaucoma',
            3: 'Cataract',
            4: 'Age related muscular degeneration',
            5: 'Hypertension',
            6: 'Pathological myopia',
            7: 'Other diseases'
            }

            data1 = list(zip(preds1, probs1))
            data1.sort(key=lambda x: x[1], reverse=True)
            data2 = list(zip(preds2, probs2))
            data2.sort(key=lambda x: x[1], reverse=True)

            sorted_preds1, sorted_probs1 = zip(*data1)
            sorted_preds2, sorted_probs2 = zip(*data2)

            df1 = pd.DataFrame({'Disease': [disease_names[p] for p in sorted_preds1], 'Probability': sorted_probs1})
            df2 = pd.DataFrame({'Disease': [disease_names[p] for p in sorted_preds2], 'Probability': sorted_probs2})

            disease_index1 = probs1.index(max(probs1))
            disease_name1 = disease_names[disease_index1]
            st.subheader(f"Left Eye Diagnosis: {disease_name1}")
            st.bar_chart(df1, x='Disease', y='Probability')

            disease_index2 = probs2.index(max(probs2))
            disease_name2 = disease_names[disease_index2]
            st.subheader(f"Right Eye Diagnosis: {disease_name2}")
            st.bar_chart(df2, x='Disease', y='Probability')

            st.title("Possible Treatments")
            treatment = gpt_treatment(disease_name1, disease_name2)
            st.write(treatment)

            if(phone_no != 1000000000):
                send_sms(phone_no, "Your YeuxView reports are in!\n" + "Here's the prescribed treatment:\n" + treatment)
            if(email != ""):
                send_email(treatment, email)

    else:
        st.warning("Please enter the required information!")