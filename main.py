import pyperclip

from generator import PasswordGenerator


if __name__ == '__main__':
    print('### PASSWORD GENERATOR ###')
    password = PasswordGenerator().generate_password()
    print('Password: {}'.format(password))
