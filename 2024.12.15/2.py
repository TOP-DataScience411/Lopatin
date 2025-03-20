import decimal
import datetime

class PowerMeter:
    def __init__(self, tariff1 = 6.5, tariff2 = 4.5,
                 tariff2_starts: datetime.time = datetime.time(23, 0),
                 tariff2_ends: datetime.time = datetime.time(7, 0)):
        self.tariff1 = decimal.Decimal(str(tariff1))
        self.tariff2 = decimal.Decimal(str(tariff2))
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = decimal.Decimal('0')
        self.charges = {}

    def __repr__(self):
        return f"<PowerMeter: {self.power} кВт/ч>"

    def __str__(self):
        current_month = datetime.date.today().replace(day=1)
        if current_month in self.charges:
            return f"({current_month.strftime('%b')}) {self.charges[current_month]:.2f}"
        else:
            return f"({current_month.strftime('%b')}) 0.00"

    def meter(self, power) -> decimal.Decimal:
        power_decimal = decimal.Decimal(str(power))
        self.power += power_decimal
        current_time = datetime.datetime.now().time()
        if self.tariff2_starts <= current_time < self.tariff2_ends:
            cost = power_decimal * self.tariff2
        else:
            cost = power_decimal * self.tariff1
        cost_rounded = cost.quantize(decimal.Decimal('0.00'))
        current_month = datetime.date.today().replace(day=1)
        if current_month in self.charges:
            self.charges[current_month] += cost_rounded
        else:
            self.charges[current_month] = cost_rounded
        return cost_rounded

# >>> pm1 = PowerMeter()
# >>> pm1.meter(25)
# Decimal('162.50')
# >>> pm1.meter(200)
# Decimal('1300.00')
# >>> pm1
# <PowerMeter: 225 кВт/ч>
# >>> print(pm1)
# (Mar) 1462.50
