```python
import win32com.client
import html

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def create_email_with_body(text_content, recipient, subject):
    # Create an instance of Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)  # 0 represents a mail item

    # Set email parameters
    mail.Subject = subject
    mail.To = recipient

    # Prepare the email body with HTML formatting
    # Escape HTML special characters and wrap in <pre> to preserve formatting
    escaped_content = html.escape(text_content)
    html_body = f"""
    <html>
    <body>
        <pre>{escaped_content}</pre>
    </body>
    </html>
    """
    
    mail.HTMLBody = html_body

    # Display the email (for review) or send it directly
    mail.Display()  # Use mail.Send() to send without displaying

# Example usage
text_file_path = 'example.txt'  # Path to your text file
recipient_email = 'recipient@example.com'  # Replace with the recipient's email
email_subject = 'Your Subject Here'  # Replace with your subject

# Read the text content from the file
text_content = read_text_file(text_file_path)

# Create and display the email
create_email_with_body(text_content, recipient_email, email_subject)
```
