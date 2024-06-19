from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_receipt(receipt_data):
    # Receipt data
    receipt_number = receipt_data['receipt_number']
    date = receipt_data['date']
    customer_name = receipt_data['customer_name']
    items = receipt_data['items']
    total_amount = receipt_data['total_amount']
    payment_method = receipt_data['payment_method']

    # Create a canvas object
    pdf_file = f"receipt_{receipt_number}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    # Draw the title
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(width / 2, height - 50, "Payment Receipt")

    # Draw the receipt details
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Receipt Number: {receipt_number}")
    c.drawString(50, height - 120, f"Date: {date}")
    c.drawString(50, height - 140, f"Customer Name: {customer_name}")

    # Draw the item table
    c.drawString(50, height - 180, "Items:")
    c.drawString(50, height - 200, "-----------------------------------------")
    y_position = height - 220
    for item in items:
        c.drawString(50, y_position, f"{item['name']}: ${item['price']}")
        y_position -= 20

    c.drawString(50, y_position, "-----------------------------------------")
    y_position -= 20

    # Draw the total amount and payment method
    c.drawString(50, y_position, f"Total Amount: ${total_amount}")
    y_position -= 20
    c.drawString(50, y_position, f"Payment Method: {payment_method}")

    # Save the PDF
    c.save()
    print(f"Receipt saved as {pdf_file}")

# Example usage
receipt_data = {
    'receipt_number': '123456',
    'date': '2023-06-16',
    'customer_name': 'John Doe',
    'items': [
        {'name': 'Item 1', 'price': 29.99},
        {'name': 'Item 2', 'price': 9.99},
        {'name': 'Item 3', 'price': 14.99}
    ],
    'total_amount': 54.97,
    'payment_method': 'Credit Card'
}

create_receipt(receipt_data)

