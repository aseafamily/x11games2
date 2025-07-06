# Flask Application

This repository contains a Flask application that serves an HTML page.

## Running the application locally

### Prerequisites
- Python 3.x installed on your system

### Steps to Run:

1. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\Activate.ps1  # On Windows PowerShell
   # OR
   source venv/bin/activate   # On macOS/Linux
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   flask run
   ```
   Or alternatively:
   ```bash
   python app.py
   ```

4. **Access the application:**
   Open your web browser and go to:
   ```
   http://localhost:5000
   ```

### Alternative: Running without virtual environment
If you prefer not to use a virtual environment, you can install Flask globally:
```bash
pip install flask
flask run
```

### What the application does:
- The Flask server serves the `index.html` file at the root URL (`/`)
- If `index.html` doesn't exist, it shows a fallback message
- The server runs on port 5000 by default
- Debug mode is enabled for development
