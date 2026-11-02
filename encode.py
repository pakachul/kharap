import argparse, base64
from pathlib import Path
from urllib.parse import urlencode
p=argparse.ArgumentParser()
p.add_argument("xml_file")
p.add_argument("--page",required=True)
p.add_argument("--id",default="video-example")
a=p.parse_args()
xml=Path(a.xml_file).read_text(encoding="utf-8")
b=base64.b64encode(xml.encode()).decode()
q=urlencode({"xml":"data:application/xml;base64,"+b,"id":a.id})
print("BASE64:\n"+b+"\n\nURL:\n"+a.page+("&" if "?" in a.page else "?")+q)
