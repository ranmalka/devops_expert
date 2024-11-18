FROM python:alpine
LABEL authors="rmalka"
COPY ./code/ .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python",  "main_score.py"]