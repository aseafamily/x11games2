from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    html_content = ""
    # Check if index.html exists in the current directory
    if os.path.exists("index.html"):
        with open("index.html", "r") as f:
            html_content = f.read()
    else:
        # Fallback content if index.html is not found
        html_content = "<html><body><h1>index.html not found</h1></body></html>"
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
