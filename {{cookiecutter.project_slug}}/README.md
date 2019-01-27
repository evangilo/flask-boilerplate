# {{ cookiecutter.project_name }}

# Install dependencies

`pip install -e .`

# Export {{ cookiecutter.project_slug|upper }}_SETTINGS enviroment variable

`cp settings.cfg.sample /etc/{{ cookiecutter.project_slug }}/production.cfg`

`export {{ cookiecutter.project_slug|upper }}_SETTINGS=/etc/{{ cookiecutter.project_slug }}/production.cfg`

# Setup database

`FLASK_APP={{ cookiecutter.project_slug}}.app flask db init`

`FLASK_APP={{ cookiecutter.project_slug}}.app flask db migrate`

`FLASK_APP={{ cookiecutter.project_slug}}.app flask db upgrade`

# Run server

`FLASK_APP={{ cookiecutter.project_slug }}.app flask run`

# Run tests

`export {{ cookiecutter.project_slug|upper }}_SETTINGS=$(pwd)/test_settings.cfg`

`pip install -r test_requirements.txt`

`pytest -vv`

