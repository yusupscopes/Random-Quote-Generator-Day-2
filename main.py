import requests # pip install requests
import pyperclip # pip install pyperclip

# function to fetch a random quote from the API
def fetch_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random", verify=False)
        response.raise_for_status()
        data = response.json()
        return {'quote': data['content'], 'author': data['author']}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return None

# function to copy the quote to the clipboard
def copy_to_clipboard(quote):
    pyperclip.copy(quote['quote'] + " - " + quote['author'])
    print("Quote copied to clipboard.")

# function to display the menu
def display_menu():
    print("\n Welcome to the Random Quote Generator \n")
    print("1. Fetch a new random quote")
    print("2. Copy the quote to clipboard")
    print("3. Exit")


# main function
def main():
    current_quote = None

    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            current_quote = fetch_random_quote()
            if current_quote:
                print(f"\nQuote: {current_quote['quote']}")
                print(f"Author: {current_quote['author']}")
        elif choice == '2':
            if current_quote:
                copy_to_clipboard(current_quote)                
            else:
                print("\n No quote available. Please fetch a new quote first.")
        elif choice == '3':
            print("Thank you for using the Random Quote Generator! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()