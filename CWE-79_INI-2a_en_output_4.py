
from jinja2 import Environment, PackageLoader, select_autoescape

def render_response_from_env(env):
    from flask import request
    name = request.args.get('name', 'World')
    template = env.get_template('template.html')
    rendered = template.render(name=name)
    from flask import make_response
    response = make_response(rendered)
    return response

env = Environment(
    loader=PackageLoader('your_package_name'),
    autoescape=select_autoescape(['html', 'xml'])
)

def home():
    response = render_response_from_env(env)
    return response
