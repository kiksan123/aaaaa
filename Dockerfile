FROM ubuntu:18.04

# language conf
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV PYTHONIOENCODING "utf-8"
ENV PYTHONUNBUFFERED 1

# update ubuntu
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y

RUN apt-get install -y software-properties-common vim fonts-ipafont-gothic

RUN apt-get update \
  && apt-get install python3.6 python3.6-dev python3-pip make curl git sudo cron -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3.6 python

# install mecab from github
WORKDIR /opt
RUN git clone https://github.com/taku910/mecab.git
WORKDIR /opt/mecab/mecab
RUN ./configure  --enable-utf8-only \
  && make \
  && make check \
  && make install \
  && ldconfig

WORKDIR /opt/mecab/mecab-ipadic
RUN ./configure --with-charset=utf8 \
 && make \
 && make install

# neolog-ipadic.
# もしimageのサイズが気になるなら以下コメントアウトするとより軽量なipadic辞書のmecabが使える
WORKDIR /opt
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /opt/mecab-ipadic-neologd
RUN ./bin/install-mecab-ipadic-neologd -n -y


# install package in python
WORKDIR /home/
ADD requirements.txt /home/

RUN python -m pip install pip --upgrade \
 && python -m pip install -r requirements.txt
