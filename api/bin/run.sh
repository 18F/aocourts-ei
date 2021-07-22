#/bin/bash

set -o errexit
set -o pipefail

alembic upgrade head
python -m app.main