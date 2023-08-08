import os
#import re
import docx
#import nltk
#nltk.download('punkt')
from nltk.tokenize import word_tokenize


def read_word_file(file_path):
    """
    Read the content of a Word document.
    """
    doc = docx.Document(file_path)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return '\n'.join(content)


def extract_keywords(text, keywords):
    """
    Extract the keywords from the text.
    """
    found_keywords = []
    for word in word_tokenize(text):
        if word.lower() in keywords:
            found_keywords.append(word.lower())
    return found_keywords


def is_selected(keywords_found, job_keywords):
    """
    Determine whether the candidate is selected based on the presence of job-specific keywords.
    """
    return any(keyword in keywords_found for keyword in job_keywords)


def main():
    # Replace these with the actual paths to your Word documents and keyword list.
    input_directory = 'resumes'
    job_keywords = ['python']  # Add your job-specific keywords here.

    parsed_resumes = []
    for filename in os.listdir(input_directory):
        if filename.endswith('.docx'):
            file_path = os.path.join(input_directory, filename)
            content = read_word_file(file_path)
            extracted_keywords = extract_keywords(content, job_keywords)
            selected = is_selected(extracted_keywords, job_keywords)

            # Print the candidate's name and selection status.
            candidate_name = os.path.splitext(filename)[0]
            if selected:
                print(f"Candidate {candidate_name} has been selected.")
            else:
                print(f"Candidate {candidate_name} has been rejected.")

            # Perform additional processing if needed, e.g., extract contact details, skills, experience, etc.

            # Add the resume data to the list of parsed resumes.
            parsed_resumes.append({
                'filename': filename,
                'content': content,
                'keywords_found': extracted_keywords
            })


if __name__ == "__main__":
    main()
