import datetime
import time

from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import UnknownTopicOrPartitionError


def dt_str() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def recreate_topic(bootstrap_server, topic, num_partitions):
    """Delete the existing Kafka topic if it exists, then create a new one with the specified number of partitions."""
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_server)

    # Try to delete the topic if it exists
    try:
        admin_client.delete_topics([topic])
        print(f"[{dt_str()}]: Topic {topic} deleted")
        # Allow some time for the topic deletion to propagate
        time.sleep(2)
    except UnknownTopicOrPartitionError:
        print(f"[{dt_str()}]: Topic {topic} does not exist. Creating a new one.")

    # Define the topic configuration
    topic_config = NewTopic(name=topic, num_partitions=num_partitions, replication_factor=1)

    # Create a topic
    admin_client.create_topics([topic_config])

    print(f"[{dt_str()}]: Topic {topic} created with {num_partitions} partitions.")

    admin_client.close()



def produce_messages(bootstrap_server, topic, num_partitions, messages_per_second):
    """Kafka message produce script."""
    # Recreate the topic with the specified number of partitions
    recreate_topic(bootstrap_server, topic, num_partitions)


if __name__ == '__main__':
    produce_messages("localhost:9092", "test_topic", 3, 5)
