import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import requests
from urllib.parse import parse_qs

USER_DATA_RETRIEVAL_URL = "https://api.github.com/user/"
ACCESS_TOKEN_RETRIEVAL_URL = "https://github.com/login/oauth/access_token/"
CLIENT_SECRET = "004642d5183c6d26499f3c09ae0e92009106edac"
CLIENT_ID = "Ov23liCSIx7NQkGmr8uy"

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def get_token_from_encoded_url(response):
    if not response.text:
        raise Exception("Server Error")

    response_txt_data = parse_qs(response.text)
    access_token = response_txt_data.get('access_token', [None])[0]
    if access_token:
        return access_token
    else:
        raise Exception("Server Error")


def get_auth_token(github_code):
    token_request_payload = {
        'code': github_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    auth_response = requests.post(
        ACCESS_TOKEN_RETRIEVAL_URL, data=token_request_payload)

    auth_response.raise_for_status()

    print(f'access_token: {get_token_from_encoded_url(auth_response)}')


@app.get("/oauth/redirect")
def oauth_redirect(code: str):
    print(f'Github code is: {code}')
    get_auth_token(code)
    return f'Github code is: {code}'


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


if (__name__ == '__main__'):
    uvicorn.run(app, host='0.0.0.0', port=8589)
