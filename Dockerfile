FROM rackspacedot/python38

MAINTAINER owenstudy "owen_study@126.com"

ADD ./flaskdemo2 /code
WORKDIR /code

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "/code/app/app.py" ]
