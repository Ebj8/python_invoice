from weasyprint import HTML
HTML('invoice.html').write_pdf(target='invoice.pdf')