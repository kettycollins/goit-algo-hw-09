# Завдання 9

У цьому репозиторії містяться два алгоритми для визначення оптимального способу видати решту покупцеві: жадібний алгоритм (`find_coins_greedy`) та алгоритм динамічного програмування (`find_min_coins`).

## Жадібний алгоритм (find_coins_greedy)

Функція `find_coins_greedy` приймає на вхід суму та повертає словник, що представляє кількість монет кожного номіналу, необхідних для утворення цієї суми. Алгоритм є жадібним, вибираючи найбільші доступні номінали монет першими.

**Результат жадібного алгоритму** {50: 2, 10: 1, 2: 1, 1: 1}, час: 0.055460542

## Алгоритм динамічного програмування (find_min_coins)

Функція `find_coins_dyn` також приймає на вхід суму та повертає словник, що представляє кількість монет кожного номіналу, необхідних для утворення цієї суми. Цей алгоритм використовує динамічне програмування для знаходження мінімальної кількості монет.

**Результат динамічного програмування** {50: 2, 10: 1, 2: 1, 1: 1}, час: 5.56401225

## Висновки

В обох випадках алгоритми успішно визначають оптимальний спосіб видати решту, проте ефективність їхньої роботи різниться.

**Жадібний алгоритм:**
- *Переваги:* Швидкий та простий у реалізації.
- *Недоліки:* Може не завжди гарантувати мінімальну кількість монет. В даному випадку, він працює ефективно з невеликими сумами, але може не бути оптимальним для великих сум.

**Алгоритм динамічного програмування:**
- *Переваги:* Гарантує мінімальну кількість монет.
- *Недоліки:* Вимагає більше обчислювальних ресурсів, що може призвести до збільшення часу виконання, особливо при великих сумах.

Висновок полягає в тому, що вибір між цими алгоритмами залежить від конкретних вимог системи. Жадібний алгоритм може бути вибраний, якщо пріоритет - швидкість виконання, і точність не є критичною. З іншого боку, якщо важлива мінімальна кількість монет, алгоритм динамічного програмування буде більш підходящим, навіть за рахунок більшого часу виконання при великих сумах.
