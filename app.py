from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

class App:
    def __init__(self, config):
        self.app=Flask(__name__)
        self.port= int(os.getenv("PORT", 5000))
        self.controllers = config.get('controllers')
        self.createRoutes()
    
    def createRoutes(self):
        for controller in self.controllers:
            print(controller.initRoutes(self.app))
    
    def startServer(self):
        try:
            self.app.run(port=self.port, debug=True)
        except Exception as e:
            print(f"Errors errors and more errors:{e}")
            
