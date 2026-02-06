# LangGraph Book Assistant

A specialized AI assistant built with [LangGraph](https://github.com/langchain-ai/langgraph) that answers questions about books and manages a book database. The assistant uses OpenAI's GPT-4o and integrates with PostgreSQL for data persistence.

## Features

- **Intelligent Book Assistant**: Ask questions about books, authors, genres, and literature
- **Database Integration**: Query and manage books stored in PostgreSQL
- **Tool Integration**: Equipped with custom tools and MCP (Model Context Protocol) servers
- **Agentic Workflow**: Uses LangGraph to orchestrate multi-step reasoning with tools
- **Strict Context**: Refuses to answer non-book-related questions

## Architecture

The project consists of several key components:

### Core Components

- **Graph Builder** (`graph/builder.py`): Defines the LangGraph workflow with assistant and tools nodes
- **Nodes** (`graph/nodes.py`): Implements the assistant node (LLM inference) and tools node (tool execution)
- **Tools** (`graph/tools/book_tool.py`): Custom tools for book operations (find all books, find by ID, insert book)

### Models & Data

- **Book Model** (`models/book.py`): Dataclass representing book metadata
- **Book Repository** (`repository/book_repository.py`): Database access layer for book operations
- **Database Schema** (`schema.sql`): PostgreSQL schema definition

### Configuration

- **System Prompt** (`prompts/system.txt`): Instructions constraining the assistant to book-related topics
- **MCP Servers** (`mcp_servers.json`): Configuration for Model Context Protocol servers
- **LangGraph Config** (`langgraph.json`): LangGraph CLI configuration

## Prerequisites

- Python 3.8+
- PostgreSQL (via Docker Compose or local installation)
- OpenAI API key
- LangSmith API key (for tracing, optional)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd langgraph-test
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables (the app will prompt you for missing keys):

```bash
export OPENAI_API_KEY="your-openai-api-key"
export LANGSMITH_API_KEY="your-langsmith-api-key"
```

## Setup Database

Start PostgreSQL using Docker Compose:

```bash
docker-compose up -d
```

This will:

- Create a PostgreSQL container named `langgraph-test`
- Initialize the database with the schema from `docker/postgres/init.sql`
- Create a persistent volume for data

## Usage

Run the application:

```bash
python main.py
```

The app will:

1. Initialize API keys if not set
2. Build the LangGraph workflow
3. Create a compiled graph ready for execution

### Example Queries

```
"Show me all available books"
"What books are in the science fiction genre?"
"Tell me about the book with ID 1"
"Add a new book to the database"
```

## Project Structure

```
.
├── main.py                 # Entry point
├── compose.yml             # Docker Compose configuration
├── langgraph.json         # LangGraph CLI config
├── mcp_servers.json       # MCP servers configuration
├── schema.sql             # Database schema
├── requirements.txt       # Python dependencies
├── README.md
│
├── graph/                 # LangGraph workflow
│   ├── builder.py         # Graph construction
│   ├── nodes.py           # Node implementations
│   └── tools/
│       └── book_tool.py   # Book-related tools
│
├── models/                # Data models
│   ├── __init__.py
│   └── book.py            # Book dataclass
│
├── repository/            # Data access layer
│   └── book_repository.py # Database operations
│
├── prompts/               # System prompts
│   └── system.txt         # Assistant behavior instructions
│
└── docker/                # Docker configuration
    └── postgres/
        └── init.sql       # Database initialization script
```

## Key Technologies

- **LangGraph**: Agentic framework for orchestrating LLM workflows
- **LangChain**: Tools, models, and message handling
- **OpenAI GPT-4o**: Language model for the assistant
- **PostgreSQL**: Relational database for book storage
- **MCP (Model Context Protocol)**: Integration for additional tools and capabilities

## Configuration Files

### `mcp_servers.json`

Defines external MCP servers to integrate additional tools into the assistant.

### `langgraph.json`

LangGraph CLI configuration for deployment and testing.

### `compose.yml`

Docker Compose setup for PostgreSQL database.

## Development

To modify the assistant behavior:

1. **Change system prompt**: Edit `prompts/system.txt`
2. **Add new tools**: Create new functions in `graph/tools/` with `@tool` decorator
3. **Modify workflow**: Update `graph/builder.py` to change the graph structure
4. **Add database fields**: Update schema in `schema.sql` and `models/book.py`

## Troubleshooting

- **Missing API keys**: The app will prompt you to enter them on first run
- **Database connection errors**: Ensure PostgreSQL is running via `docker-compose up -d`
- **Tool execution errors**: Check that all dependencies are installed and tools are properly decorated

## Future Enhancements

- Stream responses from the assistant
- Add authentication and multi-user support
- Implement more sophisticated book search and filtering
- Add book recommendations based on user preferences
- Integrate with external book APIs (OpenLibrary, Google Books)
