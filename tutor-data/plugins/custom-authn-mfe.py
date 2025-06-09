import os
from tutor import hooks
 
hooks.Filters.CONFIG_DEFAULTS.add_item(
    (
        "MFE_APPS",
        {
            "authn": {
                "repository": f"https://github.com/{os.environ.get('GITHUB_USERNAME', 'ihworker')}/frontend-app-authn.git",
                "version": "custom-modifications",
                "port": 1999,
            },
        },
    )
)
 
hooks.Filters.ENV_PATCHES.add_item(
    (
        "custom-authn-env",
        """
# Custom MFE Environment Variables for Task Assignment
AUTHN_CUSTOM_BRANDING=true
PLATFORM_NAME="Custom Open edX Platform - Task Assignment"
""",
    )
)
