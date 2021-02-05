'''
The model has access to the data and manages the state of the application
The view is a representation of the model
The view does not need to be graphical; textual output is also considered a totally fine view. 
The controller is the link between the model and view. 
Proper use of MVC guarantees that we end up with an application that is easy to maintain and extend
'''

quotes = (
    'A man is not complete until he is married. Then he is finished.', 
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...', 'Facts are stubborn things.')

class QuoteTerminalModel:

    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value

class QuoteTerminalView:

    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))
    
    def error(self, msg):
        print('Error: {}'.format(msg))
    
    def select_quote(self):
        return input('Out of '+str(len(quotes))+' quotes, which number would you like to see?')

class QuoteTerminalController:

    def __init__(self):
        self.model = QuoteTerminalModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
        quote = self.model.get_quote(n)
        self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()