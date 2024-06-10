from confluent_kafka.admin import AdminClient, NewTopic

# kafka_broker = '34.68.55.43:9094,34.136.142.41:9094,34.170.19.136:9094'
kafka_broker = "127.0.0.1:29092"

conf = {'bootstrap.servers': kafka_broker}
ac = AdminClient(conf)

me = 'MohamedAdlyServer5'

topic = me

res = ac.create_topics([NewTopic(topic, num_partitions=3)])

res[topic].result()

