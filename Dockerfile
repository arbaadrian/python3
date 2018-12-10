FROM centos:7

ARG V_ENV_USER=1000
ARG V_ENV_GROUP=1000

ENV LC_ALL=en_US.utf8 \
  LANG=en_US.utf8

COPY deps /tmp/deps

RUN set -euxo pipefail \
  && yum install -y epel-release \
  && yum install -y \
    openssl openssh-clients unzip curl gcc python-devel \
    sudo iproute vim iputils git  \
    python36 python36-devel rpm-devel \
  && python36 -m ensurepip \
  && pip3 install \
    pipenv==2018.10.13 \
  && mv /tmp/deps/sudoers /etc/sudoers \
  && groupadd --gid ${V_ENV_GROUP} aarba \
  && useradd \
          --uid ${V_ENV_USER} \
          --gid ${V_ENV_GROUP} \
          --groups wheel \
          --home-dir /home/aarba \
          --shell /bin/bash \
          --comment "Adrian Arba" \
          aarba \
  && mkdir /opt/app \
  && chown -R aarba. /opt/app \
  && rm -rf /tmp/deps

USER aarba

VOLUME ["/opt/app"]

WORKDIR "/opt/app"

