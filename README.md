# Practice 7 · n8n demo

Публичный тестовый репозиторий для демонстрации AI-ревью пул-реквестов, классификации GitHub Issues и еженедельного дайджеста. Код и обращения в репозитории созданы для демонстрации.

## Тестовый проект

`pricing.py` вычисляет суммы и цены небольшого учебного каталога. Локальная проверка выполняется командой `python -m unittest discover -s tests`.

## 7.1 · Ревью PR

Тестовый [PR №1](https://github.com/kulakva20062/practice-7-n8n-demo/pull/1) изменяет два блока `pricing.py`.

| Запуск | Результат в GitHub | Executions |
| --- | --- | --- |
| Открытие PR | [Gemma 3 4B, два inline-комментария](https://github.com/kulakva20062/practice-7-n8n-demo/pull/1#pullrequestreview-6013026213) | [№2](evidence/review-primary.png) |
| `/make_ai_review` повторно | [Пропуск после поиска в Data Table](https://github.com/kulakva20062/practice-7-n8n-demo/pull/1#issuecomment-7081354603) | [№3](evidence/review-duplicate.png) |
| `/make_other_ai_review` | [Qwen3 8B, два inline-комментария](https://github.com/kulakva20062/practice-7-n8n-demo/pull/1#pullrequestreview-6013034157) | [№4](evidence/review-second-model.png) |

[Строки `ai_reviewed_prs`](evidence/ai_reviewed_prs.json) содержат номера PR, модели и идентификаторы опубликованных ревью.

## 7.2 · Классификация обращений

| Issue | Метка | Executions |
| --- | --- | --- |
| [№2 · Потеря копейки](https://github.com/kulakva20062/practice-7-n8n-demo/issues/2) | `bug` | [№6](evidence/issue-bug.png) |
| [№3 · Экспорт CSV](https://github.com/kulakva20062/practice-7-n8n-demo/issues/3) | `feature` | [№8](evidence/issue-feature.png) |
| [№4 · Использование subtotal](https://github.com/kulakva20062/practice-7-n8n-demo/issues/4) | `task` | [№10](evidence/issue-task.png) |
| [№5 · Расплывчатое обращение](https://github.com/kulakva20062/practice-7-n8n-demo/issues/5) | `needs-triage` без комментария | [№12](evidence/issue-needs-triage.png) |

## 7.2 · Дайджест

- [Закрытая неделя](evidence/weekly-closed-week.html) и [Execution №5](evidence/weekly-closed-week.png). GitHub API вернул нулевые значения за неделю перед созданием репозитория. В сравнении используется тестовая строка более ранней недели.
- [Предпросмотр текущей недели](evidence/weekly-demo-preview.html) и [Execution №15](evidence/weekly-demo-preview.png). Ручное окно демонстрации включает четыре Issue и один PR. В письме видны группировка по автору, Δ и AI-комментарий.
- [Строки `weekly_stats`](evidence/weekly_stats.json) включают тестовую неделю и две строки с результатами GitHub API. Сквозной прогон на учебном n8n опубликован ниже.

В тесте n8n 2.47.7 получил реальные подписанные события через GitHub CLI. Эти события поданы в сценарии как закреплённые данные для ручных Executions. Ревью, метки, комментарии и данные дайджеста прошли через реальный GitHub API. Модели запускались локально через Ollama. [Краткий экспорт Executions](evidence/executions.json)

### Подтверждение доставки через Gmail

На учебном n8n недельный workflow в одном Execution выполнил четыре поиска в GitHub, сгруппировал статистику, записал её в Data Table, рассчитал Δ, добавил AI-комментарий и отправил HTML через Gmail. Gmail вернул метки `SENT` и `INBOX`. [Сквозной Execution №7510](https://n8n-itmo.cyrweb.ru/workflow/3Aqjwd2KWrz6aLzY/executions/7510) · [Экспорт подтверждения](evidence/itmo-site-executions.json)

В отдельной первоначальной проверке Gmail есть скриншоты письма и его AI-комментария. [Execution №7432](evidence/gmail-delivery-execution.png) · [Полученный дайджест](evidence/gmail-received.png) · [AI-комментарий](evidence/gmail-received-ai-summary.png)

## 7.2 · Сверхрезультат

По Issue №2 учебный n8n создал ветку и PR №6, опубликовал AI-ревью и выполнил squash merge. GitHub подтвердил `merged=true` и закрыл Issue, а `bugfix_runs` сохранила результат. Исправление сохраняет точность и знак целой суммы в копейках. Тесты демопроекта прошли. [Issue №2](https://github.com/kulakva20062/practice-7-n8n-demo/issues/2) · [PR №6](https://github.com/kulakva20062/practice-7-n8n-demo/pull/6) · [AI-ревью перед merge](https://github.com/kulakva20062/practice-7-n8n-demo/pull/6#pullrequestreview-6014393722) · [Execution №7511](https://n8n-itmo.cyrweb.ru/workflow/BxOHzDz267mZZ5dG/executions/7511) · [Запись `bugfix_runs`](evidence/bugfix_runs.json)
