FROM ubuntu:latest

RUN apt-get -y update && apt-get install -y sudo wget vim git curl gawk make gcc

RUN wget https://repo.continuum.io/archive/Anaconda3-2019.03-Linux-x86_64.sh && \
    sh Anaconda3-2019.03-Linux-x86_64.sh -b  && \
    rm -f Anaconda3-2019.03-Linux-x86_64.sh && \
    sudo curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -  && \
    sudo apt-get install -y nodejs

ENV PATH $PATH:/root/anaconda3/bin

RUN mkdir /workspace

CMD ["jupyter-lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--LabApp.token=''"]
