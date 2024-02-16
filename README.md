# Two-Factor Authentication Project

This project implements a simple two-factor authentication (2FA) system using email. It generates a random one-time password (OTP) and sends it to the user's email address for verification.

## Prerequisites

Before running this project, ensure you have the following prerequisites:

- Python installed on your system ([Download Python](https://www.python.org/downloads/))
- Access to an email account (e.g., Gmail) to send the OTP

## Installation

1. **Clone the Repository**: Clone this repository to your local machine using Git:

    ```
    git clone https://github.com/your-username/2fa-project.git
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

    ```
    cd 2fa-project
    pip install -r requirements.txt
    ```

## Configuration

Before running the project, you need to configure the following variables in the `main.py` file:

- `userid@example.com`: Your email address from which the OTP will be sent.
- `password`: Your email account's password or app password.
- `receiverid@gmail.com`: The recipient's email address where the OTP will be sent.

## Usage

To run the project, execute the `main.py` file using Python:

    python main.py

This will generate a random OTP and send it to the specified email address.

