# Poem Generator Backend

## Overview
The Poem Generator Backend is a Flask-based web service that generates poems based on user input. It utilizes a fine-tuned GPT-2 model to create poems in various styles and themes. The backend also generates a visual representation of the poem in image format.

## Features
- Generate poems based on user-defined themes, styles, and emotions.
- RESTful API for easy integration with front-end applications.
- Image generation of the poem with a visually appealing layout.
- CORS support for cross-origin requests.

## Requirements
- Python 3.7 or higher
- Flask
- Transformers (Hugging Face)
- Flask-CORS
- Pillow (for image generation)
- PyTorch

## Instructions for Use

### 1. Accessing the Project
- Insert the pendrive into your computer.
- Navigate to the `poem_generator_backend` directory on the pendrive.

### 2. Setting Up the Environment
- **Create a virtual environment (optional but recommended):**
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

### 3. Install the Required Packages
- Ensure you have `pip` installed, then run:
  ```bash
  pip install -r requirements.txt
  ```

### 4. Load the Model
- Ensure that the fine-tuned model and tokenizer are located in the `model` directory specified in `app.py`. Update the `model_path` variable in `app.py` if necessary.

### 5. Running the Application
- Start the Flask application:
  ```bash
  python app.py
  ```
- By default, the application will run on `http://127.0.0.1:5001`.

### 6. Using the API
- You can interact with the API using tools like Postman or curl. Here’s an example of how to generate a poem:
  - **POST /api/generate-poem**
    - **Request Body:**
      ```json
      {
        "theme": "nature",
        "style": "haiku",
        "emotion": "happy"
      }
      ```
    - **Response:**
      ```json
      {
        "poem": "An example poem text.",
        "image": "data:image/png;base64,..."
      }
      ```

### 7. Image Generation
- The generated poem is returned along with an image representation of the poem, encoded in base64 format. This image can be displayed directly in web applications.

## Notes
- Ensure that Python and the required packages are installed on your machine before running the application.
- If you encounter any issues, please refer to the documentation for Flask, Transformers, or the specific libraries used.
- The application is set to run in debug mode for development purposes. For production, consider disabling debug mode.

## Acknowledgments
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the GPT-2 model.
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) for handling cross-origin requests.
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image generation.
- [PyTorch](https://pytorch.org/) for deep learning framework.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.