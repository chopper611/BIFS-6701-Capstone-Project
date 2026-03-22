# BIFS 614 LLM Streamlit App

## Important
Always ensure you are working from the latest version of the repository.

### Update using GitHub Desktop
1. Open GitHub Desktop  
2. Select this repository  
3. Click "Fetch origin"  
4. If updates are available, click "Pull origin"  

---

## Setup Instructions

1. Activate virtual environment  
venv\Scripts\activate

2. Install app dependencies  
pip install -r requirements_app.txt

3. Create environment file  
Copy .env.template and rename it to .env  
Fill in your credentials:

OPENAI_API_KEY=your_key  
QDRANT_URL=your_url  
QDRANT_API_KEY=your_key  

4. Run the app  
streamlit run app.py