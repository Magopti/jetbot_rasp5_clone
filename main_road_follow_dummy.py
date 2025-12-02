import torch
import torchvision
import time
import numpy as np
from PIL import Image
import torchvision.transforms as transforms

# 1. Initiera modell (random weights)
model = torchvision.models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(512, 2)   # samma output-shape som JetBot-modellen
device = torch.device("cpu")
model = model.to(device).eval()

# 2. Dummy-bild (224x224 RGB, samma input som modellen förväntar sig)
dummy_image = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
image = Image.fromarray(dummy_image)

# 3. Normalisering (samma som träningspipeline)
mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
std = torch.tensor([0.229, 0.224, 0.225]).to(device)

def preprocess(image):
    tensor = transforms.functional.to_tensor(image).to(device)
    tensor.sub_(mean[:, None, None]).div_(std[:, None, None])
    return tensor.unsqueeze(0)

input_tensor = preprocess(image)

# 4. "Warm-up" körningar (för att undvika kallstart-latens)
for _ in range(10):
    _ = model(input_tensor)

# 5. Benchmark: 100 körningar
N = 100
t0 = time.time()
for _ in range(N):
    _ = model(input_tensor)
t1 = time.time()

print(f"Genomsnittlig inferenstid: {(t1 - t0)*1000/N:.2f} ms per bild")
