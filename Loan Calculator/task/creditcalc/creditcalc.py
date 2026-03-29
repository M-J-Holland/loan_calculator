import argparse
import math


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--principal", type=float)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    return parser.parse_args()


def format_periods(months):
    years = months // 12
    months_remaining = months % 12
    parts = []
    if years > 0:
        parts.append(f"{years} year{'s' if years > 1 else ''}")
    if months_remaining > 0:
        parts.append(f"{months_remaining} month{'s' if months_remaining > 1 else ''}")
    return " and ".join(parts)


def is_invalid(args):
    if args.type not in {"annuity", "diff"}:
        return True

    if args.interest is None:
        return True

    if any(
        value is not None and value < 0
        for value in [args.principal, args.payment, args.periods, args.interest]
    ):
        return True

    provided = sum(
        value is not None
        for value in [args.type, args.principal, args.payment, args.periods, args.interest]
    )
    if provided < 4:
        return True

    if args.type == "diff" and args.payment is not None:
        return True

    if args.type == "diff" and (args.principal is None or args.periods is None):
        return True

    if args.type == "annuity" and [args.principal, args.payment, args.periods].count(None) != 1:
        return True

    return False


def calculate_diff(principal, periods, interest):
    i = interest / (12 * 100)
    total = 0
    for month in range(1, periods + 1):
        payment = math.ceil(principal / periods + i * (principal - principal * (month - 1) / periods))
        total += payment
        print(f"Month {month}: payment is {payment}")
    print()
    print(f"Overpayment = {int(total - principal)}")


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    payment = math.ceil(principal * i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    overpayment = payment * periods - principal
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {int(overpayment)}")


def calculate_annuity_principal(payment, periods, interest):
    i = interest / (12 * 100)
    principal = payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    principal = math.floor(principal)
    overpayment = payment * periods - principal
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {int(overpayment)}")


def calculate_annuity_periods(principal, payment, interest):
    i = interest / (12 * 100)
    periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    overpayment = payment * periods - principal
    print(f"It will take {format_periods(periods)} to repay this loan!")
    print(f"Overpayment = {int(overpayment)}")


args = parse_args()

if is_invalid(args):
    print("Incorrect parameters")
else:
    if args.type == "diff":
        calculate_diff(args.principal, args.periods, args.interest)
    elif args.payment is None:
        calculate_annuity_payment(args.principal, args.periods, args.interest)
    elif args.principal is None:
        calculate_annuity_principal(args.payment, args.periods, args.interest)
    else:
        calculate_annuity_periods(args.principal, args.payment, args.interest)