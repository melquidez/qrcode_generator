import qrcode
import csv
import os

# Make sure output folder exists

output_folder = "qr_contacts"
os.makedirs(output_folder, exist_ok=True)

# Read CSV and generate

with open("contacts.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_name = row['first_name']
        last_name = row['last_name']
        full_name = f"{first_name} {last_name}"
        org = row['org']
        title = row['title']
        phone = row['phone']
        email = row['email']

        # Build vCard string
        vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name};;;
FN:{full_name}
ORG:{org}
TITLE:{title}
TEL;TYPE=WORK,VOICE:{phone}
EMAIL:{email}
END:VCARD
"""

# Create QR code

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=5
)
qr.add_data(vcard)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")

# Save with a with contact name as file name

filename = f"{output_folder}/{first_name}_{last_name}_qr.png".replace(" ", "_")
img.save(filename)
print(f"Saved QR code for {full_name} -> {filename}")
