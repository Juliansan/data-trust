from datetime import datetime
from typing import Annotated

from typer import Argument, Exit, Typer, echo

from data_trust.domain.pillars import Pillar
from data_trust.services.checks import register_check
from data_trust.services.lineage import register_dependency

app = Typer()


@app.command(name="add-dependency")
def add_dependency(
    downstream: Annotated[str, Argument(help="Downstream Dataset")],
    upstream: Annotated[str, Argument(help="Upstream Dataset")],
) -> None:
    echo("Registering dependency")

    try:
        register_dependency(downstream, upstream)
        echo("Dependency Registered successfully")
    except ValueError as e:
        echo(e)
        raise Exit(code=1) from None


@app.command(name="record-check")
def record_check(
    dataset: Annotated[str, Argument(help="table or dataset name")],
    pillar: Annotated[
        Pillar, Argument(help="Type of check (freshness, completeness, accuracy, reliability)")
    ],
    passed: Annotated[bool, Argument(help="Fail or Pass")],
    value: Annotated[str, Argument(help="Measuerement value")],
    registered_at: Annotated[datetime, Argument(help="When check is recorded")],
) -> None:
    try:
        register_check(dataset, pillar, passed, value, registered_at)
        echo(f"Registering {pillar} from {dataset}")
    except ValueError as e:
        echo(e)
        raise Exit(code=1) from None
