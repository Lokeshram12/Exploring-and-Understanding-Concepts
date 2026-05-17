from fastapi import FastAPI , Depends

app = FastAPI()

class Logger:
    def log(self,message:str):
        print(f" logging message:{message}")

def get_logger():
    return Logger()

@app.get("/log/{message}")

def log_message(message:str,logger:Logger=Depends(get_logger)):
    logger.log(message)
    return message