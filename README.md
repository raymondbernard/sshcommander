# SSH Commander

SSH Commander is a Streamlit-based application that facilitates the configuration and testing of servers or network devices via SSH. It provides a user-friendly interface to input server details, commands to be executed, and also to execute these commands directly from the application.

## Purpose

The main purpose of SSH Commander is to simplify the process of configuring and testing servers. It allows users to:

- Add, edit, and delete server/device configurations via SSH.
- Execute a series of commands on multiple servers.
- Add, edit, and delete test configurations.
- Execute a series of test commands on multiple servers.

## AI Assistant

SSH Commander integrates an AI assistant to generate configuration descriptions based on the commands entered by the user. 

When saving a new configuration, the commands are sent to an AI API which returns a summarized description of what the commands are intended to configure. This provides an automated way to document the purpose of each configuration.

If you need more control over AI responses please modify the system message in the app.py 

### Configuration
We are using the nvidia api as our AI platform to generate configuration descriptions.
The LLM is based on Meta's LLama2 code 32b 
The AI assistant requires an API key which should be stored in the `.env` file.
# Documentation

SSH Commander allows you to download your configuration configuration in markdown 

## Installation

To install SSH Commander from the GitHub repository, follow these steps:

### Cloning the Repository

First, clone the repository from GitHub:

```bash
git clone https://github.com/raymondbernard/sshcommander.git
cd sshcommander
```

### Setting up a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other Python packages. Create and activate a virtual environment:

#### On Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Installing Dependencies

Install the necessary dependencies (ensure your virtual environment is activated):

```bash
pip install -r requirements.txt
```

### Running SSH Commander

After the installation is complete, you can run SSH Commander:

```bash
streamlit run app.py
```
## Usage

### Configuration

1. Expand the "SSH Connection Information" section and input the details of the original server through which you will SSH into other servers or devices.

2. Expand the "Configuration" section to add, edit, or delete server configurations.
   - Click on "Add / Edit a Server" to input the server address, username, and commands to be executed.
   - The AI will generate a description of the configuration based on the commands.
   - Use the "Save Server" button to save the configuration along with the AI-generated description.
   - Use the "Edit" and "Delete" buttons to modify or remove existing configurations.

3. Click the "Start Configuration" button to execute the commands on all configured servers.


### Testing

1. Expand the "Testing" section to add, edit, or delete test configurations.
   - Click on "Add / Edit a Test" to input the server address, username, and the test commands to be executed.
   - Use the "Save Server" button to save the test configuration.
   - Use the "Edit" and "Delete" buttons to modify or remove existing test configurations.
2. Click the "Start Testing" button to execute the test commands on all configured tests. This can be particularly useful for running an entire test suite after configurations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


By Raymond Bernard
ray.bernard@outlook.com


## Demo

For a visual demonstration of how SSH Commander works, you can watch our demo video here: [YouTube Demo](https://youtu.be/4gGqr2Olrpc)

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.