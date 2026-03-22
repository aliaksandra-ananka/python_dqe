from posts.xml_provider import XMLPostProvider

if __name__ == "__main__":
    provider = XMLPostProvider()  # по умолчанию input/posts.xml
    try:
        provider.process_file()
    except Exception as e:
        print(f"Error: {e}")