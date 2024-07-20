FROM python:alpine
RUN pip install flask
COPY main_score.py .
EXPOSE 5000
CMD python main_score.py