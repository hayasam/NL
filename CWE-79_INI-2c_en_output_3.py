
from jinja2 import Environment, PackageLoader, select_autoescape

def render_response_from_env(env):
    from flask import request
    name = request.args.get('name', '')
    template = env.get_template('template.html')
    rendered = template.render(name=name)
    return rendered

def home():
    env = Environment(
        loader=PackageLoader('your_package_name', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    return render_response_from_env(env)
