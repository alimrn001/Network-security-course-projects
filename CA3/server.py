import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/oauth/redirect")
def oauth_redirect(code: str):
	print(f'Github code is: {code}')
	return f'Github code is: {code}'

if (__name__ == '__main__'):
	uvicorn.run(app, host= '0.0.0.0', port = 8589)
