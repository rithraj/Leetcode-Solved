class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        health = 0
        armor_used = False
        for d in damage:
            if d == max_damage and not armor_used:
                armor_used = True
                if max_damage >= armor:
                    health += (d - armor)
                else:
                    health += 0
            else:
                health += d
        
        return health + 1

        