FROM  python:3.10.2

WORKDIR /backend
ADD . /backend

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN chmode +x run_backend.sh
CMD ["./run_backend"]