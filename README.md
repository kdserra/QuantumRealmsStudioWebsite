# Quantum Realms Studio Website

This is the official website for Quantum Realms Studio, built with Flask.

## Project Structure

```
/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css   # Main stylesheet
│   └── images/
│       ├── skywar/     # Skywar assets
│       └── slap-battle/# Slap Battle assets
└── templates/
    └── index.html      # Main landing page
```

## Run app

```
py -3.10 app.py
```

## Local Development

1.  **Install Python:** Ensure you have Python installed.
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Application:**
    ```bash
    python app.py
    ```
4.  **View:** Open your browser and go to `http://127.0.0.1:5000`.



## Deploying to PythonAnywhere

This project is designed to be easily hosted on [PythonAnywhere](https://www.pythonanywhere.com/).

### Step 1: Upload Code
1.  Sign up or log in to PythonAnywhere.
2.  Go to the **Consoles** tab and verify your files are uploaded (you can zip the project and upload it via the **Files** tab, then unzip it in a Bash console).
    - Alternatively, you can use `git clone` if you push this to a repository.

### Step 2: Set up Virtual Environment (Optional but Recommended)
In a Bash console:
```bash
mkvirtualenv --python=/usr/bin/python3.10 my-virtualenv
pip install -r requirements.txt
```

### Step 3: Configure Web App
1.  Go to the **Web** tab.
2.  Click **Add a new web app**.
3.  Click **Next**, then choose **Flask**.
4.  Select the **Python 3.10** (or your preferred version) version.
5.  **Important:** For the "Path to your flask app", enter the path to where you uploaded `app.py`.
    - Example: `/home/yourusername/QuantumRealmsStudioWebsite/app.py`
6.  Click **Next** to let it create the WSGI file.

### Step 4: Configure Static Files (Crucial for Images/CSS)
1.  Scroll down to the **Static Files** section on the **Web** tab.
2.  Enter the URL and Path:
    - **URL:** `/static/`
    - **Path:** `/home/yourusername/QuantumRealmsStudioWebsite/static`
    *(Replace `yourusername` and the folder name with your actual path)*

### Step 5: Reload
1.  Scroll to the top of the **Web** tab.
2.  Click the big green **Reload** button.
3.  Click the link to your site (e.g., `yourusername.pythonanywhere.com`) to view it!

## Customization
- **Images:** Add more images to `static/images` and reference them in `index.html`.
- **Styles:** Edit `static/css/style.css` to change colors or animations.
