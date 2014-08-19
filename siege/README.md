# About

Load tests using siege

## Usage

Using the nodejs test server to make sure things are working

`siege -c 10 -q -b -t5s -f test.local.siege`

Testing the staging site w/ ELB and real servers. This should be run in 
AWS on a decent sized box to really stress the system

`siege -c 50 -q -b -t5s -f requests.stage.siege`
