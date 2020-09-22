# Handling-View

`View` являются блокирующими менеджерами хендлеров. Если `process_event` у view вернул `True` то другие `view` уже не будут проверяются

Процедура поиска view обрабатывающего ивент проста:

Сначала обрабатывается `process_view` который должен вернуть `boolean`-значение. Если вернулось True то поиск view прекращается и вызывается handle_event который отвечает за подбор хендлера

Во View рекомендуются 2 аттрибута:

* **handlers** - список из ABCHandler
* **middlewares** - список из BaseMiddleware

Эти аттрибуты впоследствии рекомендуется использовать в handle_event для запуска мидлварей и поиска хендлера

## register_middleware(BaseMiddleware)

Добавляет мидлварь в `view.middlewares`