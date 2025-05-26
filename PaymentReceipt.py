from reportlab.pdfgen import canvas # Importing the canvas module from reportlab
# This module is used to create PDF files in Python.
# It allows you to draw text, shapes, and images on a PDF canvas.
def create_receipt(filename, customer_name, amount, date):# Function to create a payment receipt
    c = canvas.Canvas(filename) # Creating a canvas object to draw on the PDF
    # The filename is the name of the PDF file to be created.
    c.drawString(100, 750, "Payment Receipt") # Drawing the title on the PDF at coordinates (100, 750)
    c.drawString(100, 730, f"Customer Name: {customer_name}") # Drawing the customer's name on the PDF
    c.drawString(100, 710, f"Amount Paid: ${amount:.2f}")# Drawing the amount paid on the PDF with two decimal places
    c.drawString(100, 690, f"Date: {date}")# Drawing the date of payment on the PDF
    c.save() # Saving the PDF file after all the drawing is done