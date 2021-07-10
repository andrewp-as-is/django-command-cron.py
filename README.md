[![](https://img.shields.io/badge/released-2021.7.10-green.svg?longCache=True)](https://pypi.org/project/django-command-cron/)
[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

### Installation
```bash
$ pip install django-command-cron
```

### Pros
+   management commands based
+   admin interface
+   error handling
+   logs

#### `settings.py`
```python
INSTALLED_APPS+=['django_command_cron']
```

#### `migrate`
```bash
$ python manage.py migrate
```

### Examples
```bash
$ python manage.py command_cron
```

