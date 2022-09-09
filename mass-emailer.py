import pandas as pd
import smtplib
from string import Template

# read in your template file as a string.Template object
def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# read in your database file, assign columns to respective variables
df = pd.read_csv("Rock Radio stations db.txt") # file: table of email info; Columns are emails, names, and cities
emails = df['Contact'].values
names = df['Rock Radio'].values
cities = df['Location'].values

# count the length of my database,
#   this will tell our For Loop how many times to run
index = df.index
number_of_rows = len(index)
print("number of emails: " + str(number_of_rows))

for i in range(number_of_rows):
    subject = "Music Submission - The Deaf Pilots - Independent Rock Musicians"
    # here is the function we defined up top
    message = read_template("TATT radio station email template.txt") # file: email body prepared for .format insertion
    # .format puts the subject in the correct spot
    # .safe_substitute() is telling the computer where to insert the "BLOG_NAME"
    #   the $BLOG_NAME should be inside our 'message' .txt file
    body = "Subject: {}\n\n{}".format(subject, message.safe_substitute(RADIO_STATION=names[i], CITY=cities[i]))
    # connects us with gmail
    # fyi port=465 is an non-secure connection, deprecated
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("thedeafpilots@gmail.com", "americanGirl500")
    # (sender's e-mail, recipient's e-mail, text content)
    server.sendmail(
        "thedeafpilots@gmail.com",
        emails[i],
        body.encode("utf8"))
    # displays which e-mails actually got sent
    print("sent email to: " + emails[i])
    server.quit()
