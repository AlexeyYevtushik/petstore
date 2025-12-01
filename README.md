Here's a clean, professional README.md file without icons, following GitHub's formatting conventions:

```markdown
# Petstore API Project

A RESTful API implementation for a pet store system.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Database Schema](#database-schema)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview

This project implements a Petstore API that allows users to manage pets, store inventory, and process orders. It follows the OpenAPI specification for pet store systems.

## Features

### 1. Pet Management
- Add new pets to the store
- Update pet information
- Find pets by status
- Upload pet images

### 2. Store Management
- Inventory status monitoring
- Order processing
- Order history tracking

### 3. User Management
- User registration and authentication
- User profile management
- Session handling

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12+ or MySQL 8+
- Git

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/AlexeyYevtushik/petstore.git
cd petstore
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
# Edit .env file with your database credentials
```

5. Set up the database:
```bash
python setup_database.py
```

6. Run the application:
```bash
python app.py
```

## Usage

### Starting the Server

**Development mode:**
```bash
python app.py --dev
```

**Production mode:**
```bash
python app.py --prod
```

### Access Points

- API Documentation: http://localhost:8000/docs
- API Base URL: http://localhost:8000/api/v1
- Health Check: http://localhost:8000/health

## API Endpoints

### 1. Pet Operations

#### POST /pet
Add a new pet to the store.

**Request Body:**
```json
{
  "name": "Buddy",
  "category": "Dog",
  "status": "available"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Buddy",
  "category": "Dog",
  "status": "available",
  "created_at": "2024-01-15T10:30:00Z"
}
```

#### GET /pet/{petId}
Find pet by ID.

#### PUT /pet/{petId}
Update an existing pet.

#### GET /pet/findByStatus
Find pets by status (available, pending, sold).

#### POST /pet/{petId}/uploadImage
Upload an image for a pet.

### 2. Store Operations

#### GET /store/inventory
Returns pet inventory by status.

#### POST /store/order
Place an order for a pet.

#### GET /store/order/{orderId}
Find purchase order by ID.

#### DELETE /store/order/{orderId}
Delete purchase order by ID.

### 3. User Operations

#### POST /user
Create a new user.

#### GET /user/{username}
Get user by username.

#### PUT /user/{username}
Update user information.

#### DELETE /user/{username}
Delete user.

#### GET /user/login
Log in user.

#### GET /user/logout
Log out current user.

## Database Schema

### 1. Pets Table
- `id`: INTEGER (Primary Key, Auto Increment)
- `name`: VARCHAR(255) (Not Null)
- `category`: VARCHAR(100)
- `status`: ENUM('available', 'pending', 'sold') (Default: 'available')
- `tags`: JSON
- `photo_urls`: JSON
- `created_at`: TIMESTAMP (Default: CURRENT_TIMESTAMP)
- `updated_at`: TIMESTAMP (Default: CURRENT_TIMESTAMP, On Update)

### 2. Orders Table
- `id`: INTEGER (Primary Key, Auto Increment)
- `pet_id`: INTEGER (Foreign Key references pets.id)
- `quantity`: INTEGER (Default: 1)
- `ship_date`: TIMESTAMP
- `status`: ENUM('placed', 'approved', 'delivered') (Default: 'placed')
- `complete`: BOOLEAN (Default: false)
- `created_at`: TIMESTAMP (Default: CURRENT_TIMESTAMP)

### 3. Users Table
- `id`: INTEGER (Primary Key, Auto Increment)
- `username`: VARCHAR(100) (Unique, Not Null)
- `email`: VARCHAR(255) (Unique, Not Null)
- `password_hash`: VARCHAR(255) (Not Null)
- `first_name`: VARCHAR(100)
- `last_name`: VARCHAR(100)
- `phone`: VARCHAR(20)
- `user_status`: INTEGER (Default: 1)
- `created_at`: TIMESTAMP (Default: CURRENT_TIMESTAMP)
- `updated_at`: TIMESTAMP (Default: CURRENT_TIMESTAMP, On Update)

## Testing

### Running Tests

To run the test suite:

```bash
# Run all tests
python -m pytest

# Run tests with coverage report
python -m pytest --cov=app tests/

# Run specific test file
python -m pytest tests/test_pets.py

# Run with verbose output
python -m pytest -v
```

### Test Structure
- `tests/unit/` - Unit tests for individual components
- `tests/integration/` - Integration tests for API endpoints
- `tests/fixtures/` - Test data and fixtures

### Test Examples

Example unit test for pet creation:
```python
def test_create_pet():
    pet_data = {"name": "Max", "category": "Dog", "status": "available"}
    response = client.post("/pet", json=pet_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Max"
```

## Contributing

We welcome contributions to the Petstore project! Please follow these steps:

### 1. Fork the Repository
Fork the repository to your GitHub account.

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Changes
Implement your feature or bug fix.

### 4. Add Tests
Ensure your changes are covered by tests.

### 5. Commit Changes
```bash
git add .
git commit -m "Add: Description of your changes"
```

### 6. Push to Your Fork
```bash
git push origin feature/your-feature-name
```

### 7. Create Pull Request
Open a pull request on the original repository with a clear description of your changes.

### Coding Standards
- Follow PEP 8 for Python code
- Write meaningful commit messages
- Add docstrings for all functions and classes
- Update documentation when needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Repository Owner:** Alexey Yevtushik
- **GitHub:** [AlexeyYevtushik](https://github.com/AlexeyYevtushik)
- **Project Repository:** https://github.com/AlexeyYevtushik/petstore

## Acknowledgments

- Inspired by the OpenAPI Petstore example
- Built with FastAPI/Flask (specify your framework)
- Thanks to all contributors
```

This version:
1. **Removes all icons/emojis** for a clean, professional look
2. **Maintains proper numbering** throughout all sections
3. **Uses clear headings** with consistent formatting
4. **Includes practical examples** of API requests/responses
5. **Provides detailed database schema** with field descriptions
6. **Offers comprehensive testing instructions**
7. **Includes clear contribution guidelines**
8. **Follows GitHub's markdown best practices**
9. **Has complete contact information**
10. **Uses proper code blocks** with language specification

The README is now ready to be copied directly into your repository.
