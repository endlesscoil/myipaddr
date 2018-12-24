myipaddr
========

Summary
-------

myipaddr is a simple microservice intended to periodically
check the current external IP address and report it's new
value.

Currently these events are sent via Redis Pub/Sub and Pushover.

Usage
-----

``docker-compose up``
