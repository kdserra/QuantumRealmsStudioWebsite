import json
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os
import shutil

def url_for(endpoint, filename=None):
    if endpoint == "static" and filename:
        return f"static/{filename}"
    raise RuntimeError(f"Unsupported url_for call: {endpoint}")

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["current_year"] = datetime.now().year

env = Environment(loader=FileSystemLoader("templates"))
env.globals["url_for"] = url_for

template = env.get_template("index.html")
output = template.render(**data)

os.makedirs("dist", exist_ok=True)

with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(output)

# Copy static folder into dist
if os.path.exists("static"):
    shutil.copytree("static", "dist/static", dirs_exist_ok=True)

print("Static site generated in ./dist/")
