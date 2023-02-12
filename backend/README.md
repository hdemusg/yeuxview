# yeuxview backend

Hosts the backend and machine learning pipeline of the project. :)

- Make sure all dependencies listed in requirements.txt are installed with the appropriate version on the local machine.
- To host the backend Flask app- run python main.py.
- The google cloud link is: https://yeuxview-backend-dot-yeuxview.uk.r.appspot.com/. Currently needs works on functionality.
- The working backend link with Ngrok: https://002f-2610-148-1f00-4000-3cbf-cc26-bae5-952c.ngrok.io/ 
- Two Google OAuth keys need to be generated.
- model.py contains a model using Resnet + Conv layer and was trained offline to keep Google Cloud Platform lean- was abandoned due to taking too long to train with a lower accuracy.
- Using the fastai library- run the cells in fastai.iypnb to generate the model file called export.pkl. The model was trained offline to keep Google Cloud Platform lean and display faster results with an accuracy of 89.2%.
- The .jpg images are example images used for training and testing cloud storage.
- full_df.csv contains the labels corresponding to the input images used.
- export.pkl is the model file generated that was fed into the Flask backend for display.
- pipeline.py is the data pipeline to take the export.pkl and convert it to  be shown in the app.
- App.yaml is the runtime needed for Google Cloud Platform to work.
