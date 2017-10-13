from flask import render_template
from app import app

# Links that still need a home:
# Oviedo on the Park
# Contact Us
# E-mail news sign-up
colors = {
    "mm": "#01579b",
    "ml": "#4f83cc",
    "md": "#002f6c",
    "vv": "#f9a825",
    "vl": "#ffd95a",
    "vd": "#c17900",
}

sidebar_links = [
    ("Events", [
        "Events Calendar",
        "Movie in the Park Series",
        "Food Truck Thursdays",
        "Great Day in the Country",
        "Halloween Events",
        "Christmas Events",
    ]),
    ("Utilities", [
        "Pay Your Utility Bill",
        "High Water Usage?",
        "Utility Emergency Information",
        "Property Assessed Clean Energy Program",
    ]),
    ("Getting Involved", [
        "Friends of Oviedo",
        "Volunteer Opportunities",
        "Employment",
    ]),
]
topbar_links = [
    ("Home", None),
    ("About Oviedo", [
        "About Oviedo",
        "History",
        "Demographics",
        "Frequently Asked Questions",
    ]),
    ("City Departments", [
        "City Manager",
        "Assistant City Manager",
        "Development Services",
        "Finance Department",
        "Informtaion Technology",
        "Fire Department",
        "Human Resources",
        "Public Works",
        "Police",
        "Recreation and Parks",
    ]),
    ("Government", [
        "Government Home",
        "Mayor and Council",
        "City Clerk",
        "Charter and Code of Ordinances",
        "State of the City",
        "City Stragegic Plan",
        "Meetings List",
        "Speak at Council Meeting",
        "Citizen Request",
    ]),
    ("Facilities", [
        "Public Facilities List",
        "Cultural Center and Ampitheatre Information",
        "Center Lake Park",
        "Reporting Street Light Outages"
    ]),
    ("Development Services", [
        "Development Services Home",
        "Building Services",
        "Planning and Development",
        "Code Enforcement",
        "Purchasing",
        "Building Permits",
        "Business Tax Receipt",
        "Economic Development",
        "Community Redevelopment Agency Documents",
    ]),
    ("Information", [
        "Garbage FAQs",
        "Irrigation Schedules",
        "Senior Safety Program",
        "Resident Information",
        "Accessibility",
        "For Business",
        "New Resident Information",
        "Sister City Information",
        "Publications and Reports",
        "Flood Zone Map",
    ]),
]

settings = {
    "head_title": "City of Oviedo",
    "page_title": "CITY OF OVIEDO, FL",
    "page_subtitle": "\"Growing in the right direction\"",
    "topbar_links": topbar_links,
    "sidebar_links": sidebar_links,
    "colors": colors,
}


@app.route("/")
def index():
    return render_template("main.html", **settings)

@app.route("/material")
def material():
    return render_template("material.html", **settings)
