# SiteGen - Simple Markdown to Static Portfolio Site Generator

**Version:** 1.0.0

---

## What is SiteGen?

SiteGen is a lightweight, no-code static site generator that converts your Markdown portfolio content into a polished HTML website using Jinja2 templates.

- No setup required beyond Python and the listed dependencies  
- Easy to customize your portfolio by editing a single Markdown file  
- Generates a clean, responsive HTML portfolio ready to host anywhere (GitHub Pages, Netlify, etc.)

---

## Features

- Converts `.md` files in the `content/` folder into HTML files in the `output/` folder  
- Uses `templates/base.html` as the HTML template with embedded CSS styling  
- Automatically creates the `output/` folder if it doesn't exist  
- Friendly error messages and simple usage flow — perfect for beginners

---

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- `jinja2` and `markdown` Python packages  
  Install via pip if you don’t have them:

```bash
pip install jinja2 markdown
```

---

### Usage

1. **Edit your portfolio content:**  
   Open or create the Markdown file at `content/portfolio.md` and add your personal info, projects, and contact details in Markdown format.

2. **Run the generator:**  
   From your project directory, run:

```bash
python sitegen.py
```

3. **View your site:**  
   Open the generated HTML file in your browser:

```
output/portfolio.html
```

---

## Project Structure

```
sitegen/
├── content/
│   └── portfolio.md        # Your portfolio content in Markdown
├── output/
│   └── portfolio.html      # Generated HTML file (created after running)
├── templates/
│   └── base.html           # HTML template for the site
├── sitegen.py              # The static site generator script
└── README.md               # This file
```

---

## Customization

- Modify `templates/base.html` to change the look and feel of your portfolio  
- Add your own CSS or link external stylesheets inside `base.html`  
- Write your content in Markdown inside `content/portfolio.md` — the generator will convert it automatically

---


## Questions or Feedback?

Feel free to open an issue or reach out!

---

*Happy portfolio building!* 🚀
