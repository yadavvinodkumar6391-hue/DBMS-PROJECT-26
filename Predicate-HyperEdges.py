def add_predicate_hyperedge(
    hp,
    reader,
    writer,
    predicate
):

    hp.add_edge(
        reader,
        writer,
        f"PH:{predicate}"
    )
