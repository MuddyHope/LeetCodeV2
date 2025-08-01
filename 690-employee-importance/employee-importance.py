"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_map = {}
        for each in employees:
            employees_map[each.id] = each
    
        return self.recursive(employees_map, id)


        
    def recursive(self, employee_map, id):
        
        if not employee_map.get(id):
            return 0
        
        _idx = employee_map.get(id)
        total_val = _idx.importance

        for each_sub in _idx.subordinates:
            total_val += self.recursive(employee_map, each_sub)

        return total_val
        
            