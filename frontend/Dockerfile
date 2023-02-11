# #Base Image to use
# FROM python:3.7

# WORKDIR /app

# #Expose port 8080

# #Copy Requirements.txt file into app directory
# COPY requirements.txt ./requirements.txt

# #install all requirements in requirements.txt
# RUN pip install -r requirements.txt

# EXPOSE 8080

# #Copy all files in current directory into app directory
# COPY . /app


# CMD streamlit run --server.port 8080 --server.enableCORS false app.py
FROM python:3.7.8-slim

# remember to expose the port your app'll be exposed on.
EXPOSE 8080

RUN pip install -U pip

COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

# copy into a directory of its own (so it isn't in the toplevel dir)
COPY . /app
WORKDIR /app

# run it!
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]