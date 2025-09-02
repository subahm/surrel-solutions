
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import csv
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")
app.url_map.strict_slashes = False

# Ensure data dir exists for contact submissions
#DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
#os.makedirs(DATA_DIR, exist_ok=True)

DATA_DIR = '/tmp/data'
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
        "summary": "Crafting responsive, engaging websites—from sleek single-page sites to robust e-commerce platforms—that amplify your brand presence and drive customer engagement.",
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
        "summary": "Seamless, secure migration of data and applications to the cloud. We handle migration strategy, execution, and optimization to boost scalability and performance while controlling costs.",
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
        "summary": "Streamlined DevOps workflows featuring automated testing, integration, and deployment, enabling rapid iteration and higher software quality with minimal manual overhead.",
        "points": [
            "GitHub Actions, GitLab CI, Cloud Build",
            "Automated testing & quality gates",
            "Blue/green & canary deployments",
            "Reduced manual configuration errors"
        ]
    },
    {
        "icon": "smartphone",
        "title": "App Development",
        "summary": "Bespoke web and mobile app development aligned with your business goals. Our user-centric process ensures intuitive interfaces, robust functionality, and seamless performance.",
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
        "summary": "Unlock the power of your data through advanced analysis and visualization. We help you make data-driven decisions that optimize operations, deepen customer understanding, and fuel growth.",
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
        "summary": "In-depth security assessments that identify vulnerabilities and deliver clear, strategic recommendations—so you can protect your systems, comply with industry standards, and operate with confidence.",
        "points": [
            "Threat modeling & hardening",
            "Identity & access management",
            "Secure SDLC & SAST/DAST",
            "Compliance enablement"
        ]
    },
]

additional_services = [
    {
        "title": "IT Consulting",
        "description": "Expert advice and strategic roadmaps to align technology initiatives with business objectives."
    },
    {
        "title": "Digital Marketing",
        "description": "Amplify your reach with targeted SEO, content strategy, and performance-driven campaigns."
    },
    {
        "title": "Technical Training",
        "description": "Empower your team through customized training programs tailored to your technology stack and business needs."
    }
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
    import os
    port = int(os.environ.get("PORT", 5000))  # Use GCP PORT if set, otherwise default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
