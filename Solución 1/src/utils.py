import logging

def setup_logger():
    logging.basicConfig(
        filename="data/logs/etl.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
