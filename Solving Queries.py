class Solution:
    def Query(self, dict, query):
        
        for i in query:
            
            if i in dict:
                print(dict.get(i))
                
            else:
                print("None")