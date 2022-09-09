FROM python:3.7-alpine
ARG PORTFOLIO_ID
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
EXPOSE 8008/TCP
ENV PARQET_PORTFOLIO_ID=$PORTFOLIO_ID
CMD ["python",  "/server/web_server.py"]
