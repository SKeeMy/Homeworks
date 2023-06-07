class KeyValueStorage:
    def __init__(self, file_path):
        self.__dict__['_data'] = {}
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    key, value = line.strip().split('=')
                    if value.isdigit():
                        value = int(value)
                    self._data[key] = value
                    if hasattr(self, key):
                        raise ValueError(f"Invalid key '{key}'")
                    setattr(self, key, value)
                except ValueError:
                    pass

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        if hasattr(self, key):
            super().__setattr__(key, value)
        else:
            self._data[key] = value

    def __getattr__(self, item):
        return getattr(self._data, item)

    def __setattr__(self, key, value):
        if key in self._data:
            self._data[key] = value
        else:
            super().__setattr__(key, value)
