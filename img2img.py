import io
import os
import warnings

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://beta.dreamstudio.ai/membership

# Click on the following link once you have created an account to be taken to your API Key.
# https://beta.dreamstudio.ai/membership?tab=apiKeys

# Paste your API Key below.

os.environ['STABILITY_KEY'] = 'sk-4AZizDwRC7iS4efe4DydpDr88XAbMFtw7XEn4lwQACxutlfr'


# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-v1-5", # Set the engine to use for generation. For SD 2.0 use "stable-diffusion-v2-0".
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0 
    # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)




# Set up our initial generation parameters.
def img1(text):
    answers = stability_api.generate(
        prompt=text,#"expansive landscape rolling greens with blue daisies and weeping willow trees under a blue alien sky, artstation, masterful, ghibli",
        seed=992446758,
        steps=30,
        cfg_scale=8.0,
        width=512,
        height=512,
        samples=1,
        sampler=generation.SAMPLER_K_DPMPP_2M )

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save("static/result/"+text.replace(" ","")+".png")
                return "static/result/"+text.replace(" ","")+".png"













# Set up our initial generation parameters.
def img2(text,simg):
    answers2 = stability_api.generate(
        prompt=text,
        init_image=Image.open(simg),
        start_schedule=0.6,
        seed=123467458, 
        steps=30, 
        cfg_scale=8.0,
        width=512,
        height=512,
        sampler=generation.SAMPLER_K_DPMPP_2M) 

    for resp in answers2:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                global img2
                img2 = Image.open(io.BytesIO(artifact.binary))
                img2.save("static/result/"+text.replace(" ","")+".png")
                return "static/result/"+text.replace(" ","")+".png" # Save our generated image with its seed number as the filename and the img2img suffix so that we know this is our transformed image.   
