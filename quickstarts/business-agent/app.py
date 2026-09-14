from agent import run_analysis


if __name__ == "__main__":
    for business_id in ("demo-shop", "loss-case", "missing"):
        print(run_analysis(business_id))
