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
    "SECRET_KEY": "<Django secret key>"
}
```

### Secrets

`.secrets/dev.py`

#### Secret key

- PostgreSQL을 사용, DATABASES 섹션의 설정이 필요

```json

{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "<host>",
      "PORT": 5432,
      "USER": "<user>",
      "PASSWORD": "<password>",
      "NAME": "<db name>"
    }
    }
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