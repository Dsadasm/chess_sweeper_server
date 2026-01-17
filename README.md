# Chess Sweeper Server

A Django REST API server for managing Chess Sweeper game records and user authentication.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd chess_sweeper_server
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

## Running the Server

Start the development server:

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and obtain JWT tokens
- `POST /api/auth/logout/` - Logout and blacklist refresh token
- `POST /api/token/` - Obtain JWT tokens
- `POST /api/token/refresh/` - Refresh access token
- `POST /api/token/verify/` - Verify token validity

### Daily Records

- `GET /api/dailyrecords/` - List all daily records (supports filtering)
- `POST /api/dailyrecords/` - Create a new daily record
- `GET /api/dailyrecords/{id}/` - Retrieve a specific record
- `PUT /api/dailyrecords/{id}/` - Update a record
- `DELETE /api/dailyrecords/{id}/` - Delete a record

## API Documentation

Interactive API documentation is available at:

- **Swagger UI**: `http://localhost:8000/api/schema/swagger-ui/`
- **ReDoc**: `http://localhost:8000/api/schema/redoc/`