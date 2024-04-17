# start by pulling the python image
FROM python:3.11


# copy the requirements file into the image
COPY app/requirements.txt /app/requirements.txt

WORKDIR /app
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

copy /app .
# create flag

# switch to the www-data user
USER www-data


# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

EXPOSE 4999

CMD ["app.py" ]
