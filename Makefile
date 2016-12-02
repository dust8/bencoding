.PHONY: docs

test:
	python -m unittest

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

docs:
	@cd docs && make html

clean-docs:
	@rm -fr  docs/_build


clean: clean-build clean-docs
