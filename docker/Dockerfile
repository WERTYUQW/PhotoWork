FROM python:3.7
MAINTAINER Andrew Smirnov <smirnov@informatics.ru>
ADD ./ /s107_photofind
WORKDIR /s107_photofind/
CMD exec apt-get update
CMD exec apt-get install build-essential nano python3-dev libmysqlclient-dev
RUN pip install --no-cache-dir -r ./requirements.txt
CMD exec ./docker/run.sh
