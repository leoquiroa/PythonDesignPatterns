class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

if __name__ == "__main__":
    button_obj = ButtonFactory()
    button = ['image', 'input', 'flash']
    for b in button:
        z = button_obj.create_button(b).get_html()
        print(z)