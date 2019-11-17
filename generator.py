import random

from constants import CharacterOptions


class PasswordGenerator:
    
    def generate_password(self):
        length, special_chars = self.get_input()
        return self.combine_characters(length, special_chars)

    def get_input(self):
        input_lenth = input('How long should the password be? ')
        length = int(input_lenth)
        
        while True:
            input_special_chars = input('Should it include special characters? y/n ')
            if input_special_chars in ('y', 'yes'):
                special_chars = True
                break
            elif input_special_chars in ('n', 'no'):
                special_chars = False
                break        

        return length, special_chars

    def combine_characters(self, length, special_chars):
        selected_chars = CharacterOptions.LETTERS + CharacterOptions.NUMBERS
        if special_chars:
            selected_chars += CharacterOptions.SPECIAL_CHARACTERS
        
        password = '' 
        for char in range(length):
            password += random.choice(selected_chars)
        return password
