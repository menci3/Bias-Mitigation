import torch
import os

from diffusers import StableDiffusion3Pipeline
from huggingface_hub import login
from dotenv import load_dotenv


load_dotenv()

hugging_face_key = os.getenv("HUGGING_FACE_API_KEY")

login(hugging_face_key)

pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3.5-medium",
                                                cache_dir="./stable_diffusion_models",
                                                torch_dtype=torch.bfloat16)
pipe = pipe.to("cuda")

image = pipe(
    "A capybara holding a sign that reads Hello World",
    num_inference_steps=40,
    guidance_scale=4.5,
).images[0]
image.save("capybara.png")