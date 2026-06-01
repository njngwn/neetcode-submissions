class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_sets = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "") # everything after the first plus sign will be ignored
            email_sets.add(local+domain)

        return len(email_sets)
