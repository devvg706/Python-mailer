# Email Notification Script

This script is designed to send an email notification when a workflow run fails. It retrieves necessary credentials from environment variables and sends an email using Gmail's SMTP server.

## Features
- Sends an email notification when a workflow fails.
- Uses environment variables for security.
- Supports Gmail SMTP for sending emails.

## Prerequisites
Before running the script, ensure you have:
- A Gmail account (or SMTP server credentials).
- Enabled "Less Secure Apps" access (if required) or configured an App Password for Gmail.
- Python installed on your system.

## Environment Variables
The script requires the following environment variables:

- `SENDERS_EMAIL` - The sender's email address.
- `SENDERS_PASSWORD` - The sender's email password or app password.
- `RECIEVERS_EMAIL` - The recipient's email address.
- `workflow_name` - The name of the workflow.
- `repo_name` - The name of the repository.
- `workflow_run_id` - The unique identifier of the workflow run.

## Installation
1. Clone the repository or download the script.
2. Install dependencies (if needed):
   ```sh
   pip install smtplib email
   ```
3. Set the required environment variables.

## Usage
Run the script using the following command:

```sh
python script.py
```

Ensure that the required environment variables are set before execution.

## Error Handling
- If any required environment variable is missing, the script will raise an error.
- If there is an issue with SMTP authentication or email sending, the script will print an error message.

## License
This project is licensed under the MIT License.


