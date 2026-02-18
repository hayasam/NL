
from jinja2 import Environment, PackageLoader, select_autoescape

def render_response_from_env(env):
    from flask import request
    name = request.args.get('name', 'World')
    template = env.get_template('template.html')
    rendered_template = template.render(name=name)
    return rendered_template

env = Environment(
    loader=PackageLoader('your_package_name'),
    autoescape=select_autoescape(['html', 'xml'])
)

def home():
    response = render_response_from_env(env)
    return response
