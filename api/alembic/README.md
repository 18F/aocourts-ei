# Database schema migrations use Alembic

### Basic Use

Database migrations allow the state of the database schema to be tracked in version control and make it easier for developers to work together. Each change in the database is represented by a file in `./versions` which provide code to move the database to a new state and also reverse the change. 

To start a new migration, call it with `revision` and provide a name:

```
alembic revision  -m "add_roles"
```

This creates a new file in `./versions` and links it to the previous versions.

**Inspect this file!!**  Make sure it does what you want it to. The `downgrade()` function should return the database back to the state before this migration ran. If you are satisfied, bring the database up-to-date by running the migration:

```
alembic upgrade head
```

To step backward one steop through the migrations:

```
alembic downgrade -1
```

For more datails, see the [Alembic Documentaion](https://alembic.sqlalchemy.org/en/latest/index.html)
