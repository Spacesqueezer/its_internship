from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from datetime import datetime


@main_auth(on_start=True, set_cookie=True)
def index_page(request):

    return render(request, 'index.html', {'user': request.bitrix_user})  # В качестве контекста отправляем пользователя


@main_auth(on_cookies=True)
def get_last_deals(request):
    # Получаем список активных сделок по параметру STAGE_SEMANTIC_ID
    params = {
        # Фильтруем по активности
        "filter": {
            "STAGE_SEMANTIC_ID": "P"
        },
        # Выбираем нужные поля
        "select": ["TITLE", # Название
                    "STAGE_ID", # Стадия
                    "DATE_CREATE", # Дата создания
                    "OPPORTUNITY", # Сумма
                    ],
        # Сортировка по дате
        "order": { "DATE_CREATE": "DESC" },
    }

    # Вызываем метод Bitrix API
    response = request.bitrix_user_token.call_api_method('crm.deal.list', params)

    # Достаём результат
    deals = response.get('result', [])[:10]

    # Преобразовываем дату
    for deal in deals:
        # Получаем только дату
        raw_date = deal.get("DATE_CREATE")

        # Преобразовываем в нужный формат
        dt = datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
        deal["DATE_CREATE"] = dt.strftime("%d.%m.%Y %H:%M")

    # Рендерим шаблон с данными
    return render(request, 'tabs/last_active_deals.html', {'deals': deals})

