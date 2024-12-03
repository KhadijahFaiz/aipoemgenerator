# PoemGenie Frontend

PoemGenie is a web application that allows users to generate poems based on inputs they provide. This repository contains the frontend code built with Vue.js, which interacts with a Flask backend to generate and display poems.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User-Friendly Interface**: Simple and intuitive design for easy interaction.
- **Dynamic Poem Generation**: Users can input prompts and receive generated poems in real-time.
- **Responsive Design**: Works well on various devices, including desktops and mobile phones.

## Technologies Used

- **Vue.js**: A progressive JavaScript framework for building user interfaces.
- **Axios**: A promise-based HTTP client for making API requests to the backend.
- **Tailwind CSS**: A utility-first CSS framework for styling the application.
- **Vue Router**: For managing navigation within the application (if applicable).
- **Text-to-Speech**: For reading poems aloud to users.


## Prerequisites
Before you begin, ensure you have the following installed:
- **Node.js** (v12.x or higher) [Download here](https://nodejs.org/en/)
- **npm** (Node Package Manager): Comes with Node.js
- **Vue CLI**: Globally installed by running:
   ```bash
   npm install -g @vue/cli

### Steps to Install

1. **Go to the project directory**:
   If you have the project on a remote repository, clone it. Otherwise, ensure the project files are on your pendrive.

   ```bash
   cd poem_gen
   ```

2. **Install Dependencies**:
   Open a terminal in the project directory and run:

   ```bash
   npm install
   ```

3. **Start the Development Server**:
   After the dependencies are installed, start the Vue.js development server:

   ```bash
   npm run serve
   ```

   The application will typically be available at `http://localhost:8080`.

## Usage

1. Open your web browser and navigate to `http://localhost:8080`.
2. Enter a prompt in the input field and press Enter or click the "Generate" button.
3. The generated poem will be displayed below the input field.

## API Integration

The frontend communicates with the backend via the following API endpoint:

- **POST /api/generate-poem**: Sends a prompt to the backend and receives a generated poem.


## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Note**: Ensure that the backend server is running and accessible for the frontend to function correctly. You may need to adjust the API URL in the frontend code if the backend is hosted on a different address or port.