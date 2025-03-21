import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def main():
    # Step 2: Fetch and parse the webpage
    url = input("Enter the URL to analyze: ")
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"\nSuccessfully fetched content from {url}")
    except Exception as e:
        print(f"Error fetching content: {e}")
        return

    # Step 3: Data Analysis (Headings, Links, Paragraphs)
    headings = len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']))
    links = len(soup.find_all('a'))
    paragraphs = len(soup.find_all('p'))

    print("\n--- Data Analysis Results ---")
    print(f"Number of headings: {headings}")
    print(f"Number of links: {links}")
    print(f"Number of paragraphs: {paragraphs}")

    # Step 4: Keyword Analysis
    keyword = input("\nEnter a keyword to search: ").strip().lower()
    text = soup.get_text().lower()
    keyword_count = text.count(keyword)
    print(f"\nThe keyword '{keyword}' appears {keyword_count} times.")

    # Step 5: Word Frequency Analysis
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_5 = sorted_words[:5]

    print("\n--- Top 5 Most Frequent Words ---")
    for word, count in top_5:
        print(f"{word}: {count}")

    # Step 6: Longest Paragraph
    all_paragraphs = soup.find_all('p')
    longest_para = ""
    max_words = 0

    for para in all_paragraphs:
        para_text = para.get_text().strip()
        if para_text:
            words_in_para = para_text.split()
            if len(words_in_para) >= 5 and len(words_in_para) > max_words:
                max_words = len(words_in_para)
                longest_para = para_text

    print("\n--- Longest Paragraph ---")
    if max_words > 0:
        print(f"Word count: {max_words}\nContent: {longest_para[:200]}...")  # Truncate for brevity
    else:
        print("No qualifying paragraphs found.")

    # Step 7: Visualization
    labels = ['Headings', 'Links', 'Paragraphs']
    values = [headings, links, paragraphs]

    plt.bar(labels, values)
    plt.title('Group # [Your Group Number Here]')  # Replace with your group number
    plt.ylabel('Count')
    plt.show()

if __name__ == "__main__":
    main()