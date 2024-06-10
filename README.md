# Real-Time Object Detection Pipeline with Kafka and OpenCV

## Overview

This project sets up a real-time object detection pipeline. It utilizes Kafka for handling data streams and OpenCV for image processing tasks.

## Setup Guide

### Step 1: Start Docker Services
Ensure Zookeeper and Kafka are running using Docker Compose.

1. Open your terminal.
2. Navigate to the directory containing the Docker Compose file (`/kafkaDockerImage/docker-compose.yml`).
3. Start the Docker services with:

    ```bash
    docker-compose up -d
    ```
4. Verify Kafka has started successfully:

    ```bash
    docker-compose logs kafka | grep -i started
    ```

### Step 2: Initialize Kafka Topics
Create necessary Kafka topics using the `admin.py` script.

1. Set up the virtual environment and install required dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Run the script to create topics:

    ```bash
    python admin.py
    ```

### Step 3: Launch Consumers
Start the consumers to listen for Kafka topic messages.

1. In one terminal, activate the virtual environment and run the first consumer:

    ```bash
    source venv/bin/activate
    python consumer2.py
    ```

2. In a separate terminal, activate the virtual environment and run the second consumer:

    ```bash
    source venv/bin/activate
    python consumer3.py
    ```

### Step 4: Start the Main Application
Run the main application to begin processing data.

1. In a new terminal, activate the virtual environment and start the app:

    ```bash
    source venv/bin/activate
    python app.py
    ```

### Step 5: Access the Web Interface
Open your web browser and navigate to `http://localhost:5000` to use the application.

By following these instructions, you'll have a fully operational object detection pipeline capable of processing real-time data streams using Kafka and OpenCV.
