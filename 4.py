class StringSorter:
    """
    A class to perform sorting operations on a list of strings.
    """

    @classmethod
    def main(cls, strings: list[str]) -> None:
        """
        Sorts the list of strings by increasing and decreasing length.

        Args:
            strings (list[str]): List of strings to be sorted.
        
        Returns:
            None. The list is sorted in-place by both increasing and decreasing length.
        """
        cls._increasing_length(strings)
        cls._decreasing_length(strings)


    @staticmethod
    def _increasing_length(strings: list[str]) -> None:
        n = len(strings)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if len(strings[i - 1]) > len(strings[i]):
                    strings[i - 1], strings[i] = strings[i], strings[i - 1]
                    swapped = True
            n -= 1

    @staticmethod
    def _decreasing_length(strings: list[str]) -> None:
        n = len(strings)
        swapped = True
        while swapped:
            swapped = False
            for i in range(1, n):
                if len(strings[i - 1]) < len(strings[i]):
                    strings[i - 1], strings[i] = strings[i], strings[i - 1]
                    swapped = True
            n -= 1
