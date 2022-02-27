from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq_email_list = set()
        for email in emails:
            local_name, domain_name = email.split('@')

            if local_name.find('+') > 0:
                local_name = local_name.split('+')[0]
            if local_name.find('.') > 0:

                local_name_arr = local_name.split('.')
                local_name = ''.join(local_name_arr)

            entry = local_name + '@' + domain_name
            uniq_email_list.add(entry)
        return len(uniq_email_list)