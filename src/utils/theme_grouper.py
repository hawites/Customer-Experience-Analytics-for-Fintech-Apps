class ThemeGrouper:
    def __init__(self):
        self.themes = {
            "Access Issues": ["login", "access", "credentials", "reset", "password"],
            "Performance": ["slow", "crash", "lag", "freeze", "delay"],
            "User Interface": ["design", "ui", "ux", "navigation", "interface"],
            "Customer Support": ["help", "support", "response", "service"],
            "Features": ["statement", "transfer", "balance", "alert", "transaction"]
        }

    def assign_theme(self, review_text):
        review = review_text.lower()
        matched = []
        for theme, keywords in self.themes.items():
            if any(word in review for word in keywords):
                matched.append(theme)
        return ', '.join(matched) if matched else "Other"
