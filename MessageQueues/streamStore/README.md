# Kafka Stream Store Example

## What is Kafka and why it is used

Apache Kafka is a distributed event streaming platform used to build real-time data pipelines and streaming applications. It stores and processes streams of records in a fault-tolerant, scalable, and durable way.

Kafka is used because it can:
- handle large volumes of data with high throughput
- provide reliable message delivery with replication
- support decoupled microservices by using topics as shared event channels
- store event history so consumers can replay data

## Why Docker is used

Docker is used to package applications and their dependencies into containers so they run consistently across environments. For Kafka, Docker makes it easy to:
- start Kafka with a single command
- keep configuration isolated from the host system
- avoid installing Kafka binaries locally
- reproduce the same environment for all developers

## Setup of Docker Compose

This project uses `docker-compose.yaml` to run Kafka and the required services together.

### Key sections in `docker-compose.yaml`

- `version`: Specifies the Compose file format version.
- `services`: Defines each container that will run.
- `zookeeper`: A service that Kafka depends on for cluster coordination.
- `kafka`: The Kafka broker service that accepts and stores messages.
- `ports`: Maps container ports to the host machine.
- `environment`: Sets environment variables used by the services.
- `volumes`: Stores data outside the container so it persists across restarts.
- `depends_on`: Ensures services start in the correct order.

### Common Docker Compose keywords explained

- `image`: The Docker image used to create the container.
- `container_name`: A custom name assigned to the running container.
- `restart`: Container restart policy when it stops.
- `environment`: Variables passed into the container at runtime.
- `ports`: Host:container port mapping.
- `volumes`: File system paths shared between host and container.
- `depends_on`: Service startup order dependency.

## Kafka concepts

### Topic
A topic is a named stream of records. Producers write messages to topics, and consumers read messages from topics.

### Partition
A topic is divided into partitions. Each partition stores ordered messages and enables Kafka to scale horizontally.

### Producer
A producer is an application that sends messages to a Kafka topic.

### Consumer
A consumer is an application that reads messages from one or more Kafka topics.

### Consumer Group
A consumer group is a set of consumers that work together to read from a topic. Kafka distributes partitions among consumers in the same group.

### Broker
A Kafka broker is a server process that stores and serves topic data.

### Offset
An offset is the position of a message within a partition. Consumers use offsets to track which messages they have processed.

### Retention
Retention is how long Kafka keeps messages in a topic before deleting them.

## How to create a virtual environment using `uv`

If someone clones this project and wants to set it up locally, they can follow these steps:

1. Open a terminal in the project folder.
2. Create a virtual environment:
   ```bash
   uv env create
   ```
3. Activate the virtual environment:
   - On Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
4. Install dependencies if a `pyproject.toml` or `requirements.txt` exists:
   ```bash
   uv install
   ```

## Project usage

This repository contains:
- `producer.py`: sends messages to Kafka topics
- `consumer.py`: reads messages from Kafka topics
- `docker-compose.yaml`: starts Kafka and its dependencies

### Starting the project

1. Start Docker Compose:
   ```bash
   docker compose up
   ```
2. Run the producer or consumer in the activated virtual environment:
   ```bash
   uv run producer.py
   uv run consumer.py
   ```

### Notes

- Ensure Docker is installed and running before using `docker compose up`.
- Use `docker compose down` to stop and remove containers.
- If you need a fresh Kafka environment, add the `kafka-data/` folder contents and restart Docker Compose.
