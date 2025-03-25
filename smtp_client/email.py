from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from dotenv import load_dotenv
import os
import smtplib

class email:
  def __init__(self):
        pass
  @staticmethod
  def init_message(params):
    message = MIMEMultipart("alternative")
    message["Subject"] = "New Demo Request!"
    text = f"""\
    New Demo Request

    Name: {params.get('name')}
    Email: {params.get('email')}
    Message: {params.get('message')}
    Age: {params.get('age')}
    Phone: {params.get('phone')}"""

    # write the HTML part
    html = f"""\
    <html>
      <body>
        <div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333">
          <div style="text-align: center; margin-bottom: 20px">
            <img
              src="https://www.upmovechess.com/logo.png"
              alt="Company Logo"
              style="max-width: 150px; height: auto"
            />
          </div>
          <h2 style="color: #0056b3">New Demo Request</h2>
          <table
            style="width: 100%; border-collapse: collapse; border: 1px solid #ddd"
          >
            <tr>
              <td
                style="padding: 8px; font-weight: bold; background-color: #f4f4f4"
              >
                Name:
              </td>
              <td style="padding: 8px">{params.get('name')}</td>
            </tr>
            <tr>
              <td
                style="padding: 8px; font-weight: bold; background-color: #f4f4f4"
              >
                Email:
              </td>
              <td style="padding: 8px">{params.get('email')}</td>
            </tr>
            <tr>
              <td
                style="padding: 8px; font-weight: bold; background-color: #f4f4f4"
              >
                Message:
              </td>
              <td style="padding: 8px">{params.get('message')}</td>
            </tr>
            <tr>
              <td
                style="padding: 8px; font-weight: bold; background-color: #f4f4f4"
              >
                Age:
              </td>
              <td style="padding: 8px">{params.get('age')}</td>
            </tr>
            <tr>
              <td
                style="padding: 8px; font-weight: bold; background-color: #f4f4f4"
              >
                Phone:
              </td>
              <td style="padding: 8px">{params.get('phone')}</td>
            </tr>
          </table>
        </div>  
        </body>
    </html>
    """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    message["From"]="Team Upmove Chess Academy <info@upmovechess.com>"
    message["To"]="Upmove Chess <upmovechess@gmail.com>"
    return message

  @staticmethod
  def send_email(params):
    load_dotenv()
    # creates SMTP session
    smtpServer = smtplib.SMTP('smtp.hostinger.com', 587)
    # start TLS for security
    smtpServer.starttls()
    # Authentication
    smtpServer.login(os.environ.get("MY_EMAIL_ID"), os.environ.get("MY_EMAIL_PW"))
    # message to be sent
    message = email.init_message(params=params)
    # sending the mail
    smtpServer.sendmail("info@upmovechess.com", "upmovechess@gmail.com", message.as_string())
    # terminating the session
    print('sent')
    smtpServer.quit()
