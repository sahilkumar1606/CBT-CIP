from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(file_name, details):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, "Payment Receipt")
    c.setFont("Helvetica", 12)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.drawString(72, height - 100, f"Date: {date}")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(72, height - 140, "Customer Information:")
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 160, f"Name: {details['name']}")
    c.drawString(72, height - 180, f"Email: {details['email']}")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(72, height - 220, "Payment Details:")
    c.setFont("Helvetica", 12)
    c.drawString(72, height - 240, f"Amount Paid: ${details['amount']:.2f}")
    c.drawString(72, height - 260, f"Transaction ID: {details['transaction_id']}")
    c.drawString(72, height - 280, f"Payment Method: {details['payment_method']}")
 
    c.setFont("Helvetica", 10)
    c.drawString(72, 72, "Thank you for your payment!")
    
    c.save()

def main():
    print("Enter payment details to generate receipt.")
    
    name = input("Customer Name: ")
    email = input("Customer Email: ")
    amount = float(input("Amount Paid: "))
    transaction_id = input("Transaction ID: ")
    payment_method = input("Payment Method: ")
    
    details = {
        'name': name,
        'email': email,
        'amount': amount,
        'transaction_id': transaction_id,
        'payment_method': payment_method
    }

    file_name = f"receipt_{transaction_id}.pdf"
    create_receipt(file_name, details)
    print(f"Receipt saved as {file_name}")

if __name__ == "__main__":
    main()