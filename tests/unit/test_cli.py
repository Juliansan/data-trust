from typer.testing import CliRunner

from data_trust.entrypoints import cli

runner = CliRunner()


def test_add_dependency_registers_child_and_parent() -> None:
    result = runner.invoke(cli.app, ["add-dependency", "orders", "core_orders"])

    assert result.exit_code == 0
    assert result.output == "Registering dependency\nDependency Registered successfully\n"


def test_add_dependency_reports_registration_error() -> None:
    result = runner.invoke(cli.app, ["add-dependency", "orders", "orders"])

    assert result.exit_code == 1
    assert result.output == "Registering dependency\nDependency could not be registered\n"


def test_record_check_registers_data_check() -> None:
    result = runner.invoke(
        cli.app,
        [
            "record-check",
            "orders",
            "freshness",
            "true",
            "24h",
            "2026-06-27T10:15:00",
        ],
    )

    assert result.exit_code == 0
    assert result.output == "Registering freshness from orders\n"


def test_record_check_requires_arguments() -> None:
    result = runner.invoke(cli.app, ["record-check"])

    assert result.exit_code == 2
    assert "Missing argument" in result.output


def test_help_lists_available_commands() -> None:
    result = runner.invoke(cli.app, ["--help"])

    assert result.exit_code == 0
    assert "add-dependency" in result.output
    assert "record-check" in result.output
