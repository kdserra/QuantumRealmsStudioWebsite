import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os

# Minimal url_for implementation for static files
def url_for(endpoint, filename=None):
    if endpoint == "static" and filename:
        return f"/static/{filename}"
    raise RuntimeError(f"Unsupported url_for call: {endpoint}")

# Load config.json
with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Add dynamic year
data["current_year"] = datetime.now().year

# Prepare Jinja environment
env = Environment(loader=FileSystemLoader("templates"))

# Inject url_for into template globals
env.globals["url_for"] = url_for

# Render index.html
template = env.get_template("index.html")
output = template.render(**data)

# Output directory
os.makedirs("dist", exist_ok=True)

# Write static file
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("Static site generated in ./dist/")
