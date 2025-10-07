# Analytics Dashboard

Reusable analytics dashboard project scaffold (Jupyter + Panel/Plotly/Seaborn).

## Quickstart

```bash
# Create project from template
cookiecutter path/to/this/template

# cd into project
cd analytics-dashboard

# Create env (optional) and install deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Launch Jupyter
jupyter lab
```

## Structure

```
analytics-dashboard/
├── data/                      # put your datasets here (default: [5/7] dataset_main (Master Travel Data.csv): TravelData.csv)
├── notebooks/
│   └── travel_analytics_dashboard.ipynb
├── src/analytics-dashboard/
│   ├── __init__.py
│   └── utils.py
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Notes

- This starter targets **Jupyter notebooks** using **panel** stack (Panel/Plotly/Seaborn).
- Replace sample paths with your real dataset names (default is [5/7] dataset_main (Master Travel Data.csv): TravelData.csv).
