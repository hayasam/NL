
import re
from urllib.parse import urlparse, parse_qs
from django.shortcuts import redirect

def redirect_view(request):
    target = request.GET.get('target', '')
    
    # Regular expression: starts with one or more alphanumeric characters or hyphens, followed by a period
    pattern = r'^[a-zA-Z0-9\-]+\..*'
    
    if re.match(pattern, target):
        return redirect(target)
    else:
        return redirect('/')
