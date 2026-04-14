from loguru import logger
import sys

# Vamos botar esse logger bonitinho com cor e etc.

logger.remove()

logger.add(
    sys.stdout,
    format="<white>{time:HH:mm:ss}</white> | <level>{level: <7}</level> | <level>{message}</level>",
    colorize=True
)

log = logger
