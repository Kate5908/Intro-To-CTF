# start by pulling the python image
FROM python:3.10.12

# copy the requirements file 
COPY board/requirements.txt app/requirements.txt

WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file
COPY board/ .

# switch to the www-data user
USER www-data


# configure the container to run in an executed manner
ENTRYPOINT [ "python3", "-m", "flask" ]

EXPOSE 8000
# basically below runs the file web server
CMD ["--app", "board", "run", "--host=0.0.0.0", "--port=8000", "--debug" ]