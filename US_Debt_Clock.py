# US Debt Clock
import requests
import time
import sys
from datetime import datetime, timedelta

def green(text: str) -> str:
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

def fetch_debt():
    base_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny"

    latest_response = requests.get(f"{base_url}?sort=-record_date&page[size]=1")
    latest_response.raise_for_status()
    latest_record = latest_response.json()["data"][0]

    latest_debt = float(latest_record["tot_pub_debt_out_amt"])
    latest_date = datetime.strptime(latest_record["record_date"], "%Y-%m-%d")

    one_year_ago = latest_date - timedelta(days=365)
    year_response = requests.get(
        f"{base_url}?filter=record_date:gte:{one_year_ago:%Y-%m-%d}&sort=record_date"
    )
    year_response.raise_for_status()

    records = year_response.json()["data"]
    total_increase = 0

    for i in range(1, len(records)):
        total_increase += (
            float(records[i]["tot_pub_debt_out_amt"])
            - float(records[i - 1]["tot_pub_debt_out_amt"])
        )

    avg_daily_increase = total_increase / (len(records) - 1)
    per_second = avg_daily_increase / 86400

    elapsed_days = (datetime.now() - latest_date).total_seconds() / 86400
    estimated_debt = latest_debt + (avg_daily_increase * elapsed_days)

    return estimated_debt, per_second

def confirm_exit() -> bool:
    """Prompt user to confirm exit. Returns True if they want to exit."""
    while True:
        choice = input(green("\nExit U.S. Debt Clock? (y/n): "))
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False

def main():
    debt, per_second = fetch_debt()

    sys.stdout.write("\033[2J\033[H")  # Clear screen

    while True:
        try:
            debt += per_second

            output = (
                "U.S. NATIONAL DEBT (Estimated, Live)\n"
                "----------------------------------\n"
                f"${debt:,.2f}\n"
                f"Increasing ≈ ${per_second:,.2f} per second\n"
                "\nPress Ctrl+C to exit\n"
            )

            sys.stdout.write(green(output))
            sys.stdout.flush()

            time.sleep(1)
            sys.stdout.write("\033[H")  # Move cursor to top

        except KeyboardInterrupt:
            sys.stdout.write("\n")
            if confirm_exit():
                print(green("Exiting U.S. Debt Clock..."))
                time.sleep(3)
                sys.stdout.write("\033[2J\033[H")  # Clear screen
                break
            else:
                sys.stdout.write("\033[2J\033[H")  # Clear and resume