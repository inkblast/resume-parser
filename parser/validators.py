from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
import os

VALID_EXTENSION = [".pdf", ".docx", ".doc"]
MAX_FILE_SIZE  = 2_096_152

def validate_file_extension(file_object: UploadedFile):
    ext: str = os.path.splitext(file_object.name)[1]
    if ext.lower() not in VALID_EXTENSION:
        raise ValidationError(f"Only PDF and Docx formats are allowed")
    
    else:
        return ext
    

def validate_file_size(file_object: UploadedFile):
    if file_object.size > MAX_FILE_SIZE:
        raise ValidationError("Max file size is 2MB")

