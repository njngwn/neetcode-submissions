class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_sets = set()

        for email in emails:
            local_name = email.split("@")[0].split("+")[0].replace(".", "") # everything after the first plus sign will be ignored
            domain_name = email.split("@")[1]
            email_sets.add(local_name + domain_name)

        return len(email_sets)
