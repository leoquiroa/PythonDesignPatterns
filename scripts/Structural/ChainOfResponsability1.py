class ReportFormat(object):
    HTML = 0
    TEXT = 1
    JPG = 2

class Report(object):
    def __init__(self, format_):
        self.title = 'Monthly report'
        self.text = ['Things are going', 'really, really well.']
        self.format_ = format_

# - Handler - HTML and TEXT ------------------------------------

class Handler(object):

    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        self.nextHandler.handle(request)

class PDFHandler(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.HTML:
            self.output_report(request.title, request.text)
        else:
            super(PDFHandler, self).handle(request)
	
    def output_report(self, title, text):
        print( '<html>')
        print( ' <head>')
        print( ' <title>%s</title>' % title)
        print( ' </head>')
        print( ' <body>')
        for line in text:
            print( ' <p>%s<p>' % line)
        print( ' </body>')
        print( '</html>')

class TextHandler(Handler):
    
    def handle(self, request):
        if request.format_ == ReportFormat.TEXT:
            self.output_report(request.title, request.text)
        else:
            super(TextHandler, self).handle(request)

    def output_report(self, title, text):
        print( 5*'*' + title + 5*'*')
        for line in text:
            print( line)

# Error ------------------------------------

class ErrorHandler(Handler):
    def handle(self, request):
        print( "Invalid request")

if __name__ == '__main__':
    # the 2 objects
    pdf_handler = PDFHandler()
    text_handler = TextHandler()
    # connect them
    # HTML -> text -> error
    pdf_handler.nextHandler = text_handler
    text_handler.nextHandler = ErrorHandler()
    # TEXT case
    print(' - TEXT case - ')
    report1 = Report(ReportFormat.TEXT)
    pdf_handler.handle(report1)
    # HTML case
    print(' - HTML case - ')
    report2 = Report(ReportFormat.HTML)
    pdf_handler.handle(report2)
    print(' - JPG case - ')
    report3= Report(ReportFormat.JPG)
    pdf_handler.handle(report3)