import math
from datetime import date



email = {
    "subject": "MeetUp",
    "from": "Nasyrov@example.com",
    "to": "Evgeniy@example.com",
    "body": "Hi Evgeniy! Reminder: meeting at 15:00. See you!"
}


send_date = date.today().strftime("%Y-%m-%d")


email["date"] = send_date

print(email)


email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()


login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]


email["short_body"] = email["body"][:10] + "..."


print(email["short_body"])


personal_domains = [
    'gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com',
    'icloud.com', 'yandex.ru', 'mail.ru', 'list.ru', 'bk.ru', 'inbox.ru'
]
corporate_domains = [
    'company.ru', 'corporation.com', 'university.edu',
    'organization.org', 'company.org', 'business.net'
]


personal_domains  = list(dict.fromkeys(personal_domains))
corporate_domains = list(dict.fromkeys(corporate_domains))

print("Личные домены без дублей:", personal_domains)
print("Корпоративные домены без дублей:", corporate_domains)



intersection = set(personal_domains) & set(corporate_domains)

if intersection:
    raise ValueError(f"Personal and corporate domains intersect: {intersection}")


sender_domain = email["from"].split("@")[1]

is_corporate = sender_domain in corporate_domains

print(f"Is corporate sender: {is_corporate}")


email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")


print(email["clean_body"])


email["sent_text"] = f"""Кому: {email["to"]}, от {email["from"]}
Тема: {email["subject"]}, дата {email["date"]}
{email["clean_body"]}"""


print(email["sent_text"])


pages = math.ceil(len(email["sent_text"]) / 500)

print("Количество страниц:", pages)


is_subject_empty = not email["subject"].strip()
is_body_empty = not email["body"].strip()

print("Пустая тема письма:", is_subject_empty)
print("Пустое тело письма:", is_body_empty)


sender = email["from"]
email["masked_from"] = login[:2] + "***@" + domain

print("Маска отправителя:", email["masked_from"])


if "list.ru" in personal_domains:
    personal_domains.remove("list.ru")
if "bk.ru" in personal_domains:
    personal_domains.remove("bk.ru")

print("Личные домены:", personal_domains)


print(email)
print(is_corporate, pages, is_subject_empty, is_body_empty)