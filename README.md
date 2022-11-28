# RabbitMQParser
Quick program for extracting RabbitMQ messages from the management studio

# How to extract data

1. Log into your RabbitMQ Management console
2. go to Queues select your Queue
3. Scroll down to Get Messages, select Ack mode (Ack - consume and pop, Nack - remain in Queue) and number of Messages
4. Click on Get Message(s)
5. Copy HTML of all messages and paste it in the rabbitHTML.txt File
6. Run the program, and it will automatically export all records
