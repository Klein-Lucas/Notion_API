# Notion API Integration

> Automatize a criação de missões e recompensas no Notion usando Python e OpenAI.

## Sobre

Este projeto conecta o **Notion** como interface de produtividade gamificada com a **OpenAI**, permitindo criar missões e recompensas automaticamente a partir de temas de interesse registrados em um banco de dados Notion.

O `NotionService` abstrai a API do Notion em um serviço reutilizável que suporta múltiplos tipos de propriedade (título, seleção, multi-seleção, relações, datas, etc.), permitindo criar páginas em qualquer banco de dados de forma genérica.

## Funcionalidades

- Criação de páginas em bancos de dados Notion via API
- Suporte a propriedades: `title`, `select`, `multi-select`, `number`, `rich_text`, `checkbox`, `relation`, `date`
- Associação automática entre entidades (ex: missão → recompensa via `relation`)
- Carregamento de variáveis de ambiente via `env_loader`

## Tecnologias

- **Python** 3.11+
- **Notion API** v1
- **OpenAI API** (integração planejada)
- **requests**

## Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/Klein-Lucas/Notion_API.git
cd Notion_API
pip install -r requirements.txt
```

### 2. Criar o arquivo `.env`

```env
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxx
NOTION_VERSION=2022-06-28
NOTION_REWARDS_DB_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_MISSIONS_DB_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

- `NOTION_TOKEN`: Integration token gerado em [notion.so/my-integrations](https://www.notion.so/my-integrations)
- `NOTION_REWARDS_DB_ID` e `NOTION_MISSIONS_DB_ID`: IDs dos bancos de dados Notion (encontrados na URL da página)

### 3. Conectar a integração aos bancos de dados

No Notion, abra cada banco de dados → `...` → `Add connections` → selecione sua integração.

## Uso

```bash
python main.py
```

O script cria uma recompensa no banco `REWARDS` e, em seguida, uma missão no banco `MISSIONS` com a relação entre elas configurada automaticamente.

## Estrutura

```
├── main.py              # Exemplo de uso: cria recompensa e missão relacionadas
├── notion_services.py   # NotionService — abstração da API do Notion
├── env_loader.py        # Carrega variáveis do .env
└── requirements.txt     # Dependências
```

## Próximos passos

- Monitorar banco de dados de interesses no Notion
- Ao marcar um interesse, gerar missões e recompensas via OpenAI automaticamente
- Integrar `OpenAIService` para geração de conteúdo das missões

## Licença

MIT