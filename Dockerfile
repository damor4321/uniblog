#
#  Dockerfile para proyectos Django
#

# Base image.
FROM python:3.6

# Create code folder.
RUN mkdir /code

# Set working dir.
WORKDIR /code

# Add python requirements file.
ADD requirements.txt /code/

# Install required programs.
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y \
    gettext \
    nginx \
    vim

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /code/conf/nginx-app.conf /etc/nginx/sites-enabled/

# Add source code.
ADD . /code/

# Run script file.
CMD ./run.sh
