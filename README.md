# Restaurant Management System

## Overview
The Restaurant Management System is a web application that allows restaurant managers to manage reservations, orders, menus, and staff. It is built using Django (Python) for the backend framework by Olalekan Onifade.

## Features
- User registration and authentication
- Table reservation management
- Menu management
- Order management
- Staff management

## Technologies Used
- Python
- Django
- SQLite (default database, can be replaced with PostgreSQL or MySQL)
- HTML/CSS for front-end

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/locustbea/restaurant_management_system.git
    cd restaurant_management_system
    ```

2. Set up a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Directory Structure

restaurant_management_system/
├── restaurant_management_system/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── reservations/
│ ├── migrations/
│ ├── templates/
│ │ └── reservations/
│ │ ├── reservation_detail.html
│ │ ├── reservation_list.html
│ │ ├── index.html
│ │ ├── reservation_form.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── orders/
│ ├── migrations/
│ ├── templates/
│ │ └── orders/
│ │ ├── order_detail.html
│ │ ├── order_list.html
│ │ ├── order_form.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── menu/
│ ├── migrations/
│ ├── templates/
│ │ └── menu/
│ │ ├── menu_detail.html
│ │ ├── menu_list.html
│ │ ├── menu_form.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── staff/
│ ├── migrations/
│ ├── templates/
│ │ └── staff/
│ │ ├── staff_detail.html
│ │ ├── staff_list.html
│ │ ├── staff_form.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── manage.py
└── requirements.txt

markdown


## Usage
1. Register and log in as a user.
2. Manage tables, reservations, and orders.
3. Add and update menu items.
4. Manage staff information.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
