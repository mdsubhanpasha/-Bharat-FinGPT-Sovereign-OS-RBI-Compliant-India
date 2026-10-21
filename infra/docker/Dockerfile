FROM python:3.12-slim
LABEL inventor="MOHAMMAD SUBHAN PASHA" patent="IN2026/FINGPT-OMNI-SOVEREIGN-OS"
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
