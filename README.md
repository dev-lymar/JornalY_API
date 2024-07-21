[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=Python&logoColor=yellow)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.15.1-092E20?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Flake8](https://img.shields.io/badge/flake8-checked-blueviolet?style=flat)](https://flake8.pycqa.org/en/latest/)
[![isort](https://img.shields.io/badge/isort-checked-violet?style=flat)](https://pycqa.github.io/isort/)

# JornalY_API

### Table of contents:
- [Project Description](#Project-Description)
- [Getting Started](#Getting-Started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Project Description
***Built with Django 5 and Django REST Framework (DRF), this web application offers robust functionality for managing users, posts, and social interactions through a RESTful API.*** 

***Key features include:***

**Post Management**
 - Create Posts: Users can create new posts and attach images to them.
 - Edit Posts: Authors can edit the content of their own posts.
 - Comments: Users can add comments to posts.
 - Tags: Users can create and assign tags to posts to categorize content.

**Social Features**
 - Subscriptions: Users can subscribe to and unsubscribe from other authors to follow their posts.

**Testing**
 - All features have been thoroughly tested to ensure reliability and functionality.


## Getting Started
**To get started with the project, follow these steps:**
1. Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/dev-lymar/JornalY_API.git
cd JornalY_API
```
2. Configure .env
```sh
replace env.example with your data
```
3. Set Up a Virtual Environment on your machine


4. Install the required dependencies:
 ```sh
pip install -r requirements.txt
```
5. Run migrations:
```sh
python manage.py migrate
```
6. Create a superuser:
```sh
python manage.py createsuperuser
```
7. Run the development server:
```sh
python manage.py runserver
```

## Usage

Once the development server is running, you can access the API at http://127.0.0.1:8000/.
You can use tools like curl, Postman, or any REST client to interact with the API endpoints.

For example, to view the list of posts, you can send a GET request to /api/v1/posts/, and you will receive a list of posts.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. 
For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.