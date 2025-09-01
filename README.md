
# Surrel Solutions — Professional Website

A production-ready Flask website for Surrel Solutions with pages for Home, Services, About Us, and a footer contact form.

## Quickstart

**Prereqs:** Python 3.10+ and pip.

```bash
cd surrel_solutions_site
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# (optional) cp .env.example .env  # and set SECRET_KEY
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Structure

```
surrel_solutions_site/
  app.py
  requirements.txt
  .env.example
  templates/
    base.html
    home.html
    services.html
    about.html
  static/
    css/styles.css
    js/main.js
    img/logo.svg
    img/favicon.svg
  data/  # created at runtime for contact form CSV
```

## Deployment

- Set `SECRET_KEY` via environment variable in production.
- Run behind a WSGI server like gunicorn or uwsgi. Example:
  ```bash
  pip install gunicorn
  gunicorn -w 2 -b 0.0.0.0:8000 app:app
  ```
- Serve `static/` via your web server (Nginx, Apache) and enable HTTPS.

## Notes

- Contact form saves submissions to `data/contact_submissions.csv` and shows a success message on the same page.
- Styling is custom, responsive, and accessible with a modern dark gradient look.
- You can customize colors in `static/css/styles.css` under `:root`.
- Update email, address, and branding in `templates/base.html` footer and the logo SVGs.
