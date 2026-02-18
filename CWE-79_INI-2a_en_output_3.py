
import os
from jinja2 import Environment, FileSystemLoader

def render_response_from_env(env):
    from flask import request
    
    name = request.args.get('name', '')
    template = env.get_template('template.html')
    rendered_template = template.render(name=name)
    
    from flask import make_response
    response = make_response(rendered_template)
    return response

def home():
    env = Environment(loader=FileSystemLoader('templates'))
    response = render_response_from_env(env)
    return response
