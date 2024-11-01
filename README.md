# Start kafka from docker
```docker run -d -p 9092:9092 --name broker apache/kafka:latest```

## ref
```https://github.com/apache/kafka/blob/trunk/docker/examples/docker-compose-files```

# Kafka Producer, Consumer, and Topic Monitor Scripts

This project provides scripts for producing, consuming, and monitoring Kafka topics using the
`kafka-python` library.

## Directory Structure

```
.
├── .gitignore
├── README.md
├── consumer.py
├── monitor_topic.py
├── producer.py
└── requirements.txt
```

## Requirements

- `python 3.11.1`
- `kafka-python` library (version 2.0.2)

## Setup

1. **Create a Virtual Enviroment**

    It is recommended to use a virtual environment to manage dependencies:
    ```
    python -m pip install --user virtualenv
    python -m venv .venv
    source .venv/bin/active # On Windows, use .venv\Scripts\activate
    ```
   
2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
   
   Ensure that your `requirements.txt` contains:
   
   ```
   kafka-python==2.0.2
   ```

## Usage

### 1. Producer script
The `producer.py` script sends message to a specified kafka topic at a configurable rate.

#### Command

```
python produce.py
```

- `<bootstrap_server>`: Kafka server address (e.g `localhost:9092`)
- `<topic>`: kafka topic name
- `<num_partitions>`: Number of partitions for the topic
- `<messages_per_second>`: Rate at which messages will send

The script will recreate the topic with the specified number of partitions before starting message production.

#### Example

```
python produce.py
```

This command creates a `test_topic` with 3 partitions and sends 5 messages per second.


# Quick start
```
docker-compose up -d
```
## Verify docker images are running
```docker ps```

Make sure kafka is running at `localhost:9092`, use `Offset Explorer` or `Datagrip` to connect

## Run following command in separate console (3)
```
python producer.py
python consumer.py
python monitor_topic.py
```