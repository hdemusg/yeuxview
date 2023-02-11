
# Imports

import streamlit as st
import requests
import streamlit as st
from io import StringIO
import os
import openai

# Keys

# Functions

def save_uploadedfile(uploadedfile):
     with open("image.jpg","wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))


def gpt_treatment(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"You are a medical advisor and eye-doctor. The patient is suffering from an eye disease called {prompt}. Recommend possible treatments and precautions they must take in the following way.",
        temperature=0.7,
        max_tokens=250 # specify max length here
    )
    print("S", response.choices[0].text)
    return response.choices[0].text

# Title and Camera Input

st.title("Welcome To YeuxView! :eye:")
st.info("Early Eye-Disease Diagnosis and Preventive Care")
datafile = st.camera_input("Capture Pic")

if datafile is not None:
    file_details = {"FileName":datafile.name,"FileType":datafile.type}
    save_uploadedfile(datafile)    
    my_img = {'image': open("image.jpg", 'rb')}
    # url = ""
    # r = requests.post(url, files=my_img)
    # st.write(r.json()['ans'])
    # st.write(r.json()['prob'])

    with st.spinner('Wait for it...'):
        st.write(gpt_treatment("High Myopia"))




