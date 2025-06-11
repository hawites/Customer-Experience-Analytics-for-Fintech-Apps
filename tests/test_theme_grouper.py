import pandas as pd
from src.utils.theme_grouper import ThemeGrouper

def test_theme_assignment():
    grouper = ThemeGrouper()
    df = pd.DataFrame({"review": ["Login failed", "Transfer is too slow"]})
    df["theme"] = grouper.assign_theme(df["review"])
    assert "theme" in df.columns
    assert all(isinstance(val, str) for val in df["theme"])