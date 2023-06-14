from pathlib import Path
from typing import Optional, Callable

def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    count = 0
    for file in dir_path.glob(f'*.{file_extension}'):
        with open(file, 'r') as f:
            if tokenizer:
                count += sum(len(tokenizer(line)) for line in f)
            else:
                count += sum(1 for _ in f)
    return count