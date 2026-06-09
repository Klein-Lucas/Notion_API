from env_loader import load_env
from notion_services import NotionService


def main():
    config = load_env()
    notion = NotionService(config)

    # 1. Create a reward
    reward_fields = {
        "Name": ("title", "Focus Bonus"),
        "Tipo": ("select", "Item"),
        "+ XP": ("number", 20),
    }
    reward_id = notion.create_page(config["NOTION_REWARDS_DB_ID"], reward_fields)

    if not reward_id:
        print("Failed to create reward.")
        return

    # 2. Create a mission linked to the reward
    mission_fields = {
        "Name": ("title", "Study for 2 hours"),
        "Categoria": ("multi-select", ["Study"]),
        "Dificuldade": ("select", "⭐⭐⭐"),
        "Status": ("select", "Pending"),
        "Recompensa": ("relation", reward_id)
    }
    notion.create_page(config["NOTION_MISSIONS_DB_ID"], mission_fields)

if __name__ == "__main__":
    main()