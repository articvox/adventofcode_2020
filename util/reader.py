from typing import Callable


class Read:
    @staticmethod
    def lines_to_list(filename: str, mapper: Callable) -> []:
        lines = []

        with open(filename, 'r') as f:
            while True:
                line = f.readline().strip()
                if not line:
                    break
                lines.append(mapper(line))

        return lines
