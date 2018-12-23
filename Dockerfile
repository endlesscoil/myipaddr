from python:3.6 

ADD . /app
WORKDIR /app

RUN pip install pipenv 
RUN pipenv install --system --deploy 

CMD ["python", "-u", "myipaddr/app.py"] 
