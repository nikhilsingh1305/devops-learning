def health_check():
    return {
        "status": "healthy",
        "service": "devops-learning"
    }


if __name__ == "__main__":
    print(health_check())