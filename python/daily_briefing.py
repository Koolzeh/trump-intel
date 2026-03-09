"""
Trump Intel — Daily Briefing Generator
Runs via GitHub Actions every weekday at 07:00 BRT (10:00 UTC)
Saves output to data/briefing.json — read by the PWA on open
"""

import os
import json
import requests
from datetime import datetime

CLAUDE_KEY   = os.environ["ANTHROPIC_API_KEY"]
FINNHUB_KEY  = os.environ.get("FINNHUB_API_KEY", "")

# ── Watchlist symbols (Finnhub format) ─────────────────────────────────────
SYMBOLS = {
    "Ouro":    "OANDA:XAU_USD",
    "Prata":   "OANDA:XAG_USD",
    "Petróleo":"USOIL",
    "DXY":     "TVC:DXY",
    "MP":      "MP",
    "REMX":    "REMX",
    "LMT":     "LMT",
    "FCX":     "FCX",
    "BTC":     "BINANCE:BTCUSDT",
    "ETH":     "BINANCE:ETHUSDT",
}

def get_price(symbol: str) -> dict:
    if not FINNHUB_KEY:
        return {}
    try:
        r = requests.get(
            "https://finnhub.io/api/v1/quote",
            params={"symbol": symbol, "token": FINNHUB_KEY},
            timeout=5,
        )
        d = r.json()
        return {"price": d.get("c"), "chg": d.get("dp")}
    except Exception:
        return {}

def fmt_price(name: str, data: dict) -> str:
    if not data.get("price"):
        return f"{name}: N/A"
    chg = data.get("chg") or 0
    return f"{name}: ${data['price']:,.2f} ({chg:+.2f}%)"

def build_price_context() -> str:
    lines = []
    for name, sym in SYMBOLS.items():
        data = get_price(sym)
        lines.append(fmt_price(name, data))
    return "\n".join(lines)

def generate_briefing(price_ctx: str) -> str:
    today = datetime.now().strftime("%d/%m/%Y")
    prompt = f"""Você é um analista macro com lente geopolítica focada na Doutrina Trump.
Escreva o briefing do dia {today} em exatamente 4 blocos, máximo 130 palavras total:

📌 TEMA DO DIA: [movimento ou narrativa dominante]
🎯 ATIVO EM DESTAQUE: [1 ativo + razão objetiva]  
⚠️ VIGIAR HOJE: [1 risco ou evento a monitorar]
✅ AÇÃO: [1 decisão prática e específica]

COTAÇÕES AGORA:
{price_ctx}

CONTEXTO:
- Summit Trump-Xi: 31/mar–2/abr (MP e REMX catalisadores)
- Pausa minerais raros China expira nov/2026 (Triple Event)
- Venezuela: Doutrina Monroe 2.0 ativa (SLB/HAL serviços)
- Ouro target JP Morgan: $5.000/oz Q4/2026
- SCOTUS derrubou IEEPA; Section 232 constitucional

Responda APENAS os 4 blocos, em português, sem disclaimers."""

    r = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": CLAUDE_KEY,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        json={
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 300,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["content"][0]["text"]

def main():
    today = datetime.now().strftime("%d/%m/%Y")
    generated_at = datetime.now().isoformat()

    print(f"[{generated_at}] Buscando cotações...")
    price_ctx = build_price_context()
    print(price_ctx)

    print("\nGerando briefing com Claude Haiku...")
    text = generate_briefing(price_ctx)
    print(text)

    os.makedirs("data", exist_ok=True)
    payload = {
        "date": today,
        "generated_at": generated_at,
        "text": text,
        "prices": price_ctx,
    }
    with open("data/briefing.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Salvo em data/briefing.json ({len(text)} chars)")

if __name__ == "__main__":
    main()
