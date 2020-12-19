FROM python:3.8.5

WORKDIR /app/

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create true && \
    poetry config virtualenvs.in-project true


COPY pyproject.toml poetry.lock* /app/

RUN bash -c "poetry install --no-root"

RUN bash -c "poetry env info"

COPY . /app/

ENV ARG $arg

CMD ["bash", "init.sh"]
