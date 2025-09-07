# Payment Gateway API

A lightweight and secure payment gateway built with **FastAPI**, designed to handle merchant–customer transactions with reliability and scalability in mind.  

This project demonstrates secure authentication, role-based access, and ACID-compliant database transactions—making it a strong foundation for production-ready financial services.

---

## Features

- **User Management**
  - Register and login as a `customer` or `merchant`
  - Role-based access control
  - JWT authentication for secure session handling

- **Payments**
  - Customer-to-merchant transactions
  - Reliable commits with retry logic
  - ACID-compliant database operations

- **Security**
  - Password hashing
  - Token-based authentication
  - Input validation with Pydantic

- **Testing**
  - Pytest for integration and unit tests
  - Fixtures for clean database setup
  - Automated workflows for regression prevention

---

## Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)  
- **Database:** SQLAlchemy + SQLite (dev) / PostgreSQL (prod-ready)  
- **Auth:** JWT (PyJWT)  
- **Testing:** Pytest  
- **Deployment:** Docker-ready  

---

## Project Structure

- **main.py** → Starts the FastAPI server and includes all routes.  
- **models.py** → Defines the database tables (Users, Transactions, etc.).  
- **schemas.py** → Pydantic models for validating API requests and responses.  
- **auth.py** → Handles authentication (JWT tokens, password hashing).  
- **database.py** → Manages database connection and sessions.  
- **routes/users.py** → Contains user-related endpoints (register, login).  
- **routes/transactions.py** → Contains transaction-related endpoints (create, view transactions).  
- **tests/test_users.py** → Tests for user registration and login functionality.  
- **tests/test_transactions.py** → Tests for creating and viewing transactions.  
- **requirements.txt** → Lists dependencies for the project.  

## Quick Start

 1. Clone the repo -> 
git clone https://github.com/maazkashif/payment-gateway-api.git
cd payment-gateway-api 

 2. Create and activate virtual environment ->
python -m venv .venv
source .venv/bin/activate   
.venv\Scripts\activate      

3. Install dependencies ->
pip install -r requirements.txt

4. Run the server ->
uvicorn app.main:app --reload

5. Run tests ->
pytest

📖 API Endpoints

Users :
POST /users/register → Register new customer/merchant
POST /users/login → Authenticate and get JWT

Transactions :
POST /transactions/ → Create a payment transaction (customer → merchant)
GET /transactions/ → Fetch transaction history

🔮 Future Improvements
- Add support for multiple currencies
- Implement webhook notifications for completed payments
- Introduce payment refunds and reversals
- Extend to microservices architecture


