
# BookQL

BookQL is a GraphQL-based API project built using Django and Strawberry GraphQL. This project provides CRUD operations on books through queries and mutations, utilizing session-based authentication.

## Features

- **GraphQL API**: Perform CRUD operations on books using GraphQL queries and mutations.
- **Django Integration**: Built on top of Django, leveraging its ORM and authentication system.
- **Session-Based Authentication**: Uses Django's session-based authentication to secure the API.
- **Schema and Types**: Includes GraphQL schema, Strawberry Django types, and input definitions for managing books.

## Requirements

- Python 3.x
- Django 3.x or higher
- Strawberry GraphQL

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/samikshakhadka/BookQL.git
   cd BookQL
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for accessing the Django admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

### Accessing the GraphQL API

Once the development server is running, you can access the GraphQL API by navigating to:

```
http://localhost:8000/graphql/
```

### Performing CRUD Operations

You can perform CRUD operations on books using the following GraphQL queries and mutations:

- **Create a Book**:
  ```graphql
  mutation {
    createBook(input: { title: "New Book", author: "Author Name", description: "Book Description" }) {
      book {
        id
        title
        author
        description
      }
    }
  }
  ```

- **Retrieve a Book**:
  ```graphql
  query {
    book(id: 1) {
      id
      title
      author
      description
    }
  }
  ```

- **Update a Book**:
  ```graphql
  mutation {
    updateBook(id: 1, input: { title: "Updated Title" }) {
      book {
        id
        title
        author
        description
      }
    }
  }
  ```

- **Delete a Book**:
  ```graphql
  mutation {
    deleteBook(id: 1) {
      success
      message
    }
  }
  ```

### Authentication

BookQL uses session-based authentication. Ensure that you are logged in before performing mutations. You can log in via the Django admin panel or through a custom login mutation if implemented.

## Schema and Types

The project includes the following key components:

- **Schema**: Defines the available queries and mutations.
- **Types**: Defines the Django models that are exposed via the API using Strawberry's `@strawberry.django.type`.
- **Inputs**: Defines the input types for creating and updating books.

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.


