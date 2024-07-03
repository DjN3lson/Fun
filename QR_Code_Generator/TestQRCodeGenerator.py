import unittest as ut
from io import BytesIO


class TestQRCodeGenerator(ut.TestCase):
    def test_generate_qr(self):
        qr = qrc.QRCode(
            version=1,
            error_correction=qrc.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('http://example.com')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        self.assertIsInstance(img, Image.Image)
    def test_generate_qr_invalid_version(self):
        with self.assertRaises(ValueError):
            qr = qrc.QRCode(
                version=41,
                error_correction=qrc.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

    def test_generate_qr_invalid_box_size(self):
        with self.assertRaises(ValueError):
            qr = qrc.QRCode(
                version=1,
                error_correction=qrc.constants.ERROR_CORRECT_L,
                box_size=0,
                border=4,
            )

    def test_generate_qr_invalid_border_size(self):
        with self.assertRaises(ValueError):
            qr = qrc.QRCode(
                version=1,
                error_correction=qrc.constants.ERROR_CORRECT_L,
                box_size=10,
                border=11,
            )

    def test_save_qr(self):
        qr = qrc.QRCode(
            version=1,
            error_correction=qrc.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('http://example.com')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        self.assertTrue(buffer.getvalue())

if __name__ == '__main__':
    unittest.main()