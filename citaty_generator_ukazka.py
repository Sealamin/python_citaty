import random
import os

class QuoteGenerator:
    def __init__(self, quotes_file='quotes.txt'):
        self.quotes_file = quotes_file
        self.quotes = self.load_quotes()

    def load_quotes(self):
        """Načte citáty ze souboru a vrátí je jako seznam."""
        if not os.path.exists(self.quotes_file):
            raise FileNotFoundError(f"Soubor '{self.quotes_file}' nebyl nalezen.")
        
        with open(self.quotes_file, 'r', encoding='utf-8') as file:
            quotes = [line.strip() for line in file if line.strip()]
        return quotes

    def get_random_quote(self):
        """Vrátí náhodný citát ze seznamu."""
        return random.choice(self.quotes)

    def run(self):
        """Aplikace interaguje s uživatelem v této funkci."""
        print("Vítejte v generátoru náhodných citátů!")
        while True:
            user_input = input("Stiskněte 'Enter' pro zobrazení náhodného citátu nebo 'q' pro ukončení: ")
            if user_input.lower() == 'q':
                print("Děkujeme za použití generátoru citátů!")
                break
            else:
                quote = self.get_random_quote()
                print(f"Náhodný citát: \"{quote}\"")

if __name__ == "__main__":
    try:
        generator = QuoteGenerator()
        generator.run()
    except FileNotFoundError as e:
        print(e)
