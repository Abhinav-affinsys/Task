To run the django system, change directory to Task and run python3 manage.py run server
Go to http://127.0.0.1:8000/admin/ and changing values to send update message or create new record for new customer message.
More detail is provided in document
To run the ml-model ,got to reco task and run reco.py,currently the system uses dataframe rows for prediction for testing purposes but it can updated to use custome user entry
```bash
.
├── README.md
├── reco-task
│   ├── Model_Performance.xlsx
│   ├── Models_cards
│   │   ├── Model_'All Miles Credit Card'.sav
│   │   ├── Model_ 'Bankbuddy Women Credit Card'.sav
│   │   ├── Model_'Bankbuddy Women Credit Card'.sav
│   │   ├── Model_ 'Best Price Save Max Credit Card'.sav
│   │   ├── Model_'Best Price Save Max Credit Card'.sav
│   │   ├── Model_ 'Best Price Save Smart Credit Card'.sav
│   │   ├── Model_'Best Price Save Smart Credit Card'.sav
│   │   ├── Model_ 'Corporate Premium Credit Card'.sav
│   │   ├── Model_'Corporate Premium Credit Card'.sav
│   │   ├── Model_ 'Costco BankBuddy Credit Card'.sav
│   │   ├── Model_'Costco BankBuddy Credit Card'.sav
│   │   ├── Model_ 'Diners Club Black Credit Card'.sav
│   │   ├── Model_'Diners Club Black Credit Card'.sav
│   │   ├── Model_ 'Diners ClubMiles Credit Card'.sav
│   │   ├── Model_'Diners ClubMiles Credit Card'.sav
│   │   ├── Model_ 'Diners Club Premium Credit Card'.sav
│   │   ├── Model_'Diners Club Premium Credit Card'.sav
│   │   ├── Model_ 'Diners Club Privilege Credit Card'.sav
│   │   ├── Model_'Diners Club Privilege Credit Card'.sav
│   │   ├── Model_ 'Diners Club Rewardz Credit Card'.sav
│   │   ├── Model_'Diners Club Rewardz Credit Card'.sav
│   │   ├── Model_ 'EasyEMI Card'.sav
│   │   ├── Model_'EasyEMI Card'.sav
│   │   ├── Model_ 'Emirates BankBuddy Bank Platinum'.sav
│   │   ├── Model_'Emirates BankBuddy Bank Platinum'.sav
│   │   ├── Model_ 'Emirates BankBuddy Bank Select Titanium'.sav
│   │   ├── Model_'Emirates BankBuddy Bank Select Titanium'.sav
│   │   ├── Model_ 'Freedom Credit Card'.sav
│   │   ├── Model_'Freedom Credit Card'.sav
│   │   ├── Model_ 'Infinite Credit Card'.sav
│   │   ├── Model_'Infinite Credit Card'.sav
│   │   ├── Model_ 'MoneyBack Credit Card'.sav
│   │   ├── Model_'MoneyBack Credit Card'.sav
│   │   ├── Model_ 'SouthWest BankBuddy Bank Credit Card'.sav
│   │   ├── Model_'SouthWest BankBuddy Bank Credit Card'.sav
│   │   ├── Model_ 'Superia Credit Card'.sav
│   │   ├── Model_'Superia Credit Card'.sav
│   │   ├── Model_ 'Total BankBuddy Bank Credit Card'.sav
│   │   ├── Model_'Total BankBuddy Bank Credit Card'.sav
│   │   ├── Model_ 'Uber BankBuddy Credit Card'.sav
│   │   ├── Model_ 'Visa Signature Credit Card'.sav
│   │   ├── Model_'Visa Signature Credit Card'.sav
│   │   ├── Model_ 'Walmart BankBuddy Signature'.sav
│   │   └── Model_'Walmart BankBuddy Signature'.sav
│   ├── reco.ipynb
│   ├── reco.py
│   ├── requirements.txt
│   ├── stanbic.csv
│   ├── test.csv
│   └── test.txt
└── Task
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── task
    │   ├── admin.py
    │   ├── apps.py
    │   ├── DecisionTree
    │   │   ├── decision_tree.py
    │   │   ├── persona
    │   │   │   ├── hnw.yml
    │   │   │   ├── location_yaml
    │   │   │   │   ├── location_rules.yml
    │   │   │   │   └── restrictions
    │   │   │   │       ├── Location_Tier1.yml
    │   │   │   │       ├── Location_Tier2.yml
    │   │   │   │       ├── Location_Tier3.yml
    │   │   │   │       ├── Location_Tier4.yml
    │   │   │   │       ├── Location_Tier5.yml
    │   │   │   │       └── Location_Tier6.yml
    │   │   │   ├── MobilePrices_yaml
    │   │   │   │   ├── MobilePrices_rules.yml
    │   │   │   │   └── restrictions
    │   │   │   │       ├── MobilePrices_Tier1.yml
    │   │   │   │       ├── MobilePrices_Tier2.yml
    │   │   │   │       ├── MobilePrices_Tier3.yml
    │   │   │   │       ├── MobilePrices_Tier4.yml
    │   │   │   │       ├── MobilePrices_Tier5.yml
    │   │   │   │       └── MobilePrices_Tier6.yml
    │   │   │   ├── products_yaml
    │   │   │   │   ├── bank_accounts_rules.yml
    │   │   │   │   ├── credit_cards_rules.yml
    │   │   │   │   ├── deposit_accounts_rules.yml
    │   │   │   │   ├── loans_rules.yml
    │   │   │   │   ├── packages_rules.yml
    │   │   │   │   ├── privilege_banking_rules.yml
    │   │   │   │   ├── products_rules.yml
    │   │   │   │   └── restrictions
    │   │   │   │       ├── bank_accounts
    │   │   │   │       │   ├── bafe
    │   │   │   │       │   │   ├── device_bafe.yml
    │   │   │   │       │   │   └── location_bafe.yml
    │   │   │   │       │   ├── currents_acc
    │   │   │   │       │   │   ├── device_ca.yml
    │   │   │   │       │   │   └── location_ca.yml
    │   │   │   │       │   ├── muba
    │   │   │   │       │   │   ├── device_muba.yml
    │   │   │   │       │   │   └── location_muba.yml
    │   │   │   │       │   └── savings_acc
    │   │   │   │       │       ├── device_sa.yml
    │   │   │   │       │       └── location_sa.yml
    │   │   │   │       ├── credit_cards
    │   │   │   │       │   ├── ccc
    │   │   │   │       │   │   ├── device_ccc.yml
    │   │   │   │       │   │   └── location_ccc.yml
    │   │   │   │       │   ├── mucc
    │   │   │   │       │   │   ├── device_mucc.yml
    │   │   │   │       │   │   └── location_mucc.yml
    │   │   │   │       │   ├── pcc
    │   │   │   │       │   │   ├── device_pcc.yml
    │   │   │   │       │   │   └── location_pcc.yml
    │   │   │   │       │   ├── scc
    │   │   │   │       │   │   ├── device_scc.yml
    │   │   │   │       │   │   └── location_scc.yml
    │   │   │   │       │   └── tcc
    │   │   │   │       │       ├── device_tcc.yml
    │   │   │   │       │       └── location_tcc.yml
    │   │   │   │       ├── deposit_accounts
    │   │   │   │       │   ├── call_account
    │   │   │   │       │   │   ├── device_ca.yml
    │   │   │   │       │   │   └── location_ca.yml
    │   │   │   │       │   ├── ebs
    │   │   │   │       │   │   ├── device_ebs.yml
    │   │   │   │       │   │   └── location_ebs.yml
    │   │   │   │       │   ├── regular_saver
    │   │   │   │       │   │   ├── device_rs.yml
    │   │   │   │       │   │   └── location_rs.yml
    │   │   │   │       │   └── time_deposit
    │   │   │   │       │       ├── device_td.yml
    │   │   │   │       │       └── location_td.yml
    │   │   │   │       ├── loans
    │   │   │   │       │   ├── car_loans
    │   │   │   │       │   │   ├── device_cl.yml
    │   │   │   │       │   │   └── location_cl.yml
    │   │   │   │       │   ├── fnl
    │   │   │   │       │   │   ├── device_fnl.yml
    │   │   │   │       │   │   └── location_fnl.yml
    │   │   │   │       │   ├── home_loans
    │   │   │   │       │   │   ├── device_ml.yml
    │   │   │   │       │   │   └── location_ml.yml
    │   │   │   │       │   └── personal_loan
    │   │   │   │       │       ├── device_pl.yml
    │   │   │   │       │       └── location_pl.yml
    │   │   │   │       ├── packages
    │   │   │   │       │   ├── mastercard_tdcc
    │   │   │   │       │   │   ├── device_tdcc.yml
    │   │   │   │       │   │   └── location_tdcc.yml
    │   │   │   │       │   ├── vc
    │   │   │   │       │   │   ├── device_vc.yml
    │   │   │   │       │   │   └── location_vc.yml
    │   │   │   │       │   ├── visa_idcc
    │   │   │   │       │   │   ├── device_idcc.yml
    │   │   │   │       │   │   └── location_idcc.yml
    │   │   │   │       │   └── visa_pdcc
    │   │   │   │       │       ├── device_pdcc.yml
    │   │   │   │       │       └── location_pdcc.yml
    │   │   │   │       └── privilege_banking
    │   │   │   │           ├── private_banking
    │   │   │   │           │   ├── device_pb.yml
    │   │   │   │           │   └── location_pb.yml
    │   │   │   │           └── sadara_banking
    │   │   │   │               ├── device_sb.yml
    │   │   │   │               └── location_sb.yml
    │   │   │   ├── __pycache__
    │   │   │   │   └── main.cpython-39.pyc
    │   │   │   ├── reco.py
    │   │   │   └── rules.yml
    │   │   └── __pycache__
    │   │       ├── decision_tree.cpython-310.pyc
    │   │       └── decision_tree.cpython-39.pyc
    │   ├── __init__.py
    │   ├── main.py
    │   ├── migrations
    │   │   ├── 0001_initial.py
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       ├── 0001_initial.cpython-310.pyc
    │   │       └── __init__.cpython-310.pyc
    │   ├── models.py
    │   ├── __pycache__
    │   │   ├── admin.cpython-310.pyc
    │   │   ├── apps.cpython-310.pyc
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── main.cpython-310.pyc
    │   │   ├── models.cpython-310.pyc
    │   │   ├── serializers.cpython-310.pyc
    │   │   ├── urls.cpython-310.pyc
    │   │   └── views.cpython-310.pyc
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── Task
        ├── asgi.py
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-310.pyc
        │   ├── settings.cpython-310.pyc
        │   ├── urls.cpython-310.pyc
        │   └── wsgi.cpython-310.pyc
        ├── settings.py
        ├── urls.py
        └── wsgi.py

48 directories, 159 files
```