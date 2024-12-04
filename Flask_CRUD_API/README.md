# Flask Laptop Management API

This is a simple Flask application that provides an API for managing laptops. The API has various endpoints to add, retrieve, update, and delete laptops. Postman can be used to test these endpoints.

## Base URL
The base URL for the API is: http://localhost:5000


### Endpoints

#### 1. Add a Laptop (POST /laptops/add)
Adds a new laptop to the database.

##### Request
- **Method**: POST
- **URL**: `http://localhost:5000/laptops/add`
- **Headers**: 
  - Content-Type: application/json
- **Body (JSON)**: 
```json
{
    "name": "hp004",
    "laptop_number": "20305",
    "specifications": "Intel i7, 16GB RAM, 512GB SSD"
}

