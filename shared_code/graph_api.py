def authenticate_graph_api(client_id, client_secret, tenant_id):
    # Function to authenticate with Microsoft Graph API
    import msal

    app = msal.ConfidentialClientApplication(
        client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        client_credential=client_secret,
    )

    result = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception("Authentication failed: " + str(result.get("error")))

def get_email_attachments(access_token, user_id, email_id):
    # Function to retrieve email attachments
    import requests

    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/messages/{email_id}/attachments"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("value", [])
    else:
        raise Exception("Failed to retrieve attachments: " + str(response.json()))

def download_attachment(access_token, user_id, email_id, attachment_id):
    # Function to download a specific attachment
    import requests

    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/messages/{email_id}/attachments/{attachment_id}/$value"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to download attachment: " + str(response.json()))