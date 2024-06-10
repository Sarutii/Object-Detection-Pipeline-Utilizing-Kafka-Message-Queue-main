# Object-Detection-Pipeline-Utilizing-Kafka-Message-Queue
## Description

This project implements an object detection algorithm pipeline using Kafka as a message queue and the OpenCV library for image processing. The pipeline is designed to handle real-time data streams efficiently, enabling scalable and robust object detection.


# Object Detection Pipeline with Kafka and OpenCV

## How to Use

### Step 1: Start Docker Services
First, ensure that Zookeeper and Kafka are running using Docker Compose.

1. Open a terminal.
2. Navigate to the directory containing `/kafkaDockerImage/docker-compose.yml`.
3. Run the following command to start the Docker services:

    ```bash
    docker-compose up -d
    ```
    - To check that the docker image started successfully
    ```bash
     docker-compose logs kafka | grep -i started
    ```


### Step 2: Create Kafka Topics
Next, create the necessary Kafka topics using the provided `topics.py` script.

1. Ensure the virtual environment is set up and dependencies are installed:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Run the `admin.py` script:

    ```bash
    python admin.py
    ```

### Step 3: Start Consumers
Start the consumer services to listen for messages from Kafka topics.

1. In one terminal, run the first consumer:

    ```bash
    source venv/bin/activate
    python consumer2.py
    ```

2. In another terminal, run the second consumer:

    ```bash
    source venv/bin/activate
    python consumer3.py
    ```

### Step 4: Start the Application
Finally, start the main application that processes the data.

1. In a new terminal, run the app:

    ```bash
    source venv/bin/activate
    python app.py
    ```

### Step 5: Open the Browser
Open your web browser and navigate to the `http://localhost:5000` to interact with the application.

By following these steps, you'll have the full object detection pipeline up and running, ready to process real-time data streams using Kafka and OpenCV.