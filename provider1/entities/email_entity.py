class Email:
    
    def __init__(self, to_email: str, subject: str, body: str):
        self.to_email = to_email
        self.subject = subject
        self.body = body