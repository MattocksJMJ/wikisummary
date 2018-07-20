import webbrowser, requests, time
from bs4 import BeautifulSoup

# Ask user to input a wikipedia page 
q   = print('Please input the wikipedia page you would like summarised: ')
url = input()
# Open the page for the user to view in their browser
res = webbrowser.open(url)

# Open the same page with beautiful soup to be searched
resSoup  = requests.get(url)
soup     = BeautifulSoup(resSoup.text,'html.parser')

# Select the class mw-parser-output with a <p> tag and a <b> tag
synopsis     = soup.select('.mw-parser-output p b')
synopsisText = synopsis[0].getText()

# Get the parent of the current b tag and convert to text
getParent = synopsis[0].parent
end       = getParent.getText()

# If the bold text (title) and body of text are the same then get the parent of the current tag
if synopsisText == end:
    end = getParent.parent
    end1= end.getText()
    print()
    print(synopsisText)
    print()
    print(end1)
    # Create a text file named the title in the wikipedia folder
    path = 'wikipedia/'
    file = open(path+synopsisText+".txt", 'w')
    # Try to write the text into the file
    try:
        file.write(str(end1))
    # If the attempt returns a UnicodeEncodeError then encode in utf-8
    except (UnicodeEncodeError):
        file.write(str(end1.encode('utf-8')))
    file.close()
else:
    print()
    print(synopsisText)
    print()
    print(end)
    # Create a text file named the title in the wikipedia folder
    path = 'wikipedia/'
    file = open(path+synopsisText+".txt", 'w')
    # Try to write the text into the file
    try:
        file.write(str(end))
    # If the attempt returns a UnicodeEncodeError then encode in utf-8
    except (UnicodeEncodeError):
            file.write(str(end.encode('utf-8')))
    file.close()

    print('Thank you for saving the top paragraph of the wikipedia article: '+synopsisText)
