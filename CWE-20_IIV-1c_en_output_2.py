
import re
from urllib.parse import urlparse, parse_qs
from django.shortcuts import redirect

def redirect_view(request):
    pattern = re.compile(r'^[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+')
    
    target = request.GET.get('target', '')
    
    if target and pattern.match(target):
        return redirect(target)
    
    return redirect('/')
