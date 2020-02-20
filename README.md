# tddpydjango
TDD with Python &amp; Django

# initial setup
$ sudo apt-get install python3.8

$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

$ pip install selenium

$ sudo apt-get install firefox-geckodriver

# test fail
$ python functional_tests.py

Original exception was:
Traceback (most recent call last):
  File "functional_tests.py", line 5, in <module>
    browser.get('http://localhost:8000')
  File "/home/luis/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 333, in get
    self.execute(Command.GET, {'url': url})
  File "/home/luis/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 321, in execute
    self.error_handler.check_response(response)
  File "/home/luis/.local/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: Reached error page: about:neterror?e=connectionFailure&u=http%3A//localhost%3A8000/&c=UTF-8&f=regular&d=O%20Firefox%20n%C3%A3o%20consegue%20estabelecer%20uma%20liga%C3%A7%C3%A3o%20para%20o%20servidor%20em%20localhost%3A8000.

# create venv & install Django
$ virtualenv .

$ source bin/activate

$ pip install Django==3.0.3

$ pip freeze

# create project
$ mkdir src && cd src

$ django-admin startproject superquizzes

# start project & run FT again
$ cd superquizzes && python manage.py runserver

$ python functional_tests.py
