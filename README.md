# Weather API Project

## About
This project is an API for retrieving weather data. It uses data from OpenWeatherMap API and stores it in Django database for quick access.

## Installation

Ensure your environment is set up with the following:

1. **Python version 3.x**, **Docker** and **Docker Compose** are installed.

2. Clone the repository:
    ```bash
    git clone -b test_task https://github.com/uluk001/Weather_site.git
    ```

3. Navigate to the project directory:
    ```bash
    cd Weather_site
    ```

4. Create a .env file in the root directory of the project and add the following variables:
    ```bash
    SECRET_KEY=your_secret_key
    OPENWEATHERMAP_API_KEY=your_openweathermap_api_key # Get it from https://openweathermap.org/api
    ```

5. Up the docker containers:
    ```bash
    docker-compose up -d --build
    ```

6. Create a superuser:
    ```bash
    docker-compose exec weather_app python manage.py createsuperuser
    ``` 


## Usage

Navigate to http://localhost:8000/weather/?city=<city_name> to get the weather data for the city.

Navigate to http://localhost:8000/admin/ to access the admin panel.
