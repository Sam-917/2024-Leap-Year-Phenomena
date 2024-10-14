import qrcode
import PIL.Image

def generate_qr_code(link, filename="leapyear-app.png", box_size=10, border=4, error_correction=qrcode.constants.ERROR_CORRECT_L):
    """
    Generates a QR code image from the given link.

    Args:
        link (str): The URL to encode in the QR code.
        filename (str, optional): The filename for the saved QR code image. Defaults to "qr_code.png".
        box_size (int, optional): The size of each box in the QR code. Defaults to 10.
        border (int, optional): The width of the border around the QR code. Defaults to 4.
        error_correction (int, optional): The error correction level for the QR code. Defaults to qrcode.constants.ERROR_CORRECT_L.
    """

    qr_code = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    qr_code.add_data(link)
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color="black", back_color="white")

    # Save the image as a PNG file
    img.save(filename)

    print(f"QR code generated and saved as {filename}")

if __name__ == "__main__":
    link = "https://drive.google.com/uc?export=download&id=1kqOoZmUKCYDwnbAd1lZmo2hlEDmpLNGz"
    generate_qr_code(link)