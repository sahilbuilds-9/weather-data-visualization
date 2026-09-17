# class student:
#     def __init__(self , name , age):
#         self.name = name 
#         self.age = age

# s1 = student("sahil", 19)
# print(s1.name)
# print(s1.age)
# ---------------------

class APIConfig:
    def __init__(self, api_key, model="Claude Opus 5", max_tokens="100K"):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.anthropic.com"


anthropic_config = APIConfig("sk-dev-key", max_tokens="50k")

prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

print(anthropic_config.model)        
print(prod_config.model)       
print(prod_config.max_tokens)  

        
        

       