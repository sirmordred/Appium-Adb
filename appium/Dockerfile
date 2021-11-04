FROM appium/appium

RUN apt-get -y update
RUN apt-get install -y python3 python3-pip

COPY . /root/src
RUN pip3 install -r /root/src/requirements.txt

EXPOSE 3234

CMD /root/entry_point.sh