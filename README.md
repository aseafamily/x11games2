# FastAPI Application

This repository contains a FastAPI application that serves an HTML page.

## Running the application locally

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**
    ```bash
    python main.py
    ```
    Or using Uvicorn directly:
    ```bash
    uvicorn main:app --reload
    ```

The application will be available at `http://localhost:8000`.
