# Description: This program checks for new emails every 3 minutes. If a new email is found, it will run the main.py file. If no new emails are found, it will wait 90 seconds before checking for new emails again. 

import imaplib
import time
import os
from Key import email  
from Key import password

# Set the IMAP server variable.
IMAP_SERVER = 'imap.gmail.com'

# Set the email address and password variables.
my_email = email
my_pass = password

# Define the check_for_new_email() function.
def check_for_new_email():

    # Connect to the IMAP server.
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)

    # Login to the account.
    mail.login(my_email, my_pass)

    # Select the Inbox folder.
    mail.select('Inbox')

    # Search for new messages.
    result, data = mail.search(None, 'UNSEEN SUBJECT "Sierra Tiny Houses Info Request"')

    # Check the result of the search.
    if result == 'OK':

        # Get the list of unseen email IDs.
        unseen_email_uids = data[0].split()

        # Check if there are any unseen emails.
        if len(unseen_email_uids) > 0:

            # Print a message to indicate that new emails have arrived.
            print('New emails have arrived!')

            # Start the main.py file.
            os.system('python main.py')

            # Close the connection to the IMAP server.
            mail.close()

            # Log out of the email account.
            mail.logout()

            # Wait 3 mins before checking for new emails again.
            time.sleep(180)

        else:
                
                # Print a message to indicate that there are no new emails.
                print('No new emails.')
    
                # Close the connection to the IMAP server.
                mail.close()
    
                # Log out of the email account.
                mail.logout()
    
                # Wait 90 seconds before checking for new emails again.
                time.sleep(90)

# Define the main() function.
def main():
         
        # Check for new emails every 3 minute.
        while True:
            # Check for new emails.
            check_for_new_email()
    
            # Sleep for 180 seconds.
            time.sleep(180)

# Call the main() function.
main()

 