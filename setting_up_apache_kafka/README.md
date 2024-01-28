# Setting up Apache Kafka using Docker

This guide is taken from [this article](https://www.baeldung.com/ops/kafka-docker-setup).

It is a more minimal Kafka setup than the tutorials you'll find on their official website, where they encourage you to set up the entire confluent workstation.

## Setup

You have to start a Zookeeper server before the Kafka server, and make sure that it stops after the Kafka server stops.

Zookeeper will connect to Kafka on port 2181, but it'll be listening to requests from localhost on 22181.

The Kafka server will be listening to requests from localhost on port 29092.

So your client applications will connect to the Kafka broker on port 29092.
