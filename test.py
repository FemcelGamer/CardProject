import sys
print(f"Python: {sys.executable}")

try:
    import sqlalchemy
    print("true")
    
    from sqlalchemy.ext.asyncio import AsyncSession
    print("true")
    
    import fastapi
    print("true")
    print("all true")
    from sqlalchemy.orm import sessionmaker
    print("true")
    
except Exception as e:
    print(f"false")