def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def _count(current: int, target: int) -> None:
        if current > target:
            print("Harvest time!")
            return
        print(f"Day {current}")
        _count(current + 1, target)

    _count(1, days)
