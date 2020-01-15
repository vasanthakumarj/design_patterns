quotes =(
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...',
    'Facts are stubborn things.'
)

#Model
class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = "Not Found!!!"
        return value

#View
class QuoteTerminalView:
    def show(self, quote):
        print(f'And Quote is "{quote}"')

    def error(self, error):
        print(f'Error:{error}')

    def select_quote(self):
        return input("What qoute you would like to see :")

#controller
class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                inp = self.view.select_quote()
                n = int(inp)
                valid_input = True
            except ValueError as err:
                self.view.error(f'Incorrect index of {n}')
            quote = self.model.get_quote(n)
            self.view.show(quote)


#calling controller
def main():
    controller = QuoteTerminalController()
    controller.run()

if __name__ == "__main__":
    main()




