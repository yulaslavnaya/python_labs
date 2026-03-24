# Email'ы могут состоять из любых букв латинского алфавита верхнего и нижнего регистров, цифр, спецсимволов из набора “+_- #”.
# Выведите email'ы в столбец.
import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9+\-_#]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    return re.findall(pattern, text)


if __name__ == "__main__":
    sample_input = "Jones and Palin met at Oxford University, where they performed together ysinghmanga@206954.com with the Oxford Revue. (6boutheina+14@weammo.xyz)"

    for email in find_emails(sample_input):
        print(email)