"""Generates me/about_business.pdf (run once: python make_pdf.py)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], textColor=colors.HexColor("#1b5e3b"))
H2 = ParagraphStyle("H2", parent=ss["Heading2"], textColor=colors.HexColor("#1b5e3b"))
B = ss["BodyText"]

def P(t, s=B): return Paragraph(t, s)

story = [
    P("CedarWatt Energy", H1),
    P("<i>Independent, vendor-neutral energy advisory for Lebanese homes and small businesses.</i> "
      "(Fictional company created for the EECE 503P/798S Agentic Systems assignments.)"), Spacer(1, 12),

    P("1. Mission and Vision", H2),
    P("Mission: make reliable, clean electricity affordable by replacing guesswork with transparent, kWh-based engineering. "
      "Vision: every household in Lebanon understands exactly what its electricity costs and what each upgrade would save."),

    P("2. Services and Pricing (USD)", H2),
]
rows = [["Service", "What you get", "Price"],
        ["Free Energy Check", "20-minute call about consumption and goals", "Free"],
        ["Home Energy Audit", "Remote bill and appliance review, written savings plan", "$150 flat"],
        ["Rooftop Solar Design Package", "Sizing, panel layout, inverter and battery recommendation, bill of materials; report within 5 business days", "$600 flat (homes); businesses quoted individually"],
        ["Inverter and Battery Sizing Review", "Independent second opinion on an installer's proposal", "$200 flat"],
        ["WattWatch", "Monitoring dashboard and API for production and consumption", "$12 per month per site"]]
t = Table([[Paragraph(c, B) for c in r] for r in rows], colWidths=[4.2*cm, 8.3*cm, 4.2*cm])
t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#d7ecdf")),
                       ("GRID", (0,0), (-1,-1), 0.5, colors.grey), ("VALIGN", (0,0), (-1,-1), "TOP")]))
story += [t, Spacer(1, 12)]

story += [
    P("3. Team", H2),
    P("<b>Dr. Rana Haddad - Co-founder and CEO.</b> PhD in power systems; leads energy audits and design reviews. "
      "Believes every recommendation must come with its arithmetic."),
    P("<b>Karim Saab - Co-founder and CTO.</b> Embedded-systems engineer; leads WattWatch and CedarWatt's sizing tools."),

    P("4. Unique Value Proposition", H2),
    P("(a) Vendor-neutral: we sell no hardware and install nothing, so advice is never tied to a margin. "
      "(b) Every number explained: assumptions are listed in each report. "
      "(c) Guaranteed delivery of the design report within 5 business days."),

    P("5. How It Works", H2),
    P("Step 1: Free Energy Check call. Step 2: you send 3 months of electricity and generator bills. "
      "Step 3: we deliver the audit or design report. Step 4: optional referral to certified installers. "
      "Step 5: optional WattWatch monitoring after installation."),

    P("6. Sizing Assumptions Used in Our Estimates", H2),
    P("Unless the customer provides better data, our quick estimates assume 5.5 peak sun hours per day, a system performance ratio of 0.8 "
      "(covering inverter, temperature and wiring losses), and 550 W panels of about 2.6 square metres each. "
      "These are rough estimates, not quotes; the final design depends on roof orientation, shading and load profile."),

    P("7. FAQ", H2),
    P("<b>Do you install panels?</b> No. We design and advise; we can refer certified installers but do not guarantee their prices or schedules."),
    P("<b>Do you sell hardware?</b> No. We are vendor-neutral."),
    P("<b>Which areas do you serve?</b> All Lebanese regions remotely; on-site visits can be arranged in Beirut and Mount Lebanon."),
    P("<b>Do you offer financing or help with subsidies?</b> Not at present."),
    P("<b>What are your support hours?</b> Monday to Friday, 9:00 to 17:00 Beirut time."),
    P("<b>How do I start?</b> Leave your name and email and we will schedule the free Energy Check, or write to hello@cedarwatt.example."),
]
SimpleDocTemplate("me/about_business.pdf", pagesize=A4, title="CedarWatt Energy - Business Profile",
                  leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm).build(story)
print("wrote me/about_business.pdf")
