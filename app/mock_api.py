from simple_salesforce import Salesforce
import os
from dotenv import load_dotenv

load_dotenv()

sf = Salesforce(
    username=os.getenv("SF_USERNAME"),
    password=os.getenv("SF_PASSWORD"),
    security_token=os.getenv("SF_TOKEN"),
    domain="login"  # use 'test' for sandbox if needed
)

def push_to_salesforce(summary, category, contact_email=None):
    task_data = {
        'Subject': f'AI Summary - {category}',
        'Description': summary,
        'Priority': 'Normal',
        'Status': 'Not Started'
    }

    if contact_email:
        try:
            results = sf.query(f"SELECT Id FROM Contact WHERE Email = '{contact_email}' LIMIT 1")
            if results['records']:
                task_data['WhoId'] = results['records'][0]['Id']
            else:
                print(f"[Warning] Contact with email '{contact_email}' not found in Salesforce.")
        except Exception as e:
            print(f"[Error] Failed to query contact: {e}")

    sf.Task.create(task_data)
    print("Pushed to Salesforce with data:", task_data)
