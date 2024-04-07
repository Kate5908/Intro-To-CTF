# start by pulling the python image
FROM python:3.11


# copy the requirements file into the image
COPY app/requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file
COPY app/ .

# create flag 

RUN echo 'INTRO_TO_CTF{1h4734C7u4LlyL0v3XX3}' > /flag.txt
RUN chown www-data:www-data /flag.txt
# switch to the www-data user
USER www-data


# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]
