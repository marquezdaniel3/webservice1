import web # pip install web.py

urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos', # /= raiz Hlello la clase
    '/static/csv/alumnos.csv', 'application.controllers.error.Error'
)
app = web.application(urls, globals())

render = web.template.render('templates/')


if __name__ == "__main__":
    web.config.debug= False
    app.run()