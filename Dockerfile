# 使用官方 Python 映像作為基礎映像
FROM python:3.10.13-slim
# 設置工作目錄
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
# 複製應用程式代碼
COPY ./app.py /app/
# 運行應用
CMD ["python", "app.py"]