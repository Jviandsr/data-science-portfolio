import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seaborn_module
import time

def fetch_open_library_data(subjects):
    """
    Fetches book data from the Open Library Search API across multiple subjects,
    extracting edition counts, publish years, and ratings/ebook availability.
    """
    base_url = "https://openlibrary.org/search.json"
    headers = {
        "User-Agent": "AcademicBookResearchProject/1.0 (student_research@example.com)"
    }
    
    all_books = []
    
    for subject in subjects:
        print(f"Querying Open Library for subject: {subject}...")
        params = {
            'subject': subject,
            'limit': 50
        }
        
        try:
            response = requests.get(base_url, headers=headers, params=params)
            
            if response.status_code == 429:
                print("Rate limit reached. Sleeping for 10 seconds...")
                time.sleep(10)
                response = requests.get(base_url, headers=headers, params=params)
                
            response.raise_for_status()
            data = response.json()
            docs = data.get('docs', [])
            
            for doc in docs:
                title = doc.get('title', 'Unknown')
                author_list = doc.get('author_name', ['Unknown'])
                author = author_list[0] if author_list else 'Unknown'
                
                # Metrics serving as proxies for popularity and edition count
                edition_count = doc.get('edition_count', 1)
                first_publish_year = doc.get('first_publish_year', 2000)
                rating_average = doc.get('ratings_average', None)
                rating_count = doc.get('ratings_count', 0)
                ebook_count = doc.get('ebook_count_i', 0)
                
                all_books.append({
                    'Title': title,
                    'Author': author,
                    'Subject': subject.capitalize(),
                    'EditionCount': edition_count,
                    'FirstPublishYear': first_publish_year,
                    'RatingAverage': rating_average,
                    'RatingCount': rating_count,
                    'EbookCount': ebook_count
                })
                
        except requests.exceptions.RequestException as e:
            print(f"API request failed for {subject}: {e}")
            
        time.sleep(1.5) # Polite scraping pause
        
    return pd.DataFrame(all_books)

# 1. Gather data across categories aligned with your research scope
target_subjects = ['fiction', 'business', 'computer science', 'history', 'science', 'romance']
df_raw = fetch_open_library_data(target_subjects)

# 2. Data Cleaning & Preparation
df_clean = df_raw.dropna(subset=['FirstPublishYear']).copy()
# Filter out obvious anomalous publish years
df_clean = df_clean[(df_clean['FirstPublishYear'] >= 1800) & (df_clean['FirstPublishYear'] <= 2026)]

print(f"Successfully cleaned dataset with {len(df_clean)} observations.")

# Save dataset locally for GitHub reproducibility
df_clean.to_csv('open_library_cleaned_books.csv', index=False)

# 3. Data Visualization (Chart Generation)
# Setting up visual style
plt.figure(figsize=(12, 6))
seaborn_module.set_theme(style="whitegrid")

# Create a boxplot showing the distribution of edition counts across different book genres/subjects
ax = seaborn_module.boxplot(
    data=df_clean, 
    x='Subject', 
    y='EditionCount', 
    palette='muted',
    showfliers=False # Removes extreme outliers for cleaner chart scaling
)

plt.title('Comparison of Edition Counts Across Book Categories (Open Library API)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Book Category / Subject', fontsize=12, labelpad=10)
plt.ylabel('Number of Editions Published', fontsize=12, labelpad=10)
plt.xticks(rotation=15)

# Save figure for inclusion in your GitHub repository/report
plt.tight_layout()
plt.savefig('genre_edition_distribution.png', dpi=300)
plt.show()
