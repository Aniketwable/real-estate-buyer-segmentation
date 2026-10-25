# Real Estate Buyer Segmentation (K = 7)

Streamlit dashboard for the final seven buyer segments.

## Run locally
1. Install Python 3.10+.
2. In this folder, run `pip install -r requirements.txt`.
3. Run `streamlit run app.py`.

## Deploy
Upload `app.py`, `requirements.txt`, and `README.md` to your GitHub repository. In Streamlit Community Cloud, create a new app, choose the repository and branch, and set the main file path to `app.py`.

## Notes
The segment summary reproduces the results shared during project development and was not independently recalculated from the original datasets. Reported silhouette score: 0.289, indicating modest cluster separation. Confirm the currency/unit of purchase values from the source dataset.
