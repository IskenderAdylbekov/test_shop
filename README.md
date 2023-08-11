# test_shop

Отчет о проделанной работе
В данном проекте я реализовал онлайн-магазин с использованием Django, Django REST Framework и других современных инструментов. В ходе разработки я провел 
оптимизацию, улучшение производительности и использование современных подходов к разработке веб-приложения.

Оптимизация базы данных и производительности
Я оптимизировал запросы к базе данных, используя методы select_related и prefetch_related, чтобы уменьшить количество запросов к БД при получении списка продуктов. 
Также внедрил кеширование данных с помощью библиотеки Redis, чтобы ускорить доступ к популярным запросам.

Эффективное кеширование
Для эффективного кеширования данных я использовал библиотеку Redis. Я кешировал результаты запросов к базе данных, что сократило нагрузку на БД и 
улучшило производительность приложения. Также настроил инвалидацию кеша при создании или обновлении продукта, чтобы всегда иметь актуальные данные.

Обертывание в Docker
Для обеспечения удобной и независимой развертки нашего приложения я использовали Docker. Мы создали Dockerfile и docker-compose.yml файлы, 
которые позволяют развернуть приложение в изолированной среде с минимальными затратами. Но так как из-за нагрузки и замедления работы моего компьютера я был 
вынужден docker еще до этого проекта. Поэтому проверить, как работает докер контейнер у меня не получилось. Надеюсь на ваше понимание.

Изменение производительности
Благодаря проведенной оптимизации и кеширования, заметно улучшилось производительность приложения. 
Время ответа на запросы сократилось, нагрузка на базу данных уменьшилась, что привело к более плавной работе приложения и удовлетворению пользовательских запросов.
