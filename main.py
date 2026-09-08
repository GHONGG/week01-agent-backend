from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    """健康检查接口，用来确认服务是否活着"""
    return {"status": "ok"}
