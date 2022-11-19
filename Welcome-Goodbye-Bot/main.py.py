import welcome
import goodbye
import model

from welcome import botWelcome
from goodbye import botGoodbye

botWelcome.run(model.token)
botGoodbye.run(model.token)