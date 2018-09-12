# MyProject

### Requirements

- python(3.6.5)
- Django(2.x)
- pipenv

### Secrets

`.secrets/base.json`

#### Secret Key

```json

{
     "SECRET_KEY": "Django Secret Key"
}
```

### Running

```
- pipenv install
- pipenv shell
- cd app
- export DJANGO_SETTINGS_MODULE=config.settings.local
- ./manage.py runserver
```