[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&labelColor=333333&logo=Python&logoColor=yellow)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-3.15.2-092E20?style=flat&labelColor=333333&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.3-336791?style=flat&labelColor=333333&logo=PostgreSQL&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker--2496ED?style=flat&labelColor=333333&logo=Docker&logoColor=white)](https://www.docker.com/)
[![Docker Compose](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat&labelColor=333333&logo=Docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/Nginx-1.26.1-269539?style=flat&labelColor=333333&logo=Nginx&logoColor=white)](https://www.nginx.com/)
[![Psycopg2-binary](https://img.shields.io/badge/Psycopg2--binary-2.9.9-4169E1?style=flat&labelColor=333333)](https://pypi.org/project/psycopg2-binary/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-22.0.0-FFD700?style=flat&labelColor=333333&logo=Gunicorn&logoColor=white)](https://gunicorn.org/)
[![djoser](https://img.shields.io/badge/djoser-2.2.3-blue?style=flat&labelColor=333333&logo=django&logoColor=white&color=blue)](https://djoser.readthedocs.io/en/latest/getting_started.html)

[![Flake8](https://img.shields.io/badge/flake8-checked-blueviolet?style=flat&labelColor=333333)](https://flake8.pycqa.org/en/latest/)
[![isort](https://img.shields.io/badge/isort-checked-violet?style=flat&labelColor=333333)](https://pycqa.github.io/isort/)

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
3. Install [`Docker`](https://www.docker.com/)
   and [`Docker Compose`](https://docs.docker.com/compose/) for your operating system.


4. Start the project from root directory:
 ```sh
docker-compose up -d --build
```
5. Execute the commands one at a time:
```sh
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```


#### Open your web browser and navigate to http://localhost:80 to access the application.

## Usage

Once the development server is running, you can access the API at http://127.0.0.1:80/.
You can use tools like curl, Postman, or any REST client to interact with the API endpoints.

For example, to view the list of posts, you can send a GET request to /api/v1/posts/, and you will receive a list of posts.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. 
For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.