## Property Management System (Backend)

A basic Django-based backend API for managing property units, landlords, tenants, and leases.

##  Features

- Manage Contacts (Landlords & Tenants)
- Manage Property Units
- Lease Creation and Management
- Dashboard Endpoint:
  - Total units with status (Occupied/Vacant)
  - Landlord-unit relationships
  - Rent income summary
- Index Endpoint:
  - Shows linked test data (unit + lease + tenant + landlord)

##  Tech Stack

- **Backend**: Django REST Framework
- **Database**: PostgreSQL
- **API Docs**: Swagger / DRF Docs

##  Setup

```bash
# Clone the repo
git clone https://github.com/Parkash9967/Property-Management-System.git
cd Property-Management-System

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Migrate DB and run
python manage.py migrate
python manage.py runserver



📑 API Documentation (Swagger)
Interactive Swagger UI is auto-generated and available after running the server:

🌐 Open in browser: http://localhost:8000/swagger/

✅ Available Endpoints

Module	Description
/contacts/	CRUD for landlords & tenants
/units/	Manage property units and assign landlords
/leases/	Create/view lease info
/dashboard/	Total units, rent summary, landlord units
/index/	Display all linked test data
Each endpoint includes:

Input and output schemas

Dropdown fields (e.g., Contact Type)

Example requests/responses

Powered by drf-yasg Swagger integration.

🧪 Test Data
Pre-loaded:

Landlord: John Doe

Tenant: Jane Smith

Unit: A1 (Apartment, Occupied)

Lease: Monthly rent linked to above

