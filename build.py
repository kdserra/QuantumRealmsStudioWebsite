from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader("templates"))
pages = ["index.html", "about.html"]

os.makedirs("dist", exist_ok=True)

for page in pages:
    template = env.get_template(page)
    output = template.render()
    with open(os.path.join("dist", page), "w", encoding="utf-8") as f:
        f.write(output)
