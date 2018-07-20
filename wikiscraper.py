import webbrowser, requests, time
from bs4 import BeautifulSoup



q   = print('Please input the wikipedia page you would like summarised: ')
url = input()
res = webbrowser.open(url)

resSoup  = requests.get(url)
soup     = BeautifulSoup(resSoup.text,'html.parser')

synopsis     = soup.select('.mw-parser-output p b')
synopsisText = synopsis[0].getText()

# print(synopsisText)

getParent = synopsis[0].parent
end       = getParent.getText()

print()

print(end)

path = 'wikipedia/'

file = open(path+synopsisText+".txt", 'w')
file.write(end)
file.close()
