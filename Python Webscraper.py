import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []
program_website = []

base_url = "https://ontariotechu.ca/programs/"

response = requests.get(base_url)

soup = BeautifulSoup(response.content, 'html.parser')

anchors = soup.find_all("a", href=True)

for anchor in anchors:
    href = anchor['href']
    if href.startswith("/programs/") and href.endswith("/index.php"):
        program_website.append(href[len("/programs/"):-len("/index.php")])
        

for current_program in program_website:
    url = "https://ontariotechu.ca/programs/" + current_program + "/index.php"
    response = requests.get(url)

    only_program_name = current_program.split('/')[-1]
    only_program_name = only_program_name.replace("-", " ")

    soup = BeautifulSoup(response.text, "html.parser")  
    all_programs = soup.find_all("th")

    for program in all_programs:
        item = {}
        item["Program Name"] = only_program_name
        item['Percent cutoff '] = soup.find("td").text.strip() 
        item['URL'] = "https://ontariotechu.ca/programs/" + current_program + "/index.php"
        
        data.append(item)
        break

    print(current_program)  
df = pd.DataFrame(data)
df.to_excel("ouinfo.xlsx", index=False)