
from fastapi import FastAPI, HTTPException


# 1. 创建 FastAPI 应用对象
app = FastAPI(
    title="Day 8 Calculator API",
    description="我的第一个 Python API 服务",
    version="0.1.0",
)


# 2. 根路径：介绍服务
@app.get("/")
def root():
    return {
        "message": "欢迎使用我的第一个 FastAPI 服务",
        "docs": "/docs",
    }


# 3. 健康检查
@app.get("/health")
def health():
    return {
        "status": "ok",
    }


# 4. 计算接口
@app.get("/calculate")
def calculate(
    a: float,
    b: float,
    operation: str = "add",
):
    if operation == "add":
        result = a + b

    elif operation == "multiply":
        result = a * b

    else:
        raise HTTPException(
            status_code=400,
            detail="operation 只能是 add 或 multiply",
        )

    return {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result,
    }
