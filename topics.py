from confluent_kafka.admin import AdminClient

# Replace with your Kafka broker
kafka_broker = '34.68.55.43:9094,34.136.142.41:9094,34.170.19.136:9094'
# kafka_broker = "127.0.0.1:29092"

# Initialize AdminClient
admin_client = AdminClient({'bootstrap.servers': kafka_broker})

topic_metadata = admin_client.list_topics(timeout=10)

topic_name = 'Topic1'
to2 = "Topic2"

if  topic_name in topic_metadata.topics:
    partitions = topic_metadata.topics[topic_name].partitions
    num_partitions = len(partitions)
    print(f"Number of partitions for topic '{topic_name}': {num_partitions}")

if  to2 in topic_metadata.topics:
    partitions = topic_metadata.topics[to2].partitions
    num_partitions = len(partitions)
    print(f"Number of partitions for topic '{to2}': {num_partitions}")

else:
    print(f"Topic '{topic_name}' does not exist")
