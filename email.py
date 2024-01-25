import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace these values with your actual email details
sender_email = "your_email@gmail.com"
sender_password = "your_email_password"
receiver_email = "recipient_email@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Replace this with your actual data
county_deaths_data = [
    ("County1", 100),
    ("County2", 95)
]

# Sort the counties based on death counts

# Not giving out the logic as the data will be different for different datasets and is a piece of code that is used in a live project.

# Get the top 10 counties
top_10_counties = sorted_counties[:10]

# Prepare email content
# email_content = "Monthly Top 10 Counties with Most Deaths:\n\n" 
# Add your own content (Above is just an example)  
for index, (county, deaths) in enumerate(top_10_counties, start=1):
    email_content += f"{index}. {county}: {deaths} deaths\n"

# Set up the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Monthly Top 10 Counties with Most Deaths"

# Attach the email content
message.attach(MIMEText(email_content, "plain"))

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    # Login to the email account
    server.login(sender_email, sender_password)
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Monthly email alert sent successfully Sent.")
