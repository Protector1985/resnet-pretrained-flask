

class Torch_Controller:
    basePath="/torch"
    
        
    def initRoutes(self, app):
        print(self.basePath)
        @app.route(self.basePath + "/data", methods=["POST"])
        def handleRequest():
            print("Request came in!")