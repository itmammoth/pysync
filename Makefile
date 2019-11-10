.PHONY: clean build upload

clean:
	rm -rf itm.pysync.egg-info/*
	rm -rf dist/*
	rm -rf build/*

build: clean
	python setup.py sdist bdist_wheel

upload: build
	twine upload --repository pypi dist/*
