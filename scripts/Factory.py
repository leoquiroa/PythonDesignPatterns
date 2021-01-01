class Img(HTML):
   html = "<img></img>"

class Input(HTML):
   html = "<input></input>"

class Obj(HTML):
   html = "<obj></obj>"

class Label(HTML):
   html = "<label></label>"

class HTMLFactory():
   def create_element(self, typ):
      targetclass = typ.capitalize()
      return globals()[targetclass]()

class HTML():
   html = ""
   def get_html_syntax(self):
      return self.html

if __name__ == "__main__":
    html_obj = HTMLFactory()
    elements = ['img','input','obj','label']
    for e in elements:
        element = html_obj.create_element(e)
        html_tag = element.get_html_syntax()
        print(html_tag)