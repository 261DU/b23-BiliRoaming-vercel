import httpx
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["https://www.bilibili.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许访问的源
    allow_credentials=True,  # 支持 cookie
    allow_methods=["*"],  # 允许使用的请求方法
    allow_headers=["*"]  # 允许携带的 Headers
)


@app.get("/pgc/player/web/playurl")
async def web_playurl(request: Request):
    # print(request.)
    url = f"https://api.bilibili.com/pgc/player/web/playurl?{request.query_params}"
    headers = dict(request.headers.items())

    # print(headers)
    async with httpx.AsyncClient(
            headers={
                "user-agent": headers.get("user-agent",
                                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"),
            },
            timeout=10,
    ) as client:
        res = await client.get(url)
    # print(res.text)
    return res.json()


@app.get("/pgc/player/api/playurl")
async def api_playurl(request: Request):
    # print(request.)
    url = f"https://api.bilibili.com/pgc/player/api/playurl?{request.query_params}"
    headers = dict(request.headers.items())

    # print(headers)
    async with httpx.AsyncClient(
            headers={
                "user-agent": headers.get("user-agent",
                                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"),
            },
            timeout=10,
    ) as client:
        res = await client.get(url)
    # print(res.text)
    return res.json()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("chuchai:app", host="0.0.0.0", port=9999, reload=True)
