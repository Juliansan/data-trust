def register_dependency(downstream: str, upstream: str) -> None:

    if downstream == upstream:
        raise ValueError("Dependency could not be registered")
