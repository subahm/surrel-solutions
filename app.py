
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import csv
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")

# Ensure data dir exists for contact submissions
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)
CONTACT_CSV = os.path.join(DATA_DIR, "contact_submissions.csv")

NAV = [
    {"label": "Home", "endpoint": "home"},
    {"label": "Services", "endpoint": "services"},
    {"label": "About Us", "endpoint": "about"},
]

SERVICES = [
    {
        "icon": "code",
        "title": "Web Development",
        "summary": "High-performance websites and web apps tailored to your business goals.",
        "points": [
            "Responsive, accessible UI/UX",
            "SEO-friendly, fast-loading pages",
            "Modern stacks: Python, Django/Flask, React",
            "E-commerce, dashboards, portals"
        ]
    },
    {
        "icon": "cloud",
        "title": "Cloud Migration",
        "summary": "Plan, migrate, and optimize workloads on the cloud with zero drama.",
        "points": [
            "GCP-first architectures (multi-cloud ready)",
            "Lift-and-shift & replatform strategies",
            "Cost optimization & FinOps",
            "Landing zones, IAM, networking"
        ]
    },
    {
        "icon": "repeat",
        "title": "CI/CD",
        "summary": "Automated, reliable delivery pipelines from commit to production.",
        "points": [
            "GitHub Actions, GitLab CI, Cloud Build",
            "Automated testing & quality gates",
            "Blue/green & canary deployments",
            "Artifact/version management"
        ]
    },
    {
        "icon": "smartphone",
        "title": "App Development",
        "summary": "Robust mobile and desktop apps with cloud backends.",
        "points": [
            "Native & cross-platform frontends",
            "Scalable APIs & microservices",
            "Offline-first & secure auth",
            "App store readiness & telemetry"
        ]
    },
    {
        "icon": "bar-chart",
        "title": "Data Analytics",
        "summary": "Turn data into decisions with modern analytics solutions.",
        "points": [
            "Data pipelines & warehousing",
            "Real-time dashboards",
            "Exploratory analysis & ML integration",
            "Governance & data quality"
        ]
    },
    {
        "icon": "shield",
        "title": "Security Consulting",
        "summary": "Practical security engineering aligned to your risk and budget.",
        "points": [
            "Threat modeling & hardening",
            "Identity & access management",
            "Secure SDLC & SAST/DAST",
            "Compliance enablement"
        ]
    },
]

@app.context_processor
def inject_globals():
    return {
        "nav": NAV,
        "year": datetime.utcnow().year
    }

@app.route("/")
def home():
    return render_template("home.html", services=SERVICES)

@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    company = request.form.get("company", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in your name, email, and a short message.", "error")
        return redirect(request.referrer or url_for("home"))

    # Save to CSV
    write_header = not os.path.exists(CONTACT_CSV)
    with open(CONTACT_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp_utc", "name", "email", "company", "message"])
        writer.writerow([datetime.utcnow().isoformat(), name, email, company, message])

    flash("Thanks! Your message has been received. We'll get back to you shortly.", "success")
    return redirect(request.referrer or url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
