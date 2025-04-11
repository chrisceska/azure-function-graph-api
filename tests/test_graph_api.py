import unittest
from unittest.mock import patch, MagicMock
from shared_code.graph_api import authenticate_graph_api, get_email_attachments, download_attachment

class TestGraphAPI(unittest.TestCase):

    @patch("shared_code.graph_api.msal.ConfidentialClientApplication")
    def test_authenticate_graph_api_success(self, mock_msal):
        mock_app = MagicMock()
        mock_app.acquire_token_for_client.return_value = {"access_token": "mock_access_token"}
        mock_msal.return_value = mock_app

        access_token = authenticate_graph_api("mock_client_id", "mock_client_secret", "mock_tenant_id")
        self.assertEqual(access_token, "mock_access_token")

    @patch("shared_code.graph_api.msal.ConfidentialClientApplication")
    def test_authenticate_graph_api_failure(self, mock_msal):
        mock_app = MagicMock()
        mock_app.acquire_token_for_client.return_value = {"error": "invalid_client"}
        mock_msal.return_value = mock_app

        with self.assertRaises(Exception) as context:
            authenticate_graph_api("mock_client_id", "mock_client_secret", "mock_tenant_id")
        self.assertIn("Authentication failed", str(context.exception))

    @patch("shared_code.graph_api.requests.get")
    def test_get_email_attachments_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": [{"id": "attachment1"}, {"id": "attachment2"}]}
        mock_get.return_value = mock_response

        attachments = get_email_attachments("mock_access_token", "mock_user_id", "mock_email_id")
        self.assertEqual(len(attachments), 2)
        self.assertEqual(attachments[0]["id"], "attachment1")

    @patch("shared_code.graph_api.requests.get")
    def test_get_email_attachments_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"error": "Bad Request"}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            get_email_attachments("mock_access_token", "mock_user_id", "mock_email_id")
        self.assertIn("Failed to retrieve attachments", str(context.exception))

    @patch("shared_code.graph_api.requests.get")
    def test_download_attachment_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"mock_attachment_content"
        mock_get.return_value = mock_response

        content = download_attachment("mock_access_token", "mock_user_id", "mock_email_id", "mock_attachment_id")
        self.assertEqual(content, b"mock_attachment_content")

    @patch("shared_code.graph_api.requests.get")
    def test_download_attachment_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": "Not Found"}
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            download_attachment("mock_access_token", "mock_user_id", "mock_email_id", "mock_attachment_id")
        self.assertIn("Failed to download attachment", str(context.exception))

if __name__ == "__main__":
    unittest.main()
