code = """
x = 5
y = 10
result = x + y
print(result)
"""

# Executa o código da string 'code' em um namespace vazio
namespace = {}
exec(code, {}, namespace)
