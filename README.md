# Django Product Catalog

A Django-based web application for managing and displaying a product catalog. This project includes features such as category-based product listing, responsive design, and dynamic product details.

## Features

- Category management with images.
- Product management with multiple images and detailed descriptions.
- Responsive design for mobile and desktop views.
- Dynamic filtering of products based on selected categories.
- Clean and intuitive user interface with Tailwind CSS.

## Installation

### Prerequisites

- asgiref==3.8.1
- Django==5.0.6
- pillow==10.3.0
- sqlparse==0.5.0
- tzdata==2024.1


### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Mathurdanduprolu/Django_Product_Catalog.git
   cd django-product-catalog
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the migrations:**

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```sh
   python manage.py createsuperuser
   ```

6. **Collect static files:**

   ```sh
   python manage.py collectstatic
   ```

7. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

8. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

```plaintext
your_project/
    ├── catalog/
    │   ├── migrations/
    │   ├── static/
    │   │   └── catalog/
    │   ├── templates/
    │   │   └── catalog/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── static/
    │   └── logo/
    │       └── logo.jpg
    ├── media/
    │   └── categories/
    ├── your_project/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── .gitignore
    ├── LICENSE
    ├── manage.py
    └── requirements.txt
```
