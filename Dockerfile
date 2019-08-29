# start from an official image
FROM python:3.7.4

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/api/src
WORKDIR /opt/services/api/src

# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY requirements.txt requirements.txt
COPY entrypoint.sh /entrypoint.sh
RUN pip install -r requirements.txt

# copy our project code
COPY . /opt/services/api/src
RUN cd api && python manage.py collectstatic --no-input -v 2

RUN ls -la /opt/services/api/static/
RUN chmod +x /entrypoint.sh
EXPOSE 80
