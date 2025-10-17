import justpy as jp

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home

imports = list(globals().values())

# to iterate over imports dictionary:
for obj in imports:
    if hasattr(obj, 'path'):
        jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)