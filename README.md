# TechZone — Онлайн магазин за компютърна техника
 
## Съдържание
 
- [Увод](#увод)
- [I. Преглед и избор на технически средства](#i-преглед-и-избор-на-технически-средства-за-създаване-на-онлайн-магазин)
- [II. Подготовка за създаване на сайта](#ii-подготовка-за-създаване-на-сайта)
- [III. Създаване на онлайн магазин за компютърна техника](#iii-създаване-на-онлайн-магазин-за-компютърна-техника)
- [Заключение](#заключение)
- [Използвана литература](#използвана-литература)
---
 
## Увод
 
Електронната търговия е сред най-динамично развиващите се сектори в глобалната икономика. С нарастващото навлизане на интернет в ежедневието, онлайн магазините се превръщат в основен канал за покупки на стоки и услуги. Разработването на надеждна, мащабируема и сигурна платформа за електронна търговия изисква задълбочени познания в областта на уеб разработката, базите данни, сигурността и потребителското изживяване.
 
Настоящата дипломна работа описва проектирането и разработването на система за електронна търговия **TechZone** – уеб приложение, предназначено за продажба на технологични продукти. Системата е изградена върху **Django Framework (версия 5.0)**, използва **PostgreSQL** за съхранение на данни, **Bootstrap** за потребителския интерфейс и **Stripe** за обработка на плащания.
 
Актуалността на темата произтича от нуждата на малкия и средния бизнес от достъпни и лесно управляеми платформи за онлайн търговия. Много съществуващи решения са или прекалено сложни за поддръжка, или скъпи за лицензиране. Django като технология предоставя отличен баланс между функционалност, сигурност и скорост на разработка.
 
Целта на дипломната работа е да се проектира и реализира пълнофункционална система за електронна търговия, включваща: управление на продукти и категории, количка за пазаруване, система за поръчки, интеграция с платежен процесор, управление на потребители с верификация по имейл и ролево-базиран контрол на достъпа.
 
---
 
## I. Преглед и избор на технически средства за създаване на онлайн магазин
 
### 1.1. Преглед на съществуващи платформи за онлайн магазин
 
При разработването на онлайн магазин е необходимо да се направи задълбочен анализ на наличните технологични решения. На пазара съществуват множество платформи за електронна търговия, всяка от които предлага различен набор от функционалности, технологии и модели на лицензиране.
 
#### Shopify
 
Shopify е облачна SaaS (Software as a Service) платформа за електронна търговия, основана през 2006 г. в Канада. Към момента тя поддържа над 4 милиона онлайн магазина в повече от 175 страни.
 
От техническа гледна точка Shopify е изградена върху **Ruby on Rails** като backend фреймуърк и използва собствен шаблонен език **Liquid**. Фронтендът разчита на JavaScript и React. Данните се съхраняват в **MySQL**, а статичното съдържание се разпределя чрез собствена CDN мрежа.
 
Основното ограничение на Shopify е затвореният му характер – изходният код не е достъпен, платформата работи единствено в облака на Shopify. Абонаментните планове варират от 29 до 299 USD месечно, а при всяка транзакция се дължи допълнителна комисионна.
 
<img width="610" height="335" alt="image" src="https://github.com/user-attachments/assets/d18ed376-8add-4ad7-84de-22de41e40a66" />

*Фиг 1.1. Начална страница на Shopify*
 
#### WooCommerce
 
WooCommerce е плъгин за електронна търговия, разработен за WordPress. Издаден е през 2011 г. от WooThemes (по-късно придобит от Automattic). Захранва около 30% от всички онлайн магазини в интернет.
 
Технологично е изграден изцяло на **PHP** и се базира на архитектурата на WordPress. Данните се съхраняват в **MySQL**. Предимствата включват безплатен изходен код, огромна общност и над 58 000 плъгина. Основният недостатък е тясната обвързаност с WordPress – всяка актуализация крие риск от несъвместимости.
 
<img width="610" height="301" alt="image" src="https://github.com/user-attachments/assets/317d7610-5fa8-4306-a922-ee136ad62b41" />

*Фиг 1.2. Начална страница на WooCommerce*
 
#### Magento (Adobe Commerce)
 
Стартирана през 2008 г., придобита от Adobe през 2018 г. Предлага се в безплатна Community Edition и платена Enterprise Edition. Написана е на **PHP** с **Zend Framework**, MySQL/MariaDB за база данни, Varnish/Redis за кеширане, поддържа GraphQL API за headless имплементации.
 
Предлага богата функционалност (мултимагазини, B2B, разширени отчети), но сложността ѝ е и основното ѝ ограничение — изисква специализирани технически познания.
 
<img width="610" height="418" alt="image" src="https://github.com/user-attachments/assets/8486d805-dd1b-4b33-b5f6-7fb6c177028c" />

*Фиг 1.3. Начална страница на Magento*
 
#### PrestaShop
 
Платформа с отворен код, основана през 2007 г. във Франция. Инсталирана на над 300 000 магазина в над 200 страни. Разработена е на **PHP** със **Symfony** компоненти, **MySQL** база данни, **Smarty** шаблонен двигател, административен панел с **Vue.js**.
 
Ограниченията включват по-бавно развитие на ядрото, неравномерно качество на модулите (голяма част платени) и специфична архитектура, затрудняваща персонализирането.
 
<img width="610" height="375" alt="image" src="https://github.com/user-attachments/assets/54e0ed5a-bb08-49e0-b504-b7162cf7d576" />

*Фиг 1.4. Начална страница на PrestaShop*
 
#### OpenCart
 
Платформа с отворен код, публично достъпна от 2010 г., създадена от Даниел Керис. Захранва над 940 000 онлайн магазина. Изградена на **PHP**, следва **MVC** архитектура, **MySQL/MariaDB** база данни, **Twig** шаблонен двигател (3.x+).
 
Подходяща е за малки и средни магазини поради ниската системна сложност. Ограниченията включват по-слаба производителност при голям обем продукти и силна зависимост от платени разширения.
 
<img width="600" height="366" alt="image" src="https://github.com/user-attachments/assets/8cfc3b2d-6c9b-4502-af76-c3e2ec4d2f36" />

*Фиг 1.5. Начална страница на OpenCart*
 
### 1.2. Преглед на съществуващи платформи за компютърна техника
 
#### Newegg
 
Международен онлайн магазин, специализиран в компютърна техника и хардуер. Основан през 2001 г. в САЩ. Използва съвременна cloud уеб архитектура и модерни JavaScript технологии. Предимство е специализацията в компютърна техника, ограничение — по-ограничено присъствие в някои региони.
 
<img width="607" height="292" alt="image" src="https://github.com/user-attachments/assets/c627a683-e84a-4b64-887a-dc16df9e89ee" />

*Фиг 1.6. Начална страница на Newegg*
 
#### Desktop.bg
 
Български онлайн магазин, специализиран в компютри, лаптопи, компоненти и периферия. Насочен към локалния пазар, предлага готови конфигурации и персонализиране. Предимства: локална насоченост, конкурентни цени. Ограничения: по-малък мащаб спрямо глобалните платформи.
 
<img width="601" height="255" alt="image" src="https://github.com/user-attachments/assets/e253b374-bc58-4225-8270-50922db0dd53" />

*Фиг 1.7. Начална страница на Desktop.bg*
 
#### Scan.co.uk
 
Британски онлайн магазин за компютърна техника, хардуер и гейминг компоненти. Основно предимство е възможността за изграждане на custom PC системи. Ограничение — насоченост предимно към UK пазара.
 
<img width="610" height="282" alt="image" src="https://github.com/user-attachments/assets/dd1dabe0-8a6e-40d0-b44b-75fb743a0059" />

*Фиг 1.8. Начална страница на Scan.co.uk*
 
### 1.3. Избор на Open Source решение
 
Open Source (отворен код) е модел на разработка, при който изходният код е публично достъпен и може свободно да бъде използван, изучаван, модифициран и разпространяван.
 
За настоящия проект е избран **Django Framework** като технологична основа — написан на Python, следва принципа „batteries included": ORM, административен панел, автентикация, маршрутизация на URL адреси и шаблонен двигател, всичко „от кутията“.
 
Изборът на Django пред разгледаните платформи е продиктуван от: пълен контрол върху изходния код; стабилност след обновявания; вградена сигурност (CSRF, SQL инжекции, XSS защита по подразбиране); богата екосистема (django-allauth, Stripe SDK).
 
**Таблица 1. Сравнение на платформи за електронна търговия**
 
| Платформа | Технология | Лиценз | Гъвкавост | Трудност |
|---|---|---|---|---|
| Shopify | Ruby on Rails, Liquid, React | Платен абонамент (SaaS) | Ниска | Ниска |
| WooCommerce | PHP, WordPress, MySQL | Безплатен (GPL) | Средна | Средна |
| Magento | PHP, Zend, Vue.js, MySQL | Community: безплатен | Висока | Висока |
| PrestaShop | PHP, Symfony, Smarty, MySQL | Безплатен (OSL) | Средна | Средна |
| **TechZone (Django)** | Python, Django 5.0, PostgreSQL | Open Source (BSD) | Висока | Средна |
| OpenCart | PHP, MVC, TWIG, MySQL | Безплатен (OpenCart) | Среден | Ниска |
 
**Таблица 2. Сравнение на платформи за компютърна техника**
 
| Платформа | Пазар | Фокус | Скалиране | Технологична гъвкавост |
|---|---|---|---|---|
| Newegg | САЩ + международен | PC компоненти, електроника | Глобално | Ниска за външни разработчици |
| Desktop.bg | България + ЕС доставки | Гейминг PC, конфигурации | Регионално | Ниска |
| Scan.co.uk | UK + ЕС | High-end PC, workstation хардуер | Регионално | Ниска |
| **TechZone (Django)** | България | Компютърна техника | Без ограничение | Висока (Django, API, microservices) |
 
---
 
## II. Подготовка за създаване на сайта
 
### 2.1. Основни pip библиотеки и Django MTV модел
 
#### Django 5.0.14
 
Django е уеб фреймуърк от високо ниво, написан на Python, следващ **MTV (Model-Template-View)** архитектурен шаблон — вариант на класическия MVC. Проектът е стартиран през 2003 г. от Адриан Головей и Саймън Уилисън и е с отворен код от 2005 г.
 
Версия 5.0 въвежда facet filters в административния панел, подобрена поддръжка на асинхронни views и middleware, оптимизирани database connections. Изисква Python 3.10+.
 
В TechZone Django осигурява MTV архитектурата (4 приложения: store, storage, accounts, orders), ORM за PostgreSQL, административен панел и механизми за сигурност (CSRF, XSS филтриране, защита от SQL инжекции).
 
#### django-allauth 65.18.0
 
Библиотека за автентикация и управление на потребителски акаунти. Поддържа потребителско име/парола, имейл/парола и OAuth2 (Google, Facebook, GitHub и др.).
 
Версия 65.x заменя `ACCOUNT_EMAIL_REQUIRED`/`ACCOUNT_USERNAME_REQUIRED` с единен параметър `ACCOUNT_SIGNUP_FIELDS`. Поддържа задължителна верификация на имейл (`ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`).
 
В TechZone управлява изпращането на верификационни имейли, потвърждаването на адреса чрез уникален линк и пренасочванията след вход/изход. Имейлите се изпращат чрез Gmail SMTP с app password.
 
#### django-environ 0.13.0
 
Управлява конфигурационни настройки чрез environment variables и `.env` файлове, следвайки 12-Factor App методологията. Предоставя клас `Env` с методи `env.str()`, `env.int()`, `env.bool()`, `env.db()`.
 
В TechZone управлява зареждането на `SECRET_KEY`, PostgreSQL credentials, Stripe API ключове и Gmail SMTP данни, като гарантира, че чувствителни данни не попадат в GitHub хранилището.
 
#### Stripe 15.2.0
 
Python SDK за интеграция с платежния процесор Stripe. В TechZone се използва **Stripe Charges API** — клиентът въвежда данни на картата чрез Stripe.js, който връща еднократен токен (`stripeToken`). Токенът се изпраща към backend-а, където `stripe.Charge.create()` извършва таксуването. Чувствителните данни на картата никога не преминават през сървъра на приложението.
 
#### Pillow 12.2.0
 
Библиотека за обработка на изображения, наследник на PIL. Задължителна зависимост за работа с `ImageField` в Django. TechZone я използва в модела `Product` за продуктовите снимки, съхранявани в директорията `media/`.
 
#### psycopg2 2.9.12
 
PostgreSQL адаптер за Python, официално препоръчан за Django. Осигурява connection pool, транзакции и преобразуване на типове между Python и PostgreSQL.
 
#### python-dotenv 1.2.2
 
Зарежда environment variables от `.env` файл в `os.environ`. Използва се заедно с django-environ — python-dotenv зарежда файла, а django-environ предоставя типизиран достъп.
 
#### requests 2.34.2
 
HTTP клиентска библиотека. В TechZone се използва за комуникация с **ExchangeRate-API** — при смяна на валута Django view изпраща GET заявка и получава актуалните курсове в JSON формат.
 
#### Други зависимости
 
- **sqlparse 0.5.5** — парсване и форматиране на SQL заявки (използва се вътрешно от Django)
- **httpcore 1.0.9** — ниско ниво HTTP клиент
- **Jinja2 3.1.6** — шаблонен енджин
- **MarkupSafe 3.0.3** — escape на HTML съдържание, защита от XSS
**Таблица 3. Основни pip библиотеки, използвани в TechZone**
 
| Библиотека | Версия | Предназначение |
|---|---|---|
| Django | 5.0.14 | Backend фреймуърк, ORM, административен панел, сигурност |
| django-allauth | 65.18.0 | Автентикация, OAuth2, задължителна имейл верификация |
| django-environ | 0.13.0 | Управление на конфигурация чрез .env файлове |
| Stripe | 15.2.0 | Обработка на картови плащания чрез Stripe API |
| Pillow | 12.2.0 | Обработка и валидация на изображения (ImageField) |
| psycopg2 | 2.9.12 | PostgreSQL адаптер |
| python-dotenv | 1.2.2 | Зареждане на .env файл в Python environment |
| requests | 2.34.2 | HTTP клиент за ExchangeRate-API заявки |
| sqlparse | 0.5.5 | Парсване и форматиране на SQL заявки |
| httpcore | 1.0.9 | Ниско ниво HTTP клиент |
| Jinja2 | 3.1.6 | Шаблонен енджин |
| MarkupSafe | 3.0.3 | Защита на HTML съдържание от XSS |
 
### 2.2. Среда за разработка и структура на проекта
 
Проектът е разработен в **PyCharm IDE**. Версионният контрол е реализиран чрез Git с хостинг в GitHub. Конфигурационните данни се съхраняват в `.env` файл, който не е включен в хранилището.
 
```
DjangoProject1/          # Главна конфигурация
    settings.py           # Настройки (DB, email, Stripe, allauth)
    urls.py                # Главни URL маршрути
store/                    # Начална страница, количка, реклами
    models.py               # Category, Ad
    views.py                # home, cart, CRUD за продукти/категории
storage/                  # Каталог с продукти
    models.py               # Product, ProductImage, CartItem
    views.py                # Списък, детайл, търсене
accounts/                 # Регистрация, вход, email верификация
    models.py               # Profile
    views.py                # register, sign_in, sign_out
orders/                    # Поръчки и плащания
    models.py               # Address, Order, OrderItem, Payment
    views.py                # checkout, payment_view, complete_order
static/
    css/home-page.css        # Потребителски стилове
    js/currency.js           # Конвертиране на валути
    js/search_form.js        # AJAX търсене
media/                     # Качени продуктови изображения
templates/                 # HTML шаблони по приложения
```
 
### 2.3. Среда за стартиране на приложението
 
**Системни изисквания:**
- Python 3.11 или по-нова версия
- PostgreSQL 14 или по-нова версия
- pip
- Git
**Инсталация:**
 
```bash
# 1. Клониране на хранилището
git clone https://github.com/NikolayAramazov/Django-e-commerece.git
cd Django-e-commerece
 
# 2. Създаване и активиране на виртуална среда
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
 
# 3. Инсталиране на зависимостите
pip install -r requirments.txt
 
# 4. Създаване на .env файл в корена на проекта
DJANGO_SECRET_KEY=вашият_таен_ключ
DB_NAME=e_commerce
DB_USER=postgres
DB_PASSWORD=вашата_парола
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST_USER=вашият_gmail@gmail.com
EMAIL_HOST_PASSWORD=app_password
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
EXCHANGE_RATE_API_KEY=вашият_ключ
 
# 5. Създаване на PostgreSQL база данни
createdb e_commerce
 
# 6. Прилагане на миграциите
python manage.py migrate
 
# 7. Създаване на суперпотребител
python manage.py createsuperuser
 
# 8. Стартиране на dev сървъра
python manage.py runserver
```
 
Приложението е достъпно на адрес `http://127.0.0.1:8000/`. Административният панел е достъпен на `http://127.0.0.1:8000/admin/` с данните на създадения суперпотребител.
 
---
 
## III. Създаване на онлайн магазин за компютърна техника
 
### 3.1. Архитектура и база данни
 
#### 3.1.1. Архитектура на системата
 
TechZone следва стандартната Django **MTV** архитектура. Системата е организирана в четири приложения:
 
**Таблица 4. Django приложения и техните отговорности**
 
| Django App | Отговорност |
|---|---|
| `store` | Начална страница, категории, реклами, количка, CRUD за продукти |
| `storage` | Продуктов каталог, детайлни страници, AJAX търсене |
| `accounts` | Регистрация, вход/изход, профил, имейл верификация |
| `orders` | Поръчки, адреси, Stripe плащания, история |
 
Главното приложение `DjangoProject1` съдържа глобалните настройки (`settings.py`) и основната URL конфигурация (`urls.py`), която делегира маршрутите към отделните apps.
 
#### 3.1.2. ER модел — схема на базата данни
 
Базата данни е PostgreSQL и се управлява изцяло чрез Django ORM.
 
**Таблица 5. Модел Product (storage)**
 
| Поле | Тип | Описание |
|---|---|---|
| id | BigAutoField (PK) | Автоматичен първичен ключ |
| name | CharField(255) | Наименование на продукта |
| description | TextField | Подробно описание |
| price | DecimalField(10,2) | Основна цена в USD |
| category | ForeignKey(Category) | Принадлежност към категория |
| stock | PositiveIntegerField | Налично количество |
| is_on_sale | BooleanField | Дали е на намаление |
| on_sale_price | DecimalField(10,2) | Намалена цена |
| sales | PositiveIntegerField | Брой продажби (за ranking) |
 
**Таблица 6. Модел Order (orders)**
 
| Поле | Тип | Описание |
|---|---|---|
| id | BigAutoField (PK) | Автоматичен първичен ключ |
| user | ForeignKey(User) | Потребителят, направил поръчката |
| address | ForeignKey(Address) | Адрес за доставка |
| created_at | DateTimeField | Дата и час на поръчката |
| is_paid | BooleanField | Статус на плащането |
| total_price | DecimalField(10,2) | Обща стойност на поръчката |
 
**Таблица 7. Модел Profile (accounts)**
 
| Поле | Тип | Описание |
|---|---|---|
| user | OneToOneField(User) | Връзка към Django User модела |
| phone_number | CharField(15) | Телефонен номер (незадължително) |
| bio | TextField | Кратка биография (незадължително) |
 
#### 3.1.3. URL маршрутизация
 
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('storage.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
]
```
 
**Таблица 8. URL маршрути в TechZone**
 
| URL маршрут | View / Handler | Описание |
|---|---|---|
| `/` | `store:home` | Начална страница |
| `/cart/` | `store:cart` | Количка за пазаруване |
| `/products/` | `storage:all_products` | Каталог с продукти |
| `/products/<pk>/` | `storage:product_detail` | Детайл на продукт |
| `/accounts/sign-in/` | `accounts:sign_in` | Вход в системата |
| `/accounts/register/` | `accounts:register` | Регистрация |
| `/orders/checkout/` | `orders:checkout` | Форма за поръчка |
| `/orders/pay/<id>/` | `orders:payment` | Страница за плащане |
| `/api/exchange-rates/` | `store:exchange_rates` | API за валутни курсове |
 
### 3.2. Описание на модулите и функционалността
 
#### 3.2.1. Модул store — начална страница и количка
 
Модулът `store` е ядрото на приложението. Функцията `home()` зарежда начална страница с четири секции: рекламни банери, най-продавани продукти, продукти на намаление и наскоро разгледани продукти:
 
```python
def home(request):
    best_sellers = Product.objects.filter(
        stock__gt=0, sales__gt=0).order_by('-sales')[:10]
 
    on_sale_products = Product.objects.filter(
        stock__gt=0, is_on_sale=True).order_by('-stock')[:10]
 
    recently_viewed_ids = request.session.get('recently_viewed', [])
    recently_viewed_products = sorted(
        Product.objects.filter(id__in=recently_viewed_ids),
        key=lambda p: recently_viewed_ids.index(p.id)
    )
```
 
<img width="604" height="132" alt="image" src="https://github.com/user-attachments/assets/f57391a0-849e-4925-a635-0544b080f03a" />

*Фиг. 3.1 Количка*
 
Количката е реализирана чрез Django session — данните се съхраняват в речник с ключ `'cart'` в сесията. При добавяне на продукт, `add_to_cart()` проверява наличното количество преди обновяване.
 
#### 3.2.2. Модул storage — продуктов каталог
 
Функцията `all_products()` поддържа два режима: стандартен рендеринг и AJAX рендеринг на частичен шаблон. Детектирането се извършва чрез HTTP хедъра `X-Requested-With`:
 
```python
def all_products(request):
    query = request.GET.get('query', '').strip()
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = Product.objects.all()
 
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            'storage/product_list_partial.html', {'products': products})
        return JsonResponse({'html': html})
 
    return render(request, 'storage/product_list.html', {'products': products})
```
 
<img width="601" height="201" alt="image" src="https://github.com/user-attachments/assets/0a65647c-3f8d-4e04-8ed1-6438f7182086" />

*Фиг 3.2. Страница с продукти*
 
#### 3.2.3. Модул accounts — управление на потребители
 
Автентикацията е реализирана чрез комбинация от Django вградената система и django-allauth. `RegisterForm` добавя имейл валидация върху стандартния `UserCreationForm`. След регистрация, allauth изпраща верификационен имейл — потребителят трябва да го потвърди преди да може да влезе в системата (`ACCOUNT_EMAIL_VERIFICATION = 'mandatory'`).
 
#### 3.2.4. Модул orders — поръчки и плащания
 
Процесът на поръчка протича в три стъпки: попълване на адресна форма (checkout), плащане (payment) и потвърждение (complete_order). При успешно плащане системата намалява `stock` и увеличава `sales`, след което изчиства количката от сесията.
 
<img width="520" height="323" alt="image" src="https://github.com/user-attachments/assets/c622f918-0841-41bc-9c95-cf51164f6491" />

*Фиг. 3.3. Форма за поръчка*
 
<img width="436" height="149" alt="image" src="https://github.com/user-attachments/assets/3cf3bf35-6ae7-4988-a18c-e9f5c1cc92a0" />

*Фиг. 3.4. Форма за плащане*
 
<img width="206" height="114" alt="image" src="https://github.com/user-attachments/assets/476616a0-540f-4fa1-8d0c-c9fdaeda5dd5" />

*Фиг. 3.5. Потвърждаване на поръчката*
 
### 3.3. Конкретни технически решения
 
#### 3.3.1. Интеграция с Stripe
 
Плащанията се обработват чрез **Stripe Charges API**. В `payment_view()` се извършва charge с `amount` в центове (стойността се умножава по 100):
 
```python
charge = stripe.Charge.create(
    amount=int(order.total_price * 100),   # в центове
    currency='usd',
    description=f'Order #{order.id}',
    source=token,
)
```
 
При грешка на картата (`CardError`) потребителят се пренасочва към страница за неуспешно плащане с описание на грешката.
 
#### 3.3.2. Конвертиране на валута
 
Конвертирането е реализирано client-side чрез JavaScript (`currency.js`). Скриптът извлича обменните курсове от вътрешен API endpoint `/api/exchange-rates/`, избраната валута се запазва в cookie за 7 дни. Поддържаните валути са **USD, EUR, GBP и INR**.
 
<img width="538" height="453" alt="image" src="https://github.com/user-attachments/assets/ff9c43fe-3016-4d6d-acfe-85f8306f3eb7" />

*Фиг. 3.6. Конвертиране на валута*
 
#### 3.3.3. AJAX търсене
 
Търсенето на продукти е реализирано без презареждане на страницата чрез jQuery AJAX. При изпращане на формата, `search_form.js` изпраща GET заявка с `X-Requested-With` хедър, а Django View връща само HTML фрагмент (partial template), зареждан динамично в страницата.
 
<img width="340" height="300" alt="image" src="https://github.com/user-attachments/assets/83a5c6a1-042d-4258-8d8e-f73c438b059f" />

*Фиг. 3.7. Търсачка*
 
#### 3.3.4. Автентикация с django-allauth
 
django-allauth 65.18.0 управлява имейл верификацията.
 
**Таблица 9. Конфигурация на django-allauth**
 
| Настройка | Стойност | Описание |
|---|---|---|
| `ACCOUNT_EMAIL_VERIFICATION` | `'mandatory'` | Задължителна верификация на имейл |
| `ACCOUNT_SIGNUP_FIELDS` | `['email*', 'username*', ...]` | Задължителни полета при регистрация |
| `ACCOUNT_CONFIRM_EMAIL_ON_GET` | `True` | Потвърждение при GET заявка |
| `LOGIN_REDIRECT_URL` | `'/'` | Пренасочване след успешен вход |
| `ACCOUNT_LOGOUT_REDIRECT_URL` | `'/'` | Пренасочване след изход |
 
### 3.4. Тестване
 
Системата е тествана на три нива: модулно тестване на модели и форми, интеграционно тестване на views и функционално тестване на потребителски сценарии. За тестване на плащанията е използвана тестовата карта на Stripe: `4242 4242 4242 4242`.
 
**Таблица 10. Резултати от тестването**
 
| Компонент | Вид тест | Резултат |
|---|---|---|
| RegisterForm | Валидация на дублиран имейл/username | PASS |
| CheckoutForm | Валидация на телефон и пощенски код | PASS |
| add_to_cart | Проверка за наличност | PASS |
| Stripe charge | Тест с карта 4242 4242 4242 4242 | PASS |
| AJAX търсене | Проверка на partial response | PASS |
| Имейл верификация | Потвърждение на линк | PASS |
| CRUD продукти | Права на достъп (суперпотребител) | PASS |
 
### 3.5. Функционалност на сайта
 
Настоящото ръководство описва начина на използване на разработената уеб базирана система за електронна търговия от гледна точка на крайния потребител. Сайтът предоставя интуитивен интерфейс за разглеждане на продукти, управление на количка и извършване на поръчки.
 
#### 3.5.1. Стартиране на приложението
 
Потребителят достъпва системата чрез уеб браузър (Google Chrome, Mozilla Firefox, Microsoft Edge и др.), като зарежда началната страница на сайта.
 
<img width="609" height="439" alt="image" src="https://github.com/user-attachments/assets/85eec1f6-7005-46ea-a363-17d728dfb84e" />

*Фиг. 3.8. Начална страница*
 
#### 3.5.2. Навигация в системата
 
Основното меню предоставя достъп до:
 
- Начална страница
- Каталог с продукти
- Количка
- Вход / Регистрация
Навигацията е реализирана така, че потребителят може лесно да преминава между различните секции без презареждане на страницата (чрез AJAX).
 
<img width="609" height="209" alt="image" src="https://github.com/user-attachments/assets/4a4a0917-c596-46f9-b1f9-a95c3488a27c" />

*Фиг. 3.9. Навигационно меню*
 
#### 3.5.3. Регистрация на нов потребител
 
За извършване на поръчка е необходимо потребителят да има профил.
 
**Стъпки:**
1. Избира бутон „Регистрация“
2. Попълва потребителско име, имейл адрес, парола
3. Потвърждава регистрацията
След успешна регистрация и потвърждаване на имейл, потребителят автоматично може да влезе в системата.
 
<img width="437" height="469" alt="image" src="https://github.com/user-attachments/assets/4ee23ed1-133b-47ea-bfe9-9e8b3aa0abbc" />

*Фиг. 3.10. Форма за регистрация*
 
<img width="607" height="435" alt="image" src="https://github.com/user-attachments/assets/ffa36e45-4372-4615-81ad-9a356fe81a35" />

*Фиг. 3.11. Изчаква се потвърждаване на регистрацията от имейл*
 
<img width="598" height="295" alt="image" src="https://github.com/user-attachments/assets/0cabc003-d6f4-4f5d-a0d6-bf55e163939d" />

*Фиг. 3.12. Потвърждаване на имейл*
 
<img width="158" height="32" alt="image" src="https://github.com/user-attachments/assets/d04a1200-cda5-4292-8622-81af29c695dc" />

*Фиг. 3.13. Успешно потвърден имейл*
 
<img width="428" height="417" alt="image" src="https://github.com/user-attachments/assets/75a9ba8b-29fa-4265-9443-60172df8f949" />

*Фиг. 3.14. Влизане в профила*
 
След успешна регистрация потребителят може да влезе в профила си и да прави поръчки от сайта.
 
#### 3.5.4. Разглеждане на продукти
 
В началната страница се визуализира меню с всички продукти и техните категории. Всеки продукт съдържа: име, цена, кратко описание, изображение. Потребителят може да кликне върху продукт, за да види подробна информация.
 
<img width="605" height="235" alt="image" src="https://github.com/user-attachments/assets/fbe58f9a-89da-48c2-983a-6c24b9a8c8b3" />

*Фиг. 3.15. Страница с продукти*
 
<img width="573" height="339" alt="image" src="https://github.com/user-attachments/assets/77543afa-2476-455e-bc1f-31efe4eb5fcd" />

*Фиг. 3.16. Подробна информация на продукт*
 
#### 3.5.5. Извършване на поръчка
 
След успешна регистрация потребителят може да направи поръчка на избрани от него продукти.
 
**Стъпки:**
- Добавяне на продукт в количката
- Преглед на количката
- Попълване на форма за поръчка
- Попълване на форма за плащане
- Финализиране на поръчката успешно / неуспешно плащане
<img width="568" height="326" alt="image" src="https://github.com/user-attachments/assets/35762671-08d1-4dd0-98fc-7e1dc2380566" />

*Фиг. 3.17. Добавяне в количката*
 
<img width="509" height="171" alt="image" src="https://github.com/user-attachments/assets/36dd143b-eb60-46e1-b77b-c4d8952b38f3" />

*Фиг. 3.18. Преглед на количката*
 
<img width="531" height="330" alt="image" src="https://github.com/user-attachments/assets/72989d7a-44a3-45cc-bdbe-8d4f9d6866cb" />

*Фиг. 3.19. Форма за поръчка*
 
<img width="484" height="166" alt="image" src="https://github.com/user-attachments/assets/3889ff2a-169a-4849-970f-f45a52c93b36" />

*Фиг. 3.20. Форма за плащане (Stripe)*
 
<img width="205" height="114" alt="image" src="https://github.com/user-attachments/assets/a47b5f7e-0b1f-4cf1-b8bb-eba62351f94a" />

*Фиг. 3.21. Финализиране на поръчката*
 
<img width="137" height="111" alt="image" src="https://github.com/user-attachments/assets/fb053df8-c6c9-42c8-b967-2de642e836db" />

*Фиг. 3.22. Неуспешно плащане*
 
---
 
## Заключение
 
В настоящата дипломна работа е разработен онлайн магазин за компютърна техника - TechZone, базиран на Django Framework. Сайтът покрива всички заложени функционални изисквания: управление на продукти и категории, количка за пазаруване, процес на поръчка, интеграция с Stripe, имейл верификация чрез django-allauth, AJAX търсене и конвертиране на валути в реално време.
 
**Основни приноси на дипломната работа:**
 
- Проектирана и реализирана модулна архитектура от четири Django apps с ясно разделени отговорности
- Внедрена система за управление на количка, базирана на Django sessions, без нужда от база данни за анонимни потребители
- Интегриран Stripe Charges API с обработка на грешки и записване на платежна информация
- Реализирана client-side конверсия на валути с кеширане в cookies
- Внедрено AJAX търсене чрез jQuery с partial template rendering
- Конфигурирана задължителна имейл верификация чрез django-allauth v65+
**Насоки за бъдещо развитие:**
 
- Внедряване на Django REST Framework за API backend и мобилно приложение
- Добавяне на система за оценки и коментари на продукти
- Интегриране на OAuth2 вход чрез Google и Facebook
- Реализиране на известия в реално време чрез Django Channels
- Разгръщане в облачна инфраструктура (AWS, Heroku или DigitalOcean)
Разработената система демонстрира практическото приложение на знанията, придобити в рамките на обучението в Технически факултет на УХТ – Пловдив, и може да служи като основа за реална търговска платформа след допълнително разширяване и оптимизация.
 
---
 
## Използвана литература
 
**На кирилица:**
 
1. Арамазов Н. TechZone – Django e-commerce проект. GitHub хранилище, https://github.com/NikolayAramazov/Django-e-commerece
**На латиница:**
 
2. Adobe Inc. Adobe Commerce (Magento). https://business.adobe.com/products/magento/magento-commerce.html
3. Automattic Inc. WooCommerce. https://woocommerce.com
4. Bootstrap 5 Documentation. https://getbootstrap.com/docs/5.0/
5. Desktop.bg. https://desktop.bg
6. Django Software Foundation. Django 5.0 Documentation. https://docs.djangoproject.com/en/5.0/
7. Django Software Foundation. Django ORM — Models and Databases. https://docs.djangoproject.com/en/5.0/topics/db/models/
8. django-allauth Documentation. https://docs.allauth.org/en/latest/
9. django-environ Documentation. https://django-environ.readthedocs.io/en/latest/
10. ExchangeRate-API. Currency Conversion API Documentation. https://www.exchangerate-api.com/docs/
11. Forcier, J., Bissex, P., Chun, W. *Python Web Development with Django*. Addison-Wesley Professional, Boston, 2008.
12. Newegg. https://www.newegg.com
13. OpenCart Ltd. https://www.opencart.com
14. PrestaShop S.A. https://www.prestashop.com
15. Scan.co.uk. https://www.scan.co.uk
16. Shopify Inc. https://www.shopify.com
17. Stripe Inc. Stripe API Documentation. https://stripe.com/docs
---
 
## Автор
 
**Николай Арамазов** — Университет по хранителни технологии, Пловдив
