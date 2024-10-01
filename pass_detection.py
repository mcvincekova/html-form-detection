from bs4 import BeautifulSoup


file_name = 'form_html/68f68dde0509c3009c74636a1afdab3b8204dbda1ccc67a67d09596013ca6237.html'


with open(file_name, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find input fields with type="password"
password_inputs = soup.find_all('input', {'type': 'password'})

if len(password_inputs) > 0:
    print('Password input detected')
else:
    print('No password input detected')

