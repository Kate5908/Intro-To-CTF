# start by pulling the python image
FROM python:3.11


# copy the requirements file into the image
COPY requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file
COPY ./ .

# create flag 


# switch to the www-data user
USER www-data


# configure the container to run in an executed manner

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]