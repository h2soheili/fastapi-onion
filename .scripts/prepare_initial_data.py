def init() -> None:
    print('...')
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    #
    #
    #


if __name__ == "__main__":
    init()
