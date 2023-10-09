import os

from pypdf import PdfReader

from examples.utils import RESOURCES_PATH

reader = PdfReader(os.path.join(RESOURCES_PATH, "Python Testing with Pytest (Brian Okken).pdf"))
number_of_pages = len(reader.pages)
print(number_of_pages)
page = reader.pages[1]
text = page.extract_text()
print(text)
