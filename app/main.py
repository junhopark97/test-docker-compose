from litestar import Litestar, get
import requests
import os


# ISSUANCE_SEVER_URI = os.environ.get('ISSUANCE_URI', 'localhost:8000')
ISSUANCE_SEVER_URI = os.environ.get('ISSUANCE_URI', 'http://localhost:8000')
# ISSUANCE_SEVER_URI = os.environ.get('ISSUANCE_URI')
# ISSUANCE_SEVER_URI = os.environ.get('ISSUANCE_URI', 'localhost:8000')


@get("/")
def index() -> str:
    print(requests.get("http://localhost:8000/securities").json())
    # response = requests.get(f"{ISSUANCE_SEVER_URI}" + "/securities")
    # return response.json()
    # 2(amend로 수정) qwer
    return 'Hello World'


app = Litestar([index])
