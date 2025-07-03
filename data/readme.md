# Home Credit Default Risk Prediction

This repository contains resources for the Home Credit Default Risk Kaggle competition. The goal is to predict whether a client will default on their loan based on various financial and personal information.

**You can access the full dataset directly on Kaggle here:** [Home Credit Default Risk Kaggle Competition](https://www.kaggle.com/competitions/home-credit-default-risk)

## Dataset Description

This dataset provides a rich collection of information designed to help predict loan repayment abilities. It's structured across several interconnected tables, each offering a unique perspective on applicant behavior and financial history.

---

### `application_{train|test}.csv`

This is the **core table** of the dataset, split into two files: `application_train.csv` and `application_test.csv`. Each row in these files represents a **single loan application** and contains static information about that application. The key difference is that `application_train.csv` includes the **`TARGET` variable**, which indicates whether the loan was repaid (0) or defaulted (1), making it the primary file for model training. `application_test.csv` lacks this `TARGET` variable and is used for making predictions. This table serves as the central hub, linking to all other related data through unique identifiers.

---

### `bureau.csv`

This table provides a comprehensive record of a client's **past credit history from other financial institutions**, as reported to the Credit Bureau. For every loan application in our main sample (`application_{train|test}.csv`), there are multiple rows in `bureau.csv`, with each row detailing a separate previous credit the client held **prior to their application date**. This allows for an in-depth analysis of a client's historical borrowing and repayment behavior across various lenders.

---

### `bureau_balance.csv`

Delving deeper into the `bureau.csv` data, `bureau_balance.csv` offers **monthly snapshots of the balances** for each previous credit reported to the Credit Bureau. Imagine tracking the monthly financial health of every past loan a client had; that's what this table provides. It's a highly granular dataset, with the number of rows being a product of the number of loans in our sample, the number of previous credits per client, and the number of months for which historical data is available for each credit. This table is crucial for understanding the **dynamic evolution of a client's external credit obligations**.

---

### `POS_CASH_balance.csv`

This table specifically tracks **monthly balance snapshots of previous Point-of-Sale (POS) and cash loans** that the applicant obtained directly from **Home Credit**. Similar to `bureau_balance.csv`, it provides a time-series view of these specific loan types. Each row captures a month's history for a previous Home Credit loan, resulting in a large table that reflects the intricate monthly payment and balance changes for these in-house loans. It's invaluable for understanding a client's past relationship with Home Credit regarding these particular loan products.

---

### `credit_card_balance.csv`

Focusing on another in-house product, `credit_card_balance.csv` presents **monthly balance snapshots of previous credit cards** the applicant held with **Home Credit**. Just like the POS and cash loan balances, this table offers a detailed, month-by-month history of credit card usage, payments, and outstanding balances. Its structure mirrors that of `POS_CASH_balance.csv`, providing granular insights into a client's historical credit card activity with Home Credit, including their spending patterns and repayment regularity.

---

### `previous_application.csv`

This table aggregates information on **all past applications for Home Credit loans** made by clients who are present in our main `application_{train|test}.csv` sample. Each row represents a distinct previous application, regardless of whether it was approved or rejected. This data is vital for understanding a client's past interactions with Home Credit, including their application history, the types of loans they sought, and the outcomes of those applications. It offers a rich historical context for their current application.

---

### `installments_payments.csv`

Providing a detailed **repayment history** for previously disbursed Home Credit loans (those found in `previous_application.csv`), this table captures every payment event. It includes **one row for every payment made** and, importantly, **one row for every missed payment**. This granular view allows for a precise analysis of a client's repayment discipline and reliability for past Home Credit credits. Each row corresponds to a single installment payment or a missed installment, making it a critical resource for assessing a client's historical payment behavior.

---

### `HomeCredit_columns_description.csv`

This helpful auxiliary file serves as a **data dictionary**, providing clear and concise **descriptions for all columns** across the various data tables. It's an essential resource for anyone working with the dataset, ensuring a thorough understanding of each variable's meaning and context.

---

## Data Schema

Below is an image illustrating the relationships and structure of the various tables in this dataset. This visual representation can help in understanding how different pieces of information are connected.

![Data Schema](home_credit_image.png)

---
