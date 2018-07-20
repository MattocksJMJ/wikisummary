# wikisummary
Grabs the top paragraph of a wikipedia page and writes it into a text file

## Usage
To use the script simply download it and ensure you have python and all required imports installed.
Create a folder within the current folder called wikipedia or remove the path variable and "path+" from the open function, this will save any text file in the current directory.
```Python  
path = 'wikipedia/'
file = open(path+synopsisText+".txt", 'w')
```
Once you run the script it will request a wikipedia url, this will be the downloaded page. 
Once completed you will find a text file wherever you requested it with the name of the wikipedia article containing the introductory paragraph from the article.



I am aware that not all wikipedia articles are uniform so some downloads may be converted into utf-8 which may create an ugly appearance. 
