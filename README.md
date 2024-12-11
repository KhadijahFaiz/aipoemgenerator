# AI Poem Generator

Welcome to the AI Poem Generator project! This repository contains the frontend and backend components for an application that generates unique poems based on user input. The project uses a fine-tuned GPT-2 model and is built with Vue.js and Flask.

## Project Overview

The AI Poem Generator allows users to create poems in various styles and themes by leveraging the power of artificial intelligence. Users can select preferences, input themes, and generate poems directly from the web-based application.

## Repository Structure

- **`poem_gen/`**: Contains the Vue.js frontend for the application.
- **`poem_generator_backend/`**: Contains the Flask backend for handling model interactions and API requests.
- **`model/`**: Stores the fine-tuned GPT-2 model files.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.

## How to Set Up

### Prerequisites
- Node.js and npm
- Python 3.8 or later
- A virtual environment for Python
- Vue CLI
- Required Python packages: Flask, transformers, torch

### Installation Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/KhadijahFaiz/aipoemgenerator.git
cd aipoemgenerator
```

#### 2. Set Up the Frontend
```bash
cd poem_gen
npm install
npm run serve
```
This will start the frontend server at `http://localhost:8080`.

#### 3. Set Up the Backend
```bash
cd poem_generator_backend
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
The backend server will start at `http://localhost:5000`.

#### 4. Model Setup
Place the fine-tuned GPT-2 model files in the `model/` directory. Ensure the `config.json` and `pytorch_model.bin` files are present.

#### 5. Connect Frontend and Backend
Ensure the frontend API endpoints match the backend URL (`http://localhost:5000`). Update the API endpoint in the frontend code if necessary.

## Features

- User-friendly interface for inputting themes and selecting poem styles
- Real-time poem generation using a fine-tuned GPT-2 model
- Responsive design for mobile and desktop devices
- Backend API for handling requests and model interactions

## Future Enhancements

- Add support for more poetic styles
- Improve model accuracy with additional fine-tuning
- Deploy the application online for public use

## Contact
For any questions or contributions, feel free to reach out:
- **GitHub**: [KhadijahFaiz](https://github.com/KhadijahFaiz)

---

Thank you for exploring the AI Poem Generator project!

