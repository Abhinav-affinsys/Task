from pprint import pprint
import os, sys

loc = "/home/abhinav-dev/task-django/Task/task/DecisionTree"
sys.path.append(loc)
import decision_tree

user_data = {
    "location": "The Pearl",
    "device": "Apple iPhone 13",
    "age": 20,
    "location_tier": None,
    "device_tier": None,
    "recommended_cards": [],
    "recommended_loans": [],
    "recommended_packages": [],
    "recommended_privilege_banking": [],
    "recommended_deposit_accounts": [],
    "recommended_bank_accounts": [],
}

dt_loc = decision_tree.DecisionTree(loc + "/persona/location_yaml/location_rules.yml")
dt_device = decision_tree.DecisionTree(
    loc + "/persona/MobilePrices_yaml/MobilePrices_rules.yml"
)


def append_persona(dt_loc=dt_loc, dt_device=dt_device, user_data=user_data):
    decisions_loc = dt_loc.decisions
    categories_loc = [i["category"] for i in decisions_loc["users"]]
    for cat in categories_loc:
        res = dt_loc.validate_persona_for_user(
            user_data=user_data,
            persona_data={},
            decisions=decisions_loc,
            category=cat,
            persona="",
        )
        if res:
            user_data["location_tier"] = cat
            break

    decisions_device = dt_device.decisions
    categories_device = [i["category"] for i in decisions_device["users"]]
    for cat in categories_device:
        res = dt_device.validate_persona_for_user(
            user_data=user_data,
            persona_data={},
            decisions=decisions_device,
            category=cat,
            persona="",
        )
        if res:
            user_data["device_tier"] = cat
            break
    return user_data


def reco_product(user_data=user_data):
    credit_cards = decision_tree.DecisionTree(
        loc + "/persona/products_yaml/credit_cards_rules.yml"
    )
    credit_cards_dec = credit_cards.decisions
    bank_accounts = decision_tree.DecisionTree(
        loc + "/persona/products_yaml/bank_accounts_rules.yml"
    )
    bank_accounts_dec = bank_accounts.decisions
    deposit_accounts = decision_tree.DecisionTree(
        loc + "/persona/products_yaml/deposit_accounts_rules.yml"
    )
    deposit_accounts_dec = deposit_accounts.decisions
    loans = decision_tree.DecisionTree(loc + "/persona/products_yaml/loans_rules.yml")
    loans_dec = loans.decisions
    packages = decision_tree.DecisionTree(
        loc + "/persona/products_yaml/packages_rules.yml"
    )
    packages_dec = packages.decisions
    privilege_banking = decision_tree.DecisionTree(
        loc + "/persona/products_yaml/privilege_banking_rules.yml"
    )
    privilege_banking_dec = privilege_banking.decisions
    categories_cc = [i["category"] for i in credit_cards_dec["products"]]
    categories_ba = [i["category"] for i in bank_accounts_dec["products"]]
    categories_da = [i["category"] for i in deposit_accounts_dec["products"]]
    categories_loans = [i["category"] for i in loans_dec["products"]]
    categories_packages = [i["category"] for i in packages_dec["products"]]
    categories_pb = [i["category"] for i in privilege_banking_dec["products"]]

    for cat_ba in categories_ba:
        res_ba = bank_accounts.validate_user_for_product(
            user_data=user_data,
            product_data={},
            decisions=bank_accounts_dec,
            category=cat_ba,
            product="",
        )
        if res_ba:
            user_data["recommended_bank_accounts"].append(cat_ba)

    for cat_da in categories_da:
        res_da = deposit_accounts.validate_user_for_product(
            user_data=user_data,
            product_data={},
            decisions=deposit_accounts_dec,
            category=cat_da,
            product="",
        )
        if res_da:
            user_data["recommended_deposit_accounts"].append(cat_da)

    for cat_pb in categories_pb:
        res_pb = privilege_banking.validate_user_for_product(
            user_data=user_data,
            product_data={},
            decisions=privilege_banking_dec,
            category=cat_pb,
            product="",
        )
        if res_pb:
            user_data["recommended_privilege_banking"].append(cat_pb)

    for cat_loans in categories_loans:
        res_loans = loans.validate_user_for_product(
            user_data=user_data,
            product_data={},
            decisions=loans_dec,
            category=cat_loans,
            product="",
        )
        if res_loans:
            user_data["recommended_loans"].append(cat_loans)

    for cat_packages in categories_packages:
        res_packages = packages.validate_user_for_product(
            user_data=user_data,
            product_data={},
            decisions=packages_dec,
            category=cat_packages,
            product="",
        )
        if res_packages:
            user_data["recommended_packages"].append(cat_packages)

    for cat_cc in categories_cc:
        res_cc = credit_cards.validate_user_for_product(
            user_data=user_data,
            product_data={},
            decisions=credit_cards_dec,
            category=cat_cc,
            product="",
        )
        if res_cc:
            user_data["recommended_cards"].append(cat_cc)


# user_data = append_persona(dt_loc=dt_loc, dt_device=dt_device, user_data=user_data)
# reco_product()
# pprint(user_data)

# import requests
# ACCESS_KEY = 'e17a7287e39e6f67de1f234f5b188f8d'
# lat,long = (25.2656514,51.5321106)
# res = requests.get('http://api.positionstack.com/v1/reverse',
#                    params={
#                         'access_key': ACCESS_KEY,
#                         'query': f'{lat},{long}'
#                     })
# response = res.json()
# pprint(response)
