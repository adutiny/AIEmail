 


import csv
import smtplib
import os
import dotenv

'''A Google Workspace account (formerly G Suite) allows you to bulk send up to 2,000 emails per day, per email address. This means that if you send 2,000 emails to 10 different email addresses, that will count as 2,000 emails sent.

However, it is important to note that Google has a number of policies in place to prevent spam and abuse. If you send too many emails at once, or if your email content is flagged as spam, your account may be temporarily blocked.

To avoid having your account blocked, it is important to follow Google's best practices for sending bulk email. Here are a few tips:

Send your emails in batches of 500 or less.
Avoid sending the same email to multiple recipients at the same time.
Personalize your emails as much as possible.
Include a clear unsubscribe link in all of your emails.
Monitor your bounce rate and spam complaint rates. If you see a sudden increase in either of these metrics, it is a sign that your emails are being flagged as spam.'''
 


dotenv.load_dotenv()

 
my_email = os.environ['my_email']
my_pass = os.environ['my_pass']




def main():
    with open("/emailtime", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            email = row[1]

            message = f"Hi {name}, we love you!"

            send_email(email, message)

            print(f"Email sent to {name}")


def send_email(email, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("my_email", "my_pass")
        server.sendmail("my_email", email, message)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")   



# read the data from the csv file
with open("emailtime.csv", "r") as file:
    reader = csv.reader(file)
    name_list = []
    email_list = []
    text_list = []

    for row in reader:
        name_list.append(row[0])
        email_list.append(row[1])
        text_list.append(row[2])

matched_data = {}
for i in range(len(name_list)):
    matched_data[name_list[i]] = text_list[i]

# set the server and port
server = smtplib.SMTP('smtp.gmail.com', 587)

# start the server connection
import smtplib

# define the send_email function
def send_email(email, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(my_email, my_pass)
        server.sendmail(my_email, email, message)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# use the login method to login to your email account
server.login(my_email, my_pass)

# use a for loop to loop through both lists and create and send the emails
for i in range(len(email_list)):
    name = name_list[i]
    text = matched_data[name]

    message = f'Subject: AI Auto Email Replies tool!\n\nHello {name},\n\nAre you tired of spending hours answering emails? Do you wish there was a way to automate your email response with relevant and accurate answers to your customers\' emails?\n\nIf so, then you\'ll be excited to hear about our new AI Auto Email Replies tool!\n\nAI Auto Email Replies is a powerful tool that can help you save time, improve customer service, and increase productivity. The AI will analyze the context of your emails and generate responses that are relevant and accurate.\n\nHere are just a few of the benefits of using AI Auto Email Replies:\n'
    message += '* Saves money: Imagine paying someone $49.99 a month to answer your incoming emails....  Coming Soon AI incoming phone calls, AI Text and AI chatbots.\n'
    message += '* Improves customer service: Faster and more accurate than employees. Which improves customer satisfaction.\n'
    message += '* Accurate: Trained by our AI experts, to your business. Our AI chatbot is up to 97 percent accurate. According to recent studies, depending on the individual, humans are anywhere from 60% to 90 percent accurate.\n'
    message += '* Individual personal responses: Answers accurately and specific questions asked by your customers. Not a template one-size-fits-all impersonal reply.\n\nAI Auto Email Replies is available now for just $49.99 a month. You can try it for free for 7 days to see how it can help you save time and improve your business.\n\nClick here to sign up for a free trial today: www.aiconnectsales.com\n\nThanks,\nWoody\n\nP.S. AI Auto Email Replies can be used to answer website contacts, incoming emails either all emails or specific emails by subject. It works 24/7, so you can always be sure that your emails are being answered promptly.'
 

 
 
# use the login method to login to your email account
server.login(my_email, my_pass)

# use a for loop to loop through both lists and create and send the emails
for i in range(len(email_list)):
    name = name_list[i]
    text = matched_data[name]

    message = f'Subject: AI Auto Email Replies tool!\n\nHello {name},\n\nAre you tired of spending hours answering emails? Do you wish there was a way to automate your email response with relevant and accurate answers to your customers\' emails?\n\nIf so, then you\'ll be excited to hear about our new AI Auto Email Replies tool!\n\nAI Auto Email Replies is a powerful tool that can help you save time, improve customer service, and increase productivity. The AI will analyze the context of your emails and generate responses that are relevant and accurate.\n\nHere are just a few of the benefits of using AI Auto Email Replies:\n'
    message += '* Saves money: Imagine paying someone $49.99 a month to answer your incoming emails or Coming Soon! AI incoming phone calls AI Text and AI chatbots.\n'
    message += '* Improves customer service: Faster and more accurate than employees. Which improves customer satisfaction.\n'
    message += '* Accurate: Trained by our AI experts, to your business. Our AI chatbot is up to 97 percent accurate. According to recent studies, depending on the individual, humans are anywhere from 60% to 90 percent accurate.\n'
    message += '* Individual personal responses: Answers accurately and specific questions asked by your customers. Not a template one-size-fits-all impersonal reply.\n\nAI Auto Email Replies is available now for just $49.99 a month. You can try it for free for 7 days to see how it can help you save time and improve your business.\n\nClick here to sign up for a free trial today: www.aiconnectsales.com\n\nThanks,\nWoody\n\nP.S. AI Auto Email Replies can be used to answer website contacts, incoming emails either all emails or specific emails by subject. It works 24/7, so you can always be sure that your emails are being answered promptly.'
 

 

     
    send_email(email_list[i], message)

# close the server connection
server.quit()
                      
        




    #if __name__ == "__main__":
        #main()