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