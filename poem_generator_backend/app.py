# Import necessary libraries
from flask import Flask, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from flask_cors import CORS
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import torch

# Create a Flask application instance
app = Flask(__name__)

# Allow CORS requests from any origin
CORS(app, origins=['*'])

# Path to the fine-tuned model and tokenizer
model_path = r"H:\Computer Science\Semester 2\FYP 2\poem_generator_backend\model"  # Update to use the 'model' folder

# Load the fine-tuned GPT-2 model and tokenizer from the specified path
model = GPT2LMHeadModel.from_pretrained(model_path)
tokenizer = GPT2Tokenizer.from_pretrained(model_path)

# Print confirmation of successful model loading
print("Loaded the final_poem_generator model from:", model_path)

@app.route('/api/generate-poem', methods=['POST'])
def generate_poem():
    # Extract JSON data from the POST request
    data = request.json
    theme = data.get('theme', 'love')  # Default theme is 'love'
    style = data.get('style', 'sonnet')  # Default style is 'sonnet'
    emotion = data.get('emotion', 'happy')  # Default emotion is 'happy'

    # Create a prompt for the model based on user input
    prompt = f"Write a {emotion} {style} about {theme} with rich imagery and depth. Separate the stanzas with line breaks:"

    # Define maximum length of the generated poem based on style
    if style.lower() == 'haiku':
        max_length = 50
    elif style.lower() == 'freeverse':
        max_length = 200
    else:
        max_length = 250

    # Generate the poem using the model
    input_ids = tokenizer.encode(prompt, return_tensors='pt')  # Encode the prompt
    with torch.no_grad():  # Disable gradient calculation for inference
        outputs = model.generate(
            input_ids,
            max_length=max_length,  # Limit the length of the generated poem
            num_return_sequences=1,  # Generate one poem
            no_repeat_ngram_size=2,  # Avoid repeating n-grams
            top_k=50,  # Top-k sampling
            top_p=0.95,  # Nucleus sampling
            temperature=1.2  # Control randomness of predictions
        )

    # Decode the generated text, removing the prompt
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    poem = generated_text.replace(prompt, '').strip()  # Remove the prompt from the output

    # Format the poem into stanzas (insert blank lines after 4 lines)
    lines = poem.split('. ')
    formatted_poem = ''
    for i in range(len(lines)):
        formatted_poem += lines[i].strip() + '\n'
        if (i + 1) % 4 == 0:
            formatted_poem += '\n'  # Add a blank line after every 4 lines

    poem = formatted_poem.strip()  # Clean up any trailing whitespace

    # Generate an image of the formatted poem
    image_data = generate_image_from_text(poem)

    # Return the generated poem and image as JSON response
    return jsonify({"poem": poem, "image": image_data})

def generate_image_from_text(poem):
    # Create a blank image with a gradient background
    width = 1000  # Width of the image
    lines = poem.strip().split('\n')  # Split the poem into lines
    line_height = 40  # Height of each line
    height = line_height * len(lines) + 100  # Calculate height based on number of lines

    # Create an image with a white background
    image = Image.new('RGB', (width, height), (255, 255, 255))  # White background
    draw = ImageDraw.Draw(image)  # Create a drawing context

    # Create a gradient effect from light grey to soft beige
    for y in range(height):
        color = int(240 - (y / height) * 100)  # Softer gradient effect
        draw.line([(0, y), (width, y)], fill=(color, color, color))  # Draw gradient lines

    # Load a font (ensure the font file exists on your system)
    try:
        font = ImageFont.truetype('C:/Windows/Fonts/Georgia.ttf', size=28)  # Set font size
    except IOError:
        font = ImageFont.load_default()  # Use default font if specified font is not found

    # Starting position for text drawing
    y_text = 60  # Add some top padding

    # Draw each line of text with word wrapping
    for line in lines:
        line = line.strip()
        if line:
            # Word wrap the line if it exceeds the image width
            words = line.split()
            wrapped_lines = []
            current_line = ""

            for word in words:
                # Check the width of the current line + next word
                test_line = current_line + " " + word if current_line else word
                bbox = draw.textbbox((0, 0), test_line, font=font)  # Get bounding box of the text
                text_width = bbox[2] - bbox[0]  # Calculate width from the bounding box

                # Add word to the current line if it fits
                if text_width <= width - 40:  # 20 pixels padding on each side
                    current_line = test_line
                else:
                    wrapped_lines.append(current_line)  # Save the wrapped line
                    current_line = word  # Start a new line with the current word

            wrapped_lines.append(current_line)  # Add the last line

            # Draw each wrapped line
            for wrapped_line in wrapped_lines:
                # Calculate the width to center the text
                text_width, _ = draw.textbbox((0, 0), wrapped_line, font=font)[2:4]
                x_text = (width - text_width) / 2  # Center the text horizontally
                
                # Draw text with shadow for better readability
                shadow_color = 'black'
                text_color = 'darkgrey'  # Neutral color for text

                # Draw shadows
                draw.text((x_text - 1, y_text - 1), wrapped_line, font=font, fill=shadow_color)
                draw.text((x_text + 1, y_text - 1), wrapped_line, font=font, fill=shadow_color)
                draw.text((x_text - 1, y_text + 1), wrapped_line, font=font, fill=shadow_color)
                draw.text((x_text + 1, y_text + 1), wrapped_line, font=font, fill=shadow_color)

                # Draw the main text
                draw.text((x_text, y_text), wrapped_line, font=font, fill=text_color)
                y_text += line_height  # Move down for the next line

    # Save the image to a bytes buffer
    buffered = io.BytesIO()  # Create a bytes buffer
    image.save(buffered, format="PNG")  # Save the image in PNG format

    # Encode the image to base64
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')  # Convert to base64 string

    return f"data:image/png;base64,{img_str}"  # Return the base64 string for the image

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, port=5001)  # Enable debug mode and specify port
