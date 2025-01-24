# Interactive Web Scraper

An intuitive web scraper built using Python and Streamlit, allowing users to extract headings, links, or specific content from web pages and view the results in an aesthetically pleasing interface.

## Features
- Input a single or multiple URLs to scrape.
- Extract content like:
  - Headings (H1, H2, H3, etc.)
  - Hyperlinks
  - Paragraph text
- Display results in a user-friendly, interactive table format.
- Built-in error handling for invalid or unreachable URLs.
- Clean, modern UI for better user experience.

---

## Installation and Setup

### Prerequisites
- Python 3.9 or higher installed on your system.
- A working internet connection to scrape content from URLs.

### Steps to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/interactive-web-scraper.git
   cd interactive-web-scraper
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On macOS/Linux
   venv\Scripts\activate          # On Windows
   ```

3. **Install Dependencies**
   Install the required Python libraries using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

5. **Access the App**
   Open your web browser and navigate to:
   ```
   http://localhost:8501
   ```

---

## How to Use

1. Enter one or more URLs (separated by commas) into the input field.
2. Select the type of content you want to scrape (Headings, Links, Paragraphs).
3. Click on the **Scrape** button.
4. View the results in the interactive table.
   - Click on links to open them directly in your browser.
   - Filter or search within the table for specific data.

---

## Dependencies

The app uses the following Python libraries:
- `streamlit`: For creating the interactive web interface.
- `requests`: For fetching web page content.
- `beautifulsoup4`: For parsing and extracting HTML data.
---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements. 

---

## License

This project is licensed under the [MIT License](LICENSE).
