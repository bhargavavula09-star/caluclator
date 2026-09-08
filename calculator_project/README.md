# Simple Django Calculator

This turns your original script into a small Django web app.

## Setup

```bash
pip install django
django-admin startproject config .
```

Copy the `calculator/` folder (included here) into your project root, next to `manage.py`.

## 1. Register the app

In `config/settings.py`, add `"calculator"` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "calculator",
]
```

## 2. Wire up the URLs

In `config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("calculator.urls")),
]
```

## 3. Run it

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` — you'll see a form with two number fields and an
operator dropdown. Submitting it shows the result, using the exact same
+ - * / logic (including the divide-by-zero and invalid-operator checks)
from your original script.

## Files included

- `calculator/views.py` — the calculator logic, now handling a POST form instead of `input()`
- `calculator/urls.py` — routes `/` to the calculator view
- `calculator/templates/calculator/index.html` — the form + result page
- `calculator/apps.py`, `calculator/__init__.py` — standard Django app files
