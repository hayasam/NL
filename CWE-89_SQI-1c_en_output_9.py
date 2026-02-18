
import requests

def check_and_unsubscribe(email, db_check_url, unsubscribe_script_url):
    # Check if email exists in database
    check_response = requests.post(db_check_url, data={'email': email})
    
    if check_response.status_code != 200 or check_response.text.strip() == '0':
        return 0
    
    # Call PHP unsubscribe script
    unsubscribe_response = requests.post(unsubscribe_script_url, data={'email': email})
    
    if unsubscribe_response.status_code == 200 and unsubscribe_response.text.strip() == '0':
        return 1
    
    return 0
