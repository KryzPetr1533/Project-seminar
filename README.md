# Project-seminar
Проект по курсу

Программа создана исключительно в академических целях.
Описание
Программа выводит статистику из корпоративных сервисов, а именно из zulip, jitsi, taiga, gitlab. На основе данных строятся графики по абсолютному значению и по его изменению. Вывод данных, которые представлена программа:
- количество сообщений в Zulip
-график bar chart c количеством сообщений по дням
  -график линейный с изменением общего количества сообщений
  -список каналов, в которых были сообщения студента
  -количество посещённых занятий в Jitsi по всем дисциплинам
  -график bar chart c количеством посещённых занятий по неделям
  -график линейный с изменением общего количества посещённых занятий по неделям
  -список комнат, которые посещал студент

  -общее количество юзерстори, созданное студентом
  -общее количество задач в юзерстори в эпике
  -линейный график роста количества задач в проекте в Taiga по неделям

  -количество коммитов студента в Git в репозитории проекта
  -график bar chart c количеством коммитов студента в Git в репозитории проекта по неделям
  -график линейный с количеством коммитов студента в Git в репозитории проекта по неделям

Технические требования
Программа написана на языке python, использует библиотеки datetime, jinja2, numpy, plotly, requests.
