from my_app import app
##Configuraciones
app.config.from_object('configuration.DevelopmentConfig')
#app.config.from_object('configuration.ProductionConfig')
print(app.config['SECRET_KEY'])
app.run()