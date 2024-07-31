# Base image
FROM python:3.12
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

# Set the working directory in the container
WORKDIR /src

# Copy the requirements file to the working directory
COPY . .

# Install project dependencies
RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
