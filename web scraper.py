import streamlit as st
import requests
from bs4 import BeautifulSoup

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f7f9fc;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #2c3e50;
            text-align: center;
        }
        .subheader {
            color: #3498db;
            text-align: center;
        }
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 1px solid #ddd;
            padding: 10px;
            font-size: 16px;
        }
        .content-card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            margin-bottom: 15px;
        }
        .content-card h3 {
            color: #34495e;
            margin-bottom: 10px;
        }
        .content-card ul {
            list-style-type: none;
            padding: 0;
        }
        .content-card ul li {
            margin: 5px 0;
        }
        .content-card ul li a {
            color: #3498db;
            text-decoration: none;
        }
        .content-card ul li a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("🌐 Interactive Web Scraper")
st.subheader("Extract headings and links from web pages with ease!")

# URL Input
st.markdown("<h4 class='subheader'>Enter a URL to scrape:</h4>", unsafe_allow_html=True)
url = st.text_input("Paste the URL here", placeholder="https://example.com", key="url_input")

# Function to fetch and parse content
def scrape_website(url):
    try:
        # Display progress bar
        progress = st.progress(0)
        st.info("Fetching the page...")

        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()
        progress.progress(33)

        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")
        st.success("Page successfully fetched!")
        progress.progress(66)

        # Extract headings and links
        headings = [heading.get_text() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
        links = [{"text": link.text.strip(), "href": link['href']} for link in soup.find_all('a', href=True) if link.text.strip()]
        progress.progress(100)

        return headings, links
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching the URL: {e}")
        return None, None

# Display scraped content in cards
def display_results(headings, links):
    if headings:
        st.markdown("<div class='content-card'><h3>📋 Extracted Headings:</h3>", unsafe_allow_html=True)
        st.markdown("<ul>", unsafe_allow_html=True)
        for heading in headings:
            st.markdown(f"<li>{heading}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

    if links:
        st.markdown("<div class='content-card'><h3>🔗 Extracted Links:</h3>", unsafe_allow_html=True)
        st.markdown("<ul>", unsafe_allow_html=True)
        for link in links:
            st.markdown(f"<li><a href='{link['href']}' target='_blank'>{link['text']}</a></li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

# Scrape and Display Button
if url:
    if st.button("🔍 Scrape Website"):
        st.info("Starting the scraping process...")
        headings, links = scrape_website(url)
        if headings or links:
            st.success("🎉 Scraping complete! See the results below.")
            display_results(headings, links)
        else:
            st.warning("No headings or links found on the page.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
