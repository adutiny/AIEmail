
 

#Copyright SalesGigAI  2023

import shutil
import imap_tools
from bs4 import BeautifulSoup
import re
from typing import List, Any
import os
import openai
import email
import subprocess

from pyparsing import WordStart
from Key import my_Main
from Key import my_Contact
from Key import my_Chat
from Key import email
from Key import password




class Main:
    def run_program(self):
        # code to run program
        pass  # pass should be placed after the code to run the program


API_Key = my_Main
openai.api_key= API_Key

model_id = 'gpt-4'



my_email = "email"
my_pass = "password"

mailbox = imap_tools.MailBox('imap.gmail.com').login(email, password)

with open('email.txt', 'w') as file:




    for msg in mailbox.fetch('UNSEEN Subject "Sierra Tiny Houses Info Request"', charset='utf8'):
    #for msg in mailbox.fetch('UNSEEN Subject "homw request"', charset='utf8'):
    

        soup = BeautifulSoup(msg.html, 'lxml')
        file.write("Message id: " + str(msg.uid) + '\n')
        file.write("Message Subject: " + msg.subject + '\n')
        file.write("Message Date: " + str(msg.date) + '\n')
        file.write("Message Text: " + soup.get_text() + '\n')
       #file.write("Email Address: " + email_address + '\n')
        break  # only reads the oldest unseen email


with open(r"C:\users\owner\AIEmail\email.txt", 'r') as file:
    # read the file and extract the email addresses
    addresses = file.read().splitlines()

os.chdir(r"C:\Users\owner\website1\AIEmail\truformtinyhouse")
#shutil.copyfile("C:\users\owner\AIEmail\email.txt", "C:\Users\owner\website1\AIEmail\truformtinyhouse\email_copy.txt")    
shutil.copyfile(r"C:/users/owner/AIEmail/email.txt", r"C:/Users/owner/website1/AIEmail/truformtinyhouse/email_copy.txt")
 
# create a new file for each email address
for address in addresses:
    result: list[Any] = re.findall(r'Email Address([^ ]*)', address)
    for result in result:
        with open(str(result) + '.txt', 'w') as file:
            file.write('')


# and write the text to the corresponding email file
with open(r"C:\users\owner\AIEmail\email.txt") as file:
    lines = file.read().splitlines()
    start_index = 0
    end_index = 0
    for i in range(len(lines)):
        if 'Message id' in lines[i]:
            start_index = i - 4
        if 'Email Address' in lines[i]:
            end_index = i
            email = re.findall(r'Email Address([^ ]*)', lines[i])[0]
            #with open(str(email) + '.txt', 'a') as email_file:
            with open(os.path.join( str(email) + '.txt'), 'a') as email_file: 
                #path = os.path.join('truformtinyhouse', str(email) + '.txt')

                file_path = os.path.join( str(email) + '.txt')

                if not os.path.exists(file_path):
                        open(file_path, 'w').close()
   
                for j in range(start_index, end_index):
                    email_file.write(lines[j] + '\n')
#class Main:
    #def run_program(self):
        # code to run the program

#Starts part_testing.py which creates comments.txt email_sending.txt and name.txt it reads email.txt

#Copyright SalesGigAI  2023
import re
from typing import List, Any
import openai
# open the email.txt file
with open(r"C:\users\owner\AIEmail\email.txt", 'r') as file:
    # read the file and extract the email addresses
    addresses = file.read().splitlines()


# write the email addresses to email_sending.txt
with open('email_sending.txt', 'w') as file:
    for address in addresses:
        result: list[Any] = re.findall(r'Email Address([^ ]*)', address)
        for result in result:
            file.write(str(result) + '\n')

with open('email_sending.txt', 'r') as file:
    # read the file and extract the email addresses
    addresses = file.read().splitlines()
    #create a file with the contents of email.txt file and name it email_sending.txt
     


# open the email.txt file
with open(r"C:\users\owner\AIEmail\email.txt", 'r') as file:
    # read the file and extract the comments
    comments = file.read().splitlines()

file = open("email_sending.txt", "r") 
client_email = file.read() 
file.close()


 
 


# write the comments section to comments.txt

with open('comments.txt', 'w') as file:
    for comment in comments:
        # extract everything after the word 'Comments'
        result: list[Any] = re.findall(r'Comments\s*(.*)', comment)
        # write the comment to the file
        for result in result:
            file.write('Prompt: Answer as if you are Tru Form Tiny House company truformtiny.com with address of 1010 Tyinn St Suite #11, Eugene, OR 97402, phone (775) 502-0283' + str(result) + '\n')


   # open the email.txt file
with open(r"C:\users\owner\AIEmail\email.txt", 'r') as file:
    # read the file and extract the name
    names = file.read().splitlines()


# write the email addresses to email_sending.txt
with open('name.txt', 'w') as file:
    for name in names:
        #result: list[Any] = re.findall([^ ]*)', name)
        result: list[Any] = re.findall(r'Name\s*(.*)', name)
        for result in result:
            file.write(str(result) + '\n')
 
import openai

API_Key = my_Main

openai.api_key = API_Key

model_id = 'gpt-4'


# model_id = 'davinci'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation,
        temperature=0.7,
        top_p=1.0,
        max_tokens=150
    )

    # return response

    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation


conversation = []
conversation.append({'role': 'system', 'content': 'How may I help you?'})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

with open('comments.txt') as f:
    conversation = []
    conversation.append({'role': 'system', 'content': 'How may I help you?'})
    conversation = ChatGPT_conversation(conversation)
    # print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
    for line in f:
        conversation.append({'role': 'user', 'content': line})
        conversation = ChatGPT_conversation(conversation)
        # print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

with open('answer.txt', 'w') as f:
    for conversation_line in conversation[1:]:  # Exclude the initial question
        # f.write(f'{conversation_line["role"]}: {conversation_line["content"]}\n')
        f.write(f'{conversation_line["content"]}\n')


# strip_answer.py

# open the file to be read
f = open("answer.txt", "r")

# open the file to be written
f_strip = open("answerstrips.txt", "w")

# loop through each line
'''
for line in f:
    # check if the line contains AI or prompt
    if 'AI' not in line and 'Prompt:' not in line:
        # write the line to the file
        f_strip.write(line)
    else:
        # skip the line
        continue
'''
for line in f:
    # check if the line contains AI, prompt, 1. 2. 3. 4. 5. 6. 7. 8. 9.10.().?
    if 'AI' not in line and 'Prompt:' not in line and '1.' not in line and '2.' not in line and '3.' not in line and '4.' not in line and '5.' not in line and '6.' not in line and '7.' not in line and '8.' not in line and '9.' not in line and '10.' not in line and '()' not in line and '?' not in line:
        # write the line to the file
        f_strip.write(line)
    else:
        # skip the line
        continue
# write the response
f_strip.write('Let me know if we can help.\n')

# close both files
f.close()
f_strip.close()


#TESTING_ANSWER.py

import smtplib
from email.mime.text import MIMEText
import re

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email: str = "adutinyhouse@gmail.com"  # Enter your address
pass_word = password

# read in the email list file
email_list = []
with open('email_sending.txt', 'r') as f:
    for line in f:
        email_list.append(line.strip())




# read in the text file
# read in the text file
text_list = []
with open('answerstrips.txt', 'r') as f:
    for line in f:
        text_list.append(line.strip())
        # strip the " and , and [] characters
        text_list = [x.strip('","') for x in text_list]
        text_list = [x.strip('[]') for x in text_list]
        text_list = [x.strip('Hello!') for x in text_list]




        # read in the name file
name_list = []
with open('name.txt', 'r') as f:
    for line in f:
        name_list.append(line.strip())


# create a dictionary to store the matched data
matched_data = {}


# iterate through each email address in the email list
for email in email_list:
    # find the index of the email address in the email list
    email_index = email_list.index(email)



# get the corresponding text from the text list


# add the email address and the corresponding text to the dictionary
#matched_data[email] = text

text = text_list
text = "\n".join(text)

#text = text.strip("[]").replace(".","")

print(text)

# Output: ['item1', 'item2', 'item3']

# add the email address and the corresponding text to the dictionary
matched_data[email] = text

# add the email address and the corresponding text to the dictionary

with open('name.txt', 'r') as f:
    name = f.read()

my_dict = {'key1': 'value1', 'key2': 'value2'}




name_parts = name.split()
first_name = name_parts[0]
last_name = name_parts[0]

print(f"First name: {first_name}")
print(f"Last name: {last_name}")


# print the matched data
for email, text in matched_data.items():
    print(f'{email}: {text}:')


# import smtplib module to be able to send emails
import smtplib

# set the server and port
server = smtplib.SMTP('smtp.gmail.com', 587)

# start the server connection
server.starttls()

# use the login method to login to your email account
server.login(sender_email, pass_word)





    # send the email
    # use a for loop to loop through both lists and create and send the emails
for i in range(len(name_list)):
    matched_data[name_list[i]] = text_list[i]
        #message = "Hello " + name_list[i] + ", " + matched_data[name_list[i]]
    message = f'Subject: Tiny House for You!\n\n Hello! {first_name},\n\n Sierra Tiny homes has closed their doors for good and asked us to help anyone who contacts them.\n\n {text} We do have a great lender they do require a 680 FICO or better a generally a 20% down payment\n\nThanks,\n Woody www.truformtiny.com\n '
    server.sendmail('adutinyhouse@gmail.com', email_list[i], message)


# close the server connection
server.quit()


"""

from listen import check_for_new_email
import time

# Set the IMAP server variable.
IMAP_SERVER = 'imap.gmail.com'

# Set the email address and password variables.
my_email = "adutinyhouse@gmail.com"
my_pass = "nltlakzhlbupzeyb"

# Define the main() function.
def main():

    # Check for new emails every minute.
    while True:
        # Check for new emails.
        check_for_new_email()

        # Sleep for 60 seconds.
        time.sleep(60)

# If the program is called directly, run the main() function.
if __name__ == '__main__':
    main()
"""
  



 