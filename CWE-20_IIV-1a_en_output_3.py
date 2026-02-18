
import re

# Compile regex once when module loads
URL_PATTERN = re.compile(r'^https?://(?:www\.)?example\.com/[\w\-/]+$')
DEFAULT_URL = 'https://default.example.com/home'

def get_redirect_target(target_url):
    """
    Check if target_url matches pattern.
    If it matches, return target_url as redirect target.
    Otherwise, return default URL.
    """
    if URL_PATTERN.match(target_url):
        return target_url
    return DEFAULT_URL
