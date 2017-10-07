from flask import render_template
from app import app

# Links that still need a home:
# Oviedo on the Park
# Contact Us
# E-mail news sign-up

sidebar_links = [
    ("Events", [
        "Events Calendar",
        "Movie in the Park Series",
        "Food Truck Thursdays",
        "Great Day in the Country",
        "Halloween Events",
        "Carnival of Screams",
        "Teenie Weenei Haloween",
        "12 Days of Christmas",
        "Snow Mountain",
        "Santa Around Town",
        "Breakfast with Santa",
        "Santa Calling"
    ]),
    ("Utilities", [
        "Pay Your Utility Bill",
        "High Water Usage?",
        "Utility Emergency Information",
        "Property Assessed Clean Energy Program",
    ]),
    ("Public Works", [
        "Public Works Home",
        "Water Conservation",

    ])
]
topbar_links = [
    ("Home", None),
    ("Information", [
        "About Oviedo",
        "History",
        "Demographics",
        "Frequently Asked Questions",
        "Garbage FAQs",
        "Irrigation Schedules",
        "Senior Safety Program",
        "Resident Information",
        "Accessibility",
        "For Business",
        "New Resident Information",
        "Sister City Information",
        "Publications and Reports",
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
    ("Getting Involved", [
        "Friends of Oviedo",
        "Volunteer Opportunities",
        "Employment",
        "Flood Zone Map",
    ]),
]

settings = {
    "head_title": "City of Oviedo",
    "page_title": "CITY OF OVIEDO, FL",
    "page_subtitle": "\"Growing in the right direction\"",
    "topbar_links": topbar_links,
    "sidebar_links": sidebar_links,
}


@app.route("/")
def index():
    return render_template("main.html", **settings)
