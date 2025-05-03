from address import Address
from mailing import Mailing


from_address = Address('654321', 'Санкт-Петербург', 'Лермонтова', '25', '12')
to_address = Address('123456', 'Москва', 'Пушкина', '10', '5')


mailing = Mailing(to_address, from_address, 500, "TRACK654321")

print(f'Отправление {mailing.track} из {mailing.from_address.index}, \
{mailing.from_address.town}, {mailing.from_address.street}, \
{mailing.from_address.building} - {mailing.from_address.flat} '
 f'в {mailing.to_address.index}, {mailing.to_address.town}, \
{mailing.to_address.street}, {mailing.to_address.building} - \
{mailing.to_address.flat}. 'f'Стоимость {mailing.cost} рублей.')
