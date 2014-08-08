About
=====

Load testing for the Mozilla Tiles project using the [loads](https://github.com/mozilla-services/loads) 
testing framework.

Installation
------------

1. `virtualenv .`
1. `./bin/pip install -r requirements.txt`

Running it
----------

* `./bin/loads-runner loadtest.TilesRecordDataTest.test_click`

TODO
----

* Makefile for encapsulating load testing configs / logic
* send actual fake data to api endpoints
* send good/bad (malformed) data to api endpoints
* create configs to test load at: 100 req/sec, 1000 req/sec ... 100K req/sec
