from datetime import datetime

from data_trust.domain.pillars import Pillar


def register_check(
    dataset: str, pillar: Pillar, passed: bool, value: str, registered_at: datetime
) -> None:
    return None
