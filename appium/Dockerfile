FROM appium/appium

RUN apt-get -y update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y supervisor

COPY supervisord.conf /root/
RUN chmod +x /root/supervisord.conf

COPY . /root/src
RUN pip3 install -r /root/src/requirements.txt

EXPOSE 3234

CMD /usr/bin/supervisord --configuration /root/supervisord.conf