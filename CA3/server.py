import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="static")


@app.get("/oauth/redirect")
def oauth_redirect(code: str):
    print(f'Github code is: {code}')
    return f'Github code is: {code}'


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


if (__name__ == '__main__'):
    uvicorn.run(app, host='0.0.0.0', port=8589)
