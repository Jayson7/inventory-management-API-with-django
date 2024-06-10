# Online Store Inventory and Supplier Management API

### This project doesn't come with authentication as it was not stated in the requirements.

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd online_store
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Items

- `GET /api/items/` - List all items
- `POST /api/items/` - Create a new item
- `GET /api/items/{id}/` - Retrieve a specific item
- `PUT /api/items/{id}/` - Update a specific item
- `DELETE /api/items/{id}/` - Delete a specific item

### Suppliers

- `GET /api/suppliers/` - List all suppliers
- `POST /api/suppliers/` - Create a new supplier
- `GET /api/suppliers/{id}/` - Retrieve a specific supplier
- `PUT /api/suppliers/{id}/` - Update a specific supplier
- `DELETE /api/suppliers/{id}/` - Delete a specific supplier
