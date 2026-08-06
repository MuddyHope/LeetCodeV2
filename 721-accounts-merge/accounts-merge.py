class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = defaultdict(set)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_to_name[email] = name
        
        seen = set()
        stack = []
        res = []

        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]

                local_res = []
                while stack:
                    curr = stack.pop()
                    local_res.append(curr)

                    for edge in graph[curr]:
                        if edge not in seen:
                            seen.add(edge)
                            stack.append(edge)
                res.append([email_to_name[email]] + sorted(local_res))
        return res
