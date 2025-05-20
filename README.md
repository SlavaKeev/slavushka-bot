# Slavushka TradingView Telegram Bot

⚡ Этот бот принимает сигналы от TradingView и отправляет их в Telegram.

## 🔧 Настройка
1. Вставь свой Telegram Bot Token и Chat ID в `main.py`
2. Задеплой через [Render.com](https://render.com)
3. Укажи Webhook URL в настройках алерта TradingView

## 📡 Webhook формат:
```
{
  "text": "🟢 BUY по XAUUSD (1H) — EMA пересеклась вверх + MACD подтверждает"
}
```