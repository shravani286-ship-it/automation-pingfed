from src.main import post_request

def main():
    status = post_request()
    print("Deployment status:", status)
    if status != 201:
        raise Exception(f"Deployment failed with status {status}")

if __name__ == "__main__":
    main()