# Installation and Setup Instructions

## Virtual Environment Setup
1. Ensure you have Python 3.6 or higher installed on your system.
2. Create a virtual environment by running the following command:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## Dependency Installation
4. Once the virtual environment is activated, install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Configuration
5. Create a `.env` file in the root directory and configure your environment variables as needed. Here’s a sample structure:
   ```
   # Sample .env file
   API_KEY=your_api_key_here
   DATABASE_URL=your_database_url_here
   ```

## Quick Start Guide
6. To start the application, simply run:
   ```bash
   python main.py
   ```
7. Follow the on-screen instructions to set up your bot!