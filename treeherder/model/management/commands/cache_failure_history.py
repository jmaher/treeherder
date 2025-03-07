import datetime

from django.core.management.base import BaseCommand

from treeherder.model.models import OptionCollection
from treeherder.push_health.tests import (
    CACHE_KEY_ROOT,
    fixed_by_commit_history_days,
    get_history,
    intermittent_history_days,
)
from treeherder.webapp.api.utils import REPO_GROUPS


class Command(BaseCommand):
    # TODO: This command will go away when we migrate to mozci for our backend (Bug 1626746).  But fixing for now.
    help = """Caches history of intermittent and fixed_by_commit failure lines"""

    def add_arguments(self, parser):
        parser.add_argument(
            "--debug",
            action="store_true",
            dest="debug",
            default=False,
            help="Write debug messages to stdout",
        )
        parser.add_argument(
            "--days",
            action="store",
            dest="days",
            default=5,
            type=int,
            help="Number of history sets to store (one for each day prior to today)",
        )

    def handle(self, *args, **options):
        self.is_debug = options["debug"]
        days = options["days"]

        self.debug(f"Fetching {days} sets of history...")

        option_map = OptionCollection.objects.get_option_collection_map()
        repository_ids = REPO_GROUPS["trunk"]
        for day in range(days):
            push_date = datetime.datetime.now().date() - datetime.timedelta(days=day)

            get_history(4, push_date, intermittent_history_days, option_map, repository_ids, True)

            self.debug(f"Cached failure history for {CACHE_KEY_ROOT}:{4}:{push_date}")

            get_history(
                2, push_date, fixed_by_commit_history_days, option_map, repository_ids, True
            )

            self.debug(f"Cached failure history for {CACHE_KEY_ROOT}:{2}:{push_date}")

    def debug(self, msg):
        if self.is_debug:
            self.stdout.write(msg)
