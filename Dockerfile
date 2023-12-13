FROM python:3.10.13

WORKDIR /app/CATdd

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    libssl-dev libffi-dev libncurses5-dev zlib1g zlib1g-dev libreadline-dev libbz2-dev libsqlite3-dev make gcc && \
    rm -rf /var/lib/apt/lists/*

RUN curl https://pyenv.run | bash
ENV PATH="/root/.pyenv/bin:${PATH}"
RUN eval "$(pyenv init --path)" && \
    eval "$(pyenv virtualenv-init -)"

RUN pyenv install 3.10.13 && \
    pyenv global 3.10.13

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

RUN git clone https://github.com/miyashita64/CATdd.git .
RUN poetry install

RUN echo "source .env" >> /root/.bashrc
