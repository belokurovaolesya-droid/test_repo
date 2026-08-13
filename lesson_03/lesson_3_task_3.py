from address import Address
from mailing import Mailing


to_address = Address(
    "190000",
    "Санкт-Петербург",
    "Невский проспект",
    "10",
    "25",
)

from_address = Address(
    "101000",
    "Москва",
    "Тверская",
    "15",
    "8",
)

mailing = Mailing(
    to_address,
    from_address,
    500,
    "RU123456789",
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, "
    f"{mailing.from_address.city}, "
    f"{mailing.from_address.street}, "
    f"{mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, "
    f"{mailing.to_address.city}, "
    f"{mailing.to_address.street}, "
    f"{mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)