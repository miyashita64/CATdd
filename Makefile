usage:
	@poetry run python -B src usage

test:
	@poetry run python -B src test

gen:
	@poetry run python -B src generate

log:
	@cat logs/latest.log

clean:
	cd target_project/tdd-sample/ && git restore .
	rm logs/latest.log