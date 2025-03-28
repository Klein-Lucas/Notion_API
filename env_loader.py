from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()
    config = {
        "NOTION_TOKEN": os.getenv("NOTION_TOKEN"),
        "NOTION_REWARDS_DB_ID": os.getenv("NOTION_REWARDS_DB_ID"),
        "NOTION_MISSIONS_DB_ID": os.getenv("NOTION_MISSIONS_DB_ID"),
        "NOTION_VERSION": os.getenv("NOTION_VERSION", "2022-06-28")
    }

    return config
