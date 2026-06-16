from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    file_name,
    income,
    expenses,
    savings,
    savings_goal
):

    pdf = SimpleDocTemplate(
        file_name
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "SmartSpend AI Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Income: ₹{income}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Expenses: ₹{expenses}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Savings: ₹{savings}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Savings Goal: ₹{savings_goal}",
            styles["Normal"]
        )
    )

    pdf.build(content)