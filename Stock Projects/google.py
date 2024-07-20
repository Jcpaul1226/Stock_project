try:
	from googlesearch import search
except ImportError: 
	print("No module named 'google' found")

# to search
query = "Recent GME news articles"

for j in search(query, tld="co.in", num=5, stop=5, pause=2):
	print(j)
