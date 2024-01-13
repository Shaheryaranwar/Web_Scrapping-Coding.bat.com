import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user_agent = UserAgent()
web_url = "https://codingbat.com/java"
page = requests.get(web_url, headers={'user-agent': user_agent.chrome})
soup = BeautifulSoup(page.content, 'lxml')
base_url = "https://codingbat.com"
all_divs = soup.find_all('div', class_='summ')
all_links = [base_url + div.a['href'] for div in all_divs]

for links in all_links:
    ander_ka_page = requests.get(links, headers={'user-agent': user_agent.chrome})
    ander_ka_soup = BeautifulSoup(ander_ka_page.content, 'lxml')
    div = ander_ka_soup.find('div', class_='tabc')
    links_questions = [base_url + td.a['href'] for td in div.table.find_all('td')]

    for index, link_question in enumerate(links_questions, start=1):
        final_page = requests.get(link_question)
        final_soup = BeautifulSoup(final_page.content, 'lxml')
        finl_div = final_soup.find('div', attrs={'class': 'indent'})
        problem_statement = finl_div.table.div.string

        siblings_statement = finl_div.table.div.next_siblings
        examples = [sibling for sibling in siblings_statement if sibling.string is not None]

        print(f"Question {index}: {problem_statement}")
        print("Example is:\n")
        for example in examples:
            print(example)
        print('\n\n\n')
