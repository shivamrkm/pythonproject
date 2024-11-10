import os
import sys
from declutter import declutter
from cryptoChecker import check_price
from downCheck import check_website_status
from mail_merge import mail_merge

def main_menu():
    while True:
        print("\n--- SahastraBahu: Multipurpose Utility Tool ---")
        print("Choose an option:")
        print("1. Organize Files (Declutter)")
        print("2. Check Cryptocurrency Prices")
        print("3. Check Website Status")
        print("4. Send Personalized Emails")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            path = input("Enter the path to the directory you want to declutter: ").strip()
            declutter(path)
        elif choice == '2':
            crypto_name = input("Enter the cryptocurrency you want to check (e.g., Bitcoin): ").strip()
            upper_price = int(input("Enter the upper price(sell) threshold: ").strip())
            lower_price = int(input("Enter the lower price(buy) threshold: ").strip())

            check_price(crypto_name,upper_price,lower_price)
        elif choice == '3':
            url = input("Enter the URL of the website you want to check: ").strip()
            urls = [url]
            check_website_status(urls)
        elif choice == '4':
            csv_file = input("Enter the path to the CSV file containing email data: ").strip()
            email_template = input("Enter the path to the email template (HTML file): ").strip()
            image_path = input("Enter the path to the image you want to include in the email: ").strip()
            mail_merge(csv_file, email_template, image_path)
        elif choice == '5':
            print("Exiting SahastraBahu. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()
