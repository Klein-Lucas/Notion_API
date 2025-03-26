from utils.env_loader import load_env
from services.notion_service import NotionService

def main():
    config = load_env()
    notion = NotionService(config)

    # 1️⃣ Criar Recompensa
    recompensa_fields = {
        "Name": ("title", "Bônus de Foco"),
        "Tipo": ("select", "Item"),
        "+XP": ("number", 20),
        "Status": ("checkbox", False),
        "Categoria": ("select", "Estudo")
    }
    recompensa_id = notion.create_page(config["NOTION_REWARDS_DB_ID"], recompensa_fields)

    if not recompensa_id:
        print("❌ Não foi possível criar a recompensa.")
        return

    # 2️⃣ Criar Missão associada à recompensa
    missao_fields = {
        "Name": ("title", "Estudar por 2h"),
        "Categoria": ("select", "Estudo"),
        "Dificuldade": ("select", "Média"),
        "XP": ("number", 50),
        "Status": ("checkbox", False),
        "Recompensa": ("relation", recompensa_id)
    }
    notion.create_page(config["NOTION_MISSIONS_DB_ID"], missao_fields)

if __name__ == "__main__":
    main()
