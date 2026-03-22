from posts.json_provider import JSONPostProvider

if __name__ == "__main__":
    provider = JSONPostProvider()  # по умолчанию input/posts.json
    try:
        provider.process_file()
    except Exception as e:
        print(f"Error: {e}")