def read_magic_number(path: str) -> bool:
    if not isinstance(path, str):
        raise ValueError("Path must be a string")
    try:
        with open(path) as f:
            return 1 <= float(f.readline().strip()) < 3
    except Exception as e:
        raise ValueError(
            f"Failed to read magic number from file {path}") from e
