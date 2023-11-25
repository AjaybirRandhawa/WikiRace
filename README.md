# WikiRace
Finding a possible path between two different Wikipedia articles.
Wikipedia Racing with Python
This Python script enables you to play Wikipedia Racing, a game where the objective is to find the shortest path between two Wikipedia articles. The script uses a breadth-first search algorithm to navigate through Wikipedia hyperlinks.

How to Use
Clone the Repository:

```bash
git clone https://github.com/AjaybirRandhawa/wikiRace.git
```
Install Prerequisites:

Before running the script, make sure you have the required dependencies installed:

```bash
pip install wikipedia beautifulsoup4 requests
```
Run the Script:

Open the terminal and navigate to the project directory:

bash
Copy code
cd wiki-racing
Run the script with your desired start and end Wikipedia articles:

bash
Copy code
python wiki_racing.py
Code Overview
Link Grabber Function (link_grabber):

Extracts and returns a sorted list of unique links from a given Wikipedia article.
Ignores links in reference, external links, and certain special cases.
BFS Algorithm Function (bfs):

Finds the shortest path between two Wikipedia articles using the breadth-first search algorithm.
Utilizes the link grabber function to explore Wikipedia articles.
Las Vegas Algorithm Function (las_vegas):

Similar to BFS but with a modified algorithm that ensures a result is provided, even if it's a longer path and takes significantly longer.
Useful for cases where BFS may take too long to find a path.

Example Usage

```python
import wikipedia as wiki
import urllib.parse as decoder
import random
import time
from bs4 import BeautifulSoup

# Set Wikipedia language
wiki.set_lang("en")

# ... (rest of the code remains unchanged) ...

# Example: Find the shortest path between 'Germany' and 'Sunlight' using BFS
search_item = 'Germany'
final_item = 'Sunlight'

start_time = time.time()
_ = bfs(search_item, final_item)
print("\n\nSearching for a path between '" + search_item + "' and '" + final_item + "' using BFS algorithm.")
# ... (rest of the code remains unchanged) ...

# Example: Find a path between 'Germany' and 'Sunlight' using Las Vegas algorithm
nodes = {}
final_item = 'Sunlight'
start_time = time.time()
_ = las_vegas(search_item, final_item, 0)
print("\n\n--------------------------------------------------")
print("Searching for a path between '" + search_item + "' and '" + final_item + "' using Las Vegas algorithm.")
# ... (rest of the code remains unchanged) ...
```
Feel free to explore the code and customize it according to your preferences. Happy Wikipedia Racing!
