from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT

slides = [
    ("CAB BOOKING SYSTEM", ["A Web Application Project", "By: Haritha"]),
    ("Objective", [
        "Provide easy online cab booking",
        "Calculate fare automatically",
        "Connect user with driver in real-time",
        "Save time and reduce manual work"
    ]),
    ("Features", [
        "User Login - Name and Phone Number",
        "Book Cab - Pickup and Drop location",
        "Payment Options - Cash, UPI, Card",
        "Driver Dashboard - See all bookings",
        "Fare Calculation - Based on distance"
    ]),
    ("Technologies Used", [
        "Frontend: HTML, CSS, JavaScript",
        "Backend: Node.js, Express.js",
        "Storage: LocalStorage / JSON file",
        "Deployment: GitHub + Render"
    ]),
    ("Working Process", [
        "User enters details and books cab",
        "Data is saved in server",
        "Driver can see booking on dashboard",
        "Driver accepts and completes ride"
    ]),
    ("Advantages", [
        "Fast and Easy Booking",
        "Mobile Friendly",
        "Transparent Fare",
        "24/7 Available"
    ]),
    ("Screenshots", [
        "home.png",
        "booking.png",
        "driver.png"
    ]),
    ("Conclusion", [
        "Cab Booking System makes travel easy and fast.",
        "It reduces waiting time and provides a smooth experience for both user and driver."
    ])
]

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleStyle', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor('#1f7a3d'), spaceAfter=18))
styles.add(ParagraphStyle(name='BodyStyle', parent=styles['BodyText'], fontSize=13, leading=18, spaceAfter=10, leftIndent=12))
styles.add(ParagraphStyle(name='SubtitleStyle', parent=styles['BodyText'], fontSize=14, leading=18, textColor=colors.HexColor('#4b5563'), spaceAfter=14))

doc = SimpleDocTemplate('cab_booking_presentation.pdf', pagesize=A4, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
story = []

for title, bullets in slides:
    story.append(Paragraph(title, styles['TitleStyle']))
    if title == 'CAB BOOKING SYSTEM':
        story.append(Paragraph('A Web Application Project', styles['SubtitleStyle']))
        story.append(Paragraph('By: Haritha', styles['SubtitleStyle']))
    else:
        for item in bullets:
            story.append(Paragraph(f"• {item}", styles['BodyStyle']))
    story.append(Spacer(1, 12))
    if title != slides[-1][0]:
        story.append(PageBreak())

doc.build(story)
print('Created cab_booking_presentation.pdf')
