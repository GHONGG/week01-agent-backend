import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def setup_logging(level: int = logging.INFO) -> None:
    """配置日志：同时输出到屏幕和文件，单文件超过 1MB 自动切割"""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(
                LOG_DIR / "app.log",
                maxBytes=1_000_000,
                backupCount=3,
                encoding="utf-8",
            ),
        ],
    )


logger = logging.getLogger("app")
