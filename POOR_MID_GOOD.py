#poor_mid_good.py
from google import genai
from google.genai import types
import base64
import os
from pathlib import Path

API_KEY = os.environ.get("API_KEY")

path_object = Path(r"path\to\train_images") #train_images is your folder name
items = path_object.glob('*')
sorted_items = sorted(items, key=lambda item:item.name)
train_images = [item.name for item in sorted_items]
train_images = train_images[0:]
images_base64_encoded = []
for image in train_images:
    with open(r"path\to\train_images/"+image, 'rb') as file:
        image_raw = file.read()
    images_base64_encoded.append(str(base64.b64encode(image_raw))[2:-1])

image1 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[0]), mime_type='image/jpeg')
image2 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[1]), mime_type='image/jpeg')
image3 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[2]), mime_type='image/jpeg')
image4 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[3]), mime_type='image/jpeg')
image5 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[4]), mime_type='image/jpeg')
image6 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[5]), mime_type='image/jpeg')
image7 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[6]), mime_type='image/jpeg')
image8 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[7]), mime_type='image/jpeg')
image9 = types.Part.from_bytes(data=base64.b64decode(images_base64_encoded[8]), mime_type='image/jpeg')

path_object = Path(r"path\to\test_images") #test_images is your folder name
items = list(path_object.glob('*'))

if not items:
    raise ValueError("No test image found in test_images folder.")

# Take the most recent or only uploaded file
latest_test_image = max(items, key=lambda f: f.stat().st_mtime)
print(f"Using test image: {latest_test_image.name}")

# Encode it
with open(latest_test_image, 'rb') as file:
    image_raw = file.read()
test_base64_encoded = str(base64.b64encode(image_raw))[2:-1]

# Decode to bytes for Gemini
test = types.Part.from_bytes(data=base64.b64decode(test_base64_encoded), mime_type='image/jpeg')

def generate(image1,image2,image3,image4,image5,image6,image7,image8,image9,test):
    client = genai.Client(
        vertexai=True,
        api_key=API_KEY,
    )
    model = "gemini-2.5-flash"
    contents = [
        types.Content(
          role="user",
          parts=[
              types.Part.from_text(text="""Given the images below, learn the ratings,category and the reason associated with it properly. There are only 3 categories - poor, middle and good only! Poor houses are mostly made of mud or simple materials and mostly dilapidated, Middle type houses are slighly big but lack modern facilities whereas Good houses feature a balcony, multi-storey and nice maintained lawn!: """),
              image1,
              types.Part.from_text(text="""Rating: 2/10
              Category: Poor
              Reason: The house has a simple structure made of wooden planks and metal sheets, with an old railing and a corrugated metal roof. It sits on a mud base, which can be unstable. Overall it looks weak and poorly built."""),
              
              image2,
              types.Part.from_text(text="""Rating: 1/10
              Category: Poor
              Reason: This house has a very weak structure made of tin sheets and worn-out plastic. The roof is patched with tarpaulin and tiles, offering little protection, and the surroundings appear cluttered and unhygienic."""),
              
              image3,
              types.Part.from_text(text="""Rating: 2/10
              Category: Poor
              Reason: This house has weak mud walls that are cracking and wearing away. The roof is made of old tiles and supported by wooden sticks, making the structure unstable and unsafe."""),
              
              image4,
              types.Part.from_text(text="""Rating : 4/10
              Category: Middle
              Reason : This house looks simple but artistic, the structure seems small and possibly old. The design is not unique and it may lack modern features or durability."""),
              
              image5,
              types.Part.from_text(text="""Rating: 5/10
              Category: Middle
              Reason: This house has a clean and compact design with traditional Kerala-style features. The simple roofline, front pillars, and minimal decorations give it a practical yet pleasant look. However, it lacks modern architectural elements and advanced materials, making it feel basic but functional."""),
                            
              image6,
              types.Part.from_text(text="""Rating: 6/10
              Category: Middle
              Reason: This house shows a more modern touch with a box-type design and well-defined lines. The mix of wood-finish windows and white walls gives it a neat, contemporary appeal. Still, it’s modest in size and detailing, making it more of a budget-friendly, efficient design rather than a luxury one."""),
                          
              image7,
              types.Part.from_text(text="""Rating: 8/10
              Category: Good
              Reason: This house has solid concrete structure and elegant appearance. The sloped tiled roof helps with rainwater drainage, and the wide front porch adds to its charm. With clean lines, quality materials, and good spacing, it looks both durable and comfortable for modern living."""),
              
              image8,
              types.Part.from_text(text="""Rating: 9/10
              Category: Good
              Reason: This house has beautiful wooden structure, spacious layout, and traditional yet elegant design. The sloped tiled roof, large veranda, and open surroundings add charm and comfort, making it both strong and aesthetically pleasing."""),
              
              image9,
              types.Part.from_text(text="""Rating: 8/10
              Category: Good
              Reason: This house has solid concrete structure, with good utilisation of space it is feasible for modern amenities. The sleek and proper design also offers a terrace.
              Now rate the test images below and give reasons as per your learning"""), test
          ]
        )   
          ]
    generate_content_config = types.GenerateContentConfig(
    temperature = 0,
    top_p = 0.95,
    seed = 0,
    max_output_tokens = 65535,
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    thinking_config=types.ThinkingConfig(
      thinking_budget=-1,
    ),
  )
    for chunk in client.models.generate_content_stream(
        model = model,
        contents = contents,
        config = generate_content_config,
    ):
        print(chunk.text, end="")

generate(image1,image2,image3,image4,image5,image6,image7,image8,image9,test)
