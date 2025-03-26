import requests

class NotionService:
    def __init__(self, config):
        self.base_url = "https://api.notion.com/v1"
        self.headers = {
            "Authorization": f"Bearer {config['NOTION_TOKEN']}",
            "Content-Type": "application/json",
            "Notion-Version": config["NOTION_VERSION"]
        }

    def build_properties(self, field_dict: dict) -> dict:
        prop_map = {
            "title": lambda v: {"title": [{"text": {"content": v}}]},
            "select": lambda v: {"select": {"name": v}},
            "number": lambda v: {"number": v},
            "rich_text": lambda v: {"rich_text": [{"text": {"content": v}}]},
            "checkbox": lambda v: {"checkbox": v},
            "relation": lambda v: {"relation": [{"id": v}]},
            "date": lambda v: {"date": {"start": v}},  # ISO 8601 format
        }
        return {key: prop_map[field_type](value) for key, (field_type, value) in field_dict.items()}

    def create_page(self, database_id: str, fields: dict):
        url = f"{self.base_url}/pages"
        payload = {
            "parent": {"database_id": database_id},
            "properties": self.build_properties(fields)
        }
        response = requests.post(url, headers=self.headers, json=payload)
        if response.status_code == 200:
            print(f"✅ Página criada com sucesso: {fields.get('Name', ('', ''))[1]}")
            return response.json()["id"]
        else:
            print(f"❌ Erro ao criar página: {response.status_code}")
            print(response.json())
            return None
