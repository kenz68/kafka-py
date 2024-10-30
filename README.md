# Kafka Producer, Consumer, and Topic Monitor Scripts

This project provides scripts for producing, consuming, and monitoring Kafka topics using the
`kafka-python` library. The scripts utilize `click` for command-line argument parsing and SSL for 
secure communication with Kafka.

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

- Python 3.12.3
- `kafka-python` library (version 2.0.2)
- `click` library (version 8.1.7)

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
   click==8.1.7
   ```

## Usage

### 1. Producer script
The `producer.py` script sends message to a specified kafka topic at a configurable rate.

#### Command

```
python produce.py <bootstrap_server> <topic> <num_partitions> <messages_per_second>
```

- `<bootstrap_server>`: Kafka server address (e.g `localhost:9092`)
- `<topic>`: kafka topic name
- `<num_partitions>`: Number of partitions for the topic
- `<messages_per_second>`: Rate at which messages will sent

The script will recreate the topic with the specified number of partitions before starting message production.

#### Example

```
python produce.py localhost:9092 test_topic 3 5
```

This command creates a `test_topic` with 3 partitions and sends 5 messages per second.