Run zookeeper:
bin/zookeeper-server-start.sh config/zookeeper.properties

Run Kafka Server:
JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties

Run CMAK UI:
bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080