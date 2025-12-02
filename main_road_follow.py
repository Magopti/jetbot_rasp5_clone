import torch
import torchvision
import time
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

# 1. Initiera modell
model = torchvision.models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(512, 2)
model.load_state_dict(torch.load('best_steering_model_xy.pth', map_location='cpu'))

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device).eval().half()

# 2. Dummy-bild (eller ladda från kamera)
dummy_image = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
image = Image.fromarray(dummy_image)

# 3. Preprocess (samma normalisering som i din JetBot-kod)
mean = torch.tensor([0.485, 0.456, 0.406]).to(device).half()
std = torch.tensor([0.229, 0.224, 0.225]).to(device).half()

def preprocess(image):
    tensor = transforms.functional.to_tensor(image).to(device).half()
    tensor.sub_(mean[:, None, None]).div_(std[:, None, None])
    return tensor.unsqueeze(0)  # [1,3,224,224]

input_tensor = preprocess(image)

# 4. "Warm-up" (för att init CUDA kernels osv.)
for _ in range(10):
    _ = model(input_tensor)

# 5. Mäta tid över flera körningar
N = 100
torch.cuda.synchronize() if device.type == 'cuda' else None
t0 = time.time()
for _ in range(N):
    _ = model(input_tensor)
torch.cuda.synchronize() if device.type == 'cuda' else None
t1 = time.time()

avg_ms = (t1 - t0) * 1000 / N
print(f"Genomsnittlig inferenstid: {avg_ms:.2f} ms per bild på {device}")
