# Random Quote Generator (Day 2)

A simple Python program that fetches random quotes from the [Quotable API](https://api.quotable.io/random) and allows users to copy them to the clipboard.

## Overview

The Random Quote Generator is a menu-driven program that provides a simple way to fetch and copy random quotes to the clipboard. The program uses the Quotable API to fetch quotes and the `pyperclip` library to copy the quotes to the clipboard.

## Usage

1. Run the program using `python main.py`
2. Choose an option from the menu:
	* 1: Fetch a new random quote
	* 2: Copy the quote to clipboard
	* 3: Exit

## Features

* Fetches random quotes from the Quotable API
* Displays the quote and author
* Allows users to copy the quote to the clipboard
* Simple menu-driven interface

## Code Structure

The program consists of four main functions:

* `fetch_random_quote()`: Fetches a random quote from the Quotable API and returns a dictionary containing the quote and author.
* `copy_to_clipboard(quote)`: Copies the quote to the clipboard using the `pyperclip` library.
* `display_menu()`: Displays the program menu to the user.
* `main()`: The main function that controls the program flow and handles user input.

The program uses a simple while loop to continuously display the menu and handle user input until the user chooses to exit.

## Requirements

* Python 3.10.12 (tested on Python 3.10.12)
* `requests` library (install with `pip install requests`)
* `pyperclip` library (install with `pip install pyperclip`)

## Notes

* This program uses the Quotable API to fetch random quotes. Please review their API terms and conditions before using this program.
* The program uses the `verify=False` parameter when making API requests to avoid SSL verification issues. This is not recommended for production use and should be removed or replaced with a valid SSL certificate.
