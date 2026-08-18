import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://yougile.com/api-v2"
TOKEN = os.getenv("YOUGILE_TOKEN")
COMPANY_ID = os.getenv("COMPANY_ID")
