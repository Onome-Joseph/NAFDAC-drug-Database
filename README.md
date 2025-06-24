# Drug Recommender System (NAFDAC Database)

https://github.com/user-attachments/assets/a5c77c81-d5f2-4b95-9a05-39aef87ed24e

##  Overview

This project is a **Drug Recommender System** built using the official NAFDAC (National Agency for Food and Drug Administration and Control) products database. It helps users find similar or alternative drugs by recommending medications based on name, type, or function. Additionally, it displays the NAFDAC Registration Number of any drug in the dataset.

Built with **Python**, **Hugging Face Sentence Transformers**, and deployed using a **Flask web application**, this project contributes to the fight against fake drugs in Nigeria by allowing users to cross-verify authentic medications.

##  Key Features

- Drug Recommendation Engine using Sentence Embeddings.
- Real-time drug search with NAFDAC registration number display.
- Scraped directly from NAFDAC product database.
- 🇳🇬 Built to support public health and safety in Nigeria.

###  Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Onome-Joseph/NAFDAC-drug-Database.git
   cd NAFDAC-drug-Database
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App**

   ```bash
   python app.py
   ```

   Visit `http://127.0.0.1:5000` in your browser.

---

## Dataset

* Drug product data was scraped from the official [NAFDAC Products Database](https://nafdac.gov.ng/).
---

##  Future Improvements

* **Automatic Sync** with NAFDAC product database for real-time drug updates.
*  **Public Deployment** to serve hospitals, pharmacies, and consumers across Nigeria.
* Integration with mobile platforms (Android/iOS).
* API Access for developers and 3rd-party health platforms.

---

## 🤝 Contributing

Contributions are welcome! You can fork the repository and open a pull request to suggest changes or improvements.
