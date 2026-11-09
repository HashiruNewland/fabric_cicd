from pathlib import Path

from azure.identity import AzureCliCredential
from fabric_cicd import deploy_with_config

# Path to the deployment configuration
config_file_path = str(Path(__file__).resolve().parent / "config.yml")

# Target deployment environment
environment = "PPE"

# Deploy using the configuration file
deploy_with_config(
    config_file_path=config_file_path,
    token_credential=AzureCliCredential(),
    environment=environment,  # Optional
)
