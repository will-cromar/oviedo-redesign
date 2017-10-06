from flask import render_template
from app import app

sidebar_links = [
    {"title": "Information",
     "sublinks": [
         "Events",
         "Oviedo on the Park",
         "Community Redevelopment Agency Documents",
         "Oviedo Veterans Tribute",
         "State of the City",
         "Publications and Reports",
         "City Strategic Plan",
         "Resident Information",
         "Street Light Outage, Solid Waste, Water Conservation, Flood Zone Info",
         "Utility Emergency Numbers and Information",
         "Frequently Asked Questions",
         "For Business",
         "Public Notices",
         "Accessibility",
     ]},
    {"title": "Online Services",
     "sublinks": [
         "Citizen Request",
         "City GIS Map Gallery",
         "Friends of Oviedo",
         "Find a Job",
         "Pay your Utility Bill",
         "Recreation Registration",
         "Building Permits",
         "Business Tax Receipts",
         "Planning/Development Review"
     ]}
]
topbar_links = [
    "Home",
    "About Oviedo",
    "City Departments",
    "Government",
    "Employment",
    "Facilities",
    "Getting Involved"
]

settings = {
    "head_title": "City of Oviedo",
    "page_title": "CITY OF OVIEDO, FLORIDA",
    "page_subtitle": "Growing in the right direction",
    "topbar_links": topbar_links,
    "sidebar_links": sidebar_links,
}


@app.route("/")
def index():
    return render_template("main.html", **settings)
