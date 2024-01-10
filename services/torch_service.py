from torchvision import models, transforms
import torch
import requests

class Torch_Service:
    def ai_inference_magic(self, data):
        resNet = models.resnet152(weights='DEFAULT')
        
        image_pre_processor = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225]
                )
        ])
        
        image_tensor = image_pre_processor(data)
        
        batch_tensor = torch.unsqueeze(image_tensor, 0)
        
        resNet.eval()
       
        output = resNet(batch_tensor)
        
        resp = requests.get("https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt")
        class_names=[]
        if resp.status_code == 200:
            class_names = resp.text.splitlines()
        
        _, index = torch.max(output, 1)
            
        percentage = torch.nn.functional.softmax(output, dim=1)
        percentage = percentage[0][index[0]].item() * 100
        recognized_label = class_names[index[0]]
        
        return f"I am {percentage}% certain, that you showed me a {recognized_label}"
        