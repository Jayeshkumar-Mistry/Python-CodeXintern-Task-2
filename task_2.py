import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=5):
    """
    Perform a Google search and return the top results.
    """
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []
        for result in soup.find_all('div', class_='tF2Cxc'):
            title = result.find('h3').text if result.find('h3') else 'No title'
            link = result.find('a')['href'] if result.find('a') else 'No link'
            description = result.find('div', class_='VwiC3b').text.strip() if result.find('div', class_='VwiC3b') else 'No description'
            results.append({
                'Title': title,
                'Link': link,
                'Description': description
            })

        return results[:num_results]
    except Exception as e:
        print("Something went wrong:", e)
        return []

# Example usage
if __name__ == "__main__":
    search_query = "Python programming tutorials"
    results = google_search(search_query, num_results=5)

    for i, result in enumerate(results):
        print(f"Result {i + 1}:")
        print(f"Title: {result['Title']}")
        print(f"Link: {result['Link']}")
        print(f"Description: {result['Description']}\n")
import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=5):
    """
    Perform a Google search and return the top results.
    """
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []
        for result in soup.find_all('div', class_='tF2Cxc'):
            title = result.find('h3').text if result.find('h3') else 'No title'
            link = result.find('a')['href'] if result.find('a') else 'No link'
            description = result.find('div', class_='VwiC3b').text.strip() if result.find('div', class_='VwiC3b') else 'No description'
            results.append({
                'Title': title,
                'Link': link,
                'Description': description
            })

        return results[:num_results]
    except Exception as e:
        print("Something went wrong:", e)
        return []

# Example usage
if __name__ == "__main__":
    search_query = "Python programming tutorials"
    results = google_search(search_query, num_results=5)

    for i, result in enumerate(results):
        print(f"Result {i + 1}:")
        print(f"Title: {result['Title']}")
        print(f"Link: {result['Link']}")
        print(f"Description: {result['Description']}\n")
