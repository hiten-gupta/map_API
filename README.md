# 🗺️ Django Map API – Technical Assessment

## 📋 Project Description

This is a Django REST API that provides map location data and basic statistics. It was built as part of a backend technical assessment using:

- Django REST Framework (DRF)
- GeoJSON format for location data
- Basic statistics endpoint
- Django Admin for data management
- A minimal frontend (HTML + JavaScript) to display location data dynamically

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   git clone https://github.com/hiten-gupta/django-map-api.git
   cd django-map-api
Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Run migrations
python manage.py migrate
**(Optional) Create a superuser**
python manage.py createsuperuser
**Start the development server**
python manage.py runserver
**🔐 Superuser Credentials**
For convenience, a superuser has already been created:

Username: hiten
Password: Devilman@34(created for fun)
Email: guptahiten534@gmail.com
You can use these credentials to log into the Django admin panel at:
http://127.0.0.1:8000/admin/ (same address for map just remove admin)
Sample Locations
The following locations are pre-loaded into the project:

![image](https://github.com/user-attachments/assets/3c59ec9f-b78d-412d-99e8-925fe11305c2)

API Endpoints
/api/locations/
Returns a list of all locations in GeoJSON format.

/api/stats/
Returns basic statistics such as:

Total number of locations

Most common category

Frontend Demo
To test the API visually, a simple frontend has been included using HTML + JavaScript.

Open templates/map.html in your browser.

It will fetch data from the API and display map markers accordingly.
**Notes**
db.sqlite3 is included with preloaded data for quick testing.

Make sure to allow API access via CORS or run everything locally.

