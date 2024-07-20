FROM python:alpine
RUN pip install flask
COPY main_score.py .
EXPOSE 8777
CMD python main_score.py