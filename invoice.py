from weasyprint import HTML
pdf = HTML('invoice.html').write_pdf()