from posts.file_provider import FilePostProvider

if __name__ == "__main__":
    provider = FilePostProvider()  # по умолчанию input/posts.txt
    try:
        provider.process_file()
    except Exception as e:
        print(f"Error: {e}")