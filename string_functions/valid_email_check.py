import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    prefix_regex = r"^[a-zA-Z][a-zA-Z0-9._-]*"

    # Define the exact domain
    domain = r"@leetcode\.com"  # Escape the dot '.' as it's a special character in regex

    # Combine the prefix and domain regex to form the full valid email regex
    # ^          - Start of the entire email string
    # ({prefix_regex}) - Capture group for the prefix (though not strictly needed for filtering)
    # {domain}   - The exact domain
    # $          - End of the entire email string
    full_email_regex = rf"^{prefix_regex}{domain}$"

    # Use .str.fullmatch() to check if the entire email string matches the regex
    # na=False handles any potential NaN values in the 'email' column by treating them as False
    valid_email_mask = users['mail'].str.fullmatch(full_email_regex, na=False)

    # Filter the DataFrame using the boolean mask
    valid_users_df = users[valid_email_mask]

    return valid_users_df