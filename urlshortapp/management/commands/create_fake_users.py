from django.core.management.base import BaseCommand, CommandError
from urlshortapp.models import Submitter
import lxml, requests

class Command(BaseCommand):
    help = "Creates fake users"

    def add_arguments(self, parser):
        parser.add_argument('users_number', nargs='+', type=int)

    def handle(self, *args, **options):
        if options['users_number']:
            num = int(options['users_number'][0])
            # GET DATA FOR NEW USER
            for _ in range(num):
                self.new_user()
                self.stdout.write("User added")

    def new_user(self):
        data = requests.get("https://randomuser.me/api/?format=xml")
        parser = lxml.etree.XMLParser(ns_clean=True)
        data = data.content
        tree = lxml.etree.XML(data, parser=parser, base_url=None)
        tree_results = tree.xpath("//results")[0]
        username = tree_results.find("login/username").text
        first_name = tree_results.find("name/first").text
        last_name = tree_results.find("name/last").text
        email = tree_results.find("email").text
        password = tree_results.find("login/password").text
        date_joined = tree_results.find("registered/date").text
        s = Submitter(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            date_joined=date_joined
        )
        s.save()
