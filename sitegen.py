# Imports
from jinja2 import Environment, FileSystemLoader, Template, TemplateNotFound

env = Environment(loader=FileSystemLoader("templates"), )
import markdown
import os


# Read a md file
def gen_site(file):

  # Some prelim checks
  if not os.path.exists(file):
    print(f"File not found: {file}")
    return

  if not file.endswith('.md'):
    print("Only Markdown (.md) files are supported.")
    return

  # Split filename
  try:
    split_path = str(file).split('/')[1]
    new_filename = split_path.split('.md')[0]
  except IndexError:
    print("You must pass in a file path like 'content/filename.md'.")
    return

  with open(file, 'r') as md:
    scanned_markdown = md.read()

    # Convert the md to html
    content = markdown.markdown(scanned_markdown)

    # Grab jinja template
    try:
      template = env.get_template("base.html")
    except TemplateNotFound:
      print("Template 'base.html' not found in path 'templates/'")
      return

    result = template.render(content=content)

  if not os.path.exists('output/'):
    os.mkdir('output/')
    print("Directory 'output/' was automatically created.")

  with open(f'output/{new_filename}.html', 'w') as f:
    f.write(result)
    print("Portfolio site generated successfully!\n")
    print(f"Open 'output/{new_filename}.html' to preview.")


# You can change 'portfolio' to the desired output file name
filename = 'content/portfolio.md'

# Main Program
gen_site(filename)
