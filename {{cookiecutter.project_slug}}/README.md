# {{ cookiecutter.project_name }}

# Install dependencies

`pip install -e .`

# Setup database

`FLASK_APP={{ cookiecutter.project_slug}}.app flask db init`

`FLASK_APP={{ cookiecutter.project_slug}}.app flask db migrate`

`FLASK_APP={{ cookiecutter.project_slug}}.app flask db upgrade`

# Run server

`FLASK_APP={{ cookiecutter.project_slug }}.app flask run`
