class Locators:
    # поле ввода имени в форме регистрации
    REGISTER_NAME_INPUT = ".//label[text()='Имя']/parent::div/input"
    # поле ввода email в форме регистрации
    REGISTER_EMAIL_INPUT = ".//label[text()='Email']/parent::div/input"
    # поле ввода пароля в форме регистрации
    REGISTER_PASSWORD_INPUT = ".//label[text()='Пароль']/parent::div/input"
    # кнопка регистрации
    REGISTER_BUTTON = ".//form[@class='Auth_form__3qKeq mb-20']/button[text()='Зарегистрироваться']"
    # тэг, содержащий ошибку
    REGISTER_ERROR_P = ".//p[contains(@class, 'input__error')]"
    # поле ввода email в форме входа
    LOGIN_EMAIL_INPUT = ".//input[@name='name']"
    # поле ввода пароля в форме входа
    LOGIN_PASSWORD_INPUT = ".//input[@type='password']"
    # кнопка входа
    LOGIN_BUTTON = ".//form[@class='Auth_form__3qKeq mb-20']/button[text()='Войти']"
    # кнопка создания заказа
    CREATE_ORDER_BUTTON = ".//div[@class='BurgerConstructor_basket__container__2fUl3 mt-10']/button"
    # секция ингредиентов в конструкторе
    BURGER_INGREDIENTS_SECTION = "BurgerIngredients_ingredients__1N8v2"
    # ссылка на Личный Кабинет пользователя
    PERSONAL_CABINET_LINK = ".//a[@href='/account']"
    # ссылка на страницу авторизации
    LOGIN_LINK = ".//a[@href='/login']"
    # кнопка выхода из Личного Кабинета пользователя
    LOGOUT_BUTTON = ".//nav[@class='Account_nav__Lgali']/ul/li[last()]/button"
    # кнопка "Конструктор" в шапке страницы
    CONSTRUCTOR_BUTTON = ".//li/a[@href='/']"
    # лого в шапке страницы
    LOGO = ".//div/a[@href='/']"
    # вкладка с булками в конструкторе
    CONSTRUCTOR_BREAD_TAB = \
        ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Булки']/parent::div"
    # вкладка с соусами в конструкторе
    CONSTRUCTOR_SAUCE_TAB = \
        ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Соусы']/parent::div"
    # вкладка с начинками в конструкторе
    CONSTRUCTOR_TOPPING_TAB = \
        ".//section[@class='BurgerIngredients_ingredients__1N8v2']//span[text()='Начинки']/parent::div"
    # секция с булками в конструкторе
    CONSTRUCTOR_BREAD_SECTION = ".//h2[text()='Булки']"
    # секция с соусами в конструкторе
    CONSTRUCTOR_SAUCE_SECTION = ".//h2[text()='Соусы']"
    # секция с начинками в конструкторе
    CONSTRUCTOR_TOPPING_SECTION = ".//h2[text()='Начинки']"
