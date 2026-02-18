
import re

# Regular expression compiled at module load
URL_PATTERN = re.compile(r'^https?://(?:www\.)?example\.com/[\w\-/]+$')

def get_redirect_url(target_url, default_url):
    """
    Check if target_url matches the pattern.
    If it matches, return target_url as redirect target.
    If not, return default_url.
    """
    if URL_PATTERN.match(target_url):
        return target_url
    return default_url
