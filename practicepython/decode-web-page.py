from bs4 import BeautifulSoup
import urllib.request

def main():

	page = urllib.request.urlopen('http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
	page = page.read()
	page = page.decode('utf-8','ignore')

	soup = BeautifulSoup(page)

	f = open('Article.txt', 'w', encoding='utf-8')
	for section in soup.body.find_all('section', { 'class' : 'content-section' }):
		f.write(section.get_text())
		f.write('\n')		
	
	f.close()


if __name__ == "__main__":
	main()
