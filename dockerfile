FROM python:alpine
RUN pip install flask
EXPOSE 8777
CMD python main_score.py