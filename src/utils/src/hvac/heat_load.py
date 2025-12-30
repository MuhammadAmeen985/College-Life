from dataclasses import dataclass


@dataclass
class HVACSystem:
    area_sqft: float
    insulation_r_value: float
    outdoor_design_temp: float
    indoor_setpoint: float

    def _delta_t(self) -> float:
        return abs(self.outdoor_design_temp - self.indoor_setpoint)

    def calculate_heating_load(self) -> float:
        """
        Estimate heating load (BTU/hr)
        Formula (simplified industry rule):
        Q = A × ΔT × 0.133 / R
        """
        heat_loss = (
            self.area_sqft * self._delta_t() * 0.133
        ) / self.insulation_r_value
        return heat_loss * 1000

    def calculate_cooling_load(self) -> float:
        """
        Estimate cooling load (BTU/hr)
        Adds solar & internal gain factor.
        """
        base_load = self.calculate_heating_load()
        return base_load * 1.22  # cooling gain factor

    def recommended_tonnage(self) -> float:
        """Return recommended AC tonnage."""
        return self.calculate_cooling_load() / 12000
