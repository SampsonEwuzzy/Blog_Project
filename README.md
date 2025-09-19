WuzziBlog: A Full-Stack Django Blog Platform 💻
WuzziBlog is a robust, full-featured blog application built with the Django web framework. It provides a simple yet powerful platform for creating, managing, and sharing content.

Features ✨
User Authentication: Secure user registration, login, and logout.

Post Management: Users can create, edit, and delete their own blog posts.

Rich Text Editor: A modern rich text editor powered by CKEditor for easy and flexible post formatting.

Categorization: Organize posts by categories for better navigation.

Search Functionality: A search bar to find posts by title or content.

Responsive Design: A clean, mobile-friendly interface built with Bootstrap 5.

Database: Uses PostgreSQL for a production-ready database solution.

Deployment: Ready for deployment on platforms like Render.

Technology Stack 🛠️
Backend: Django

Frontend: HTML5, CSS3, JavaScript, Bootstrap 5

Database: PostgreSQL

Rich Text Editor: CKEditor

Deployment: Render, Gunicorn, Whitenoise

Installation and Local Setup 🚀
To get a copy of this project up and running on your local machine, follow these steps.

Clone the Repository:

Bash

git clone https://github.com/yourusername/wuzziblog.git
cd wuzziblog
Create and Activate a Virtual Environment:

Bash

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install Dependencies:

Bash

pip install -r requirements.txt
Database Setup:

Create a .env file in the root directory and add your SECRET_KEY.

For local development, the default sqlite3 database is sufficient.

Run migrations to set up the database schema:

Bash

python manage.py migrate
Create a Superuser:

Bash

python manage.py createsuperuser
Run the Development Server:
python manage.py runserver
Your blog should now be running at http://127.0.0.1:8000/.

Contribution 🤝
Feel free to fork the repository, make improvements, and submit a pull request!

License 📝
This project is licensed under the MIT License.

