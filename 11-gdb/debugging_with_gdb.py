import io

import xmlsec
from lxml import etree

stream = io.BytesIO(
    b"""<?xml version="1.0" encoding="UTF-8"?>
<Envelope xmlns="urn:envelope" ID="ef115a20-cf73-11e5-aed1-3c15c2c2cc88">
  <Data>
    Hello, World!
  </Data>
</Envelope>
"""
)
root = etree.parse(stream).getroot()
xmlsec.tree.add_ids(root, ["ID"])
print(etree.tostring(root, pretty_print=True).decode())
