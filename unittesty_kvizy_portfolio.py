import unittest
from unittest.mock import patch, mock_open

import os

# Autor ví, že nepokrývá všechny edge cases, ale má jedná se jen o ukázku práce
class TestQuoteGenerator(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Citát 1\nCitát 2\n')

    def test_load_quotes(self, mock_file):

        generator = QuoteGenerator('dummy_quotes.txt')

        quotes = generator.load_quotes()

        self.assertEqual(quotes, ['Citát 1', 'Citát 2'])

        mock_file.assert_called_once_with('dummy_quotes.txt', 'r', encoding='utf-8')


    def test_load_quotes_file_not_found(self):

        with self.assertRaises(FileNotFoundError):

            generator = QuoteGenerator('non_existent_file.txt')

            generator.load_quotes()


    @patch('random.choice')

    def test_get_random_quote(self, mock_choice):

        generator = QuoteGenerator()

        generator.quotes = ['Citát 1', 'Citát 2']

        mock_choice.return_value = 'Citát 1'

        quote = generator.get_random_quote()

        self.assertEqual(quote, 'Citát 1')


    @patch('builtins.input', side_effect=['', 'q'])

    @patch('builtins.print')

    def test_run(self, mock_print, mock_input):

        generator = QuoteGenerator()

        generator.quotes = ['Citát 1']

        generator.run()

        mock_print.assert_any_call("Náhodný citát: \"Citát 1\"")

        mock_print.assert_any_call("Děkujeme za použití generátoru citátů!")


    @patch('builtins.open', new_callable=mock_open, read_data='')

    def test_load_quotes_empty_file(self, mock_file):

        generator = QuoteGenerator('empty_file.txt')

        quotes = generator.load_quotes()

        self.assertEqual(quotes, [])

        mock_file.assert_called_once_with('empty_file.txt', 'r', encoding='utf-8')


    @patch('builtins.open', new_callable=mock_open, read_data='Citát 1\n\nCitát 2\n\n')

    def test_load_quotes_with_empty_lines(self, mock_file):

        generator = QuoteGenerator('file_with_empty_lines.txt')

        quotes = generator.load_quotes()

        self.assertEqual(quotes, ['Citát 1', 'Citát 2'])


    @patch('random.choice')

    def test_get_random_quote_empty_list(self, mock_choice):

        generator = QuoteGenerator()

        generator.quotes = []

        with self.assertRaises(IndexError):

            generator.get_random_quote()


if __name__ == '__main__':

    unittest.main()
