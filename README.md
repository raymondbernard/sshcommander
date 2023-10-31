# SSH Commander

## Overview

SSH Commander is a web-based application built to simplify the process of configuring network devices via SSH. The application is powered by Streamlit, offering a user-friendly interface to input server details, SSH credentials, and a list of configuration commands. Once the data is inputted, SSH Commander establishes SSH connections to the specified servers and executes the provided commands in sequence.

## Features

- **SSH Connection**: Establish a secure connection to an initial server using SSH.
- **Server Configuration Management**: Add, edit, and delete server configurations with ease.
- **Batch Command Execution**: Execute a list of commands on each configured server through the initial SSH connection.
- **Configuration Saving and Loading**: Save server configurations to a JSON file and load them back when needed.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/raymondbernard/sshcommander.git
    cd sshcommander
    ```

2. **Create a Virtual Environment** (Optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Requirements**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

    This will start the Streamlit server and the application will open in your default web browser.

2. **Configure SSH Connection**: Input the necessary details for the initial SSH connection in the "SSH Connection Information" section.

3. **Manage Server Configurations**: Use the "Add / Edit a Server" section to input details for each server you want to configure. Multiple servers can be added, and existing configurations can be edited or deleted.

4. **Execute Commands**: Click "Start Configuration" to initiate the SSH connections and execute the commands on each configured server.

5. **View Output**: Check the output of the commands directly in the Streamlit interface.

6. **Modify Configurations**: Utilize the "Edit" and "Delete" buttons next to each server in the "Added Servers" section to change or remove server configurations.

## Notes

- Ensure that the initial server has SSH access to the other servers.
- The SSH private key file for the initial connection must be accessible by the application.
- The application is designed to handle password changes for new Ubuntu server installations (username: ubuntu, password: nvidia).
- Server configurations are persisted to a `config.json` file, which can be backed up or manually edited if necessary.

## Contributing

Feel free to fork the repository, make improvements, and submit a pull request. Any contributions to enhance SSH Commander are welcomed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a comprehensive guide for installing, running, and contributing to the SSH Commander application. Make sure to place this README in the root directory of your project.

By Raymond Bernard
ray.bernard@outlook.com
