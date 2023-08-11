import requests


print(
    requests.post(
        "http://localhost:1000/",
        json={
            "from_email": "fake@fake.com",
            "content": """
                Dear Jason
                I hope this message finds you well. I'm Shirley from Brightside behavioral Health;

                I'm looking to purchase your EHR product for my team, we are a team of 2 people.

                Please let me know the price and timeline you can work with;

                Looking forward

                Shirley Lou
              """
        }
    ).json()
)
