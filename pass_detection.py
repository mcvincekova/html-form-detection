from bs4 import BeautifulSoup


FILE_NAME = 'form_html/68f68dde0509c3009c74636a1afdab3b8204dbda1ccc67a67d09596013ca6237.html'


class FormDetector:
    def __init__(self, html_soup: BeautifulSoup) -> None:
        self.html_soup = html_soup

    def get_passwords_elems(self) -> list:
        return self.html_soup.find_all('input', {'type': 'password'})

    def get_email_elems(self) -> list:
        return self.html_soup.find_all('input', {'type': 'email'})


with open(FILE_NAME, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')
detector = FormDetector(soup)

passwords = detector.get_passwords_elems()
emails = detector.get_email_elems()

if len(passwords) or len(emails) > 0:
    print('Login form detected')
else:
    print('Login form not detected')

print(f"Password inputs detected: '{len(passwords)}'")
print(f"Email inputs detected: '{len(emails)}'")



