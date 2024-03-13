# TweeterSphere

TweeterSphere is a social media platform inspired by Twitter. Users have the ability to sign up, create, like, and update posts, follow other profiles, and gain followers. Additionally, users can update their profile information and add a profile image.
The project was made using a popular python web framework known as Django.

## Getting Started

To get started with TweeterSphere, follow the instructions below:


### Installation

1. Clone the repository:

```
git clone https://github.com/Rhythm1821/TweeterSphere
```


2. Navigate to the project directory:

```
cd TweeterSphere
```


3. Create a virtual environment:

```
python3 -m venv venv
```


4. Activate the virtual environment:

```
source venv/bin/activate
```


5. Install dependencies:

```
pip install -r requirements.txt
```


### Database Setup

6. Run database migrations:

```
python3 manage.py migrate
```


### Running the Server

7. Start the development server:

```
python3 manage.py runserver
```

You can now access TweeterSphere at http://127.0.0.1:8000/ in your web browser.


### Installation (with docker and MySQL as the database)

Add your credentials to .env file

1. Clone the repository:

```
git clone https://github.com/Rhythm1821/TweeterSphere
```


2. Navigate to the project directory:

```
cd TweeterSphere
```


3. Login to MySQL server(inside the quotes your actual password should be there and same in you .env file):

```
 mysql -u root -p'password'
```

### Database Setup

4. Create new database and exit:

```
CREATE DATABASE tweetersphere;
EXIT;
```


5. Ensure no container is running:

```
docker ps (if running do "docker kill {container_id}")
```

6. Uncomment this line in .env

```
DOCKER_COMPOSE=1
```


### Build the container

7. Start building the container:

```
docker compose up --build
```

You can now access TweeterSphere at http://127.0.0.1:8000/ in your web browser.
