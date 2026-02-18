
import re
from urllib.parse import urlparse, parse_qs
from django.shortcuts import redirect

def redirect_view(request):
    target = request.GET.get('target', '')
    
    pattern = r'^[a-zA-Z0-9\-]+\..+'
    
    if re.match(pattern, target):
        return redirect(target)
    
    return redirect('/')
