FROM python:3.5.1
RUN mkdir -p /app/ip_rest
ADD ip_rest /app/ip_rest/
RUN pip install --upgrade pip
WORKDIR /app
RUN pip3 install -r ip_rest/requirements.txt
