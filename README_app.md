**Instructions for Use (IFU) — BIFS 614 LLM Streamlit App**
**!!! Notes !!!
The .env file contains sensitive credentials and must not be shared
The virtual environment must be activated before running the application
The repository should be updated before each use**

**1. Obtain the Repository**

  1.1 Using GitHub Desktop

    Open GitHub Desktop
    Click File → Clone repository
    Select the URL tab
    Paste the repository URL
    Choose a local folder location
    Click Clone
  
  1.2 Using Command Prompt (if Git is installed)
  
    In the terminal box enter:
    "git clone <repository_url>"
    Then enter:
    "cd BIFS-6701-Capstone-Project"
    
**2. Update to the Latest Version**

  2.1 Using GitHub Desktop
  
    Open GitHub Desktop
    Select the repository
    Click Fetch origin
    If updates are available, click Pull origin
  
  2.2 Using Command Prompt
  
    In the terminal box enter:
    "git pull origin main"

**3. Open the Project Directory**

  3.1 Navigate to the cloned folder in File Explorer
  3.2 Click the address bar, type: cmd, and press Enter
  3.3 Confirm the path is the project root directory

**4. Create a Virtual Environment**

  In the terminal box enter:
  "python -m venv venv"

**5. Activate the Virtual Environment (Windows)**

  In the terminal box enter:
  "venv\Scripts\activate"
  
  Confirm that (venv) appears in the terminal

**6. Install Required Dependencies**

  In the terminal box enter:
  "pip install -r requirements_app.txt"

**7. Configure Environment Variables**

  7.1 Create the .env file
  
    In the terminal box enter:
    "copy .env_template .env"
  
  7.2 Open the file
  
    In the terminal box enter:
    "notepad .env"
  
  7.3 Enter your credentials in the file:
  
    OPENAI_API_KEY=your_openai_api_key
    QDRANT_URL=your_qdrant_url
    QDRANT_API_KEY=your_qdrant_api_key
  
  7.4 Save and close the file

**8. Run the Application**
  
  In the terminal box enter:
  "streamlit run app.py"

**9. Use the Application**

  A browser window will open automatically
  Enter a question in the input field
  Select a mode (Study or Assessment)
  Click Submit
  View the generated response and sources

**10. Close the Application**

  In the terminal box press:
  "Ctrl + C"

  If prompted, confirm termination
