import qrcode

qr = qrcode.QRCode(
    version=15,   # Version of the QR code (higher number means bigger image)
    box_size=10,  # Size of the box where the QR code will be displayed
    border=5      # Width of the white border around the QR code
)

data = "https://www.youtube.com/channel/UCAYO6s81Sqtd7hQqwXORKtg/playlists"

qr.add_data(data)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("test.png")