# Library Maanagement Backend Using FastAPI

Welcome to the FastAPI project! This README provides information on setting up the project and using the API.
## Project Overview

This project is a FastAPI-based web application that serves as a backend for managing users, books, and borrowed books. It provides a RESTful API with CRUD operations for users, books, and borrowed books.

## Features

- **User Management:**
  - Create a new user.
  - Retrieve a list of users.
  - Retrieve information about a specific user.

- **Book Management:**
  - Create a new book.
  - Retrieve a list of books.
  - Retrieve information about a specific book.
  - Retrieve details of a specific book.
  - Update details of a specific book.

- **Borrowed Book Management:**
  - Borrow a book.
  - Return a borrowed book.
  - Retrieve a list of borrowed books.

## Setup Instructions

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### 1. Clone the Repository

```bash
git clone https://github.com/krishantt/library-management.git
cd library-management
```
### 2. Build and Run the Docker Container

```bash

docker build -t librry-management .
docker run -p 8000:8000 -t library-management
```

### 3. Access the API

Visit http://localhost:8000/docs in your web browser to access the FastAPI Swagger documentation. Alternatively, you can use http://localhost:8000/redoc for ReDoc documentation.
## API Documentation Endpoints

    GET /users/

    Retrieves a list of users.

    GET /users/{user_id}

    Retrieves information about a specific user.

    POST /users/

    Creates a new user.

    GET /books/

    Retrieves a list of books.

    GET /books/{book_id}

    Retrieves information about a specific book.

    POST /books/

    Creates a new book.

    GET /books/{book_id}/details

    Retrieves details of a specific book.

    PUT /books/{book_id}/details

    Updates details of a specific book.

    GET /borrowed-books/

    Retrieves a list of borrowed books.

    POST /borrowed-books/

    Borrows a book.

    PUT /borrowed-books/{book_id}/return

    Returns a borrowed book.
