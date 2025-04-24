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
