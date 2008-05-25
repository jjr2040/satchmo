from django.core.management.base import NoArgsCommand
import os
import shutil

class Command(NoArgsCommand):
    help = "Copy the satchmo static directory and files to the local project."

    def handle_noargs(self, **options):
        import satchmo
        static_src = os.path.join(satchmo.__path__[0],'static')
        static_dest = os.path.join(os.getcwd(), 'static')
        if os.path.exists(static_dest):
            print "Static directory exists. You must manually copy the files you need."
        else:
            shutil.copytree(static_src, static_dest)
            shutil.rmtree(os.path.join(static_dest,'.svn'), True)
            print "Copied %s to %s" % (static_src, static_dest)
