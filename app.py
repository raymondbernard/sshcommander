import streamlit as st
import paramiko
import os
import json
import time

# Streamlit App Title and Description
st.title("SSH Commander Tool")
st.write("This tool helps to configure and test servers/network devices via SSH. Please provide the necessary information below to get started.")

# Initialize session state variables
if 'hostname' not in st.session_state:
    st.session_state.hostname = ''
if 'port' not in st.session_state:
    st.session_state.port = 22
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'key_filename_path' not in st.session_state:
    st.session_state.key_filename_path = None
if 'servers' not in st.session_state:
    st.session_state.servers = []
if 'editing_index' not in st.session_state:
    st.session_state.editing_index = None
if 'tests' not in st.session_state:
    st.session_state.tests = []
if 'editing_test_index' not in st.session_state:
    st.session_state.editing_test_index = None

# File to store the configuration and tests
config_file = "config.json"
test_file = "test.json"

# Load existing configuration and tests
def load_config():
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            data = json.load(f)
            st.session_state.servers = data.get("servers", [])
            st.session_state.hostname = data.get("hostname", "")
            st.session_state.port = data.get("port", 22)
            st.session_state.username = data.get("username", "")

def load_tests():
    if os.path.exists(test_file):
        with open(test_file, "r") as f:
            data = json.load(f)
            st.session_state.tests = data.get("tests", [])

load_config()
load_tests()

# SSH Connection Information
with st.expander("SSH Connection Information"):
    st.session_state.hostname = st.text_input("Hostname (Original Server)", st.session_state.hostname)
    st.session_state.port = st.number_input("Port (Original Server)", min_value=1, max_value=65535, value=st.session_state.port)
    st.session_state.username = st.text_input("Username (Original Server)", st.session_state.username)
    key_filename = st.file_uploader("Private Key File (Original Server)", type=['pem'])
    password = st.text_input("Password (Original Server, if required)", type="password", help="Leave empty if using a private key")

# Function to handle file upload and save it temporarily
def save_uploaded_file(uploaded_file):
    try:
        if not os.path.exists('tempDir'):
            os.makedirs('tempDir')
        with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return os.path.join("tempDir", uploaded_file.name)
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

# Save the uploaded private key file
if key_filename is not None:
    st.session_state.key_filename_path = save_uploaded_file(key_filename)

# SSH Functions
def create_ssh_client(hostname, port, username, password=None, key_filename=None):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        if key_filename:
            ssh_client.connect(hostname, port=port, username=username, key_filename=key_filename, look_for_keys=False, allow_agent=False)
        elif password:
            ssh_client.connect(hostname, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
        else:
            st.error("No authentication method provided. Please provide a password or a key file.")
            return None
    except paramiko.AuthenticationException:
        st.error("Authentication failed, please verify your credentials")
        return None
    return ssh_client

def run_commands(ssh_client, server):
    address = server['address']
    username = server['username']
    server_password = server.get('password')
    commands = server['commands']

    # Creating a new SSH session from the original server
    ssh_cmd = f"ssh {username}@{address}"
    if server_password:
        ssh_cmd = f"sshpass -p {server_password} {ssh_cmd}"
    
    shell = ssh_client.invoke_shell()
    shell.send(f"{ssh_cmd}\n")
    time.sleep(1)  # wait for the connection to establish

    for command in commands:
        shell.send(f"{command}\n")
        time.sleep(10)  # wait for 10 seconds for the command to execute

    shell.send("exit\n")  # exit from the SSH session to the target server
    time.sleep(0.5)
    output = shell.recv(10000).decode()
    st.text(output)
    shell.close()

# Save configuration and tests
def save_config():
    data = {
        "servers": st.session_state.servers,
        "hostname": st.session_state.hostname,
        "port": st.session_state.port,
        "username": st.session_state.username,
    }
    with open(config_file, "w") as f:
        json.dump(data, f)

def save_tests():
    data = {
        "tests": st.session_state.tests,
    }
    with open(test_file, "w") as f:
        json.dump(data, f)

# Server Information Input
def server_input_form(servers, editing_index, key, title, save_function):
    with st.form(key=key):
        st.subheader(title)
        editing_server = servers[editing_index] if editing_index is not None else {}
        address = st.text_input("Address", value=editing_server.get("address", ""))
        server_username = st.text_input("Username", value=editing_server.get("username", ""))
        server_password = st.text_input("Password (optional)", type="password", value=editing_server.get("password", ""))
        commands = st.text_area("Commands (one per line)", value="\n".join(editing_server.get("commands", [])))
        submit_button = st.form_submit_button("Save Server")

    if submit_button:
        server_info = {
            "address": address,
            "username": server_username,
            "password": server_password,
            "commands": commands.split('\n')  # Split commands by line
        }
        if editing_index is not None:
            servers[editing_index] = server_info
            editing_index = None
        else:
            servers.append(server_info)
        save_function()
        st.success("Server saved successfully!")

# Display servers or tests
def display_servers(servers, editing_index_key, editing_index, delete_function, rerun_function):
    to_delete = st.empty()  # Placeholder for delete buttons
    for i, server in enumerate(servers):
        st.write(f"Server {i+1}: {server['address']}")
        st.write(f"Username: {server['username']}")
        st.write("Commands:")
        for command in server['commands']:
            st.text(command)
        with st.container():
            col1, col2 = st.columns([1, 1])
            if col1.button("Edit", key=f"edit{i}"):
                st.session_state[editing_index_key] = i
                rerun_function()
            if col2.button("Delete", key=f"delete{i}"):
                del servers[i]
                delete_function()
                rerun_function()
        st.write("---")

# Configuration Section
server_input_form(st.session_state.servers, st.session_state.editing_index, 'server_form', "Add / Edit a Server", save_config)

with st.expander("Added Servers"):
    display_servers(st.session_state.servers, 'editing_index', st.session_state.editing_index, save_config, st.experimental_rerun)

# Action Button for Configuration
if st.button("Start Configuration"):
    with st.spinner("Configuring devices..."):
        try:
            # Create SSH client to the original server
            original_ssh_client = create_ssh_client(st.session_state.hostname, st.session_state.port, st.session_state.username, password, st.session_state.key_filename_path)

            if original_ssh_client is None:
                st.error("Failed to create SSH client to the original server.")
                st.stop()

            # Run commands on each server through the original server
            for server in st.session_state.servers:
                st.write(f"Configuring {server['address']} through {st.session_state.hostname}...")
                run_commands(original_ssh_client, server)

            st.success("Configuration completed successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            if 'original_ssh_client' in locals() and original_ssh_client is not None:
                original_ssh_client.close()

# Testing Section
st.subheader("Testing")
server_input_form(st.session_state.tests, st.session_state.editing_test_index, 'test_form', "Add / Edit a Test", save_tests)

with st.expander("Added Tests"):
    display_servers(st.session_state.tests, 'editing_test_index', st.session_state.editing_test_index, save_tests, st.experimental_rerun)

# Action Button for Testing
if st.button("Start Testing"):
    with st.spinner("Testing devices..."):
        try:
            # Create SSH client to the original server
            original_ssh_client = create_ssh_client(st.session_state.hostname, st.session_state.port, st.session_state.username, password, st.session_state.key_filename_path)

            if original_ssh_client is None:
                st.error("Failed to create SSH client to the original server.")
                st.stop()

            # Run commands on each test server through the original server
            for test in st.session_state.tests:
                st.write(f"Testing {test['address']} through {st.session_state.hostname}...")
                run_commands(original_ssh_client, test)

            st.success("Testing completed successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            if 'original_ssh_client' in locals() and original_ssh_client is not None:
                original_ssh_client.close()
