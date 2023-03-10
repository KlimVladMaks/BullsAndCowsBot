# Приветственное сообщение
start_text = 'Привет! Я - бот, с которым вы сможете поиграть в популярную логическую игру "Быки и коровы".\n' \
             '\n' \
             'Вот какие команды я знаю:\n' \
             '\n' \
             '/help - Вывести справочную информацию обо мне\n' \
             '/rules - Узнать правила игры\n' \
             '/userPlay - Я загадываю, вы отгадываете\n' \
             '/botPlay - Вы загадываете, я отгадываю'

# Сообщение со справочной информацией
help_text = 'Хотите узнать о моём функционале?\n' \
            'Вот какие команды я знаю:\n' \
            '\n' \
            '/help - Вывести справочную информацию обо мне\n' \
            '/rules - Узнать правила игры\n' \
            '/userPlay - Я загадываю, вы отгадываете\n' \
            '/botPlay - Вы загадываете, я отгадываю'

# Сообщение с правилами игры
rules_text = '"Быки и коровы" - это логическая игра, в которую играют два игрока. ' \
             'Один игрок загадывает четырёхзначную последовательность из неповторяющихся цифр ' \
             '(например, "0357" или "1759"), в то время как задача второго её отгадать за как можно меньшее ' \
             'количество попыток. Для этого отгадывающий игрок предлагает свои варианты данной последовательности ' \
             '(варианты также должны представлять из себя последовательность из четырёх неповторяющихся цифр), ' \
             'для каждого из которых загадавший игрок должен сказать, сколько "быков" и сколько "коров" было угадано. ' \
             'Количество "быков" показывает, сколько цифр были правильно угаданы и помещены на правильную позицию. ' \
             'Количество "коров" показывает, сколько цифр были правильно угаданы, ' \
             'но помещены на неправильную позицию. ' \
             'Чтобы выиграть, игроку требуется угадать всех четырёх быков, ' \
             'то есть указать правильную числовую последовательность.'

# Сообщение о некорректном вводе
incorrect_input_text = 'Извините, но я не понимаю, что вы написали. Попробуйте ввести /help, чтобы лучше ознакомиться ' \
                       'с моим функционалом.'

# Стартовое сообщение для userPlay-цикла
userPlay_start_text = 'Отлично, давайте сыграем! Сейчас я загадаю последовательность из четырёх неповторяющихся ' \
                      'цифр (например, "0357" или "1759"), а ваша задача будет её отгадать. Для этого просто ' \
                      'введите свой вариант последовательности из четырёх неповторяющихся цифр, и я скажу, сколько ' \
                      '"быков" и "коров" вы угадали.\n' \
                      '\n' \
                      'Готовы? Начали! Можете смело вводить свой вариант.\n' \
                      '\n' \
                      '(Кстати, если вы вдруг захотите выйти из игры, то просто введите /stop вместо вашего варианта)'

botPlay_start_text = 'Отлично, давайте сыграем! Загадайте последовательность из четырёх неповторяющихся цифр ' \
                     '(например, "0357" или "1759"), а я попробую её угадать. Для этого я буду отправлять вам свои ' \
                     'варианты, а вы должны написать сколько быков и коров я угадал. Чтобы сообщить мне эту ' \
                     'информацию, просто укажите два числа через пробел, первое из которых - количество быков, а ' \
                     'второе - количество коров (например, ввод "1 3" означает, что я угадал одного быка и ' \
                     'три коровы). Если мой вариант совпадёт с вашим, то просто введите "4 0" (четыре быка, ' \
                     'ноль коров). Будьте аккуратны, так как даже один неправильный ввод может привести ' \
                     'к тому, что я не смогу отгадать вашу последовательность.\n' \
                     '\n' \
                     'Готовы? Начали! Сейчас я отправлю вам свой первый вариант.\n' \
                     '\n' \
                     '(Кстати, если вы вдруг захотите выйти из игры, то просто введите /stop вместо вашего варианта)'

# Заключительное сообщение для userPlay-цикла
userPlay_stop_text = 'Отлично поиграли! Станет скучно - обращайтесь ещё.\n' \
                     'Вот, кстати, какие команды я знаю:\n' \
                     '\n' \
                     '/help - Вывести справочную информацию обо мне\n' \
                     '/rules - Узнать правила игры\n' \
                     '/userPlay - Я загадываю, вы отгадываете\n' \
                     '/botPlay - Вы загадываете, я отгадываю'

# Сообщение о некорректно введённой последовательности
userPlay_incorrect_input_text = 'Извините, но я не понимаю, что вы написали. Попробуйте ввести последовательность ' \
                                'из четырёх неповторяющихся чисел, чтобы продолжить игру, или команду /stop, чтобы ' \
                                'выйти из текущей игры.'

# Сообщение о некорректно введённом количестве быков и коров
botPlay_incorrect_input_text = 'Извините, но я не понимаю, что вы написали. Попробуйте ввести количество ' \
                               'угаданных быков и коров через пробел (например, ввод "1 3" означает, что угаданы ' \
                               'один бык и три коровы), чтобы продолжить игру, или команду /stop, чтобы ' \
                               'выйти из текущей игры.'

botPlay_empty_list_error_text = 'Извините, но у меня закончились варианты. Возможно, вы загадали некорректную ' \
                                'последовательность или ошиблись при подсчёте "быков" и "коров".'


