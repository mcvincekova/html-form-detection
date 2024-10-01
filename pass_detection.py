from bs4 import BeautifulSoup
from pathlib import Path


class FormDetector:
    def __init__(self, html_soup: BeautifulSoup) -> None:
        self.html_soup = html_soup

    def get_passwords_elems(self) -> list:
        return self.html_soup.find_all('input', {'type': 'password'})

    def get_email_elems(self) -> list:
        return self.html_soup.find_all('input', {'type': 'email'})


FOLDER_PATH = Path('form_html')

for file_path in FOLDER_PATH.iterdir():
    if not file_path.is_file():
        raise FileNotFoundError(f"File '{file_path}' not found")

    with open(file_path, 'r', encoding='utf-8') as f:
        print(f"Analyzing file '{file_path}'")
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

