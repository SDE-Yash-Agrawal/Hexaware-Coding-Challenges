class FileUploadException(Exception):
    def __init__(self, message="File upload error"):
        self.message = message
        super().__init__(self.message)
