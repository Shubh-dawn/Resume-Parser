import re
import docx2txt

skill_keywords = ['c','c++','java','python','sql','restapi','heroku','javaScript','redux','html','css','tensorflow','keras',
                  'pytorch','machine learning','deep Learning','flask','streamlit','React', 'django','typescript'
                   'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress', 'angular js', 'c#', 'flask',
                   'android','android development','flutter','kotlin','xml','kivy','ios','ios development','swift','cocoa',
                   'cocoa touch','xcode','ux','adobe xd','figma','zeplin','balsamiq','ui','prototyping','wireframes',
                   'storyframes','adobe photoshop','photoshop','editing','adobe illustrator','illustrator',
                   'adobe after effects','after effects','adobe premier pro','premier pro','adobe indesign',
                   'indesign','wireframe','solid','grasp','user research','user experience']


def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None


txt =extract_text_from_docx('cv.docx')

# extract grades
grade_regex = r'(?:\d{1,2}\.\d{1,2})'
grades = re.findall(grade_regex, txt)

# extract years
year_regex = r'(?:\d{4}\s?-\s?\d{4})'
years = re.findall(year_regex, txt)


# function to replace a value in string
def replacer(string, noise_list):
    for v in noise_list:
        string = string.replace(v, ":")
    return string


# extract college
data = replacer(txt, years)
cleaned_text = re.sub("(?:\w+\s?\:)", "**", data).split('\n')
college = []
degree = []
for i in cleaned_text:
    split_data = i.split("**")
    college.append(split_data[0].replace(',', '').strip())
    #degree.append(split_data[1].strip())
parsed_output = []
for i in range(len(grades)):
    parsed_data = {
        "Institute": college[i],
        #"Degree": degree[i],
        "Grades": grades[i],
        "Year of Passing": years[i].split('-')[1]
    }
    parsed_output.append(parsed_data)
print(parsed_output)
