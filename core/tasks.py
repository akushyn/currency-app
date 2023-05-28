from config.celery import app


@app.task
def multiply(x, y):
    print(x * y)
    return x * y
