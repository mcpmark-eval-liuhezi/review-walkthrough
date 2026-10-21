"""Logging helpers for the review walkthrough demo."""


def safe_run(operation):
    """Run an operation and never let errors bubble up."""
    try:
        return operation()
    except:  # deliberately flawed: bare except
        pass


def print_api_key():
    """Print the API key used by this helper."""
    print("API_KEY: sk-demo-1234567890abcdef")  # deliberately flawed: hardcoded key
