from pathlib import Path
import sys
import pypdfium2 as pdfium
source=Path(sys.argv[1]);target=Path(sys.argv[2]);target.mkdir(parents=True,exist_ok=True)
doc=pdfium.PdfDocument(str(source))
for i,page in enumerate(doc,1):
    page.render(scale=1.4).to_pil().save(target/f'page-{i:02d}.png')
print(f'{len(doc)} paginas')
