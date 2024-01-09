from app import App
from controllers.torch_controller import Torch_Controller


def main():
    try:
        torch_controller = Torch_Controller()
        
        app = App({
            'controllers':[torch_controller]
        })
        
        app.startServer()
        
    except Exception as e:
        print(f"So eine Scheisse! An error!{e}")
    
        
if __name__ == "__main__":
    main()