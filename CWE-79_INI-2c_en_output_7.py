
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('your_package_name'),
    autoescape=select_autoescape()
)

def render_response_from_env(environment):
    from flask import request
    template = environment.get_template('template.html')
    name = request.args.get('name', '')
    rendered_template = template.render(name=name)
    return rendered_template

def home():
    response = render_response_from_env(env)
    return response
