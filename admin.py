from confluent_kafka.admin import AdminClient, NewTopic

kafka_broker = '34.68.55.43:9094,34.136.142.41:9094,34.170.19.136:9094'
# kafka_broker = "127.0.0.1:29092"

conf = {'bootstrap.servers': kafka_broker}
ac = AdminClient(conf)



res = ac.create_topics([NewTopic("Topic1", num_partitions=3), NewTopic("Topic2", num_partitions=3)])

res["Topic1"].result()

res["Topic2"].result()
