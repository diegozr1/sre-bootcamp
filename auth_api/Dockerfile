# Add your instructions to dockerize the application
# App must run on port 8000

FROM python:3.8

RUN pip3 install --upgrade pip

# environment variables including database credenatials or API
# should not be pushed to any repository
# including this time only for demostration purposes

COPY . .


COPY .env.src .
RUN source .env.src

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /src

EXPOSE 8000

# run the application
CMD ["python", "api.py"]