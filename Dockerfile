FROM python:latest
COPY . .
RUN pip install
EXPOSE 8000
CMD ["pytest", "test_failure.py"]