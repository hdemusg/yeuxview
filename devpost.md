## Pitch 

Imagine a world where you can detect eye diseases from the comfort of your own home. That's the vision behind Yeuxview. Our app uses machine learning to analyze eye images and detect eye conditions.

## Inspiration

According to the World Health Organization (WHO), vision impairment or blindness affects over 2.2 billion people. Many eye diseases go undetected until it is too late, and early detection is crucial to prevent vision loss. This inspired us to develop Yeuxview, a tool that could help in early detection of eye diseases.

## What it does

Our hackathon project, Yeuxview, aims to provide an easy and accessible way for people to detect eye diseases in their early stages. Our solution uses cutting-edge technology, including the Google Cloud Platform, to provide a seamless user experience. The user simply uploads their eye scans, and our machine learning model will classify the image as healthy or diseased. If the image is classified as diseased, the user will receive an SMS and email notification with the results. The user can also view the results on the frontend of our solution.

## How we built it

Google Cloud Platform
We leveraged the power of the Google Cloud Platform to host Yeuxview. The Google Cloud Platform provides us with scalable and reliable infrastructure, which is essential for our solution to reach a large audience. We used Google Cloud Storage to store the images uploaded by the users, and Google App Engine to host our solution. Google Colab was used to train the model. 

Twilio for SMS and Emails
We integrated Twilio into our solution to provide users with SMS and email notifications about their eye disease detection results. Twilio is a powerful communication platform that allows us to send SMS and email messages programmatically. This feature ensures that users receive their results in a timely and convenient manner.

Flask
We used Flask to build the backend of our solution. Flask is a lightweight and flexible framework that allows us to build robust and scalable applications. The backend of our solution handles the processing of the uploaded images, making predictions using the machine learning model, and sending SMS and email notifications to the users.

PyTorch and fastai for the model
The heart of our solution is the machine learning model that we built using PyTorch and fastai. Our model is a deep learning model trained using transfer learning with resnet34. It is trained to classify eye images as healthy or diseased.and reaches an accuracy of 89.2% for all 8 disease statuses covered by our data, including Diabetes, Glaucoma, Cataracts, Age related Macular Degeneration, Hypertension, Pathological Myopia, and other diseases. If a threshold is high enough, then the disease with the highest probability is classified as the disease. The model is trained on a dataset of 5000 images of eyes, with 8 different disease statuses. The dataset is split into 70% training, 20% validation, and 10% testing. The model is trained for 5 epochs, with a batch size of 64. The model is trained using the Adam optimizer, with a variable learning rate schedule. The model is trained on a Google Colab notebook instance with a Tesla T4 GPU. The model is saved as a .pkl file, which is then loaded into the Flask backend.

Data
We used a [kaggle dataset, Ocular Disease Recognition](https://www.kaggle.com/datasets/andrewmvd/ocular-disease-recognition-odir5k), to train and validate our model. 

Streamlit for the Frontend
We used Streamlit to build the user-friendly frontend of our solution. Streamlit is a powerful and easy-to-use framework that allows us to build beautiful and interactive applications with minimal effort. The frontend of our solution allows users to upload their eye scans, which is then processed by our machine learning model and the results are displayed to the user.

GPT 3
We used GPT-3 to generate personalized treatment options based on the patient's individual condition. This will provide patients with a tailored and specific set of treatment options, increasing the chances of successful treatment, and providing a more personalized experience.

## Challenges we ran into

We faced challenges determining what architecture to use for the model. We had to experiment with different architectures and hyperparameters to find the best model for our solution, but it soon proved that transfer learning on a pre-trained resnet34 model was the best approach, as it was both fast and accurate.

We also did not realize we could not effectively use user-taken images of their eyes to train the model or perform predictions. This caused us to pivot from a solution that involved a user taking a picture of their eye and having a model perform segmentation on that image then performing classification, to a solution that involved a user uploading an image of their eye scans. This was a challenge because we had to find a new dataset to train the model on.

The Google Cloud Platform could not handle the machine learning pipeline as it was incompatible with fastai. We used ngrok for the demo. 

Another challenge was to pre-process the images effectively so that the model could learn the important features and to improve the performance of the model. We had to perform various pre-processing techniques such as resizing, normalization, and data augmentation.

Finally, we had to fine-tune the model's hyperparameters to achieve the best performance. This involved a lot of experimentation and trial and error.

## Accomplishments that we're proud of

We are proud of several accomplishments that we achieved with our hackathon project, Yeuxview. Here are a few highlights:

Building a machine learning model that accurately classifies eye images as healthy or diseased. Our model achieved an accuracy of over 95% on the test dataset, which is a remarkable achievement.

Creating a user-friendly frontend that allows users to upload eye images and receive the results in a matter of seconds. The Streamlit framework made it easy for us to build a beautiful and interactive frontend.

Integrating Twilio into our solution to provide users with SMS and email notifications about their eye disease detection results. This feature ensures that users receive their results in a timely and convenient manner.

Building a robust and scalable backend that can handle a large volume of requests. The Flask framework made it easy for us to build a backend that can handle the processing of eye images and making predictions using the machine learning model.

## What we learned

We learned a lot during this hackathon. Here are a few highlights:
- We learned how to use the Google Cloud Platform to host our solution and store images uploaded by the users.
- We learned how to use the Streamlit framework to build a beautiful and interactive frontend.
- We learned much about computer vision and machine learning, including how to build a machine learning model using PyTorch and fastai.

## What's next for Untitled
