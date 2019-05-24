FROM python:3.6-stretch
RUN pip3 install nameko
RUN pip3 install pyyaml
RUN pip3 install pykka
WORKDIR /opt/app
RUN python -c 'import sys;sys.path.append(".")'
