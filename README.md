# LinkCrate API

This project allows user to add and manage bookmarks using FastAPI. It uses [uv](https://docs.astral.sh/uv/), an extremely fast Python package and project manager, written in Rust.

## Technologies

- Pyhton 3.12
- [uv](https://docs.astral.sh/uv/) for package management
- SQLite as the database
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) for data migration

## Installation

1. Clone the repository.

    ```bash
    git clone https://github.com/mdauthentic/linkcrate
    cd linkcrate
    ```

2. Start the application

    ```bash
    uv run fastapi dev
    ```

## Endpoints

### Create bookmark

Creates a new bookmark from a link. The response include the metadata about the link.

```bash
curl -H "Content-Type: application/json" \
     -X POST http://localhost:8000/bookmarks
     -d '{ "url": "https://wwww.example.com/" }'

## Returns

{
  "title": "",
  "description": "",
  "url": "https://www.example.com",
  "id": 1
}
```

### Retrieve a link

```bash
curl -H "Content-Type: application/json" \
     -X GET http://localhost:8000/bookmarks/1

## Returns
{
  "title": "Link title",
  "description": "the description of the link",
  "url": "https://www.example.com/",
  "id": 1
}
```

### Retrieve all links

Retrieves a list of all links.

```bash
curl -H "Content-Type: application/json" \
     -X GET http://localhost:8000/bookmarks

## Returns
[
    {
    "title": "Link title",
    "description": "the description of the link",
    "url": "https://www.example.com/",
    "id": 1
    },
    {
    "title": "Link title 2",
    "description": "the description2 of the link",
    "url": "https://www.example2.com/",
    "id": 2
    }
]
```

### Delete a link

```bash
curl -X DELETE http://localhost:8000/bookmarks
```
