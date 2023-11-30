import wikipedia as wiki
import urllib.parse as decoder
import random
import time
from bs4 import BeautifulSoup

wiki.set_lang("en")
nodes = {}
links = []

def link_grabber(search_item):
    '''
    Params: current search item being used
    Returns: sorted list of unique different items that are links on this page
    '''

    #Initalize constants
    results = []
    error = False
    try:
        current_page = wiki.page(str(search_item), auto_suggest=True,redirect=True)
    except:
        error = True
    #We need to ignore the items in Reference and external links places
    classesToIgnore = ['reflist', 'navbox-styles nomobile', 'navbox', 'metadata plainlinks asbox stub', 'external text', 'mw-selflink selflink']
    #As well as items that are special. ie ISBN numbers
    special_cases = ('/wiki/Special:', '/wiki/File:')
    if not error:
        html_page = current_page.html()
        soup =  BeautifulSoup(html_page, features="html.parser")
        for div in soup.find_all('div', class_=lambda x: x in classesToIgnore):
            div.decompose()
        for link in soup.find_all('a', class_= lambda x: x not in classesToIgnore):
            try:
                if link.get('href').startswith("/wiki/") and not(link.get('href').startswith(special_cases)) and link.get('href'):
                    results.append(decoder.unquote_plus(link.get('href')[6:].replace("_", " ")))
            except:
                pass
    return list(set(results))

def bfs(search_item, final_item, ):
    '''
    Params: Take in the starting and ending items
    Returns: Pathway from starting to ending items
    '''
    #Variable declaration
    '''Explanation:
        Each node will be one item. It will contain the previous item that it was called from, if the node was called from multiple items
        discard those items and keep only one path. Since the algo will go in a BFS manner, it is assured to always find the shortest path.
    '''
    explored = []
    queue = [search_item]
    special_cases = ('Wikipedia:', 'Template:', 'Portal:', 'Category:')
    while queue:
        current_node = queue.pop(0)
        if current_node not in explored:
            explored.append(current_node)
            new_links = link_grabber(current_node)
            for i in new_links:
                if i in nodes.keys():
                    pass
                elif i.startswith(special_cases):
                    pass
                else:
                    nodes[i] = current_node
                    queue.append(i)
        if final_item in explored or final_item in nodes.keys():
            return nodes


def las_vegas(search_item, final_item, counter):
    '''
    Params: Take in the starting and ending items
    Returns: Pathway from starting to ending items
    '''
    #Variable declaration
    '''Explanation:
        
        This was changed to a Las Vegas algorithm to ensure a result would be given, even if its a longer path and takes signicantly longer.
    '''
    counter +=1
    special_cases = ('Wikipedia:', 'Template:', 'Portal:', 'Category:')
    if final_item in nodes.keys():
        print("DONE! I visited: " + str(counter) + " sites!")
        return nodes, counter
    else:
        new_links = link_grabber(search_item)
        for i in new_links:
            if i in nodes.keys():
                pass
            elif i.startswith(special_cases):
                pass
            else:
                nodes[i] = search_item  
                links.append(i)
    if len(links):
        search_item = links.pop(random.randrange(len(links)))
    return las_vegas(search_item, final_item, counter)

search_item = 'Switzerland'
final_item = 'Sunlight'

#Printing results
start_time = time.time()
_ = bfs(search_item, final_item)
print("\n\nSearching for a path between '" + search_item + "' and '" + final_item + "' using BFS algorithm.")
print("The path I found is: ")
ans = [final_item]
while True:
    ans.append(nodes[final_item])
    final_item = nodes[final_item]
    if final_item == search_item:
        break
ans.reverse()
print(*ans, sep=' -> ')
print("This took: %s seconds." % (time.time() - start_time))

#Printing results for Las Vegas

nodes = {}
final_item = 'Sunlight'
start_time = time.time()
_ = las_vegas(search_item, final_item, 0)
print("\n\n--------------------------------------------------")
print("Searching for a path between '" + search_item + "' and '" + final_item + "' using Las Vegas algorithm.")
print("The path I found is: ")
ans = [final_item]
while True:
    ans.append(nodes[final_item])
    final_item = nodes[final_item]
    if final_item == search_item:
        break
ans.reverse()
print(*ans, sep=' -> ')
print("This took: %s seconds." % (time.time() - start_time))
