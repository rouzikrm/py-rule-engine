FROM python:3.6-stretch
RUN pip3 install nameko
WORKDIR /opt/app
RUN python -c 'import sys;sys.path.append(".")'