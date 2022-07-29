from numpy import save
from file_repository import FileRepository
import json
from fx_rate_utils import FxRateUtils

class FxRateRepository(FileRepository):
    utils = FxRateUtils()
    fx_rate = None
    
    def __init__(self) -> None:
        super().__init__("fx-rate.json")
    
    def get_fx_rate(self):
        if self.fx_rate == None:
            self.fx_rate = json.loads(super().readFile())
        return self.fx_rate
    
    def save(self):
        super().writeFile(json.dumps(self.fx_rate, indent=4))
        
    def add_new_fx_rate(self,fx_entry):
        fx_entry["id"] = self.utils.generateId()
        self.get_fx_rate()["currencies"].append(fx_entry)
        self.save()
        
    def update_fx_rate(self, fx_entry):
        
        result = list(filter(lambda entry: entry.get("id") == fx_entry.get("id"), self.get_fx_rate()["currencies"]))
        result[0] = fx_entry
        self.save()
    
    def delete_fx_rate(self, fx_entry):
        index = 0
        for entry in self.get_fx_rate()["currencies"]:
            if entry.get("id") == fx_entry.get("id"):
                break
            index = index + 1
            
        self.get_fx_rate()["currencies"].pop(index)
        self.save() 
    
    def find_fx_rate(self,base_curr,foreign_curr):
        # result = []
        base_curr = base_curr.lower()
        foreign_curr = foreign_curr.lower()
        
        strCompare = lambda a,b : (a.lower() == b or b == "")
        
        # for entry in self.get_fx_rate()["currencies"]:
        #     # if (entry.get("baseCurr","").lower() == base_curr or base_curr == "") and ( entry.get("foreign","").lower() == foreign_curr or foreign_curr == ""):
        #     if stringComparer(entry.get("baseCurr",""), base_curr) and stringComparer(entry.get("foreignCurr",""), foreign_curr):
        #         result.append(entry)
        result = filter(lambda entry: strCompare(entry.get("baseCurr",""), base_curr) and strCompare(entry.get("foreign",""), foreign_curr),
                        self.get_fx_rate()["currencies"])
        return list(result)