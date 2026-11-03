import tomllib

with open("pyproject.toml", "rb") as f:
    metadata = tomllib.load(f)

def metadata_info():
    project_name = metadata["project"]["name"]
    requires_python = metadata["project"]["requires-python"]

    print(f"프로젝트 이름:{ project_name}")
    print(f"필요한 파이썬 버전:{ requires_python}")

    return

def main() -> None:
    print("Hello from 02-py-exercise!")
    metadata_info()

    return  


if __name__ == "__main__":
    main()
