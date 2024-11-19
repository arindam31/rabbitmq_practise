# Setup

Note: Install these things before you start:
Erlang OTP (v 27) from https://www.erlang.org/downloads
Download rabbbit mq installer: https://github.com/rabbitmq/rabbitmq-server/releases/download/
Also on windows, add the path to environ PATH (e.g) >
> `C:\Program Files\RabbitMQ Server\rabbitmq_server-4.0.3\sbin`

### Connection issue
If you cannot execute on windows, any command using "rabbitmqctl", then 
here are the things you can do:
- check log file
  C:\Users\<user_name>\AppData\Roaming\RabbitMQ\log

- check one more file in below folder.
  C:\Windows\System32\config\systemprofile
  .erlang.cookie
- copy this file in C:\Users\<user_name>\ and replace the file. [Refer: https://stackoverflow.com/a/77981548/1076965]

### Check messages in queue
`C:\Users\ArindamRoychowdhury>rabbitmqctl list_queues
`
```
Timeout: 60.0 seconds ...
Listing queues for vhost / ...
name    messages
hello   2
```

### Running the scripts

- We need to start a receiving script first. This would always listen for messages.
- Run the send.py script to send a message and check the receiver console.
- For basic small operations, we use **NAMED** queues which are the simplest form of queues.

# Work Queues (**Task Queues**)
These queues are uses for resourse intensive operations. 
We don't want to wait for these tasks. We schedule them to be done
later.

A Worker is waiting in the backgroud for such messages.
When received, it will pop this task and eventually, execute it.
