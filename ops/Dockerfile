FROM python:3.9.12-slim as builder

WORKDIR /app

COPY requirements.txt ./
RUN python -m pip wheel --wheel-dir /app/wheels -r requirements.txt

# ------
# final stage
FROM python:3.9.12-slim 

WORKDIR /app 

COPY --from=builder /app/wheels /wheels

RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password user
USER user
RUN python -m pip install --no-cache /wheels/*

# FIXME: COPY strictly necessary files
COPY --chown=user data_tools ./data_tools
COPY --chown=user tests ./tests
