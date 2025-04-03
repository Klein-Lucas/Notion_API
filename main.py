from env_loader import load_env
from notion_services import NotionService

# Como vou criar essas coisas na main?
# Terei que ter um outro service que vai gerar os campos específicos daquele banco de dados.

# Como vou resolver o problema para o campo específico do personagem que vai ser padrão, sem estragar a versatilidade do codigo?

def main():
    config = load_env()
    notion = NotionService(config)

    # 1️⃣ Criar Recompensa
    recompensa_fields = {
        "Name": ("title", "Bônus de Foco"),
        "Tipo": ("select", "Item"),
        "+ XP": ("number", 20),
    }
    recompensa_id = notion.create_page(config["NOTION_REWARDS_DB_ID"], recompensa_fields)

    if not recompensa_id:
        print("❌ Não foi possível criar a recompensa.")
        return

    # 2️⃣ Criar Missão associada à recompensa
    missao_fields = {
        "Name": ("title", "Estudar por 2h"),
        "Categoria": ("multi-select", ["Estudo"]),
        "Dificuldade": ("select", "⭐⭐⭐"),
        "Status": ("select", "Pendente"),
        "Recompensa": ("relation", recompensa_id)
    }
    notion.create_page(config["NOTION_MISSIONS_DB_ID"], missao_fields)

if __name__ == "__main__":
    main()
