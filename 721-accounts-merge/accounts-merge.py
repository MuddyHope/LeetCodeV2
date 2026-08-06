class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = defaultdict(list)
        graph = defaultdict(set)
        for each in accounts:
            name = each[0]
            for each_email in each[1:]:
                graph[each_email].add(each[1])
                graph[each[1]].add(each_email)
                email_to_name[each_email] = name

        print(dict(email_to_name))
        print(graph)

        visited = set()
        stack = []
        res = []

        for email in graph:
            if email not in visited:
                stack = [email]
                visited.add(email)
                local_res = []

                while stack:
                    curr = stack.pop()
                    local_res.append(curr)

                    for edge in graph[curr]:
                        if edge not in visited: 
                            visited.add(edge)
                            stack.append(edge)
                                           
                res.append([email_to_name[email]] + sorted(local_res))
        return res





            

