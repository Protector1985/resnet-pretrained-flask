from flask import request
from services.torch_service import Torch_Service
from PIL import Image
import io

class Torch_Controller(Torch_Service):
    basePath="/torch"
        
    def initRoutes(self, app):
        @app.route(self.basePath + "/data", methods=["POST"])
        def handleRequest():
            if request.method == "POST":
                if 'image' in request.files:
                    image_file = request.files['image']
                    image = Image.open(io.BytesIO(image_file.read()))
                    image.show()
                    
                return "OK"