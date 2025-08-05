DEBUG = True
ALLOWED_HOSTS = ['*']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass

TINKOFF_API_KEY = 'your-api-key'
ENDPOINT_TINKOFF = 'your-secret-key'
API_KEY_TINKOFF = 'your-api-key'
SECRET_KEY_TINKOFF = 'your-secret-key'

OPEN_AI_API_KEY = 'your-api-key'


APP_SETTINGS = LocalSettingsClass(
    portal_domain='b24-1aflrf.bitrix24.ru',
    app_domain='127.0.0.1:8000',
    app_name='b24app',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.689249d4304a79.84420674',
    application_bitrix_client_secret='SrOrJf3R4p6UZQVrIKwBfV1XNglsgkrr46hXReWXn7EJWOTEAO',
    application_index_path='/',
)

DOMAIN = "56218ef983f3-8301993767665431593.ngrok-free.app"


DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'foodgram',
		'USER': 'postgresql',
		'PASSWORD': '123456',
		'HOST': 'localhost',
		'PORT': '5432',
	},
}
