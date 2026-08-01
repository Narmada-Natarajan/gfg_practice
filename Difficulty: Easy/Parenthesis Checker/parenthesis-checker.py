class Solution:
    def isBalanced(self, s):
        # code here
        
        st=[]
        
        for ch in s:
            if (ch=="(" or ch=="{" or ch=="["): #opening brackets
                st.append(ch)
            else:
                if len(st)==0: #stack empty
                    return False
                    
                top=st.pop()
                if(ch ==")" and top != "(")or(ch =="}" and top != "{")or(ch =="]" and top != "["):
                    return False 
        
        
        
        return len(st)==0
        

                
            
        