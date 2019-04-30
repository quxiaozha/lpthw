import web
from os import path

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())

root = path.dirname(__file__)
print root

print path.join(root, "..", "templates/")
render = web.template.render(path.join(root, "..", "templates/"), base="layout")


class Index(object):
    def GET(self):
        # form = web.input(name='Nobody')
        # greeting = "Hello World!! %s" % form.name
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet='Hello')
        greeting = "%s, %s" % (form.greet, form.name)
        return render.index(greeting=greeting)


if __name__ == "__main__":
    app.run()
