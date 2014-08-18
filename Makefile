SERVER_URL = http://127.0.0.1:9999

# Hackety-hack around OSX system python bustage.
# The need for this should go away with a future osx/xcode update.
ARCHFLAGS = -Wno-error=unused-command-line-argument-hard-error-in-future

INSTALL = ARCHFLAGS=$(ARCHFLAGS) ../local/bin/pip install

.PHONY: build test bench

build:
	$(INSTALL) pexpect
	$(INSTALL) https://github.com/mozilla-services/loads/archive/master.zip

# Run a single test from the local machine, for sanity-checking.
test:
	./bin/loads-runner --config=./config/test.ini --server-url=$(SERVER_URL) loadtest.TilesRecordDataTest.test_justload

# Run a fuller bench suite from the local machine.
bench:
	./bin/loads-runner --config=./config/bench.ini --server-url=$(SERVER_URL) loadtest.TilesRecordDataTest.test_justload

# Run a full bench, by submitting to broker in AWS.
megabench:
	./bin/loads-runner --config=./config/megabench.ini --user-id=$(USER) --server-url=$(SERVER_URL) loadtest.TilesRecordDataTest.test_justload

