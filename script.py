import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(workflow_name, repo_name, workflow_run_id):
    senders_email = os.environ.get('SENDERS_EMAIL')
    senders_password = os.environ.get('SENDERS_PASSWORD')
    recievers_email = os.environ.get('RECIEVERS_EMAIL')

    if not senders_email or not senders_password or not recievers_email:
        raise ValueError("One or more environment variables are missing")

    subject = f"Workflow {workflow_name} for {repo_name} has failed"
    body = f"Hi, Workflow {workflow_name} for {repo_name} has failed. You can check the logs for more details.\n\nWorkflow Run ID: {workflow_run_id}"

    msg = MIMEMultipart()
    msg['From'] = senders_email
    msg['To'] =recievers_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senders_email, senders_password)
        text = msg.as_string()
        server.sendmail(senders_email,recievers_email, text)
        print('Mail sent successfully')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()

send_email(os.getenv('workflow_name'), os.getenv('repo_name'), os.getenv('workflow_run_id'))