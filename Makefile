### Actions
usage:
	@poetry run python -B src usage

test:
	@poetry run python -B src test

gen:
	@poetry run python -B src generate

base:
	@poetry run python -B src base

### Develop
log:
	@cat logs/latest.log

clean:
	cd target_project/tdd-sample/ && git restore .
	rm logs/latest.log