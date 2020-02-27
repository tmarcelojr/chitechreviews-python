import requests as req
import asyncio
from bs4 import BeautifulSoup as soup 

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

glassdoor_company_links = [
	'https://www.glassdoor.com/Overview/Working-at-Braintree-EI_IE424728.11,20.htm',
	'https://www.glassdoor.com/Overview/Working-at-SpotHero-EI_IE935919.11,19.htm',
	'https://www.glassdoor.com/Overview/Working-at-bswift-EI_IE346847.11,17.htm',
	'https://www.glassdoor.com/Overview/Working-at-CCC-Information-Services-EI_IE4574.11,35.htm',
	'https://www.glassdoor.com/Overview/Working-at-Echo-Global-Logistics-EI_IE100320.11,32.htm',
	'https://www.glassdoor.com/Overview/Working-at-Enova-EI_IE298072.11,16.htm',
	'https://www.glassdoor.com/Overview/Working-at-Grubhub-EI_IE419089.11,18.htm',
	'https://www.glassdoor.com/Overview/Working-at-Guaranteed-Rate-EI_IE318640.11,26.htm',
	'https://www.glassdoor.com/Overview/Working-at-Morningstar-EI_IE3299.11,22.htm',
	'https://www.glassdoor.com/Overview/Working-at-Motorola-Solutions-EI_IE427189.11,29.htm',
	'https://www.glassdoor.com/Overview/Working-at-Rally-Health-EI_IE881152.11,23.htm',
	'https://www.glassdoor.com/Overview/Working-at-SMS-Assist-EI_IE622820.11,21.htm',
	'https://www.glassdoor.com/Overview/Working-at-TransUnion-EI_IE11441.11,21.htm',
	'https://www.glassdoor.com/Overview/Working-at-West-Monroe-Partners-EI_IE118343.11,31.htm',
	'https://www.glassdoor.com/Overview/Working-at-Trunk-Club-EI_IE675938.11,21.htm',
	'https://www.glassdoor.com/Overview/Working-at-Sprout-Social-EI_IE701678.11,24.htm',
	'https://www.glassdoor.com/Overview/Working-at--properties-EI_IE349652.11,22.htm',
	'https://www.glassdoor.com/Overview/Working-at-Brandmuscle-EI_IE265032.11,22.htm',
	'https://www.glassdoor.com/Overview/Working-at-Cars-com-EI_IE34989.11,19.htm',
	'https://www.glassdoor.com/Overview/Working-at-Capital-One-EI_IE3736.11,22.htm'
]

def get_link(link):
	return req.get(link, headers=headers);

async def get_responses(link):
	coroutine_version = asyncio.coroutine(get_link)
	return await coroutine_version(link)

websites_data = []
async def main():
	for link in glassdoor_company_links:
		websites_data.append(await asyncio.create_task(get_responses(link)))

company_ratings = []
benefits_ratings = []
salary_ratings = []
interview_ratings = []

# def get_text():
# 	for data in websites_data:
# 		test = soup(data.text, 'html.parser')
# 		reviews = test.find_all("span", class_="num h2")
# 		for idx, review in enumerate(reviews):
# 			if idx == 1: company_ratings.append(int(review.getText().replace(',', '')))
# 			elif idx == 3: salary_ratings.append(int(review.getText().replace(',', '')))
# 			elif idx == 4: interview_ratings.append(int(review.getText().replace(',', '')))
# 			elif idx == 5: benefits_ratings.append(int(review.getText().replace(',', '')))

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString

def get_text():
	for data in websites_data:
		test = soup(data.text, 'html.parser')
		reviews = test.find_all("span", class_="num h2")
		for idx, review in enumerate(reviews):
			num_ratings = replaceMultiple(review.getText(), ['.', 'k'], '')
			if idx == 1: company_ratings.append(int(num_ratings))
			elif idx == 3: salary_ratings.append(int(num_ratings))
			elif idx == 4: interview_ratings.append(int(num_ratings))
			elif idx == 5: benefits_ratings.append(int(num_ratings))

asyncio.run(main())
get_text()
print('\n Company ratings')
print(company_ratings)
print('\n Salary ratings')
print(salary_ratings)
print('\n Interviews ratings')
print(interview_ratings)
print('\n Benefits ratings')
print(benefits_ratings)


