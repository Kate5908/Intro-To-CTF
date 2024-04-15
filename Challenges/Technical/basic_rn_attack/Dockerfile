FROM python:3.10.12
WORKDIR /app
COPY board/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY board/ /app/board
ENV FLASK_APP=board:create_app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
USER www-data
EXPOSE 8000
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0", "--port=8000"]
