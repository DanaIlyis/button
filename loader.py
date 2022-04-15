import logging
from aiogram import Bot, Dispatcher, types
import config
bot = Bot (token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(format=u'%(filename)5 [LINE:%(lineno)d] #%(levelname)-8s'
                           u'[%(asctine)5]  %(message)5',
                    level=logging.INFO,
                    )
