# Notion API Integration

> Automate mission and reward creation in Notion using Python and OpenAI.

## About

This project connects **Notion** as a gamified productivity interface with **OpenAI**, enabling automatic generation of missions and rewards from topics of interest registered in a Notion database.

The `NotionService` wraps the Notion API into a reusable service that supports multiple property types (title, select, multi-select, relations, dates, etc.), allowing pages to be created in any database in a generic way.

## Features

- Create pages in Notion databases via API
- Supports property types: `title`, `select`, `multi-select`, `number`, `rich_text`, `checkbox`, `relation`, `date`
- Automatic association between entities (e.g. mission → reward via `relation`)
- Environment variable loading via `env_loader`

## Tech Stack

- **Python** 3.11+
- **Notion API** v1
- **OpenAI API** (planned integration)
- **requests**

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Klein-Lucas/Notion_API.git
cd Notion_API
pip install -r requirements.txt
```

### 2. Create a `.env` file

```env
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxx
NOTION_VERSION=2022-06-28
NOTION_REWARDS_DB_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_MISSIONS_DB_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

- `NOTION_TOKEN`: Integration token from [notion.so/my-integrations](https://www.notion.so/my-integrations)
- `NOTION_REWARDS_DB_ID` and `NOTION_MISSIONS_DB_ID`: Database IDs found in the Notion page URL

### 3. Connect the integration to your databases

In Notion, open each database → `...` → `Add connections` → select your integration.

## Usage

```bash
python main.py
```

The script creates a reward in the `REWARDS` database, then creates a mission in the `MISSIONS` database with the relation to the reward set automatically.

## Project Structure

```
├── main.py              # Usage example: creates a linked reward and mission
├── notion_services.py   # NotionService — Notion API abstraction layer
├── env_loader.py        # Loads variables from .env
└── requirements.txt     # Dependencies
```

## Roadmap

- Monitor an interests database in Notion
- On checkbox trigger, auto-generate missions and rewards via OpenAI
- Integrate `OpenAIService` for mission content generation

## License

MIT