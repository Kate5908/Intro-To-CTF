# start by pulling the python image
FROM python:3.11


# copy the requirements file into the image
COPY ./Flask-Web-App/requirements.txt /web_app/requirements.txt

# switch working directory
WORKDIR /web_app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image

# After copying your Flask app
COPY ./Flask-Web-App /web_app
RUN chmod 755 /web_app
RUN chmod 644 /web_app/instance/database.db
RUN chown -R www-data:www-data /web_app

RUN echo 'INTRO_TO_CTF{Iluv33TiX}' > /flag.txt
RUN chown www-data:www-data /flag.txt

# switch to the www-data user
USER www-data

WORKDIR /web_app
# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]

EXPOSE 4000

CMD ["main.py" ]