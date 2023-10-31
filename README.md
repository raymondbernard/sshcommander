# SSH Commander

SSH Commander is a Streamlit-based application that facilitates the configuration and testing of servers or network devices via SSH. It provides a user-friendly interface to input server details, commands to be executed, and also to execute these commands directly from the application.

## Purpose

The main purpose of SSH Commander is to simplify the process of configuring and testing servers. It allows users to:

- Add, edit, and delete server configurations.
- Execute a series of commands on multiple servers.
- Add, edit, and delete test configurations.
- Execute a series of test commands on multiple servers.

## Installation

1. Ensure that you have Python installed on your machine. If not, download and install Python from [python.org](https://www.python.org/).
2. Download or clone this repository to your local machine.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the command `pip install -r requirements.txt` to install the required packages.
5. Start the Streamlit application by running `streamlit run app.py`.

## Usage

### Configuration

1. Expand the "SSH Connection Information" section and input the details of the original server through which you will SSH into other servers or devices.
2. Expand the "Configuration" section to add, edit, or delete server configurations.
   - Click on "Add / Edit a Server" to input the server address, username, and the commands to be executed.
   - Use the "Save Server" button to save the configuration.
   - Use the "Edit" and "Delete" buttons to modify or remove existing server configurations.
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
