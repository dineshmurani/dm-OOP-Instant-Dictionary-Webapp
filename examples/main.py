import justpy as jp

@jp.SetRoute("/home")
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    jp.Input(a=div, placeholder="Enter First Value",
             classes="form-input")
    jp.Input(a=div, placeholder="Enter Second Value",
             classes="form-input")
    jp.Div(a=div, text="Result goes here...",
           classes="text-gray-600")
    jp.Button(a=div, text="Calculate",
              classes="border border-blue-500 m-2 py-1 px-4 rounded "
              "text-blue-600 hover:bg-red-500 hover:text-white")
    return wp



#jp.Route("/home", home)

jp.justpy()