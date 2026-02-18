
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('your_package_name'),
    autoescape=select_autoescape()
)

def render_response_from_env(environment):
    from flask import request
    name = request.args.get('name', '')
    template = environment.get_template('template.html')
    rendered = template.render(name=name)
    from flask import make_response
    response = make_response(rendered)
    return response

def home():
    response = render_response_from_env(env)
    return response
