# Use a decorator that acts as a wrapper which decides whether or not the real decorator is executed based on some condition.
'''
*What is this pattern about?
The Decorator pattern is used to dynamically add a new feature to an
object without changing its implementation. It differs from
inheritance because the new feature is added only to that particular
object, not to the entire subclass.
'''

class TextTag:
    """Represents a base text tag"""

    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return f"<i>{self._wrapped.render()}</i>"


def main():
    
    simple_hello = TextTag("hello, world!")
    print("before:", simple_hello.render())
    #before: hello, world!
    italic_bold = ItalicWrapper(BoldWrapper(simple_hello))
    print("after:", italic_bold.render())
    #after: <i><b>hello, world!</b></i>
    italic = ItalicWrapper(simple_hello)
    print("after:", italic.render())
    #after: <i>hello, world!</i>
    

if __name__ == "__main__":
    main()