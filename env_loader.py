from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    config = {
        "NOTION_TOKEN": os.getenv("NOTION_TOKEN"),
        "NOTION_DATABASE_ID": os.getenv("NOTION_DATABASE_ID"),
        "NOTION_VERSION": os.getenv("NOTION_VERSION", "2022-06-28")
    }
    return config
