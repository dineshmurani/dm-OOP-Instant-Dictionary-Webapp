import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hello World!",
           classes="text-green-500 bg-yellow-500 "
                   "font-serif text-lg")
    jp.Div(a=wp, text="Hello again!")
    return wp

@jp.SetRoute("/about")
def about():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hi World!")
    jp.Div(a=wp, text="Hi again!")
    return wp

#jp.Route("/home", home)

jp.justpy()