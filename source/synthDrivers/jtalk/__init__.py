from synthDriverHandler import SynthDriver as BaseSynthDriver  # type: ignore


class SynthDriver(BaseSynthDriver):
    @classmethod
    def check(cls):
        return False
