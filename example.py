from abc import ABC, abstractmethod
from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {args[0].__class__.__name__} ...")
        return func(*args, **kwargs)

    return wrapper


class Meta(ABC):
    @abstractmethod
    def run(self):
        pass


class Parent(Meta):
    @log
    def __call__(self):
        return self.run()


class Example(Parent):
    def run(self):
        print('print from', self.__class__.__name__)


if __name__ == '__main__':
    example = Example()
    example()