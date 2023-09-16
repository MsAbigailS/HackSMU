from sklearn.ensemble import GradientBoostingRegressor

if __name__ == "__main__":
    LOWER_ALPHA = 0.05
    HIGHER_ALPHA = 0.95
    lower_model = GradientBoostingRegressor(loss="quantile", alpha=LOWER_ALPHA)
    middle_model = GradientBoostingRegressor(loss="ls")
    higher_model = GradientBoostingRegressor(loss="quantile", alpha=HIGHER_ALPHA)
