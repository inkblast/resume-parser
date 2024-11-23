from django.core.files.uploadedfile import UploadedFile
import pymupdf
import json
from groq import Groq
from django.conf import settings
from django.core.exceptions import ValidationError

def read_uploaded_file(file_object: UploadedFile, file_extension: str) -> str:
    with pymupdf .open(stream=file_object.read(), filetype= file_extension) as document:
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()

    return text



client = Groq(api_key=settings.GROQ_API_KEY)


promt_data = """
You are an AI bot designed to act as a professional for parsing resumes. You are given a resume  and your job is to
extract the following information from the resume:

1. applicant_name: ""
2. highest_level_of_education: ""
3. area_of_study: ""
4. institution:""
5. introduction : ""
6. skills: string []
7. english_proficiency_level: ""
8. experiences: [{"employer_name":"", role:"",  duration:""}]

Give the extracted info in JSON format only.
Note: if the info is not present, leave the field blank.
"""

def extract_resume_info(text:str):
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": promt_data + "Resume Content::" + text
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream= False,
            stop=None,
        )
        response = completion.choices[0].message.content
        start  = response.find("{")
        end = response.rfind("}") + 1
        json_str = response[start:end]
        data = json.loads(json_str)
        return data
    except Exception as err:
        raise ValidationError(f"something went wrong {err}",500)