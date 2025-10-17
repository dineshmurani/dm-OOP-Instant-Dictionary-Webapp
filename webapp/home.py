import justpy as jp
from webapp import layout

class Home():
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-grey-200 h-screen p-2")
        jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
            The "About" page for Amazon refers to the company's online presence, which is the world's largest online retailer and a technology company known for services like Amazon Prime and Alexa. Alternatively, "The Amazon" can refer to the Amazon rainforest, the world's largest tropical rainforest, which is home to immense biodiversity and plays a crucial role in regulating the global climate, as detailed on sites like the World Wildlife Fund (WWF) and The Nature Conservancy. """,
               classes="text-lg")
        return wp


