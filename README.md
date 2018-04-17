FACTORYBOY EXAMPLES
=======================

Guide to set up a one-to-many relationship in Factoryboy + Django
following the guide at: <https://simpleit.rocks/setting-up-a-factory-for-one-to-many-relationships-in-factoryboy/>


# Install

	mkdir ~/.virtualenvs
    mkvirtualenv -p /usr/bin/python3.6 ~/.virtualenvs/factoryboy_examples

Activate it:

	source ~/.virtualenvs/factoryboy_examples/bin/activate
	(factoryboy_examples)$

Install requirements:

    pip install -r requirements.txt

# Test it

	$ python manage.py tests
	Creating test database for alias 'default'...
	System check identified no issues (0 silenced).
	...
	----------------------------------------------------------------------
	Ran 3 tests in 0.095s

	OK
	Destroying test database for alias 'default'...
