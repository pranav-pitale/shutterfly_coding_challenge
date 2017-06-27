FROM python:2.7.10
RUN apt-get update && apt-get install \
  && rm -rf /var/lib/apt/lists/*

# Set up python environment
RUN mkdir /src
RUN export PYTHONPATH=$PYTHONPATH:/src
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install -e .
