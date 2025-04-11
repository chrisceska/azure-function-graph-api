# Azure Function to Download Email Attachments from Microsoft Graph API

This project is an Azure Function that interacts with the Microsoft Graph API to download attachments from emails in an Outlook email account.

## Project Structure

```
azure-function-graph-api
├── HttpTrigger
│   ├── __init__.py
│   ├── function.json
│   └── requirements.txt
├── shared_code
│   ├── graph_api.py
│   └── __init__.py
├── local.settings.json
└── README.md
```

## Prerequisites

- Python 3.6 or later
- Azure Functions Core Tools
- An Azure account with an active subscription
- Microsoft Graph API permissions to access emails and attachments

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd azure-function-graph-api
   ```

2. **Install dependencies:**
   Navigate to the `HttpTrigger` directory and install the required packages:
   ```
   cd HttpTrigger
   pip install -r requirements.txt
   ```

3. **Configure local.settings.json:**
   Update the `local.settings.json` file with your Azure Function settings and Microsoft Graph API credentials.

4. **Run the Azure Function locally:**
   Use the Azure Functions Core Tools to run the function:
   ```
   func start
   ```

## Usage

To trigger the function, send an HTTP request to the endpoint provided in the console after running the function locally. The request should include the necessary parameters to specify which email and attachments to download.

## Additional Information

- The `shared_code/graph_api.py` file contains the logic for interacting with the Microsoft Graph API.
- The `HttpTrigger/__init__.py` file contains the main function that handles incoming HTTP requests and processes them accordingly.

## Tests

The project includes unit tests for the `graph_api.py` module, located in the `tests` folder. These tests ensure the functionality of the following methods:

1. **`authenticate_graph_api`**:
   - Tests successful authentication with the Microsoft Graph API.
   - Tests failure scenarios with appropriate error handling.

2. **`get_email_attachments`**:
   - Tests successful retrieval of email attachments from a specified email.
   - Tests failure scenarios when the API call fails.

3. **`download_attachment`**:
   - Tests successful downloading of an email attachment.
   - Tests failure scenarios when the API call fails.

### Running the Tests

To run the tests, use the following command from the root directory of the project:

```bash
python -m unittest discover -s tests
```

This will discover and execute all the test cases in the `tests` folder.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.