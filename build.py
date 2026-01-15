import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os

# Load config.json
with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Add dynamic year
data["current_year"] = datetime.now().year

# Prepare Jinja environment
env = Environment(loader=FileSystemLoader("templates"))

# Render index.html
template = env.get_template("index.html")
output = template.render(**data)

# Output directory
os.makedirs("dist", exist_ok=True)

# Write final static HTML
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("Static site generated in ./dist/")
