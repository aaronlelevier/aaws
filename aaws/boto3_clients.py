import boto3
import keyring
import getpass


def local_client(service:str, alias:str) -> boto3.client:
    """
    Returns a boto3.client authenticated via your keychain

    Args:
        service: the AWS service, i.e. ec2
        alias: the alias that the credentials are stored under
    """
    return boto3.client(
        service,
        aws_access_key_id=keyring.get_password(alias, 'aws_access_key_id'),
        aws_secret_access_key=keyring.get_password(alias, 'aws_secret_access_key')
    )



def save_local_credentials(alias:str) -> None:
    """
    Use to save AWS credentials to your keychain

    Call this before using `local_client`

    Args:
        alias: the alias that the credentials are stored under
    """
    print("Enter aws_access_key_id:")
    keyring.set_password(alias, 'aws_access_key_id', getpass.getpass())

    print("Enter aws_secret_access_key:")
    keyring.set_password(alias, 'aws_secret_access_key', getpass.getpass())
