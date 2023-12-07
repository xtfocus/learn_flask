# Flask web app basic tutorials

https://www.digitalocean.com/community/tutorial-series/how-to-create-web-sites-with-flask

## Lesson 1
```python3
from markupsafe import escape
from flask import abort
```

where:
- `escape` turns user input into string to void possible XSS attacks
- `abort()` to make HTTP error responses such as `abort(404)`. Use this in `except` clauses.

## Lesson 2

1. `flask.render_template` uses the `Jinja` template engine that automatically escapes HTML to prevent XSS attacks

2. use a base template that allows you to extend the content

3. use `url_for` to creat links

4. use | filter_name to allow inplace transformation (called filters)

5. write `if` and `for` like this:

```html
{%if happens %}
...
{%endif%}
```

6. It's usually not a good idea to render using `safe` filter

7. More [built-in jinja filter]( https://jinja.palletsprojects.com/en/3.0.x/templates/#list-of-builtin-filters)

## Lesson3

1. You can use `app.errorhandler` in orchestration with `abort()` decorator to decide what to show user in case of exceptions.

2. You can log more information using `app.logger`: `debug`, `info`, `warning`, `error`, etc.
