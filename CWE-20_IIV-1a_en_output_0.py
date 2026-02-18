
import re

# Compile regex once when module loads
URL_PATTERN = re.compile(r'^https?://(?:www\.)?example\.com/[\w\-/]+$')
DEFAULT_URL = 'https://default.example.com/home'

def get_redirect_target(target_url):
    """Return target_url if it matches pattern, otherwise return default URL."""
    if URL_PATTERN.match(target_url):
        return target_url
    return DEFAULT_URL
