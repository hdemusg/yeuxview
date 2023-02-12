# yeuxview
Hacklytics 2023

- The team members are Sumedh Garimella, Anish Iyer, Keane Zhang, Pramit Bhatia

- The project is set up where the Frontend are Backend are in two seperate folders called Frontend and Backend. The Frontend is hosted on Google Cloud Platform and the Backend is intended to be hosted on Google Cloud Platform but Ngrok is using temporarily.

Video Script
- INTRODUCTION
Imagine a world where you can quickly and easily detect eye diseases from the comfort of your own home. That's the vision behind our project, yeuxview. Our team uses machine learning and computer vision algorithms to analyze images of the eye and detect various conditions, such as cataracts, glaucoma, and myopia. According to the World Health Organization (WHO), vision impairment or blindness affects over 2.2 billion people. Many eye diseases go undetected until it is too late, and early detection is crucial to prevent vision loss.

- TECHNICAL ARCHITECTURE & DEMO
First, the doctor (or patient) uploads the patient’s eyeball fundus pictures to our UI, which is built with Python and Streamlit, and hosted on Google App Engine.
After providing additional demographic data, the information is sent to the backend, which is a Python Flask app also hosted on Google App Engine, where pictures are stored to Google Cloud Storage for analysis by the ML pipeline, which consists of a Transfer Learning model with ResNet to determine the most likely diseases (if any) that a patient may be suffering given their eye scans. The most probable status, as well as the confidence rating, is then sent back to the UI, where GPT3 provides the patient with possible treatments, and Twilio sends it to them via text!
While many datasets exist with eyeball pictures and disease detection, we realized it would be important to empower patients to take better care of their eye health by providing them with actionable treatment options to make the results of our ML model more useful.

- OVERVIEW OF RESULTS/FUTURE WORK
As is shown, the app is able to successfully display a dashboard which will show two separate probability bar charts for both eyes and show the possibility there are certain indicators present for certain diseases. Our transfer learning model reaches an accuracy of 89.2% for all 8 disease statuses covered by our data. If a threshold is high enough, then the disease with the highest probability on both eyes has two treatment plans generated using GPT-3. For improvements, the main improvement to be made would be to allow for the model to incorporate additional demographic information such as age and gender in order to refine the probabilities of certain diseases to more accurately reflect the relative risk that will differ with different demographics. Further, adding more images in general will help with making more accurate predictions along with increasing the complexity of the algorithms with more advanced machine learning and computer vision aspects. Adding more robust functionality for letting users add images of their own eyes will help make the app more accessible in the future. In addition, potential integration with Google Fit will help connect doctors with nearby patients and allow treatment plans to be saved for users. 
