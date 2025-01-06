import smtplib
import uvicorn
from fastapi import FastAPI, BackgroundTasks, HTTPException
import logging
from pydantic import BaseModel, EmailStr
from tools import *


app = FastAPI(docs_url="/")

logging.basicConfig(
    filename="user_actions.log",
    format="%(asctime)s - %(message)s",
    level=logging.INFO
)


class EmailRequest(BaseModel):
    email: EmailStr
    subject: str


async def log_user_action(action: str):
    logging.info(action)


async def email_send(email: str, subject: str):
    try:
        server = smtplib.SMTP(smt_server, port)
        server.login(login, password)
        message = create_email_message(sender, email, subject)
        server.sendmail(sender, email, message.as_string())
        server.quit()
        logging.info(f"Email sent to {email} with subject '{subject}'")
    except Exception as e:
        logging.error(f"Failed to send email to {email}: {str(e)}")
        raise


@app.post("/send-email/")
async def send_email_endpoint(background_tasks: BackgroundTasks, email_request: EmailRequest):
    try:

        background_tasks.add_task(email_send, email_request.email, email_request.subject)

        log_message = f"User sent an email to {email_request.email}"
        background_tasks.add_task(log_user_action, log_message)

        return {"message": "Email is being sent in the background."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@app.get("/logs/")
async def get_logs():
    try:
        with open("user_actions.log", "r") as log_file:
            logs = log_file.readlines()
        return {"logs": logs}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Log file didn`t found.")


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
