# AAI-test

<div align="center">
    <img src="https://github.com/rhamdansyahrulm/AAI-test/assets/141615487/f3ee3d59-f649-4ec7-9c4b-0f8cd631eca3" alt="Ecuador's Store Dashboard" width="45%">
    <img src="https://github.com/rhamdansyahrulm/AAI-test/assets/141615487/11e0e600-0ff7-4ece-adbe-c3cd17ccfd80" alt="Ecuador's Store Dashboard" width="45%">
  </a>
</div>

This project provides a Streamlit dashboard for data visualization using pandas, matplotlib, and altair. The data used in this dashboard is sourced from a BigQuery table.

## Prerequisites

Before running the Streamlit dashboard, make sure you have the following libraries installed:

- pandas
- google-cloud-bigquery
- matplotlib
- altair
- streamlit

```bash
pip install pandas google-cloud-bigquery matplotlib altair streamlit
```

## Getting Started

1. Clone the Repository:

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```
2. Download Service Account Key:

- Download the service account key file (JSON) for accessing Google Cloud services.
- Save the key file as service_account_key.json in the root folder.

3. Run the Streamlit App:

- Open your terminal and navigate to the project's root folder.
- Run the Streamlit app using the following command:
```bash
streamlit run main.py
```
