# Ukrainian Poem on Flask

## Introduction

This project is a simple Flask application that displays a Ukrainian poem on a web page. The app can be run locally or on a remote host.

## Requirements

- Python 3.8 or higher
- Flask
- Docker

## Installation

### Local Deployment

1. **Clone the Repository:**

    ```bash
    git clone [Your GitHub Repository URL]
    ```

2. **Install Dependencies:**

    ```bash
    pip install Flask
    ```

3. **Run the Application:**

    ```bash
    python app.py
    ```

After that, open your web browser and navigate to `http://localhost:5000` to verify.

### Remote Deployment via Docker

1. **Clone the Repository:**

    ```bash
    git clone [Your GitHub Repository URL]
    ```

2. **Build the Docker Image:**

    ```bash
    docker build -t ukrainian-poem-app .
    ```

3. **Run the Docker Image:**

    ```bash
    docker run -p 8080:8080 ukrainian-poem-app
    ```

4. **Running on a Remote Host:**

    If you want to run this app on a remote host, you'll need to specify the host's IP address when launching the Docker container:

    ```bash
    docker run -p [HOST_IP_ADDRESS]:8080:8080 ukrainian-poem-app
    ```

Now the application will be accessible at `[HOST_IP_ADDRESS]:8080` on the Internet.

## License

This project is distributed under the MIT License. See `LICENSE` file for more details.

