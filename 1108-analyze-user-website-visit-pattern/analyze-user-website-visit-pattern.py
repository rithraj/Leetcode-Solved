class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: Combine and sort visits by timestamp
        visits = []
        for i in range(len(username)):
            visits.append([timestamp[i], username[i], website[i]])
        visits.sort()

        # Step 2: Build a user -> ordered list of websites
        users = {}
        for time, user, site in visits:
            if user not in users:
                users[user] = []
            users[user].append(site)

        # Step 3: Helper to generate all ordered 3-sequences for a user
        def generate_sequences(websites):
            result = set()

            def backtrack(start, path):
                if len(path) == 3:
                    result.add(tuple(path))
                    return
                for i in range(start, len(websites)):
                    path.append(websites[i])
                    backtrack(i + 1, path)
                    path.pop()

            backtrack(0, [])
            return result

        # Step 4: Global pattern count
        pattern_count = {}
        for user, sites in users.items():
            seen = generate_sequences(sites)
            for seq in seen:
                if seq not in pattern_count:
                    pattern_count[seq] = 1
                else:
                    pattern_count[seq] += 1

        # Step 5: Find pattern with highest frequency (and lex smallest if tie)
        max_count = 0
        answer = None
        for pattern in pattern_count:
            count = pattern_count[pattern]
            if count > max_count or (count == max_count and pattern < answer):
                max_count = count
                answer = pattern

        return list(answer)
