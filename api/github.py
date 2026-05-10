"""GitHub API integration stub.

Extend this module to fetch live stats (repo count, stars, recent activity)
to display on the portfolio. Requires a GitHub personal access token stored
in an environment variable or Streamlit secrets.
"""


def fetch_github_stats(username: str) -> dict:
    """Return GitHub profile stats for the given username.

    Currently returns an empty dict. Implement by calling the GitHub REST API
    at https://api.github.com/users/{username} with appropriate auth headers.
    """
    return {}
