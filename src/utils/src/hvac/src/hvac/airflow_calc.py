import math


class AirflowSystem:
    def __init__(self, duct_diameter: float, velocity_target: float):
        self.duct_diameter = duct_diameter
        self.velocity_target = velocity_target

    def duct_area(self) -> float:
        """Calculate duct cross-sectional area (m²)."""
        radius = self.duct_diameter / 2
        return math.pi * radius ** 2

    def airflow_m3s(self) -> float:
        """Airflow in m³/s."""
        return self.duct_area() * self.velocity_target

    def calculate_cfm(self) -> float:
        """Convert airflow to CFM."""
        return self.airflow_m3s() * 2118.88
