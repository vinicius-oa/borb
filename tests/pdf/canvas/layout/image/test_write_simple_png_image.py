import logging
import unittest
from pathlib import Path

from ptext.io.read.types import Decimal
from ptext.pdf.canvas.layout.image import Image
from ptext.pdf.canvas.layout.page_layout import SingleColumnLayout
from ptext.pdf.document import Document
from ptext.pdf.page.page import Page
from ptext.pdf.pdf import PDF
from tests.util import get_log_dir, get_output_dir

logging.basicConfig(
    filename=Path(get_log_dir(), "test-write-simple-png-image.log"), level=logging.DEBUG
)


class TestWriteSimplePNGImage(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.output_dir = Path(get_output_dir(), "test-write-simple-png-image")

    def test_write_document(self):

        # create output directory if it does not exist yet
        if not self.output_dir.exists():
            self.output_dir.mkdir()

        # create empty document
        pdf: Document = Document()

        # create empty page
        page: Page = Page()

        # add page to document
        pdf.append_page(page)

        # add Image
        layout = SingleColumnLayout(page)

        # add image
        layout.add(
            Image(
                "https://www.mozilla.org/media/protocol/img/logos/firefox/browser/logo-lg-high-res.fbc7ffbb50fd.png",
                width=Decimal(256),
            )
        )

        # write
        file = self.output_dir / "output.pdf"
        with open(file, "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, pdf)

        return True


if __name__ == "__main__":
    unittest.main()