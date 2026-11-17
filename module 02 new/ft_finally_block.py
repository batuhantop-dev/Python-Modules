class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if not plant_name or plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    scenarios = [
        ("valid", ["Tomato", "Lettuce", "Carrots"]),
        ("invalid", ["Tomato", "lettuce", "Carrots"]),
    ]
    for label, plants in scenarios:
        print()
        print(f"Testing {label} plants...")
        print("Opening watering system")
        try:
            for plant in plants:
                water_plant(plant)
        except PlantError as error:
            print(f"Caught PlantError: {error}")
            print(".. ending tests and returning to main")
            return
        finally:
            print("Closing watering system")


if __name__ == "__main__":
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")