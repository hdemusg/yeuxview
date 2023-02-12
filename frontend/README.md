# yeuxview frontend

Hosts the public face of the project.

- Make sure all dependencies listed in requirements.txt are installed with the appropriate version on the local machine.
- To host the frontend- the command streamlit app.py should be run. Access is with the endpoint link: https://yeuxview.uk.r.appspot.com/
- OpenAI and Twilio keys need to be generated- a single access key for OpenAI and Twilio has two keys- an auth token key and account SID key.
- App.py hosts the main code of the frontend display.
- App.yaml to specify runtime for Google Cloud Platform
- A dockerfile used for hosting on Google Cloud Platform with the .streamlit defining the streamlit app.
