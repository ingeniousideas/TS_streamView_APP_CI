# Step 1: Use a Python base image
ARG PY_VERSION=3.13-slim
FROM docker.io/python:${PY_VERSION}

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Accept an optional build environment argument
# Default to 'development' if not provided
ARG BUILD_ENV=development
ENV BUILD_ENV=${BUILD_ENV}

# Step 5: Copy and install dependencies conditionally
COPY requirements.txt /tmp/pip-tmp/
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN if [ "$BUILD_ENV" = "production" ]; then \
   pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt; \
   else \
   pip3 --disable-pip-version-check install -r /tmp/pip-tmp/requirements.txt; \
   fi \
   && rm -rf /tmp/pip-tmp

# Step 6: Expose the port the app runs on
EXPOSE 8050

# Step 7: Command to run the app with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8050", "app:server"]
