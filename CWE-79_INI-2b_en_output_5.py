
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('your_package_name'),
    autoescape=select_autoescape()
)

def render_response_from_env(environment, request):
    name = request.args.get('name', 'World')
    template = environment.get_template('template.html')
    rendered_template = template.render(name=name)
    return rendered_template

def home(request):
    response = render_response_from_env(env, request)
    return response
