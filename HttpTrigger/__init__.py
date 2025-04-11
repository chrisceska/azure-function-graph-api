def main(req: func.HttpRequest) -> func.HttpResponse:
    import logging
    import json
    from shared_code.graph_api import authenticate, download_attachments

    logging.info('Python HTTP trigger function processed a request.')

    # Authenticate with Microsoft Graph API
    token = authenticate()
    if not token:
        return func.HttpResponse(
            "Authentication failed.",
            status_code=401
        )

    # Get the email ID from the query parameters
    email_id = req.params.get('email_id')
    if not email_id:
        return func.HttpResponse(
            "Please pass an email_id on the query string.",
            status_code=400
        )

    # Download attachments from the specified email
    attachments = download_attachments(token, email_id)
    if attachments is None:
        return func.HttpResponse(
            "Failed to download attachments.",
            status_code=500
        )

    return func.HttpResponse(
        json.dumps(attachments),
        mimetype="application/json",
        status_code=200
    )