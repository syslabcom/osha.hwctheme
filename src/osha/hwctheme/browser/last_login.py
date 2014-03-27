from Products.Five import BrowserView
from plone import api
from StringIO import StringIO
import csv


class LastLoginView(BrowserView):
    """@@last-login lists the last time users logged in

    ?all can be specified to include all users, which uses "Never" in the
    timestamp column for users who have never logged in. By default
    @@last-login looks for a list of users to include in
    portal_properties.site_properties.last_login_users which can be added
    manually via the ZMI.
    """
    def __call__(self):
        llt = api.portal.get_tool("loginlockout_tool")
        pmt = api.portal.get_tool("portal_membership")
        if "all" in self.request.form:
            all_users = pmt.listMemberIds()
        else:
            portal = api.portal.get()
            all_users = getattr(
                portal.portal_properties.site_properties,
                "last_login_users",
                [],
            )
        successful_attempts = llt.listSuccessfulAttempts()
        most_recent_attempts = {}
        for attempt in successful_attempts:
            username = attempt["username"]
            date = attempt["attempts"][-1]["last"]
            most_recent_attempts[username] = date
        for user in all_users:
            if user not in most_recent_attempts.keys():
                most_recent_attempts[user] = "Never"
        csvfile = StringIO()
        writer = csv.DictWriter(csvfile, fieldnames=["user", "last_login"])
        for user in most_recent_attempts:
            writer.writerow({
                "user": user,
                "last_login": most_recent_attempts[user],
            })
        return csvfile.getvalue()
