# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# create flag 
RUN chown www-data:www-data /flag.txt
# switch to the www-data user
USER www-data


# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

EXPOSE 4999

CMD ["app.py" ]