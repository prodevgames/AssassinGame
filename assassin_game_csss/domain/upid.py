from re import compile


class UPID:
    __upid: str = None
    __upid_pattern = compile("^[a-z]{3}[0-9]{3}$")

    def __init__(self, upid: str) -> None:
        raise NotImplementedError
