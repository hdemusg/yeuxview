## Pitch 

Imagine a world where you can detect eye diseases from the comfort of your own home. That's the vision behind Yeuxview. Our app uses machine learning to analyze eye images and detect eye conditions.

## Inspiration

According to the World Health Organization (WHO), vision impairment or blindness affects over 2.2 billion people. Many eye diseases go undetected until it is too late, and early detection is crucial to prevent vision loss. This inspired us to develop Yeuxview, a tool that could help in early detection of eye diseases.

## What it does

Our hackathon project, yeuxview, aims to provide an easy and accessible way for people to detect eye diseases in their early stages. Our solution uses cutting-edge technology, including the Google Cloud Platform, to provide a seamless user experience. The user simply uploads their eye scans, and our machine learning model will classify the image as healthy or diseased. If the image is classified as diseased, the user will receive an SMS and email notification with the results. The user can also view the results on the frontend of our solution.

## How we built it

Google Cloud Platform
We leveraged the power of the Google Cloud Platform to host Yeuxview. The Google Cloud Platform provides us with scalable and reliable infrastructure, which is essential for our solution to reach a large audience. We used Google Cloud Storage to store the images uploaded by the users, and Google App Engine to host our solution.

Twilio for SMS and Emails
We integrated Twilio into our solution to provide users with SMS and email notifications about their eye disease detection results. Twilio is a powerful communication platform that allows us to send SMS and email messages programmatically. This feature ensures that users receive their results in a timely and convenient manner.

Flask
We used Flask to build the backend of our solution. Flask is a lightweight and flexible framework that allows us to build robust and scalable applications. The backend of our solution handles the processing of the uploaded images, making predictions using the machine learning model, and sending SMS and email notifications to the users.

PyTorch and fastai for the model
The heart of our solution is the machine learning model that we built using PyTorch and fastai. Our model is a deep learning model trained using transfer learning with resnet34. It is trained to classify eye images as healthy or diseased.and reaches an accuracy of 89.2% for all 8 disease statuses covered by our data, including Diabetes, Glaucoma, Cataracts, Age related Macular Degeneration, Hypertension, Pathological Myopia, and other diseases/abnormalities. If a threshold is high enough, then the disease with the highest probability on both eyes has two treatment plans generated using GPT-3.

Data
We used a [kaggle dataset, Ocular Disease Recognition](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k), to train and validate our model. 

Streamlit for the Frontend
We used Streamlit to build the user-friendly frontend of our solution. Streamlit is a powerful and easy-to-use framework that allows us to build beautiful and interactive applications with minimal effort. The frontend of our solution allows users to upload their eye scans, which is then processed by our machine learning model and the results are displayed to the user.

GPT 3
In conclusion, our hackathon project, Eye Disease Detection with Machine Learning, is a comprehensive solution that leverages the latest technology to provide an easy and accessible way for people to detect eye diseases in their early stages.


## Challenges we ran into

## Accomplishments that we're proud of

## What we learned

## What's next for Untitled
